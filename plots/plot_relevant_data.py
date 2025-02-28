import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./data/clean_spy.csv")

data['Date'] = pd.to_datetime(data['Date'], format="ISO8601")
data = data.sort_values(by='Date')

data['HLOC'] = (data['Open'] + data['Close'] + data['Low'] + data['High']) / 4
data['Relative_return'] = (data['Close'] - data['Close'].shift(1)) / data['Close'].shift(1)
data['Log_return'] = np.log(data['HLOC'] / data['HLOC'].shift(1))

data['Realized_volatility_20d'] = data['Log_return'].rolling(window=20).std()
data['Variance_20d'] = data['Realized_volatility_20d']**2

def plot_price():
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("HLOC")
    plt.plot(data["Date"], data["HLOC"], label="Price")
    plt.legend()

def plot_relative_return():
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Relative Return")
    plt.plot(data["Date"], data["Relative_return"], label="Relative Return")
    plt.legend()

def plot_variance():
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Variance")
    plt.plot(data["Date"], data["Variance_20d"], label="Variance")
    plt.legend()

def plot_rv():
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Realized volatility")
    plt.plot(data["Date"], data["Realized_volatility_20d"], label="Realized Volatility")
    plt.legend()

def plot_iv_black_scholes():
    pass

def plot_log_return():
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Log Return")
    plt.plot(data["Date"], data["Log_return"], label="Log Return")
    plt.legend()

plot_price()
plot_variance()
plot_log_return()
plot_relative_return()
plot_rv()

plt.show()

