import numpy as np
import matplotlib.pyplot as plt

T = 1.0
N = 1000
dt = T / N
mu = 0

dW = np.random.normal(mu, np.sqrt(dt), N)

W = np.cumsum(dW)

plt.figure(figsize=(10, 5))
plt.plot(W, label="Brownian Motion $W_t$")
plt.xlabel("Time Steps")
plt.ylabel("Value")
plt.title("Brownian Motion Simulation")
plt.legend()
plt.show()

