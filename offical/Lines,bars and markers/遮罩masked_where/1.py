import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(1,3,sharex=True,sharey=True)
x = np.arange(0, 2*np.pi, 0.02)
y1 = np.sin(2*x)
ym1 = np.ma.masked_where(y1 > 0.5, y1)
ym2 = np.ma.masked_where(y1 < -0.5, y1)
for no,i in enumerate([y1,ym1,ym2]):
    ax[no].plot(x,i,label=str(no))
    ax[no].legend(loc=2)


fig.suptitle('Masked line demo')
plt.show()