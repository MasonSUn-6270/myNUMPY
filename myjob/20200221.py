import numpy as np
import matplotlib.pyplot as plt



fig,ax = plt.subplots()
ax.plot(np.random.rand(20,20),np.random.rand(20,20),dashes=[10, 10, 50, 20])
ax.plot(np.random.rand(20,20),np.random.rand(20,20),dashes=[10, 10, 50, 20])
# ax.errorbar(np.random.rand(5,5),np.random.rand(5,5),yerr=0.2,c='white')

a=0.1
x = [-a, -a, 1+a, 1+a]
y = [-a, 1+a, 1+a, -a]
ax.fill(x, y,alpha=0.1)

def a():
    return np.random.randint(0,100,(5,2))/100

def b():
    temp = np.random.randint(0,100,(1,2))/100
    return temp[0]




ax.broken_barh([(0.5,0.2),(0.9,0.12)],(0,0.5),facecolor= 'blue',alpha=0.2)
ax.broken_barh([(0.5,0.2),(0.9,0.12)],(0,-0.03),facecolor= 'black')
x1= np.linspace(0,1,100)
y1 = np.sin(3*x1*np.pi)
y2 = 1/np.sin(30*x1*np.pi)/10000000000000

ax.fill_between(x1,y2,y1+0.5)
plt.show()