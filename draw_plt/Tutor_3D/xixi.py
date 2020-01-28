from draw_plt.Tutor_3D import *


def r_p(x, y):
    return np.random.rand(x, y)


a = (10, 30,)
f = plt.figure()


class Pic:
    def __init__(self, loc_code):
        self.loc = f.add_subplot(loc_code)
        print(dir(self.loc))
    def colorful(self, ac, bc, cc):
        self.loc.scatter(r_p(*a), r_p(*a), c=ac, s=np.random.randn(10, 30) * 100)
        self.loc.scatter(r_p(*a), r_p(*a), c=bc, s=np.random.randn(10, 30) * 100)
        self.loc.scatter(r_p(*a), r_p(*a), c=cc, s=np.random.randn(10, 30) * 200, alpha=0.1)
        for tick in self.loc.get_xticklabels() + self.loc.get_yticklabels():
            tick.set_color('none')


Pic(111).colorful('blue', 'red', 'grey')

plt.show()
