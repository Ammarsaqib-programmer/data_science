import numpy as np
def simulate_stock_prices(start_price, days, volatility, drift):
    daily_returns = np.random.normal(drift, volatility, days)
    prices = start_price * np.cumprod(1 + daily_returns)
    return prices


def main():
    print("Welcome to the Stock Market Simulator!")
    start_price = float(input("Enter the starting stock price: "))
    days = int(input("Enter the number of days to simulate: "))
    volatility = float(input("Enter daily volatility (e.g., 0.02 for 2%): "))
    drift = float(input("Enter daily expected return (e.g., 0.001 for 0.1%): "))

    prices = simulate_stock_prices(start_price, days, volatility, drift)

    print("\nSimulation Results:")
    print(f"Initial Price: ${start_price:.2f}")
    print(f"Final Price: ${prices[-1]:.2f}")
    print(f"Highest Price: ${np.max(prices):.2f}")
    print(f"Lowest Price: ${np.min(prices):.2f}")

