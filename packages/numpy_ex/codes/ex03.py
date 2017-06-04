# -*- coding : utf-8 -*-
import numpy as np

a = np.array([1,2,3])
a.shape
b = np.array([[1,2,3],[2,3,4]])
b.shape
# 上下合并
c = np.vstack((a,b))
c

# 左右合并
c = np.hstack((b,b))
c
c = np.hstack((a,b))
