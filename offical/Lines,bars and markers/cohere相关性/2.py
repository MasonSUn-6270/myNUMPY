import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(1000)

y = x**2
x1 = np.arange(600)
print(
    x1
)
y1=x1**2

fig,axes = plt.subplots(3,1)

axes[0].plot(x,y,)
axes[1].cohere(x1,y1)
axes[2].cohere(y1,x1)
plt.savefig('2')
plt.show()