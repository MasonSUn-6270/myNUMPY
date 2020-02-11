from draw_plt import *
x= np.linspace(-1,1,30)
y=np.sin(x**2)
z=np.random.randn(30)
print(len(plt.style.available))
for style in plt.style.available:
    plt.style.use(style)
    fig=plt.figure()
    plt.bar(x,z,width=1/30)
    plt.plot(x,y)
    plt.title(style)
    plt.savefig(f'./styles/{style}')
    print(f'{style} done!')