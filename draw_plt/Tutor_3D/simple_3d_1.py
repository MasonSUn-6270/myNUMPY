from draw_plt.Tutor_3D import *

f = plt.figure()
ax1 = f.add_subplot(222, projection='3d')
x = np.linspace(0, 400, 10)
y = np.linspace(0, 400, 10)
x, y = np.meshgrid(x, y)
z = np.arange(100).reshape(10, 10) ** 2
ax1.plot_wireframe(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax1.plot_wireframe(-x, -y, z, rstride=1, cstride=1, ls=':', cmap=plt.get_cmap('rainbow'))
ax1.plot_surface(-x, -y, -z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax1.text(100, 100, 9000, 'hello world')
ax1.text3D(100, 100, -9000, 'hello world')
ax2 = f.add_subplot(223, projection='3d')
ax2.scatter3D(-x, y, z, c='lime', s=40)
ax3 = f.add_subplot(224)
ax3.plot(x, y, 'H')
plt.show()
