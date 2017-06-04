# -*- coding : utf-8 -*-

import numpy as np
# 新建ndarray
array = np.array([[1,"aa",3],[2,3,4]])
array.shape
array.ndim
print array
array.size
array.dtype
# 指定类型新建ndarray
a = np.array([2,3,4], dtype=float)
a
# 新建全0数组
a = np.zeros((3,4), dtype=int)   #如果不指定类型，则默认是float64类型
a
# 新建全1数组
a =np.ones((3,4))
a.dtype
a
# 新建空数组
b = np.empty((3,4))
b.dtype
print b
# 自定义数组
b = np.full((3,4), 7)
b
c = np.arange(5)
c
