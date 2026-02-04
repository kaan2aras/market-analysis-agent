# Market Analysis Agent

An AI-powered market research agent that automatically conducts market research on AI apps from multiple marketplaces, outputting results in a formatted Excel sheet.

## Features

- 🤖 **Automated Market Research**: Dynamically scrapes data from multiple sources
- 📱 **Multi-Source Collection**: Scrape from Google Play Store, Apple App Store, and Sensor Tower (with API)
- 🆕 **New Releases**: Filter for newly released apps (last 90 days)
- 🔥 **Trending Apps**: Identify trending apps with high ratings and downloads
- 📊 **Excel Output**: Generates professionally formatted Excel files with clickable hyperlinks
- 🔍 **Advanced Filtering**: Filter by category, region, source, and more
- 📑 **Multi-Sheet Support**: Optionally group data by category in separate sheets
- ⚙️ **CLI Interface**: Easy-to-use command-line interface
- 🛡️ **Error Handling**: Robust retry logic and rate limiting to avoid blocks
- 🐍 **Pure Python**: Built with Python, pandas, openpyxl, and scraper libraries

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install from source

```bash
# Clone the repository
git clone https://github.com/kaan2aras/market-analysis-agent.git
cd market-analysis-agent

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Usage

### Command Line Interface

#### Basic Usage
```bash
# Generate market analysis with sample data (default)
python -m src.agent

# Or use the installed script
market-agent
```

#### Scraping from Real Sources

```bash
# Scrape from Google Play Store
python -m src.agent -s play-store -l 20

# Scrape from Apple App Store
python -m src.agent -s app-store -l 20

# Scrape from multiple sources
python -m src.agent -s play-store -s app-store -l 50

# Scrape from all available sources
python -m src.agent -s all -l 100
```

#### Filtering Options

```bash
# Filter for trending apps
python -m src.agent -s play-store --trending -l 20

# Filter for new releases (last 90 days)
python -m src.agent -s play-store --new-releases -l 20

# Combine filters
python -m src.agent -s all --trending --new-releases -l 30
```

#### Category Filtering

```bash
# Filter by specific category
python -m src.agent -s play-store -c Entertainment -l 15

# Multiple categories (run separately)
python -m src.agent -s play-store -c Games -l 10
python -m src.agent -s app-store -c Finance -l 10
```

#### Advanced Examples
```bash
# Specify output filename
python -m src.agent -o my_analysis.xlsx

# Filter by category
python -m src.agent -c Chatbot

# Filter by region
python -m src.agent -r Global

# Limit number of results
python -m src.agent -l 10

# Group by category (creates separate sheets)
python -m src.agent -g

# Combine multiple options
python -m src.agent -c "Image Generation" -l 5 -o image_apps.xlsx
```

#### List Available Options
```bash
# List available categories
python -m src.agent --list-categories

# List available regions
python -m src.agent --list-regions

# List available data sources
python -m src.agent --list-sources

# Show help
python -m src.agent --help
```

### Sensor Tower Integration

To use Sensor Tower API (requires API key):

```bash
# Set API key as environment variable
export SENSOR_TOWER_API_KEY="your_api_key_here"

# Then use sensor-tower source
python -m src.agent -s sensor-tower -l 20
```

Or pass the API key programmatically:

```python
from src.sensor_tower_client import SensorTowerClient
client = SensorTowerClient(api_key="your_api_key_here")
```

### Python API

```python
from src.agent import MarketAnalysisAgent

# Create agent instance
agent = MarketAnalysisAgent()

# Run with default settings (sample data)
agent.run()

# Scrape from Play Store with filters
agent.run(
    output_file='play_store_apps.xlsx',
    sources=['play-store'],
    trending=True,
    limit=20
)

# Scrape from multiple sources
agent.run(
    output_file='all_sources.xlsx',
    sources=['play-store', 'app-store'],
    new_releases=True,
    limit=50
)

# Run analysis with default settings
agent.run()

# Run with custom options
agent.run(
    output_file='custom_output.xlsx',
    category='Chatbot',
    region='Global',
    limit=15,
    group_by_category=True
)
```

### Using Components Separately

```python
from src.data_collector import DataCollector
from src.excel_writer import ExcelWriter

# Collect data from multiple sources
collector = DataCollector()
data = collector.collect_from_sources(
    sources=['play-store', 'app-store'],
    trending=True,
    limit=20
)

# Or use sample data
sample_data = collector.get_data(category='Chatbot', limit=10)

# Write to Excel
writer = ExcelWriter(filename='output.xlsx')
writer.write_data(data)

# Use individual scrapers
from src.play_store_scraper import PlayStoreScraper
from src.app_store_scraper import AppStoreScraper

play_scraper = PlayStoreScraper()
apps = play_scraper.scrape_apps(categories=['Games'], trending=True, limit=10)

app_scraper = AppStoreScraper()
apps = app_scraper.scrape_apps(categories=['Finance'], new_releases=True, limit=10)
```

## Configuration Options

### Categories
- Chatbot
- Image Generation
- Video/Audio
- Productivity
- Code Assistant
- Writing Assistant
- Data Analysis
- Entertainment
- Finance
- Food & Drink
- Games
- Graphics & Design
- Health & Fitness
- Kids
- Lifestyle
- Medical
- Music
- Navigation
- News
- All (no filter)

### Data Sources
- **play-store**: Google Play Store (requires internet access)
- **app-store**: Apple App Store (requires internet access)
- **sensor-tower**: Sensor Tower API (requires API key)
- **sample**: Built-in sample data of 29 AI apps
- **all**: Collect from all available sources

### Regions
- Global
- North America
- Europe
- Asia
- All (no filter)

### Filter Options
- **--trending**: Apps with high ratings (≥4.0) and significant downloads/reviews
- **--new-releases**: Apps released within the last 90 days

### Output Settings
- Default filename: `market_analysis_output.xlsx`
- Configurable via `-o` or `--output` flag
- Excel format (.xlsx) with professional formatting

## Output Format

The generated Excel file includes the following columns:

| Column | Description |
|--------|-------------|
| App Name | Name of the application |
| Company | Company/organization behind the app |
| Category | App category (Chatbot, Image Generation, etc.) |
| Pricing Model | Free, Freemium, Paid |
| Rating | User rating (0-5 scale) |
| Downloads | Download/user count or review count |
| App Store Link | Apple App Store link (clickable hyperlink) |
| Play Store Link | Google Play Store link (clickable hyperlink) |
| Website | Official website (clickable hyperlink) |
| Key Features | Brief summary of key features |
| Region | Country/region availability |
| Release Date | Initial release date |
| Last Updated | Last update date |
| Source | Which marketplace the data came from |
| Trending Rank | Trending position (if available) |

### Sample Output

The repository includes a sample output file in `examples/sample_output.xlsx` demonstrating the format.

## Project Structure

```
market-analysis-agent/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── setup.py                  # Package installation configuration
├── src/
│   ├── __init__.py           # Package initialization
│   ├── agent.py              # Main agent logic and CLI
│   ├── data_collector.py     # Data collection and orchestration
│   ├── play_store_scraper.py # Google Play Store scraper
│   ├── app_store_scraper.py  # Apple App Store scraper
│   ├── sensor_tower_client.py # Sensor Tower API client
│   ├── excel_writer.py       # Excel output generation
│   └── config.py             # Configuration settings
├── tests/
│   ├── test_agent.py         # Unit tests for agent
│   └── test_scrapers.py      # Unit tests for scrapers
└── examples/
    └── sample_output.xlsx    # Sample output file
```

## How It Works

### Data Collection Flow

1. **Source Selection**: Choose from Play Store, App Store, Sensor Tower, or sample data
2. **Scraping**: Each scraper fetches app data from its respective source
3. **Filtering**: Apply filters for trending apps, new releases, or categories
4. **Deduplication**: Merge data from multiple sources and remove duplicates
5. **Export**: Generate formatted Excel file with all collected data

### Rate Limiting & Error Handling

- **Retry Logic**: Automatically retries failed requests up to 3 times
- **Rate Limiting**: 1-second delay between requests to avoid blocking
- **Graceful Degradation**: If one source fails, others continue
- **Timeout Protection**: 30-second timeout on all API requests

## Sample Data Included

The agent includes data on 29 real AI applications across multiple categories:

### Chatbots/Assistants (8 apps)
- ChatGPT, Claude, Gemini, Microsoft Copilot, Perplexity, Character.AI, Pi, Poe

### Image Generation (6 apps)
- Midjourney, DALL-E, Leonardo AI, Adobe Firefly, Canva AI, Stable Diffusion

### Video/Audio (5 apps)
- Runway, ElevenLabs, Synthesia, HeyGen, Descript

### Productivity (5 apps)
- Notion AI, Grammarly, Jasper, Copy.ai, Otter.ai

### Code Assistants (5 apps)
- GitHub Copilot, Cursor, Tabnine, Codeium, Amazon CodeWhisperer

## Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_agent

# Run with verbose output
python -m unittest discover tests -v
```

## Development

### Setting up development environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate

# Install in development mode
pip install -e .
```

### Adding new apps

To add more AI apps to the sample database, edit `src/data_collector.py` and add entries to the `_get_sample_data()` method following the existing format.

### Extending Scrapers

To add new data sources:

1. Create a new scraper class in `src/` following the pattern of `PlayStoreScraper` or `AppStoreScraper`
2. Implement `scrape_apps()` method that returns list of app dictionaries
3. Add the scraper to `DataCollector` in `src/data_collector.py`
4. Update `Config.AVAILABLE_SOURCES` in `src/config.py`

## Requirements

- Python >= 3.8
- pandas >= 2.0.0
- openpyxl >= 3.1.2
- xlsxwriter >= 3.1.0
- google-play-scraper >= 1.2.4
- app-store-scraper >= 0.3.5
- requests >= 2.31.0
- tenacity >= 8.2.3

## Limitations

- **Network Access**: Play Store and App Store scrapers require internet access
- **Rate Limits**: Heavy scraping may trigger rate limits; use reasonable limits
- **API Access**: Sensor Tower requires a paid API subscription
- **Data Accuracy**: Scraped data depends on source availability and format
- **Geographic Restrictions**: Some apps may not be available in all regions

## Troubleshooting

### Scraper Returns No Results

- Check internet connectivity
- Verify search queries are appropriate
- Try increasing the limit parameter
- Check if sources are blocking automated access

### Sensor Tower Not Working

- Ensure API key is set: `export SENSOR_TOWER_API_KEY="your_key"`
- Verify API subscription is active
- Check API endpoint documentation for your subscription level

### Import Errors

- Reinstall dependencies: `pip install -r requirements.txt`
- Ensure Python version is 3.8 or higher

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Data collected from publicly available information about AI apps and marketplaces
- Built with Python, pandas, openpyxl, and xlsxwriter
