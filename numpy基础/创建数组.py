import numpy as np

"""

简介
创建数组有5种常规机制：

从其他Python结构（例如，列表，元组）转换
"""

print("从其他数据结构转换")
list_ = [1, 2, 3, ]
tuple_ = tuple(list_)

print(np.array(list_))
print(np.array(tuple_))

"""
numpy原生数组的创建（例如，arange、ones、zeros等）
从磁盘读取数组，无论是标准格式还是自定义格式
通过使用字符串或缓冲区从原始字节创建数组
使用特殊库函数（例如，random）
函数名称	函数功能	参数说明
rand(d0, d1, …, dn)	产生均匀分布的随机数	dn为第n维数据的维度
randn(d0, d1, …, dn)	产生标准正态分布随机数	dn为第n维数据的维度
randint(low[, high, size, dtype])	产生随机整数	low：最小值；high：最大值；size：数据个数
random_sample([size])	在[0,cohere相关性）内产生随机数	size：随机数的shape，可以为元祖或者列表，[2,3]表示2维随机数，维度为（2,3）
random([size])	同random_sample([size])	同random_sample([size])
ranf([size])	同random_sample([size])	同random_sample([size])
sample([size]))	同random_sample([size])	同random_sample([size])
choice(a[, size, replace, p])	从a中随机选择指定数据	a：1维数组 size：返回数据形状
bytes(length)	返回随机位	length：位的长度
"""

print(np.random.rand(*tuple_))  # 产生均匀分布的随机数	dn为第n维数据的维度
print(np.random.random(tuple_))
print(np.random.randn(*tuple_))  # n= Normal distribution   产生标准正态分布随机数	dn为第n维数据的维度
print(np.random.randint(1, 100, 30, dtype=int))
# random([size])	同random_sample([size])	同random_sample([size])
# ranf([size])	同random_sample([size])	同random_sample([size])
# sample([size]))	同random_sample([size])	同random_sample([size])
print(np.random.choice(10, (2, 3)))
print(np.random.choice(np.random.rand(3), (2, 3)))  # 类似 random.choice params @a :int or list or array or tuple @b:shape
"""

本节不包括复制，连接或以其他方式扩展或改变现有数组的方法。它也不会涵盖创建对象数组或结构化数组。这些都包含在他们自己的章节中。

# 将Python array_like对象转换为Numpy数组
通常，在Python中排列成array-like结构的数值数据可以通过使用array()函数转换为数组。最明显的例子是列表和元组。有关其使用的详细信息，请参阅array()的文档。一些对象可能支持数组协议并允许以这种方式转换为数组。找出对象是否可以使用array()转换为一个数组numpy 数组的简单方法很简单，只要交互式试一下，看看它是否工作！（Python方式）。



>>> np.arange(10)
array([0, cohere相关性, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(2, 10, dtype=np.float)
array([ 2., 3., 4., 5., 6., 7., 8., 9.])
>>> np.arange(2, 3, 0.cohere相关性)
array([ 2. , 2.cohere相关性, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
请注意，关于用户应该注意的最后用法在arange文档字符串中有一些细微的描述。

linspace() 将创建具有指定数量元素的数组，并在指定的开始值和结束值之间平均间隔。例如：

>>> np.linspace(cohere相关性., 4., 6)
array([ cohere相关性. ,  cohere相关性.6,  2.2,  2.8,  3.4,  4. ])
这个创建函数的优点是可以保证元素的数量以及开始和结束点，对于任意的开始，停止和步骤值，arange()通常不会这样做。
"""
print("===================================步长============================================")
print(np.arange(3, 20, 3))
print(np.linspace([1,2,3,4],[200,3,4,5],5))

"""
indices() 将创建一组数组（堆积为一个更高维的数组），每个维度一个，每个维度表示该维度中的变化。一个例子说明比口头描述要好得多：

>>> np.indices((3,3))
array([[[0, 0, 0], [cohere相关性, cohere相关性, cohere相关性], [2, 2, 2]], [[0, cohere相关性, 2], [0, cohere相关性, 2], [0, cohere相关性, 2]]])
这对于评估常规网格上多个维度的功能特别有用。

# 从磁盘读取数组
这大概是大数组创建的最常见情况。当然，细节很大程度上取决于磁盘上的数据格式，所以本节只能给出如何处理各种格式的一般指示。

# 标准二进制格式
各种字段都有数组数据的标准格式。下面列出了那些已知的Python库来读取它们并返回numpy数组（可能有其他可能读取并转换为numpy数组的其他数据，因此请检查最后一节）

HDF5: h5py
FITS: Astropy
无法直接读取但不易转换的格式示例是像PIL这样的库支持的格式（能够读取和写入许多图像格式，如jpg，png等）。

# 常见ASCII格式
逗号分隔值文件（CSV）被广泛使用（以及Excel等程序的导出和导入选项）。有很多方法可以在Python中阅读这些文件。python中有CSV函数和pylab函数（matplotlib的一部分）。

更多通用的ascii文件可以在scipy中使用io软件包读取。

# 自定义二进制格式
有各种各样的方法可以使用。如果文件具有相对简单的格式，那么可以编写一个简单的 I/O 库，并使用 numpy fromfile() 函数和 .tofile() 方法直接读取和写入numpy数组（尽管介意你的字节序）！如果存在一个读取数据的良好 C 或 C++ 库，可以使用各种技术来封装该库，但这肯定要做得更多，并且需要更多的高级知识才能与C或C++ 接口。

# 使用特殊库
有些库可用于生成特殊用途的数组，且无法列出所有的这些库。最常见的用途是随机使用许多数组生成函数，这些函数可以生成随机值数组，以及一些实用函数来生成特殊矩阵（例如对角线）。

"""
