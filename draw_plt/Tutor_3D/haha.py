from draw_plt.Tutor_3D import *

f = plt.figure()
ax = Axes3D(f)
a = np.random.randn(20)
b = np.random.randn(20)
a,b = np.meshgrid(a,b)
z= np.random.randn(20,20)
ax.plot_surface(a,b,z,rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'),alpha=0.5)
plt.show()
