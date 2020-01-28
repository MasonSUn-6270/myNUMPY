from draw_plt.Tutor_3D import *

f = plt.figure()
ax =Axes3D(f)
a = np.arange(1000)
ax.scatter3D(np.sin(a),np.cos(a-50)*2,(a-100)*2)
ax.scatter3D(np.sin(a-1000)**3,np.cos(a-50)*2,(a-100)*2,'-')
plt.show()