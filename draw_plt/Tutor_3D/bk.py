from draw_plt.Tutor_3D import *
from random import choice as rc
colors = ['purple','gold']
f = plt.figure()
ax =Axes3D(f)
a=np.random.randn(100)*100
b= np.random.randn(100)*100
c = np.random.randn(100)*10000
A,B = np.meshgrid(np.random.randn(5)*100,100*np.random.randn(5))
ax.plot(a,b,c,'+',c='gold',)
ax.plot(a,b,-c,'1',c='purple')
for i in np.random.randn(100)*10:
    ax.plot_surface(A+i,B-i,np.random.randn(5,5)*10000,rstride=1, cstride=1, color= rc(colors),alpha=0.9)
plt.show()