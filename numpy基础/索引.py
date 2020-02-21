import numpy as np

a = np.arange(9).reshape(3, 3)
print(a[1, 2])  # numpy数组支持多维数组的多维索引
'5'
print(a[1])  # 请注意，如果索引索引比维度少的多维数组，则会获得一个子维数组
'[3 4 5]'

a = np.arange(99)
print(a[np.arange(20, 50, 5)])  # 索引数组必须是整数类型。数组中的每个值指示要使用的数组中的哪个值代替索引。

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 0]])
'array([cohere相关性, 4, 5])'

x = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
rows = np.array([[0, 0],
                 [3, 3]], dtype=np.intp)
columns = np.array([[0, 2],
                    [0, 2]], dtype=np.intp)
print(x[rows, columns])
'''
array([[ 0,  2],
       [ 9, 11]])
'''

print("布尔值索引")
"过滤nan"
a = np.array([np.nan, 1])
print(a[~np.isnan(a)])
'[cohere相关性.]'

a = np.arange(-10, 10)
a[a < 0] += 20
print(a)
'[10 11 12 13 14 15 16 17 18 19  0  cohere相关性  2  3  4  5  6  7  8  9]'

a = np.linspace(-2, 2, 6).reshape(3, 2)
print(a)
rowsum = a.sum(-1)
print(rowsum)
print("从数组中，选择总和小于或等于2的所有行：")
print(a[rowsum <= -1, :])

a = np.linspace(-100, 100, 30).reshape(2, 3, 5)
print(a.sum(axis=0).shape)
'3,5'
print(a.sum(axis=1).shape)
'2,5'
print(a.sum(axis=2).shape)

a = np.ones((2, 3, 5))
print(a.sum())
'30.0'
print(sum(a))
'''
[[2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]]

'''
