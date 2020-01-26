from draw_plt import *

x = np.linspace(-10000, 10000)
y = x ** 3 - x ** 2
plt.plot(x, y, )
ax = plt.gca()
print(dir(ax.spines['bottom']))
ax.set_facecolor('pink')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

"传入tuple"
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.grid()
plt.show()
