"""Main agent module for market analysis."""

import argparse
import os
from .data_collector import DataCollector
from .excel_writer import ExcelWriter
from .config import Config


class MarketAnalysisAgent:
    """Main agent for conducting market research on AI apps/marketplaces."""
    
    def __init__(self):
        """Initialize the market analysis agent."""
        self.data_collector = DataCollector()
    
    def run(self, output_file=None, category=None, region=None, limit=None, 
            group_by_category=False):
        """
        Run the market analysis agent.
        
        Args:
            output_file: Path to output Excel file
            category: Filter by category
            region: Filter by region
            limit: Maximum number of results
            group_by_category: Whether to create separate sheets by category
            
        Returns:
            Path to the generated Excel file
        """
        print("🤖 Market Analysis Agent Starting...")
        print(f"📊 Collecting data on AI apps and marketplaces...")
        
        # Get data
        data = self.data_collector.get_data(
            category=category,
            region=region,
            limit=limit
        )
        
        print(f"✅ Found {len(data)} apps matching criteria")
        
        # Initialize Excel writer
        excel_writer = ExcelWriter(filename=output_file)
        
        # Write data
        if group_by_category:
            print("📝 Generating Excel file with sheets by category...")
            # Group data by category
            categories = {}
            for app in data:
                cat = app['Category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(app)
            
            # Also add "All Apps" sheet
            categories['All Apps'] = data
            
            output_path = excel_writer.write_multiple_sheets(categories)
        else:
            print("📝 Generating Excel file...")
            output_path = excel_writer.write_data(data)
        
        print(f"✨ Excel file created successfully: {output_path}")
        print(f"📁 Total apps in output: {len(data)}")
        
        return output_path


def main():
    """Command-line interface for the market analysis agent."""
    parser = argparse.ArgumentParser(
        description='AI-powered market research agent for AI apps/marketplaces'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=Config.DEFAULT_OUTPUT_FILENAME,
        help=f'Output Excel file name (default: {Config.DEFAULT_OUTPUT_FILENAME})'
    )
    
    parser.add_argument(
        '-c', '--category',
        type=str,
        choices=Config.AVAILABLE_CATEGORIES,
        help='Filter by category'
    )
    
    parser.add_argument(
        '-r', '--region',
        type=str,
        choices=Config.AVAILABLE_REGIONS,
        help='Filter by region'
    )
    
    parser.add_argument(
        '-l', '--limit',
        type=int,
        help='Maximum number of results to include'
    )
    
    parser.add_argument(
        '-g', '--group-by-category',
        action='store_true',
        help='Create separate sheets for each category'
    )
    
    parser.add_argument(
        '--list-categories',
        action='store_true',
        help='List available categories and exit'
    )
    
    parser.add_argument(
        '--list-regions',
        action='store_true',
        help='List available regions and exit'
    )
    
    args = parser.parse_args()
    
    # Handle list options
    if args.list_categories:
        print("Available categories:")
        for cat in Config.AVAILABLE_CATEGORIES:
            print(f"  - {cat}")
        return
    
    if args.list_regions:
        print("Available regions:")
        for region in Config.AVAILABLE_REGIONS:
            print(f"  - {region}")
        return
    
    # Run the agent
    agent = MarketAnalysisAgent()
    agent.run(
        output_file=args.output,
        category=args.category,
        region=args.region,
        limit=args.limit,
        group_by_category=args.group_by_category
    )


if __name__ == '__main__':
    main()
