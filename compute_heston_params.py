import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("clean_ibm.csv")

data['Date'] = pd.to_datetime(data['Date'], format="ISO8601")
data = data.sort_values(by='Date')
data['HLOC'] = (data['Open'] + data['Close'] + data['Low'] + data['High']) / 4
data['Log_return'] = np.log(data['HLOC'] / data['HLOC'].shift(1))


def compute_mu():
    mu = data['Log_return'].mean()
    return mu

def compute_theta():
    data['Realized_volatility_20d'] = data['Log_return'].rolling(window=20).std()
    data['Variance_20d'] = data['Realized_volatility_20d']**2
    theta = data['Variance_20d'].mean()
    return theta


def compute_kappa():
    pass

def compute_xi():
    pass

def compute_rho():
    pass


mu = compute_mu()
theta = compute_theta()
print(f"The mu:     {mu}")
print(f"The theata: {theta}")
print(f"The annualized theata: {theta * 252}")

