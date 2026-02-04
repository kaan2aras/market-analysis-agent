"""Configuration settings for the market analysis agent."""

class Config:
    """Configuration class for market analysis agent."""
    
    # Default output settings
    DEFAULT_OUTPUT_FILENAME = "market_analysis_output.xlsx"
    
    # Categories available for filtering
    AVAILABLE_CATEGORIES = [
        "Chatbot",
        "Image Generation",
        "Video/Audio",
        "Productivity",
        "Code Assistant",
        "Writing Assistant",
        "Data Analysis",
        "All"
    ]
    
    # Regions available for filtering
    AVAILABLE_REGIONS = [
        "Global",
        "North America",
        "Europe",
        "Asia",
        "All"
    ]
    
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
    
    # Column headers for the Excel output
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
        'Last Updated'
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
        'Last Updated': 12
    }
