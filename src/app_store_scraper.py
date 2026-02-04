"""Apple App Store scraper module."""

import time
from datetime import datetime, timedelta
from app_store_scraper import AppStore
from tenacity import retry, stop_after_attempt, wait_exponential
from .config import Config


class AppStoreScraper:
    """Scraper for Apple App Store apps."""
    
    def __init__(self):
        """Initialize the App Store scraper."""
        self.config = Config()
    
    @retry(stop=stop_after_attempt(Config.MAX_RETRIES), 
           wait=wait_exponential(multiplier=1, min=Config.RETRY_DELAY, max=10))
    def _search_apps(self, query, country='us', num_results=50):
        """
        Search for apps on App Store.
        
        Args:
            query: Search query string
            country: Country code (default: 'us')
            num_results: Number of results to fetch
            
        Returns:
            List of app dictionaries
        """
        try:
            store = AppStore(country=country, app_name=query, app_id=None)
            store.search()
            time.sleep(Config.RATE_LIMIT_DELAY)
            return store.search_results[:num_results] if store.search_results else []
        except Exception as e:
            print(f"Warning: Error searching App Store for '{query}': {e}")
            return []
    
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
                for fmt in ['%Y-%m-%d', '%b %d, %Y', '%Y/%m/%d', '%Y-%m-%dT%H:%M:%SZ']:
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
        # Simple heuristic: high rating + significant review count
        rating = app_data.get('rating', 0) or 0
        review_count = app_data.get('rating_count', 0) or 0
        
        return (rating >= Config.MIN_RATING_TRENDING and review_count > 100)
    
    def _extract_app_data(self, app_details):
        """
        Extract and format app data from App Store details.
        
        Args:
            app_details: Raw app details from app_store_scraper
            
        Returns:
            Formatted dictionary matching expected schema
        """
        if not app_details:
            return None
        
        # Map category to unified format (if available)
        raw_category = app_details.get('primaryGenreName', 'Unknown')
        category = Config.CATEGORY_MAPPING.get(raw_category, raw_category)
        
        # Determine pricing model
        price = app_details.get('price', 0) or 0
        in_app_purchases = app_details.get('inAppPurchases', False)
        
        if price == 0 and not in_app_purchases:
            pricing = 'Free'
        elif price == 0 and in_app_purchases:
            pricing = 'Freemium'
        else:
            pricing = 'Paid'
        
        # Format rating
        rating = app_details.get('rating', 0) or 0
        if rating:
            rating = round(float(rating), 1)
        
        # Format review count as downloads (App Store doesn't expose download numbers)
        review_count = app_details.get('rating_count', 0) or 0
        if review_count >= 1000000:
            downloads = f"{review_count // 1000000}M+ reviews"
        elif review_count >= 1000:
            downloads = f"{review_count // 1000}K+ reviews"
        else:
            downloads = f"{review_count} reviews"
        
        # Format release date
        release_date = app_details.get('releaseDate', 'N/A')
        if release_date and release_date != 'N/A':
            try:
                if 'T' in str(release_date):
                    release_date = datetime.strptime(str(release_date), '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
                elif isinstance(release_date, str):
                    # Try to parse and format
                    for fmt in ['%Y-%m-%d', '%b %d, %Y']:
                        try:
                            release_date = datetime.strptime(release_date, fmt).strftime('%Y-%m-%d')
                            break
                        except ValueError:
                            continue
            except:
                pass
        
        # Format current version release date as last updated
        updated = app_details.get('currentVersionReleaseDate', 'N/A')
        if updated and updated != 'N/A':
            try:
                if 'T' in str(updated):
                    updated = datetime.strptime(str(updated), '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
            except:
                pass
        
        # Get app ID and build URL
        app_id = app_details.get('id', '')
        app_url = f"https://apps.apple.com/us/app/id{app_id}" if app_id else 'N/A'
        
        return {
            'App Name': app_details.get('title', 'N/A') or app_details.get('trackName', 'N/A'),
            'Company': app_details.get('developer', 'N/A') or app_details.get('artistName', 'N/A'),
            'Category': category,
            'Pricing Model': pricing,
            'Rating': rating,
            'Downloads': downloads,
            'App Store Link': app_url,
            'Play Store Link': 'N/A',
            'Website': app_details.get('sellerUrl', 'N/A') or 'N/A',
            'Key Features': (app_details.get('description', '') or '')[:200] or 'N/A',
            'Region': 'Global',
            'Release Date': release_date,
            'Last Updated': updated,
            'Source': 'Apple App Store',
            'Trending Rank': 'N/A'
        }
    
    def scrape_apps(self, categories=None, new_releases=False, trending=False, limit=None):
        """
        Scrape apps from Apple App Store.
        
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
        
        print(f"🔍 Searching Apple App Store...")
        
        for query in search_queries:
            try:
                print(f"  Searching for: {query}")
                search_results = self._search_apps(query, num_results=min(20, Config.MAX_APPS_PER_CATEGORY))
                
                for app_details in search_results:
                    if not app_details:
                        continue
                    
                    # Apply filters
                    if new_releases and not self._is_new_release(app_details.get('releaseDate')):
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
        
        print(f"✅ Found {len(apps)} apps from Apple App Store")
        return apps
