"""Configuration settings for the market analysis agent."""

# Field names for Excel output
FIELD_NAMES = [
    "App Name",
    "Company/Developer",
    "Category",
    "AI Features",
    "App Store Link",
    "Play Store Link",
    "Website",
    "Rating (iOS)",
    "Rating (Android)",
    "Downloads",
    "Pricing",
    "Monthly Active Users",
    "Trending Score",
    "Region Availability",
    "Last Updated"
]

# Mapping from database keys to field names
FIELD_MAPPING = {
    "app_name": "App Name",
    "company": "Company/Developer",
    "category": "Category",
    "ai_features": "AI Features",
    "app_store_link": "App Store Link",
    "play_store_link": "Play Store Link",
    "website": "Website",
    "rating_ios": "Rating (iOS)",
    "rating_android": "Rating (Android)",
    "downloads": "Downloads",
    "pricing": "Pricing",
    "monthly_active_users": "Monthly Active Users",
    "trending_score": "Trending Score",
    "region_availability": "Region Availability",
    "last_updated": "Last Updated"
}

# Excel styling
HEADER_COLOR = "366092"  # Dark blue
HEADER_FONT_COLOR = "FFFFFF"  # White
EVEN_ROW_COLOR = "D9E1F2"  # Light blue
ODD_ROW_COLOR = "FFFFFF"  # White
