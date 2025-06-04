# WeChat Public Account Scraper Example

This example shows how to scrape the content of a WeChat public account article using the Firecrawl Python SDK.

> **Note**: WeChat pages often implement anti-crawling measures and may require authentication. Success is not guaranteed. Always ensure that your use complies with WeChat's terms of service and privacy policy.

## Usage

1. Install dependencies:
   ```bash
   pip install firecrawl-py python-dotenv
   ```
2. Set your Firecrawl API key as `FIRECRAWL_API_KEY` in an `.env` file. Optionally provide the target article URL via `WECHAT_URL`.
3. Run the script:
   ```bash
   python wechat_public_scraper.py
   ```
   The script will output the article content in Markdown if the request succeeds.
