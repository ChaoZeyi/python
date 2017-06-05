#### numpy

同为ndarray，注意一维矩阵和数组的区别：

![01.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/01.jpg?raw=true)

b[0]是一个一维矩阵，大小为（1，N）

c是一个数组，大小为（N，）   

#### pandas

对于DataFrame类型数据，可以通过列名作为索引进行访问，但不能通过行的索引访问，不管是默认行索引还是自定义行索引，但可以使用[:]跨越多行。

而且需要注意，使用[:]跨越多行时，使用默认行索引时，是一个半开半闭区间，使用自定义索引时，是全闭空间。