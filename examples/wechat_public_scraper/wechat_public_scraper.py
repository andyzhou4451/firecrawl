import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

# Replace with the WeChat article URL you want to scrape
WECHAT_URL = os.getenv("WECHAT_URL", "https://mp.weixin.qq.com/")


def main():
    app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) "
            "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 "
            "Mobile/15A372 Safari/604.1"
        )
    }

    data = app.scrape_url(
        WECHAT_URL,
        formats=["markdown", "html"],
        headers=headers,
    )

    if data.success:
        print(data.markdown)
    else:
        print(f"Error: {data.error}")


if __name__ == "__main__":
    main()
