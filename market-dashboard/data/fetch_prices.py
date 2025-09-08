import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300)
def get_price_data(symbol: str, period: str = "1y") -> pd.DataFrame:
    """Fetch historical daily data for a symbol."""
    df = yf.download(symbol, period=period, interval="1d", progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]
    df.reset_index(inplace=True)
    return df.copy()
