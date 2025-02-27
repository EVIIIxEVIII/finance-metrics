import numpy as np
import matplotlib.pyplot as plt

# Heston Model Parameters
S0 = 200     # Initial stock price
v0 = 0.04    # Initial variance

mu = 0.010440259988853659    # Expected return
theta = 0.0875747520494337 # Long-term variance
kappa = 0.9105743607865966  # Mean reversion speed
xi = 0.15456171818321993     # Volatility of volatility
rho = -0.7   # Correlation between dW_S and dW_v
dt = 1 / 252 # One trading day

# Initialize variables
S = S0
v = v0

price = [S0]
vol = [v0]

for i in range(504):
    Z1 = np.random.normal(0, 1)   # Standard normal for stock price
    Z2 = np.random.normal(0, 1)   # Independent standard normal
    Zs = Z1
    Zv = rho * Z1 + np.sqrt(1 - rho**2) * Z2  # Correlated noise

    v = max(v + kappa * (theta - v) * dt + xi * np.sqrt(v * dt) * Zv, 1e-8)
    S = S * np.exp((mu - 0.5 * v) * dt + np.sqrt(v * dt) * Zs)

    price.append(S)
    vol.append(v)

    print(f"Next volatility: {np.sqrt(v):.6f}")


plt.figure()
plt.xlabel("Time")
plt.ylabel("Price")
plt.plot(price)

plt.figure()
plt.xlabel("Time")
plt.ylabel("Volatility")
plt.plot(vol)

plt.show()
