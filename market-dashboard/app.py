import streamlit as st
from data.fetch_prices import get_price_data
from data.fetch_news import get_finlight_news
from utils.indicator_functions import calculate_average_mfi, calculate_average_rsi, calculate_sma, calculate_support_resistance_levels
from utils.chart_functions import display_gauge, display_price_chart, display_metric_safe
from data.fetch_news import get_finlight_news

# -----------------------
# Data fetching function
# -----------------------
symbol = "^GSPC"
df = get_price_data(symbol)

# Metric tool tip html
tooltip_html = f"""
<div style="position: relative; display: inline-block; border-bottom: 1px dotted black;">
  <span style="font-size:20px; font-weight:bold;">Hello</span>
  <span style="visibility:hidden; width:120px; background-color:black; color:#fff;
               text-align:center; border-radius:6px; padding:5px; position:absolute;
               z-index:1; bottom:125%; left:50%; margin-left:-60px;">
    Hello
  </span>
</div>
"""

st.set_page_config(layout="wide")

# CSS for 90% width
st.markdown(
    """
    <style>
    .block-container {
        max-width: 90%;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------
# MFI calculation function
# -----------------------
calculate_average_mfi(df)

# RSI Calculation
calculate_average_rsi(df)

# Calculate 50 amd 200 day moving average
calculate_sma(df)

# Calculate Support and resistance
calculate_support_resistance_levels(df)

# Get current price
current_price = df["Close"].iloc[-1]

# -----------------------
# Streamlit UI
# -----------------------
st.title("Market Dashboard")


assets = {
    "S&P 500": "^GSPC",
    "NASDAQ": "^IXIC",
    "Bitcoin": "BTC-USD",
    "Ethereum": "ETH-USD",
    "Gold": "GC=F"

}
st.markdown("<h3 style='font-size:20px; color:white;'>Select An Asset</h3>", unsafe_allow_html=True)
selected_asset = st.selectbox("Select an asset", list(assets.keys()), index=0, label_visibility="collapsed")
st.markdown("<h3 style='font-size:20px; color:white;'>Select A Period</h3>", unsafe_allow_html=True)
period = st.selectbox("Select a period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3, label_visibility="collapsed")
st.markdown("### ")  # blank line
st.markdown("<br>", unsafe_allow_html=True)

if selected_asset:
    symbol = assets[selected_asset]

    # Fetch data for the selected asset
    df = get_price_data(symbol, period)

    # Calculate indicators for this asset
    avg_mfi, df = calculate_average_mfi(df)
    avg_rsi, df = calculate_average_rsi(df)
    sma_50, sma_200, df = calculate_sma(df)
    support_50, resistance_50, df = calculate_support_resistance_levels(df)

    # Display all components
    st.subheader(f"{selected_asset} ({symbol})")

    # --- Price chart and news ---
    col1, col2 = st.columns([2, 1])
    with col1:
        display_price_chart(df, column_name="Close", asset_name=selected_asset)

    with col2:
        st.subheader("Latest Market News")
        links = get_finlight_news(symbol, 5)
        for link in links:
            st.markdown(f"**[{link.title}]({link.link})**")

    # --- Metrics and gauges ---
    st.subheader(f"{selected_asset} Metrics & Indicators")
    st.markdown("### ")  # blank line
    col1, col2, col3 = st.columns(3)
    with col1:
        display_metric_safe(st, "Current Price", current_price, help="Last Closing Price")
        display_metric_safe(st, "50-day SMA", sma_50, help="Moving Average Price Over Last 50 Days")
        display_metric_safe(st, "200-day SMA", sma_200, help="Moving Average Price Over Last 200 Days")
    with col2:
        display_metric_safe(st, f"Average MFI ({period})", avg_mfi, help="Money Flow Index")
        display_metric_safe(st, "50-day Low", support_50, help="Lowest CLosing Price In Last 50 Days")
        display_metric_safe(st, "50-day High", resistance_50, help="Highest Closing Price In Last 200 Days")
    with col3:
        g1, g2 = st.columns(2, gap="medium")
        display_gauge(g1, avg_mfi, "MFI")
        display_gauge(g2, avg_rsi, "RSI")





