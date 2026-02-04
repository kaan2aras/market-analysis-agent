"""Tests for the market analysis agent."""

import os
import unittest
from src.agent import MarketAnalysisAgent
from src.data_collector import DataCollector
from src.excel_writer import ExcelWriter
from src.config import Config


class TestDataCollector(unittest.TestCase):
    """Test cases for DataCollector."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.collector = DataCollector()
    
    def test_get_all_data(self):
        """Test getting all data."""
        data = self.collector.get_data()
        self.assertGreaterEqual(len(data), 20)
        self.assertIsInstance(data, list)
    
    def test_get_data_by_category(self):
        """Test filtering by category."""
        data = self.collector.get_data(category='Chatbot')
        self.assertGreater(len(data), 0)
        for app in data:
            self.assertEqual(app['Category'], 'Chatbot')
    
    def test_get_data_with_limit(self):
        """Test limiting results."""
        limit = 5
        data = self.collector.get_data(limit=limit)
        self.assertEqual(len(data), limit)
    
    def test_get_categories(self):
        """Test getting unique categories."""
        categories = self.collector.get_categories()
        self.assertIsInstance(categories, list)
        self.assertGreater(len(categories), 0)
    
    def test_get_regions(self):
        """Test getting unique regions."""
        regions = self.collector.get_regions()
        self.assertIsInstance(regions, list)
        self.assertGreater(len(regions), 0)
    
    def test_data_structure(self):
        """Test that data has required fields."""
        data = self.collector.get_data(limit=1)
        self.assertEqual(len(data), 1)
        app = data[0]
        
        required_fields = Config.EXCEL_COLUMNS
        for field in required_fields:
            self.assertIn(field, app)


class TestExcelWriter(unittest.TestCase):
    """Test cases for ExcelWriter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_file = '/tmp/test_output.xlsx'
        self.writer = ExcelWriter(filename=self.test_file)
        self.collector = DataCollector()
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_write_data(self):
        """Test writing data to Excel."""
        data = self.collector.get_data(limit=5)
        output_file = self.writer.write_data(data)
        
        self.assertEqual(output_file, self.test_file)
        self.assertTrue(os.path.exists(output_file))
    
    def test_write_multiple_sheets(self):
        """Test writing multiple sheets."""
        data = self.collector.get_data()
        data_dict = {
            'Chatbot': [app for app in data if app['Category'] == 'Chatbot'][:3],
            'Image Generation': [app for app in data if app['Category'] == 'Image Generation'][:3]
        }
        
        output_file = self.writer.write_multiple_sheets(data_dict)
        
        self.assertEqual(output_file, self.test_file)
        self.assertTrue(os.path.exists(output_file))


class TestMarketAnalysisAgent(unittest.TestCase):
    """Test cases for MarketAnalysisAgent."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = MarketAnalysisAgent()
        self.test_file = '/tmp/test_market_analysis.xlsx'
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_run_basic(self):
        """Test basic agent run."""
        output_file = self.agent.run(output_file=self.test_file, limit=5)
        
        self.assertEqual(output_file, self.test_file)
        self.assertTrue(os.path.exists(output_file))
    
    def test_run_with_category(self):
        """Test agent run with category filter."""
        output_file = self.agent.run(
            output_file=self.test_file,
            category='Chatbot',
            limit=3
        )
        
        self.assertTrue(os.path.exists(output_file))
    
    def test_run_with_grouping(self):
        """Test agent run with grouping by category."""
        output_file = self.agent.run(
            output_file=self.test_file,
            group_by_category=True,
            limit=10
        )
        
        self.assertTrue(os.path.exists(output_file))


if __name__ == '__main__':
    unittest.main()
