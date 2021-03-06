import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(0)
x = np.arange(10.0)
y = np.sin(np.arange(10.0) / 20.0 * np.pi)

plt.errorbar(x, y, yerr=0.1)

y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 1
plt.errorbar(x, y, yerr=0.1, uplims=True)

y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 2
upperlimits = np.array([1, 0] * 5)
lowerlimits = np.array([0, 1] * 5)
plt.errorbar(x, y, yerr=0.1, uplims=upperlimits, lolims=lowerlimits)
y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 3
plt.errorbar(x, y, yerr=0.1, uplims=True, lolims=True)
y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 4
plt.errorbar(x, y, yerr=0.1, uplims=np.array([0, 4] * 5))

plt.xlim(-1, 10)
plt.savefig('1')