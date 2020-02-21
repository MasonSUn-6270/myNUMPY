from draw_plt.Tutor_3D import *


def c(): return np.random.randn(500)

plt.style.use('dark_background')
f = plt.figure()
ax = Axes3D(f)
ax.plot3D(c()*50, c()*30, np.ones_like(c())*(-190),':', ms=20,c='gold',alpha=0.3)
ax.plot3D(c()*50, c()*30, np.ones_like(c())*(-150),':', ms=20, c='purple',alpha=0.3)
ax.plot3D(c()*30, c()*30, c()*30, 'cohere相关性', c='black', ms=140)
ax.plot3D(c()*20, c()*20, c()*20, 'cohere相关性', c='purple', ms=70)
ax.plot3D(c()*10, c()*10, c()*10, 'cohere相关性', c='yellow', ms=120)
ax.plot3D(c()*3, c()*3, c()*3, 'cohere相关性', c='purple', ms=50)
ax.plot3D(c()*1, c()*1, c()*1, 'cohere相关性', c='white', ms=200)
ax.set_title('Kobe',color='white')
ax.text(0, 0, 10, 'R\nI\nP\n',color = 'white')
for i in ax.get_xticklabels() + ax.get_yticklabels() + ax.get_zticklabels():
    i.set_color('none')
ax.grid(False)
print(dir(ax))
plt.show()
