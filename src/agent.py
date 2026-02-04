"""Main CLI entry point for the market analysis agent."""

import argparse
import sys
from src.data_collector import DataCollector
from src.excel_writer import ExcelWriter


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Market Research Agent for AI-Powered Mobile and Web Apps",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get all AI-powered apps
  python -m src.agent --output ai_apps_research.xlsx
  
  # Filter by category
  python -m src.agent --category photo --output photo_ai_apps.xlsx
  
  # Filter by platform
  python -m src.agent --platform ios --output ios_ai_apps.xlsx
  
  # Get top trending only
  python -m src.agent --trending --limit 20 --output trending_ai_apps.xlsx
  
  # Filter by region
  python -m src.agent --region global --output global_ai_apps.xlsx
        """
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="ai_apps_research.xlsx",
        help="Output Excel filename (default: ai_apps_research.xlsx)"
    )
    
    parser.add_argument(
        "--category",
        type=str,
        help="Filter by category (e.g., photo, video, productivity, social, education)"
    )
    
    parser.add_argument(
        "--platform",
        type=str,
        choices=["ios", "android", "both"],
        help="Filter by platform (ios, android, or both)"
    )
    
    parser.add_argument(
        "--trending",
        action="store_true",
        help="Get only top trending apps"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of results"
    )
    
    parser.add_argument(
        "--region",
        type=str,
        help="Filter by region availability (e.g., global, us, europe)"
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize data collector
        collector = DataCollector()
        
        # Get filtered apps
        apps = collector.get_apps(
            category=args.category,
            platform=args.platform,
            trending=args.trending,
            limit=args.limit,
            region=args.region
        )
        
        if not apps:
            print("No apps found matching the specified criteria.")
            sys.exit(1)
        
        print(f"Found {len(apps)} AI-powered apps")
        
        # Create Excel writer
        writer = ExcelWriter(args.output)
        
        # Write 'All Apps' sheet with filtered results
        writer.write_all_apps(apps)
        
        # Only create additional sheets if no filters are applied (showing all data)
        if not any([args.category, args.platform, args.trending, args.region, args.limit]):
            # Write 'By Category' sheet
            categories = collector.get_apps_by_category_grouped()
            writer.write_by_category(categories)
            
            # Write 'Top Trending' sheet
            trending_apps = collector.get_apps(trending=True, limit=20)
            writer.write_top_trending(trending_apps)
            
            # Write 'By Region' sheet
            regions = collector.get_apps_by_region_grouped()
            writer.write_by_region(regions)
            
            print("Created 4 sheets: All Apps, By Category, Top Trending, By Region")
        else:
            print("Created 1 sheet: All Apps (filtered results)")
        
        # Save the workbook
        writer.save()
        
        print(f"✓ Successfully generated {args.output}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
