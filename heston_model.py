import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
T = 1.0      # Total time (years)
N = 1000     # Number of time steps
dt = T / N   # Time step size
M = 1        # Number of simulated paths

# Heston Model Parameters
S0 = 100     # Initial stock price
v0 = 0.04    # Initial variance

mu = 0.05    # Expected return
theta = 0.04 # Long-term variance
kappa = 2.0  # Mean reversion speed
xi = 0.3     # Volatility of volatility
rho = -0.7   # Correlation between dW_S and dW_v

# Initialize arrays
plt.figure(figsize=(10, 5))
for i in range(25):
    S = np.zeros((M, N))  # Asset prices
    v = np.zeros((M, N))  # Variance
    S[:, 0] = S0
    v[:, 0] = v0

    # Simulate Heston Process
    for t in range(1, N):
        Z1 = np.random.normal(0, 1, M)  # Independent standard normal
        Z2 = np.random.normal(0, 1, M)
        ZS = Z1                          # First normal variable
        Zv = rho * Z1 + np.sqrt(1 - rho**2) * Z2  # Correlated second variable

        # Variance process (ensure v_t stays positive using max)
        v[:, t] = np.maximum(v[:, t-1] + kappa * (theta - v[:, t-1]) * dt +
                             xi * np.sqrt(v[:, t-1]) * np.sqrt(dt) * Zv, 0)

        # Asset price process
        S[:, t] = S[:, t-1] * np.exp((mu - 0.5 * v[:, t-1]) * dt +
                                      np.sqrt(v[:, t-1]) * np.sqrt(dt) * ZS)

    # Plot the simulated stock price path
    plt.plot(np.linspace(0, T, N), S.T, lw=1)

plt.xlabel("Time (Years)")
plt.ylabel("Stock Price")
plt.title("Heston Stochastic Volatility Model Simulation")
plt.show()

