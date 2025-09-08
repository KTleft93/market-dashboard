import pandas as pd
from unittest.mock import patch
from data.fetch_prices import get_price_data


dummy_df = pd.DataFrame({
    "Open": [100, 102, 101],
    "High": [103, 104, 102],
    "Low": [99, 100, 100],
    "Close": [102, 101, 101],
    "Volume": [1000, 1500, 1200]
})

@patch("data.fetch_prices.yf.download")
def test_get_price_data(mock_download):

    mock_download.return_value = dummy_df

    df = get_price_data("BTC-USD", period="5d")

    assert isinstance(df, pd.DataFrame)
    assert "Open" in df.columns
    assert len(df) == 3
    mock_download.assert_called_once_with("BTC-USD", period="5d", interval='1d', progress=False)
