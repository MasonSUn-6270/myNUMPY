from draw_plt import *

x = np.linspace(-100,100,200)
y = x ** 2 - 1000
z = 1/x
q = np.random.rand(100,100)
plt.plot(x, y, )
plt.plot(x, z, )
plt.plot(np.random.rand(100,100),np.random.rand(100,100),'h' )
plt.ylim()
ax =plt.gca()
set_func=[i for i in (dir(ax)) if 'set' in i]
get_func=[i for i in (dir(ax)) if 'get' in i]
print(set_func,'\n',get_func)
for i in ax.get_xticklabels()+ax.get_yticklabels():
    print(dir(i))
    i.set_color('purple')
    i.set_style('italic')
    i.set_weight('heavy')
    i.set_alpha(0.7)
    i.set_bbox({'facecolor':'red','alpha':0.5,'edgecolor':'white'})

plt.show()
