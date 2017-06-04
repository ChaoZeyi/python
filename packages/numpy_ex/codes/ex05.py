# -*- coding : utf-8 -*-
import numpy as np

a = np.arange(3)
b = a
b[0] = 100
a

c = a.copy()
c
a[0] = 200
c

d = [1,2]
e = d[:]
d[1] = 3
d
e
