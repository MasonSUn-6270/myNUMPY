import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y= np.exp(x)
fig,ax = plt.subplots()
tar = ax.bar(x,y)
print(tar)
for i in tar:
    tx=(i.get_x())
    ty=(i.get_height())
    ax.text(tx,1.01*ty,int(ty),ha='left',va='bottom')
plt.savefig('2')
plt.close()