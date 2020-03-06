import numpy as np
import matplotlib.pyplot as plt

a=np.random.rand(3,5,3)
t=a.shape
x=a[:,:,0]*100000
y=a[:,:,1]*1000000
z= a[:,:,2]
for _,name in zip(range(len(a)),['bmw','benz','audi']):
    params=dict(s=y[_]/600,alpha=0.3)
    plt.scatter(x[_],z[_],**params)
    for v,k in zip(x[_],z[_],):
        plt.text(v-1000,k,name)

plt.grid()
plt.show()