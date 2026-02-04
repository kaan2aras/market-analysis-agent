"""Configuration settings for the market analysis agent."""

class Config:
    """Configuration class for market analysis agent."""
    
    # Default output settings
    DEFAULT_OUTPUT_FILENAME = "market_analysis_output.xlsx"
    
    # Categories available for filtering (expanded list from requirements)
    AVAILABLE_CATEGORIES = [
        "Chatbot",
        "Image Generation",
        "Video/Audio",
        "Productivity",
        "Code Assistant",
        "Writing Assistant",
        "Data Analysis",
        "Entertainment",
        "Finance",
        "Food & Drink",
        "Games",
        "Graphics & Design",
        "Health & Fitness",
        "Kids",
        "Lifestyle",
        "Medical",
        "Music",
        "Navigation",
        "News",
        "All"
    ]
    
    # Category mapping between different stores to unified format
    CATEGORY_MAPPING = {
        # Google Play Store categories to unified categories
        'ENTERTAINMENT': 'Entertainment',
        'FINANCE': 'Finance',
        'FOOD_AND_DRINK': 'Food & Drink',
        'GAME': 'Games',
        'ART_AND_DESIGN': 'Graphics & Design',
        'HEALTH_AND_FITNESS': 'Health & Fitness',
        'PARENTING': 'Kids',
        'LIFESTYLE': 'Lifestyle',
        'MEDICAL': 'Medical',
        'MUSIC_AND_AUDIO': 'Music',
        'MAPS_AND_NAVIGATION': 'Navigation',
        'NEWS_AND_MAGAZINES': 'News',
        'PRODUCTIVITY': 'Productivity',
        'BUSINESS': 'Productivity',
        'COMMUNICATION': 'Chatbot',
        # Apple App Store categories to unified categories
        'Entertainment': 'Entertainment',
        'Finance': 'Finance',
        'Food & Drink': 'Food & Drink',
        'Games': 'Games',
        'Graphics & Design': 'Graphics & Design',
        'Health & Fitness': 'Health & Fitness',
        'Kids': 'Kids',
        'Lifestyle': 'Lifestyle',
        'Medical': 'Medical',
        'Music': 'Music',
        'Navigation': 'Navigation',
        'News': 'News',
        'Productivity': 'Productivity',
        'Business': 'Productivity',
        'Social Networking': 'Chatbot',
    }
    
    # Google Play Store category IDs
    PLAY_STORE_CATEGORIES = {
        'Entertainment': 'ENTERTAINMENT',
        'Finance': 'FINANCE',
        'Food & Drink': 'FOOD_AND_DRINK',
        'Games': 'GAME',
        'Graphics & Design': 'ART_AND_DESIGN',
        'Health & Fitness': 'HEALTH_AND_FITNESS',
        'Kids': 'PARENTING',
        'Lifestyle': 'LIFESTYLE',
        'Medical': 'MEDICAL',
        'Music': 'MUSIC_AND_AUDIO',
        'Navigation': 'MAPS_AND_NAVIGATION',
        'News': 'NEWS_AND_MAGAZINES',
        'Productivity': 'PRODUCTIVITY',
    }
    
    # Apple App Store genre IDs (numeric IDs from Apple's system)
    APP_STORE_GENRES = {
        'Entertainment': '6016',
        'Finance': '6015',
        'Food & Drink': '6023',
        'Games': '6014',
        'Graphics & Design': '6027',
        'Health & Fitness': '6013',
        'Kids': '6016',  # Using Entertainment as fallback
        'Lifestyle': '6012',
        'Medical': '6020',
        'Music': '6011',
        'Navigation': '6010',
        'News': '6009',
        'Productivity': '6007',
    }
    
    # Regions available for filtering
    AVAILABLE_REGIONS = [
        "Global",
        "North America",
        "Europe",
        "Asia",
        "All"
    ]
    
    # Scraper settings
    MAX_APPS_PER_CATEGORY = 50  # Limit per category to avoid excessive scraping
    REQUEST_TIMEOUT = 30  # Seconds
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # Seconds between retries
    RATE_LIMIT_DELAY = 1  # Seconds between requests to avoid being blocked
    
    # Trending/New releases settings
    NEW_RELEASE_DAYS = 90  # Apps released in last 90 days are considered "new"
    MIN_RATING_TRENDING = 4.0  # Minimum rating for trending apps
    
    # Excel formatting settings
    EXCEL_HEADER_FORMAT = {
        'bold': True,
        'bg_color': '#4472C4',
        'font_color': '#FFFFFF',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
    }
    
    EXCEL_CELL_FORMAT = {
        'border': 1,
        'align': 'left',
        'valign': 'vcenter',
        'text_wrap': True
    }
    
    # Column headers for the Excel output (updated with new columns)
    EXCEL_COLUMNS = [
        'App Name',
        'Company',
        'Category',
        'Pricing Model',
        'Rating',
        'Downloads',
        'App Store Link',
        'Play Store Link',
        'Website',
        'Key Features',
        'Region',
        'Release Date',
        'Last Updated',
        'Source',
        'Trending Rank'
    ]
    
    # Column widths (in characters)
    COLUMN_WIDTHS = {
        'App Name': 20,
        'Company': 18,
        'Category': 15,
        'Pricing Model': 12,
        'Rating': 8,
        'Downloads': 12,
        'App Store Link': 15,
        'Play Store Link': 15,
        'Website': 15,
        'Key Features': 40,
        'Region': 12,
        'Release Date': 12,
        'Last Updated': 12,
        'Source': 15,
        'Trending Rank': 12
    }
    
    # Data source options
    AVAILABLE_SOURCES = [
        'play-store',
        'app-store',
        'sensor-tower',
        'sample',
        'all'
    ]
