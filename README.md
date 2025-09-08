# 📊 Market Dashboard

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Educational--Non--Commercial-green)](LICENSE)


A **Streamlit-powered dashboard** for monitoring financial markets.  
It fetches real-time market data from **Yahoo Finance**, computes popular technical indicators, and displays the latest asset-specific news from the **Finlight News API**.  

---

## 🚀 Features

- 📈 **Price Data** from Yahoo Finance (via `yfinance`)  
- 🔍 **Technical Indicators**:
  - Money Flow Index (MFI)  
  - Relative Strength Index (RSI)  
  - Simple Moving Averages (50-day & 200-day)  
  - Support & Resistance Levels (50-day High & Low)  
- 📰 **Latest Market News** using Finlight API  
- 📊 Interactive **charts and gauges** (via Plotly + Streamlit)  
- 🎨 Responsive dashboard layout with a clean UI
- Running screenshot available in assets folder



---

## ⚙️ Setup & Run

Python **3.10+** recommended.

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/market-dashboard.git
   cd market-dashboard
   ```

2. **Set up environment variables**  
   Create a `.env` file in the root directory with your Finlight API key:

   ```bash
   API_KEY=your_finlight_api_key
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

5. Open your browser → [http://localhost:8501](http://localhost:8501)


## 📜 License

This project is licensed under the **Educational/Non-Commercial License**:

- ✅ You can use, copy, and modify this project for personal or educational purposes.  
- ❌ You cannot use this project for commercial purposes.  

See [LICENSE](https://github.com/KTleft93/market-dashboard/blob/main/LICENSE.md) for full details.

## 🙌 Acknowledgements

- [Yahoo Finance](https://pypi.org/project/yfinance/) via `yfinance`  
- [Finlight API](https://finlight.com) for market news  
- [Streamlit](https://streamlit.io) for the dashboard framework  
- [Plotly](https://plotly.com/python/) for interactive charts  

