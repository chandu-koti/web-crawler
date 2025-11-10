# Web Crawling Application

A simple Streamlit application for web crawling using Firecrawl API.

## Features

- Simple web interface for URL input
- Web crawling using Firecrawl API
- Loading indicator during crawling process
- Display crawled content

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your Firecrawl API key in `.env` file:
   ```
   FIRECRAWL_API_KEY=your_api_key_here
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a URL in the input field
2. Click "Crawl Website" button
3. Wait for the crawling process to complete
4. View the extracted content

## Dependencies

- streamlit: Web application framework
- firecrawl-py: Firecrawl API client
- python-dotenv: Environment variable management
