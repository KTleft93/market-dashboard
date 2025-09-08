import pytest
import pandas as pd
import importlib
from unittest.mock import patch, MagicMock


dummy_df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=10),
    "Open": range(100, 110),
    "High": range(101, 111),
    "Low": range(99, 109),
    "Close": range(100, 110),
    "Volume": [1000 + i*10 for i in range(10)]
})


@pytest.mark.smoke
@patch("data.fetch_prices.get_price_data", return_value=dummy_df)
@patch("data.fetch_news.get_finlight_news", return_value=[MagicMock(title="t", link="l")])
@patch("utils.indicator_functions.calculate_average_mfi", return_value=(50, dummy_df))
@patch("utils.indicator_functions.calculate_average_rsi", return_value=(45, dummy_df))
@patch("utils.indicator_functions.calculate_sma", return_value=(102, 108, dummy_df))
@patch("utils.indicator_functions.calculate_support_resistance_levels", return_value=(95, 115, dummy_df))
@patch("utils.chart_functions.display_price_chart")
@patch("utils.chart_functions.display_metric_safe")
@patch("utils.chart_functions.display_gauge")
def test_app_runs_without_errors(
    mock_gauge,
    mock_metric,
    mock_chart,
    mock_sr,
    mock_sma,
    mock_rsi,
    mock_mfi,
    mock_news,
    mock_prices
):

    app = importlib.import_module("app")

    mock_prices.assert_called()
    mock_mfi.assert_called()
    mock_rsi.assert_called()
    mock_sma.assert_called()
    mock_sr.assert_called()
    mock_news.assert_called()
    mock_chart.assert_called()
    mock_metric.assert_called()
    mock_gauge.assert_called()
