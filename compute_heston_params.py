import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv("clean_ibm.csv")

data['Date'] = pd.to_datetime(data['Date'], format="ISO8601")
data = data.sort_values(by='Date')
data['HLOC'] = (data['Open'] + data['Close'] + data['Low'] + data['High']) / 4
data['Log_return'] = np.log(data['HLOC'] / data['HLOC'].shift(1))
data['Variance'] = data['Log_return']**2

data.dropna(inplace=True)

def compute_mu():
    mu = data['Log_return'].mean()
    return mu * 252

def compute_theta():
    theta = data['Variance'].mean()
    return theta * 252

def compute_kappa():
    data['Variance_lagged'] = data['Variance'].shift(1)
    data.dropna(inplace=True)

    X = data['Variance_lagged']
    Y = data['Variance']

    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    b = model.params[1]

    kappa = 1 - b
    return kappa

def compute_xi():
    data['Variance_change'] = data['Variance'].diff()
    xi = data['Variance_change'].std()
    return xi * np.sqrt(252)

def compute_rho():
    pass


mu = compute_mu()
theta = compute_theta()
kappa = compute_kappa()
xi = compute_xi()

print(f"The mu:     {mu}")
print(f"The theata: {theta}")
print(f"The kappa:  {kappa}")
print(f"The xi:     {xi}")
