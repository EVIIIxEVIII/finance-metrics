import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv("clean_ibm.csv")
data['Date'] = pd.to_datetime(data['Date'], format="ISO8601")
data = data.sort_values(by='Date')

data['HLOC'] = (data['Open'] + data['Close'] + data['Low'] + data['High']) / 4
data['Log_return'] = np.log(data['HLOC'] / data['HLOC'].shift(1))

data['rv_2d'] = data['Log_return'].rolling(window=2).std()
data['rv_20d'] = data['Log_return'].rolling(window=20).std()
data['Variance_20d'] = data['rv_20d']**2

mean_price = data['Log_return'].mean()
mean_rv = data['rv_20d'].mean()

print("Mean HLOC: ", mean_price)
print("Mean RV: ", mean_rv)

data.dropna(inplace=True)

def compute_mu():
    mu = data['Log_return'].mean()
    return mu * 252

def compute_theta():
    theta = data['Variance_20d'].mean()
    return theta * 252

def compute_kappa():
    data['Variance_lagged'] = data['Variance_20d'].shift(1)
    data.dropna(inplace=True)

    X = data['Variance_lagged']
    Y = data['Variance_20d']

    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    b = model.params[1]

    kappa = 1 - b
    return kappa

def compute_xi():
    data['Variance_change'] = data['Variance_20d'].diff()
    xi = data['Variance_change'].std()
    return xi * np.sqrt(252)

def compute_rho():
    return data[['Log_return', 'rv_2d']].corr().iloc[0, 1]

mu = compute_mu()
theta = compute_theta()
kappa = compute_kappa()
xi = compute_xi()
rho = compute_rho()

print(f"The mu     (average return):           {mu}")
print(f"The theata (long term variance):       {theta}")
print(f"The kappa (mean reversion return):     {kappa}")
print(f"The xi (volatility of volatility):     {xi}")
print(f"The rho (cor of price and volatility): {rho}")
