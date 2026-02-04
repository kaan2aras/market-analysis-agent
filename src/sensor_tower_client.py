"""Sensor Tower API client module."""

import os
import time
from datetime import datetime
import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from .config import Config


class SensorTowerClient:
    """Client for Sensor Tower API."""
    
    def __init__(self, api_key=None):
        """
        Initialize the Sensor Tower API client.
        
        Args:
            api_key: Sensor Tower API key (can also be set via SENSOR_TOWER_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('SENSOR_TOWER_API_KEY')
        self.base_url = 'https://api.sensortower.com/v1'
        self.config = Config()
        
        if not self.api_key:
            print("⚠️  Warning: Sensor Tower API key not configured.")
            print("   Set SENSOR_TOWER_API_KEY environment variable or pass api_key parameter.")
            print("   Sensor Tower data collection will be skipped.")
    
    def is_available(self):
        """
        Check if Sensor Tower API is available.
        
        Returns:
            Boolean indicating if API is configured and available
        """
        return self.api_key is not None
    
    @retry(stop=stop_after_attempt(Config.MAX_RETRIES), 
           wait=wait_exponential(multiplier=1, min=Config.RETRY_DELAY, max=10))
    def _make_request(self, endpoint, params=None):
        """
        Make a request to the Sensor Tower API.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            JSON response or None on failure
        """
        if not self.api_key:
            return None
        
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(
                url, 
                headers=headers, 
                params=params,
                timeout=Config.REQUEST_TIMEOUT
            )
            
            time.sleep(Config.RATE_LIMIT_DELAY)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print(f"❌ Error: Invalid Sensor Tower API key")
                return None
            elif response.status_code == 429:
                print(f"⚠️  Warning: Rate limited by Sensor Tower API")
                time.sleep(5)  # Wait longer before retry
                return None
            else:
                print(f"⚠️  Warning: Sensor Tower API returned status {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print(f"⚠️  Warning: Sensor Tower API request timed out")
            return None
        except Exception as e:
            print(f"⚠️  Warning: Error calling Sensor Tower API: {e}")
            return None
    
    def _extract_app_data(self, app_details, source_store='combined'):
        """
        Extract and format app data from Sensor Tower response.
        
        Args:
            app_details: Raw app details from Sensor Tower API
            source_store: Which store the data is from (ios/android/combined)
            
        Returns:
            Formatted dictionary matching expected schema
        """
        if not app_details:
            return None
        
        # Map category to unified format
        raw_category = app_details.get('category', 'Unknown')
        category = Config.CATEGORY_MAPPING.get(raw_category, raw_category)
        
        # Extract store links
        ios_url = app_details.get('ios_url', 'N/A')
        android_url = app_details.get('android_url', 'N/A')
        
        # Format downloads
        downloads = app_details.get('downloads', 0)
        if downloads >= 1000000000:
            downloads_str = f"{downloads // 1000000000}B+"
        elif downloads >= 1000000:
            downloads_str = f"{downloads // 1000000}M+"
        elif downloads >= 1000:
            downloads_str = f"{downloads // 1000}K+"
        else:
            downloads_str = str(downloads) if downloads else 'N/A'
        
        # Format dates
        release_date = app_details.get('release_date', 'N/A')
        # Date is already in expected format from API
        
        updated = app_details.get('last_updated', 'N/A')
        # Date is already in expected format from API
        
        return {
            'App Name': app_details.get('name', 'N/A'),
            'Company': app_details.get('publisher', 'N/A') or app_details.get('developer', 'N/A'),
            'Category': category,
            'Pricing Model': app_details.get('pricing_model', 'N/A'),
            'Rating': round(app_details.get('rating', 0), 1),
            'Downloads': downloads_str,
            'App Store Link': ios_url,
            'Play Store Link': android_url,
            'Website': app_details.get('website', 'N/A') or 'N/A',
            'Key Features': (app_details.get('description', '') or '')[:200] or 'N/A',
            'Region': 'Global',
            'Release Date': release_date,
            'Last Updated': updated,
            'Source': 'Sensor Tower',
            'Trending Rank': app_details.get('rank', 'N/A')
        }
    
    def get_trending_apps(self, categories=None, limit=50):
        """
        Get trending apps from Sensor Tower.
        
        Note: This is a placeholder implementation. The actual endpoint and response
        format will depend on your Sensor Tower API subscription and access level.
        
        Args:
            categories: List of categories to filter
            limit: Maximum number of apps to return
            
        Returns:
            List of app dictionaries
        """
        if not self.is_available():
            return []
        
        print(f"🔍 Querying Sensor Tower API...")
        apps = []
        
        try:
            # Example endpoint - adjust based on actual Sensor Tower API documentation
            endpoint = 'apps/trending'
            params = {
                'limit': limit,
                'country': 'US'
            }
            
            if categories and categories != ['All']:
                params['category'] = ','.join(categories)
            
            response = self._make_request(endpoint, params)
            
            if response and 'apps' in response:
                for app_data in response['apps']:
                    formatted_app = self._extract_app_data(app_data)
                    if formatted_app:
                        apps.append(formatted_app)
            
            print(f"✅ Found {len(apps)} apps from Sensor Tower")
            
        except Exception as e:
            print(f"❌ Error fetching apps from Sensor Tower: {e}")
        
        return apps
    
    def scrape_apps(self, categories=None, new_releases=False, trending=False, limit=None):
        """
        Scrape apps from Sensor Tower API.
        
        Args:
            categories: List of categories to scrape (unified format)
            new_releases: Filter for newly released apps
            trending: Filter for trending apps
            limit: Maximum number of apps to return
            
        Returns:
            List of app dictionaries
        """
        if not self.is_available():
            print("⚠️  Skipping Sensor Tower - API key not configured")
            return []
        
        # Use trending endpoint if trending flag is set
        if trending:
            return self.get_trending_apps(categories=categories, limit=limit)
        
        # Otherwise, this would require different Sensor Tower endpoints
        # For now, return empty list as this requires specific API documentation
        print("ℹ️  Sensor Tower integration requires specific API endpoint configuration")
        print("   See documentation for your Sensor Tower API subscription level")
        return []
