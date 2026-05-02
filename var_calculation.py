import yfinance as yf
import numpy as np
import pandas as pd


stock = "AAPL"


data = yf.download(
    stock,
    start="2024-01-01",
    end="2025-01-01"
)


data["Returns"] = data["Close"].pct_change()


mean_return = data["Returns"].mean()
std_dev = data["Returns"].std()


z_score = 1.65


var_95 = mean_return - (z_score * std_dev)

print("Mean Return:", mean_return)
print("Standard Deviation:", std_dev)
print("95% VaR:", var_95)