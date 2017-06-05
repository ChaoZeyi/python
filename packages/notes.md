#### numpy

同为ndarray，注意一维矩阵和数组的区别：

![01.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/01.jpg?raw=true)

b[0]是一个一维矩阵，大小为（1，N）

c是一个数组，大小为（N，）   

#### pandas

##### DataFrame

对于DataFrame类型数据，可以通过列名作为索引进行访问，但不能通过行的索引访问，不管是默认行索引（0——N-1）还是自定义行索引。

![02.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/02.jpg?raw=true)

![03.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/03.jpg?raw=true)

可以先通过列索引，得到一个Series类型，再根据0——N-1索引得到对应值。

![07.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/07.jpg?raw=true)

可以使用行索引[:]跨越多行，而且需要注意，使用[:]跨越多行，使用默认行索引时，是一个半开半闭区间，使用自定义索引时，是全闭空间。

![04.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/04.jpg?raw=true)

为了可以使用行索引，有两种方式：

- 使用自定义索引（标签）：loc

  ![06.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/06.jpg?raw=true)

- 使用默认索引（位置）：iloc

  ![08.jpg](https://github.com/ChaoZeyi/python/blob/master/packages/photos/08.jpg?raw=true)

使用索引（loc、iloc）来确定位置，修改对应位置的值。

注意区分内连接和外连接：![09.png](https://github.com/ChaoZeyi/python/blob/master/packages/photos/09.png?raw=true)

使用merge进行合并时，有四种连接方式：

inner：内连接

outer：外连接

left：左连接

right：右连接