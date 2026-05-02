import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


stock = "AAPL"


data = yf.download(
    stock,
    start="2024-01-01",
    end="2025-01-01"
)

close_prices = data["Close"]


returns = close_prices.pct_change().dropna()


last_price = close_prices.iloc[-1]
simulations = 100
days = 30

mean_return = returns.mean()
std_dev = returns.std()


simulation_df = np.zeros((days, simulations))

for i in range(simulations):
    price = last_price
    for j in range(days):
        price = price * (1 + np.random.normal(mean_return, std_dev))
        simulation_df[j, i] = price


plt.plot(simulation_df)
plt.title("Monte Carlo Simulation - AAPL")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()