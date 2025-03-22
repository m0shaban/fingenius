# FinGenius Project

## Description
This repository contains the FinGenius project, a comprehensive financial analysis web application that helps businesses analyze financial statements, create projections, and gain AI-powered insights.

## Features

- **Financial Data Analysis**: Upload and analyze financial statements
- **Interactive Dashboard**: Visualize key financial metrics and trends
- **Financial Projections**: Generate data-driven financial forecasts
- **AI-Powered Insights**: Get intelligent recommendations based on your financial data
- **What-If Analysis**: Test different financial scenarios
- **SWOT Analysis**: Document and track business strengths, weaknesses, opportunities, and threats
- **SMART Goals**: Set and track financial goals

## Installation

```bash
# Clone the repository
git clone https://github.com/m0shaban/FinGenius.git

# Navigate to the project directory
cd FinGenius

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Set up environment variables
# Create a .env file with necessary configuration

# Run the development server
python run.py

# Or use the toolkit for easier management
fingenius_toolkit.bat
```

## Deployment on Render
This project is configured for deployment on Render. Follow these steps:

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect to your GitHub repository
4. Use the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
5. Add the following environment variables:
   - `SECRET_KEY`: A secure random string
   - `FLASK_APP`: run.py
   - `DEEPSEEK_API_KEY`: Your DeepSeek API key (if applicable)
   - `CLAUDE_API_KEY`: Your Claude API key (if applicable)

## License
MIT License
