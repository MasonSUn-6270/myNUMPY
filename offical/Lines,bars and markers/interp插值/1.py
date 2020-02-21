import matplotlib.pyplot as plt
import numpy as np
"""
一维线性插值。



返回函数的一维分段线性插值

对于给定的离散数据点（`xp`，`fp`），计算值为'x`。



参数

----------

x:阵列

计算插值的x坐标。



xp:1-D浮动序列

数据点的x坐标，必须增加if参数

`未指定句点。否则，“xp”在内部排序

用“xp=xp%period”规范化周期边界。



fp:1-D浮点或复数序列

数据点的y坐标，长度与“xp”相同。



左：与fp对应的可选浮点或复数

“x<xp[0]`要返回的值，默认值为'fp[0]`。”。



右：与fp对应的可选float或complex

“x>xp[-1]`要返回的值，默认值为'fp[-1]`。



周期：无或浮动，可选

x坐标的周期。此参数允许

角x坐标的插值。参数“left”和“right”`

如果指定了“period”，则忽略。



.. 版本号：1.10.0



退换商品

-------

y：浮点或复数（对应于fp）或ndarray

插值，与“x”形状相同。



提高

------

值错误

如果“xp”和“fp”的长度不同

如果“xp”或“fp”不是一维序列

如果'period==0`



笔记

-----

不检查x坐标序列“xp”是否在增加。

如果“xp”没有增加，结果就是胡说八道。

增加的一个简单检查是："""
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)
yp = 10
xi = np.linspace(x[0], x[-1], 100)
yi = np.interp(xi, x, y, )
x2 = np.linspace(-1, 8, 200 )
y2 = np.interp(x2,x,y,left =0.5,right=0.5)
# Parameters:
# x : 要估计坐标点的x坐标值。
#
# xp : x坐标值，must be increasing if argument period is not specified. Otherwise, xp is internally sorted after normalizing the periodic boundaries with xp = xp % period.
#
# fp : y坐标值, same length as xp.
#
# right : 对应x > xp[-1]时fp的default is fp[-1].
#
# period : x坐标轴的周期，声明忽略左边或者右边的插值。

fig, ax = plt.subplots()
ax.plot(x, y, 'o', xi, yi, '.',x2,y2,'Y')
plt.show()