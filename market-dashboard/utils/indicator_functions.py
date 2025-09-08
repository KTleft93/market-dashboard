import pandas as pd
from ta.volume import MFIIndicator
from ta.momentum import RSIIndicator


def calculate_average_mfi(df: pd.DataFrame, window: int = 14):
    """Compute MFI and return average over the period."""
    df_local = df.copy()
    for col in ['High', 'Low', 'Close', 'Volume']:
        df_local[col] = pd.to_numeric(df_local[col], errors='coerce')

    mfi_indicator = MFIIndicator(
        high=df_local['High'],
        low=df_local['Low'],
        close=df_local['Close'],
        volume=df_local['Volume'],
        window=window
    )
    df_local['MFI'] = mfi_indicator.money_flow_index()

    avg_mfi = df_local['MFI'].mean()
    return avg_mfi, df_local


def calculate_average_rsi(df: pd.DataFrame, window: int = 14):
    """
    Calculate RSI over the dataframe.
    Returns the average RSI value and the df with RSI column.
    """
    df_local = df.copy()
    df_local['RSI'] = RSIIndicator(close=df_local['Close'], window=window).rsi()
    avg_rsi = df_local['RSI'].mean()
    return avg_rsi, df_local


def calculate_sma(df: pd.DataFrame):
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    sma_50 = df['SMA_50'].iloc[-1]
    sma_200 = df['SMA_200'].iloc[-1]

    return sma_50, sma_200, df


def calculate_support_resistance_levels(df: pd.DataFrame):

    support_50_days = df['Low'].tail(50).min()
    resistance_50_days = df['High'].tail(50).max()

    return support_50_days, resistance_50_days, df

