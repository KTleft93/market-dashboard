import pandas as pd
import pytest
from unittest.mock import MagicMock, patch
from utils.chart_functions import display_metric_safe, display_gauge, display_price_chart
import plotly.graph_objs as go


@pytest.fixture
def mock_column():
    """Return a mock Streamlit column with a metric method."""
    col = MagicMock()
    col.metric = MagicMock()
    return col


@pytest.fixture
def dummy_df():
    return pd.DataFrame({
        "Date": pd.date_range("2025-01-01", periods=5),
        "Close": [100, 102, 105, 103, 108]
    })

# -------------------------------
# Test display_metric_safe
# -------------------------------


def test_display_metric_safe_with_price_related_label(mock_column):
    """Should add $ when label contains price-related label """
    display_metric_safe(mock_column, "50-day SMA", 123.456, help="test")
    mock_column.metric.assert_called_once_with(
        label="50-day SMA",
        value="$123.46",
        help="test"
    )


def test_display_metric_safe_with_non_price_label(mock_column):
    """Should not add $ when label is RSI"""
    display_metric_safe(mock_column, "RSI", 55.4321, help="test")
    mock_column.metric.assert_called_once_with(
        label="RSI",
        value="55.43",
        help="test"
    )


def test_display_metric_safe_with_none_value(mock_column):
    """Should display fallback message if value is None."""
    display_metric_safe(mock_column, "Current Price", None, help="missing")
    mock_column.metric.assert_called_once_with(
        label="Current Price",
        value="Not Enough Data...",
        help="missing"
    )


def test_display_metric_safe_with_nan_value(mock_column):
    """Should display fallback message if value is NaN."""
    display_metric_safe(mock_column, "Current Price", float("nan"), help="nan case")
    mock_column.metric.assert_called_once_with(
        label="Current Price",
        value="Not Enough Data...",
        help="nan case"
    )


# -------------------------------
# Test display_gauge
# -------------------------------
@patch("plotly.graph_objects.Figure")
def test_display_gauge(mock_fig):
    mock_col = MagicMock()
    display_gauge(mock_col, 55, "Test Gauge", bar_color="green")
    mock_col.plotly_chart.assert_called_once()
    # Ensure the value was passed correctly to go.Indicator
    fig_call_args = mock_fig.call_args[0][0]
    assert fig_call_args['mode'] == "gauge+number"
    assert fig_call_args['value'] == 55
    assert fig_call_args['title']['text'] == "Test Gauge"


# -------------------------------
# Test display_price_chart
# -------------------------------


@patch("utils.chart_functions.st.plotly_chart")
def test_display_price_chart_calls_streamlit(mock_plotly_chart, dummy_df):
    """Ensure st.plotly_chart is called with a valid Plotly Figure."""
    display_price_chart(dummy_df, column_name="Close", asset_name="Test Asset")

    mock_plotly_chart.assert_called_once()

    args, kwargs = mock_plotly_chart.call_args
    fig = args[0]

    assert isinstance(fig, go.Figure)

    assert fig.layout.title.text == "Test Asset Price"

    assert kwargs["use_container_width"] is True
