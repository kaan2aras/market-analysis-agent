"""Tests for scraper modules."""

import unittest
from unittest.mock import patch, MagicMock
from src.play_store_scraper import PlayStoreScraper
from src.app_store_scraper import AppStoreScraper
from src.sensor_tower_client import SensorTowerClient
from src.data_collector import DataCollector


class TestPlayStoreScraper(unittest.TestCase):
    """Test cases for PlayStoreScraper."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.scraper = PlayStoreScraper()
    
    def test_initialization(self):
        """Test scraper initializes correctly."""
        self.assertIsNotNone(self.scraper)
        self.assertIsNotNone(self.scraper.config)
    
    @patch('src.play_store_scraper.search')
    def test_search_apps(self, mock_search):
        """Test searching for apps."""
        mock_search.return_value = [
            {'appId': 'com.test.app1'},
            {'appId': 'com.test.app2'}
        ]
        
        result = self.scraper._search_apps('test query', num_results=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'com.test.app1')
    
    def test_is_new_release(self):
        """Test new release detection."""
        # Test with recent date
        from datetime import datetime, timedelta
        recent_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        self.assertTrue(self.scraper._is_new_release(recent_date))
        
        # Test with old date
        old_date = (datetime.now() - timedelta(days=200)).strftime('%Y-%m-%d')
        self.assertFalse(self.scraper._is_new_release(old_date))
    
    def test_is_trending(self):
        """Test trending detection."""
        # High rating and installs - should be trending
        app_data = {'score': 4.5, 'realInstalls': 100000}
        self.assertTrue(self.scraper._is_trending(app_data))
        
        # Low rating - should not be trending
        app_data = {'score': 3.0, 'realInstalls': 100000}
        self.assertFalse(self.scraper._is_trending(app_data))


class TestAppStoreScraper(unittest.TestCase):
    """Test cases for AppStoreScraper."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.scraper = AppStoreScraper()
    
    def test_initialization(self):
        """Test scraper initializes correctly."""
        self.assertIsNotNone(self.scraper)
        self.assertIsNotNone(self.scraper.config)
    
    def test_is_new_release(self):
        """Test new release detection."""
        from datetime import datetime, timedelta
        recent_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        self.assertTrue(self.scraper._is_new_release(recent_date))
        
        old_date = (datetime.now() - timedelta(days=200)).strftime('%Y-%m-%d')
        self.assertFalse(self.scraper._is_new_release(old_date))
    
    def test_is_trending(self):
        """Test trending detection."""
        # High rating and reviews - should be trending
        app_data = {'rating': 4.5, 'rating_count': 1000}
        self.assertTrue(self.scraper._is_trending(app_data))
        
        # Low reviews - should not be trending
        app_data = {'rating': 4.5, 'rating_count': 50}
        self.assertFalse(self.scraper._is_trending(app_data))


class TestSensorTowerClient(unittest.TestCase):
    """Test cases for SensorTowerClient."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.client = SensorTowerClient()
    
    def test_initialization_without_key(self):
        """Test client initializes without API key."""
        self.assertIsNotNone(self.client)
        self.assertFalse(self.client.is_available())
    
    def test_initialization_with_key(self):
        """Test client initializes with API key."""
        client = SensorTowerClient(api_key='test_key')
        self.assertTrue(client.is_available())


class TestDataCollectorIntegration(unittest.TestCase):
    """Test cases for DataCollector with new functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.collector = DataCollector()
    
    def test_initialization(self):
        """Test collector initializes with all scrapers."""
        self.assertIsNotNone(self.collector.play_store_scraper)
        self.assertIsNotNone(self.collector.app_store_scraper)
        self.assertIsNotNone(self.collector.sensor_tower_client)
    
    def test_deduplicate_apps(self):
        """Test deduplication logic."""
        apps = [
            {'App Name': 'TestApp', 'Company': 'Test Inc', 'App Store Link': 'link1', 'Play Store Link': 'N/A'},
            {'App Name': 'TestApp', 'Company': 'Test Inc', 'App Store Link': 'N/A', 'Play Store Link': 'link2'},
            {'App Name': 'OtherApp', 'Company': 'Other Inc', 'App Store Link': 'link3', 'Play Store Link': 'N/A'}
        ]
        
        result = self.collector._deduplicate_apps(apps)
        
        # Should have 2 unique apps
        self.assertEqual(len(result), 2)
        
        # First app should have both links merged
        test_app = next((app for app in result if app['App Name'] == 'TestApp'), None)
        self.assertIsNotNone(test_app, "TestApp should be in deduplicated results")
        self.assertEqual(test_app['App Store Link'], 'link1')
        self.assertEqual(test_app['Play Store Link'], 'link2')
    
    def test_merge_data_sources(self):
        """Test merging from multiple sources."""
        source1 = [{'App Name': 'App1', 'Source': 'Source1'}]
        source2 = [{'App Name': 'App2', 'Source': 'Source2'}]
        
        result = self.collector._merge_data_sources(source1, source2)
        
        self.assertEqual(len(result), 2)
    
    def test_collect_from_sample_source(self):
        """Test collecting from sample source."""
        result = self.collector.collect_from_sources(sources=['sample'], limit=5)
        
        self.assertGreater(len(result), 0)
        self.assertLessEqual(len(result), 5)
        
        # Verify data structure
        for app in result:
            self.assertIn('App Name', app)
            self.assertIn('Source', app)


if __name__ == '__main__':
    unittest.main()
