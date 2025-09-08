from unittest.mock import patch, MagicMock
from data.fetch_news import get_finlight_news  # replace with actual file name


def test_get_finlight_news_success():
    # Mock article objects
    mock_articles = [MagicMock(title="Article 1"), MagicMock(title="Article 2")]

    # Patch client.articles.fetch_articles to return a fake response
    with patch("data.fetch_news.client.articles.fetch_articles") as mock_fetch:
        mock_fetch.return_value.articles = mock_articles

        result = get_finlight_news(query="TSLA", pageSize=2)

        # Assertions
        assert len(result) == 2
        assert result[0].title == "Article 1"
        assert result[1].title == "Article 2"
        mock_fetch.assert_called_once()  # ensure API was called


def test_get_finlight_news_error():
    # Force fetch_articles to raise an exception
    with patch("data.fetch_news.client.articles.fetch_articles", side_effect=Exception("API error")):
        result = get_finlight_news("GOOG")

        # Assertions
        assert result == []  # should return empty list
