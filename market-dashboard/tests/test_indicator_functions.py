import pandas as pd


from utils.indicator_functions import (
    calculate_average_mfi,
    calculate_average_rsi,
    calculate_sma,
    calculate_support_resistance_levels
)

sample_data = pd.DataFrame({
    "Open": [100, 102, 101, 103, 105, 104, 106],
    "High": [103, 104, 102, 105, 107, 106, 108],
    "Low": [99, 100, 100, 101, 103, 102, 104],
    "Close": [102, 101, 101, 104, 106, 105, 107],
    "Volume": [1000, 1500, 1200, 1300, 1400, 1100, 1600]
})


# -------------------------
# Test calculate_average_mfi
# -------------------------
def test_calculate_average_mfi():
    avg_mfi, df_mfi = calculate_average_mfi(sample_data, window=3)

    # Check return types
    assert isinstance(avg_mfi, float)
    assert isinstance(df_mfi, pd.DataFrame)

    assert "MFI" in df_mfi.columns

    # Last MFI value should not be NaN if enough data
    assert not pd.isna(df_mfi['MFI'].iloc[-1])


# -------------------------
# Test calculate_average_rsi
# -------------------------
def test_calculate_average_rsi():
    avg_rsi, df_rsi = calculate_average_rsi(sample_data, window=3)

    assert isinstance(avg_rsi, float)
    assert isinstance(df_rsi, pd.DataFrame)

    assert "RSI" in df_rsi.columns

    # Last RSI value should not be NaN if enough data
    assert not pd.isna(df_rsi['RSI'].iloc[-1])


# -------------------------
# Test calculate_sma
# -------------------------
def test_calculate_sma():

    sma_50, sma_200, df_sma = calculate_sma(sample_data)

    assert isinstance(sma_50, float) or pd.isna(sma_50)
    assert isinstance(sma_200, float) or pd.isna(sma_200)

    assert "SMA_50" in df_sma.columns
    assert "SMA_200" in df_sma.columns


# -------------------------
# Test calculate_support_resistance_levels
# -------------------------
def test_calculate_support_resistance_levels():
    support_50, resistance_50, df_sr = calculate_support_resistance_levels(sample_data)

    assert isinstance(support_50, int)
    assert isinstance(resistance_50, int)

    # Support should be <= any of last 50 lows
    assert support_50 == sample_data['Low'].tail(50).min()

    # Resistance should be >= any of last 50 highs
    assert resistance_50 == sample_data['High'].tail(50).max()
