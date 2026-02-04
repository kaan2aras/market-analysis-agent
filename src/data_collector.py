"""Data collection and filtering logic for AI-powered apps."""

from src.data.ai_apps_database import (
    get_all_apps,
    get_apps_by_category,
    get_apps_by_platform,
    get_trending_apps,
    get_apps_by_region
)


class DataCollector:
    """Collects and filters AI-powered app data based on criteria."""
    
    def __init__(self):
        """Initialize the data collector."""
        self.all_apps = get_all_apps()
    
    def get_apps(self, category=None, platform=None, trending=False, limit=None, region=None):
        """
        Get apps based on filtering criteria.
        
        Args:
            category (str): Filter by category (e.g., 'photo', 'productivity')
            platform (str): Filter by platform ('ios', 'android', 'both')
            trending (bool): Get only trending apps
            limit (int): Limit number of results
            region (str): Filter by region availability
            
        Returns:
            list: Filtered list of apps
        """
        if trending:
            apps = get_trending_apps(limit=limit or 20)
        elif category:
            apps = get_apps_by_category(category)
        elif platform:
            apps = get_apps_by_platform(platform)
        elif region:
            apps = get_apps_by_region(region)
        else:
            apps = self.all_apps
        
        # Apply limit if specified and not already limited by trending
        if limit and not trending:
            apps = apps[:limit]
        
        return apps
    
    def get_apps_by_category_grouped(self):
        """
        Get apps grouped by category.
        
        Returns:
            dict: Dictionary with categories as keys and app lists as values
        """
        categories = {}
        for app in self.all_apps:
            category = app["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(app)
        
        return categories
    
    def get_apps_by_region_grouped(self):
        """
        Get apps grouped by region.
        
        Returns:
            dict: Dictionary with regions as keys and app lists as values
        """
        regions = {}
        for app in self.all_apps:
            region = app["region_availability"]
            if region not in regions:
                regions[region] = []
            regions[region].append(app)
        
        return regions
