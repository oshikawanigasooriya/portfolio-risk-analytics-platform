import yfinance as yf
import pandas as pd

stocks = ['AAPL', 'MSFT', 'TSLA']

data = yf.download(
    stocks,
    start="2024-01-01",
    end="2025-01-01"
)

print(data.head())