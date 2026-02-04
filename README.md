# Market Analysis Agent

An AI-powered market research agent that automatically conducts condensed market research on AI apps and marketplaces, outputting results in a formatted Excel sheet.

## Features

- 🤖 **Automated Market Research**: Collects data on 30+ real AI applications and marketplaces
- 📊 **Excel Output**: Generates professionally formatted Excel files with clickable hyperlinks
- 🔍 **Filtering Options**: Filter by category, region, and limit results
- 📑 **Multi-Sheet Support**: Optionally group data by category in separate sheets
- ⚙️ **CLI Interface**: Easy-to-use command-line interface
- 🐍 **Pure Python**: Built with Python, pandas, and openpyxl

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
# Generate market analysis with all apps
python -m src.agent

# Or use the installed script
market-agent
```

#### With Options
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

# Show help
python -m src.agent --help
```

### Python API

```python
from src.agent import MarketAnalysisAgent

# Create agent instance
agent = MarketAnalysisAgent()

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

# Collect data
collector = DataCollector()
data = collector.get_data(category='Chatbot', limit=10)

# Write to Excel
writer = ExcelWriter(filename='output.xlsx')
writer.write_data(data)
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
- All (no filter)

### Regions
- Global
- North America
- Europe
- Asia
- All (no filter)

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
| Pricing Model | Free, Freemium, Paid, Subscription |
| Rating | User rating (if available) |
| Downloads | Download/user count (if available) |
| App Store Link | Apple App Store link (clickable hyperlink) |
| Play Store Link | Google Play Store link (clickable hyperlink) |
| Website | Official website (clickable hyperlink) |
| Key Features | Brief summary of key features |
| Region | Country/region availability |
| Last Updated | Last update date |

### Sample Output

The repository includes a sample output file in `examples/sample_output.xlsx` demonstrating the format.

## Project Structure

```
market-analysis-agent/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── setup.py              # Package installation configuration
├── src/
│   ├── __init__.py       # Package initialization
│   ├── agent.py          # Main agent logic and CLI
│   ├── data_collector.py # Data collection with 30 AI apps
│   ├── excel_writer.py   # Excel output generation
│   └── config.py         # Configuration settings
├── tests/
│   └── test_agent.py     # Unit tests
└── examples/
    └── sample_output.xlsx # Sample output file
```

## Data Included

The agent includes data on 30 real AI applications across multiple categories:

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

To add more AI apps to the database, edit `src/data_collector.py` and add entries to the `_get_sample_data()` method following the existing format.

## Requirements

- Python >= 3.8
- pandas >= 2.0.0
- openpyxl >= 3.1.2
- xlsxwriter >= 3.1.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Data collected from publicly available information about AI apps and marketplaces
- Built with Python, pandas, openpyxl, and xlsxwriter
