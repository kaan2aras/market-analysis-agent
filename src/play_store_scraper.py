"""Google Play Store scraper module."""

import time
from datetime import datetime, timedelta
from google_play_scraper import app, search
from google_play_scraper.features.reviews import Sort
from tenacity import retry, stop_after_attempt, wait_exponential
from .config import Config


class PlayStoreScraper:
    """Scraper for Google Play Store apps."""
    
    def __init__(self):
        """Initialize the Play Store scraper."""
        self.config = Config()
    
    @retry(stop=stop_after_attempt(Config.MAX_RETRIES), 
           wait=wait_exponential(multiplier=1, min=Config.RETRY_DELAY, max=10))
    def _search_apps(self, query, num_results=50):
        """
        Search for apps on Play Store.
        
        Args:
            query: Search query string
            num_results: Number of results to fetch
            
        Returns:
            List of app IDs
        """
        try:
            results = search(query, n_hits=num_results)
            time.sleep(Config.RATE_LIMIT_DELAY)
            return [result['appId'] for result in results if result.get('appId')]
        except Exception as e:
            print(f"Warning: Error searching Play Store: {e}")
            return []
    
    @retry(stop=stop_after_attempt(Config.MAX_RETRIES), 
           wait=wait_exponential(multiplier=1, min=Config.RETRY_DELAY, max=10))
    def _get_app_details(self, app_id):
        """
        Get detailed information about an app.
        
        Args:
            app_id: Google Play Store app ID
            
        Returns:
            Dictionary with app details or None on failure
        """
        try:
            result = app(app_id, lang='en', country='us')
            time.sleep(Config.RATE_LIMIT_DELAY)
            return result
        except Exception as e:
            print(f"Warning: Could not fetch details for {app_id}: {e}")
            return None
    
    def _is_new_release(self, release_date):
        """
        Check if an app is a new release.
        
        Args:
            release_date: Release date string or datetime object
            
        Returns:
            Boolean indicating if app is new
        """
        if not release_date:
            return False
        
        try:
            if isinstance(release_date, str):
                # Try to parse various date formats
                for fmt in ['%Y-%m-%d', '%b %d, %Y', '%Y/%m/%d']:
                    try:
                        release_dt = datetime.strptime(release_date, fmt)
                        break
                    except ValueError:
                        continue
                else:
                    return False
            else:
                release_dt = release_date
            
            days_since_release = (datetime.now() - release_dt).days
            return days_since_release <= Config.NEW_RELEASE_DAYS
        except Exception:
            return False
    
    def _is_trending(self, app_data):
        """
        Determine if an app is trending.
        
        Args:
            app_data: Dictionary with app details
            
        Returns:
            Boolean indicating if app is trending
        """
        # Simple heuristic: high rating + significant installs + recent updates
        rating = app_data.get('score', 0)
        installs = app_data.get('realInstalls', 0) or app_data.get('minInstalls', 0)
        
        return (rating >= Config.MIN_RATING_TRENDING and installs > 10000)
    
    def _extract_app_data(self, app_details):
        """
        Extract and format app data from Play Store details.
        
        Args:
            app_details: Raw app details from google_play_scraper
            
        Returns:
            Formatted dictionary matching expected schema
        """
        if not app_details:
            return None
        
        # Map category to unified format
        raw_category = app_details.get('genre', 'Unknown')
        category = Config.CATEGORY_MAPPING.get(raw_category, raw_category)
        
        # Determine pricing model
        free = app_details.get('free', True)
        in_app_purchases = app_details.get('offersIAP', False)
        if free and not in_app_purchases:
            pricing = 'Free'
        elif free and in_app_purchases:
            pricing = 'Freemium'
        else:
            pricing = 'Paid'
        
        # Format installs
        installs = app_details.get('realInstalls') or app_details.get('minInstalls', 0)
        if installs >= 1000000000:
            downloads = f"{installs // 1000000000}B+"
        elif installs >= 1000000:
            downloads = f"{installs // 1000000}M+"
        elif installs >= 1000:
            downloads = f"{installs // 1000}K+"
        else:
            downloads = str(installs)
        
        # Format release date
        release_date = app_details.get('released', 'N/A')
        if release_date and release_date != 'N/A':
            try:
                release_date = datetime.strptime(release_date, '%b %d, %Y').strftime('%Y-%m-%d')
            except:
                pass
        
        # Format last updated
        updated = app_details.get('updated', 'N/A')
        if updated and updated != 'N/A':
            try:
                # Handle timestamp format
                if isinstance(updated, int):
                    updated = datetime.fromtimestamp(updated / 1000).strftime('%Y-%m-%d')
                else:
                    updated = datetime.strptime(str(updated), '%b %d, %Y').strftime('%Y-%m-%d')
            except:
                pass
        
        return {
            'App Name': app_details.get('title', 'N/A'),
            'Company': app_details.get('developer', 'N/A'),
            'Category': category,
            'Pricing Model': pricing,
            'Rating': round(app_details.get('score', 0), 1),
            'Downloads': downloads,
            'App Store Link': 'N/A',
            'Play Store Link': f"https://play.google.com/store/apps/details?id={app_details.get('appId', '')}",
            'Website': app_details.get('developerWebsite', 'N/A') or 'N/A',
            'Key Features': app_details.get('summary', '')[:200] or app_details.get('description', '')[:200] or 'N/A',
            'Region': 'Global',
            'Release Date': release_date,
            'Last Updated': updated,
            'Source': 'Google Play Store',
            'Trending Rank': 'N/A'
        }
    
    def scrape_apps(self, categories=None, new_releases=False, trending=False, limit=None):
        """
        Scrape apps from Google Play Store.
        
        Args:
            categories: List of categories to scrape (unified format)
            new_releases: Filter for newly released apps
            trending: Filter for trending apps
            limit: Maximum number of apps to return
            
        Returns:
            List of app dictionaries
        """
        apps = []
        
        # Default to AI-related searches if no categories specified
        if not categories or categories == ['All']:
            search_queries = ['AI app', 'artificial intelligence', 'ChatGPT', 'AI assistant']
        else:
            search_queries = categories
        
        print(f"🔍 Searching Google Play Store...")
        
        for query in search_queries:
            try:
                print(f"  Searching for: {query}")
                app_ids = self._search_apps(query, num_results=min(20, Config.MAX_APPS_PER_CATEGORY))
                
                for app_id in app_ids:
                    app_details = self._get_app_details(app_id)
                    
                    if not app_details:
                        continue
                    
                    # Apply filters
                    if new_releases and not self._is_new_release(app_details.get('released')):
                        continue
                    
                    if trending and not self._is_trending(app_details):
                        continue
                    
                    app_data = self._extract_app_data(app_details)
                    if app_data:
                        apps.append(app_data)
                    
                    # Check limit
                    if limit and len(apps) >= limit:
                        break
                
                if limit and len(apps) >= limit:
                    break
                    
            except Exception as e:
                print(f"  Warning: Error processing query '{query}': {e}")
                continue
        
        print(f"✅ Found {len(apps)} apps from Google Play Store")
        return apps
