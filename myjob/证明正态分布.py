import numpy as np
import matplotlib.pyplot as plt

a= np.random.randn(100000)
bins = np.linspace(-4,4,1000)

fig,axes= plt.subplots()
axes.hist(a,bins)
level = {-4:'bad',0:'normal',4:'good'}
axes.set_xticks(list(level.keys()))
axes.set_xticklabels(list(level.values()))
plt.savefig('正态分布')