from draw_plt import *

k = plt.gca()
k.grid(color='red', ls=':', lw=3, alpha=0.5, axis='x')
"设置y轴的limitation"
k.set_ylim(-100, 100)
pprint(dir(k))
pprint(k.__dict__)
pprint(k.__dict__['viewLim'])
a, b = (k.__dict__['viewLim']).ymin, (k.__dict__['viewLim']).ymax

"设置刻度"
"这种两种效果是一致的，库的语法的确非常强大"
k.set_yticks(tuple(i for i in np.linspace(a, b, 20)))
k.set_xticks(np.linspace(a, b, 20))
"这种两种效果是一致的，库的语法的确非常强大"
k.set_yticklabels(['hi'] * 20)
plt.xlim(-1,1)
plt.xticks([0.5,0.9],['$a\ bb$','bb'])
plt.show()
