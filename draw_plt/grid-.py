from draw_plt import *
k=plt.gca()
k.grid(color = 'red',ls=':',lw=3,alpha=0.5,axis='x')
k.set_ylim(-100,100)
pprint(dir(k))
pprint(k.__dict__)
pprint(k.__dict__['viewLim'])
a,b=(k.__dict__['viewLim']).ymin,(k.__dict__['viewLim']).ymax
k.set_yticks(tuple(i for i in np.linspace(a,b,20)))
k.set_yticklabels(['hi']*20)
plt.show()