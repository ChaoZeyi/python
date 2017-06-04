# -*- coding : utf-8 -*-

import numpy a np

a = np.array([[1,2,3],[2,3,4]])
b = np.full((2,3), 3, dtype = int)
a
b
c = a+b
c
c = a * b
c
c = a * 3
c
c = a ** 2
c
c = np.sin(a)
c
print a < 2
c = np.arange(6).reshape((3,2))
c
d = np.dot(c,a)
d
d = c.dot(a)
d
e = np.random.random((2,3))
e
np.sum(e, axis=0)
np.min(e, axis=1)
np.max(e)
np.argmax(e)
np.argmin(e)
e[0][1]
e[0,1]
e[0][0:2]
e.flatten()
