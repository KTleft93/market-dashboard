from finlight_client import FinlightApi, ApiConfig
from finlight_client.models import GetArticlesParams
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = FinlightApi(config=ApiConfig(api_key=API_KEY))


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
