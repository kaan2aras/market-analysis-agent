# Market Analysis Agent for AI-Powered Apps

A market research tool that analyzes **trending mobile and web apps built with AI technology**. This agent focuses on consumer apps that leverage AI as a core feature, not the AI platforms themselves.

## 🎯 Overview

This tool researches and catalogs AI-powered apps across various categories including:
- **Photo & Video Apps** - AI editing, filters, effects (Lensa AI, Remini, CapCut, etc.)
- **Productivity Apps** - AI transcription, text-to-speech, writing assistance (Otter.ai, Speechify, Grammarly, etc.)
- **Education Apps** - AI tutoring, language learning (Duolingo, Photomath, Socratic, etc.)
- **Social & Entertainment** - AI recommendations, content curation (TikTok, Instagram, Spotify, etc.)
- **Health & Fitness** - AI wellness, nutrition tracking (Calm, MyFitnessPal, Headspace, etc.)
- **Shopping & Lifestyle** - AI visual search, recommendations (Pinterest, SHEIN, IKEA Place, etc.)

The database includes **35+ real, trending AI-powered apps** with accurate data.

## 📊 Features

### Data Collection
- **35+ Curated Apps** with real, verified data
- **Accurate Links** to App Store, Play Store, and official websites
- **Real Ratings** and download statistics
- **Trending Scores** based on popularity and growth

### Excel Output
The tool generates professional Excel reports with:
- ✅ **Sheet 1: All Apps** - Complete list
- ✅ **Sheet 2: By Category** - Grouped by category
- ✅ **Sheet 3: Top Trending** - Top 20 by trending score
- ✅ **Sheet 4: By Region** - Grouped by availability
- ✅ **Clickable Hyperlinks**
- ✅ **Professional Formatting**

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## 📖 Usage

```bash
# Get all AI-powered apps
python -m src.agent --output ai_apps_research.xlsx

# Filter by category
python -m src.agent --category photo --output photo_ai_apps.xlsx

# Get top trending
python -m src.agent --trending --limit 20 --output trending_ai_apps.xlsx
```

## 🧪 Testing

```bash
python -m unittest tests/test_agent.py
```
