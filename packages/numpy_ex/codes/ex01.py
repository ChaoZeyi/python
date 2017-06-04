# -*- coding : utf-8 -*-

import numpy as np
array = np.array([[1,"aa",3],[2,3,4]])
array.shape
array.ndim
print array
array.size
array.dtype
a = np.array([2,3,4], dtype=float)
a
a = np.zeros((3,4), dtype=int)   #如果不指定类型，则默认是float64类型
a
a =np.ones((3,4))
a.dtype
a
