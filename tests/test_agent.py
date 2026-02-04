"""Unit tests for the market analysis agent."""

import unittest
import os
import sys
from src.data_collector import DataCollector
from src.data.ai_apps_database import get_all_apps, get_apps_by_category, get_trending_apps


class TestDataCollector(unittest.TestCase):
    """Test cases for DataCollector class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.collector = DataCollector()
    
    def test_get_all_apps(self):
        """Test getting all apps."""
        apps = self.collector.get_apps()
        self.assertGreater(len(apps), 30, "Should have at least 30 apps")
        
    def test_get_apps_by_category(self):
        """Test filtering apps by category."""
        photo_apps = self.collector.get_apps(category="photo")
        self.assertGreater(len(photo_apps), 0, "Should have photo apps")
        
        for app in photo_apps:
            self.assertIn("photo", app["category"].lower(), 
                         f"App {app['app_name']} should be in photo category")
    
    def test_get_apps_by_platform_ios(self):
        """Test filtering apps by iOS platform."""
        ios_apps = self.collector.get_apps(platform="ios")
        self.assertGreater(len(ios_apps), 0, "Should have iOS apps")
        
        for app in ios_apps:
            self.assertTrue(app["app_store_link"], 
                          f"App {app['app_name']} should have App Store link")
    
    def test_get_apps_by_platform_android(self):
        """Test filtering apps by Android platform."""
        android_apps = self.collector.get_apps(platform="android")
        self.assertGreater(len(android_apps), 0, "Should have Android apps")
        
        for app in android_apps:
            self.assertTrue(app["play_store_link"], 
                          f"App {app['app_name']} should have Play Store link")
    
    def test_get_trending_apps(self):
        """Test getting trending apps."""
        trending = self.collector.get_apps(trending=True, limit=10)
        self.assertEqual(len(trending), 10, "Should return exactly 10 trending apps")
        
        # Verify they are sorted by trending score
        scores = [app["trending_score"] for app in trending]
        self.assertEqual(scores, sorted(scores, reverse=True), 
                        "Apps should be sorted by trending score descending")
    
    def test_get_apps_with_limit(self):
        """Test limiting number of results."""
        limited_apps = self.collector.get_apps(limit=5)
        self.assertEqual(len(limited_apps), 5, "Should return exactly 5 apps")
    
    def test_get_apps_by_region(self):
        """Test filtering apps by region."""
        global_apps = self.collector.get_apps(region="global")
        self.assertGreater(len(global_apps), 0, "Should have global apps")
        
        for app in global_apps:
            self.assertIn("global", app["region_availability"].lower(),
                         f"App {app['app_name']} should be available globally")
    
    def test_get_apps_by_category_grouped(self):
        """Test grouping apps by category."""
        categories = self.collector.get_apps_by_category_grouped()
        self.assertIsInstance(categories, dict, "Should return a dictionary")
        self.assertGreater(len(categories), 0, "Should have at least one category")
        
        for category, apps in categories.items():
            self.assertIsInstance(apps, list, "Category should contain a list of apps")
            self.assertGreater(len(apps), 0, f"Category {category} should have apps")
    
    def test_get_apps_by_region_grouped(self):
        """Test grouping apps by region."""
        regions = self.collector.get_apps_by_region_grouped()
        self.assertIsInstance(regions, dict, "Should return a dictionary")
        self.assertGreater(len(regions), 0, "Should have at least one region")


class TestDatabase(unittest.TestCase):
    """Test cases for the AI apps database."""
    
    def test_all_apps_have_required_fields(self):
        """Test that all apps have required fields."""
        required_fields = [
            "app_name", "company", "category", "ai_features",
            "app_store_link", "play_store_link", "website",
            "rating_ios", "rating_android", "downloads", "pricing",
            "monthly_active_users", "trending_score", "region_availability",
            "last_updated"
        ]
        
        apps = get_all_apps()
        for app in apps:
            for field in required_fields:
                self.assertIn(field, app, 
                            f"App {app.get('app_name', 'Unknown')} missing field: {field}")
    
    def test_all_apps_have_valid_links(self):
        """Test that all apps have valid links."""
        apps = get_all_apps()
        for app in apps:
            app_name = app.get("app_name", "Unknown")
            
            # Check App Store link
            if app["app_store_link"]:
                self.assertTrue(app["app_store_link"].startswith("https://"),
                              f"{app_name} should have valid App Store link")
            
            # Check Play Store link
            if app["play_store_link"]:
                self.assertTrue(app["play_store_link"].startswith("https://"),
                              f"{app_name} should have valid Play Store link")
            
            # Check website
            if app["website"]:
                self.assertTrue(app["website"].startswith("https://") or 
                              app["website"].startswith("http://"),
                              f"{app_name} should have valid website")
    
    def test_all_apps_have_ai_features(self):
        """Test that all apps have AI features described."""
        apps = get_all_apps()
        for app in apps:
            self.assertTrue(app["ai_features"], 
                          f"App {app['app_name']} should have AI features described")
            self.assertGreater(len(app["ai_features"]), 10,
                             f"App {app['app_name']} should have detailed AI features")
    
    def test_trending_scores_are_valid(self):
        """Test that trending scores are within valid range."""
        apps = get_all_apps()
        for app in apps:
            score = app["trending_score"]
            self.assertGreaterEqual(score, 0, 
                                  f"{app['app_name']} trending score should be >= 0")
            self.assertLessEqual(score, 100,
                               f"{app['app_name']} trending score should be <= 100")


if __name__ == "__main__":
    unittest.main()
