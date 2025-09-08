from finlight_client import FinlightApi, ApiConfig
from finlight_client.models import GetArticlesParams
from dotenv import load_dotenv
import os

# Use env var for development
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Loading API key for deployment purposes
client = FinlightApi(config=ApiConfig(api_key="sk_a92493d14517f6fdb2c9cf4b73d599697786eb0055d1aeda90279e42f0736917"))


def get_finlight_news(query="AAPL", pageSize=5):
    """
    Fetch news articles from API client.
    Returns a list of article objects.
    """
    try:
        params = GetArticlesParams(
            query=query,
            pageSize=pageSize
        )
        articles = client.articles.fetch_articles(params=params)
        return articles.articles
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
