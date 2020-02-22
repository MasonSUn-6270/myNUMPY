import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(6,6))
per_line =5
for no in range(30):
    ax = fig.add_subplot(5,6,no+1)
    ax.plot(np.random.rand(4,5),np.random.rand(4,5))
    ax.set_xticks([])
    ax.set_yticks([])
    [ax.spines[i].set_color('none') for i in ['top', 'bottom', 'left', 'right']]
plt.show()