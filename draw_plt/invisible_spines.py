from draw_plt import *
var = 1
while var <=150:
    plt.plot(np.random.rand(5,4),np.random.rand(5,4),'.',)
    var += 1

[plt.gca().spines[i].set_color('none') for i in ['top','bottom','left','right']]
plt.show()