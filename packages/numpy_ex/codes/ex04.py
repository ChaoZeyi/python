# -*- coding : utf-8 -*-
import numpy as np
############分割##############
a = np.arange(12).reshape((3,4))
a
np.split(a,2,axis=1)   #axis=0表示对行进行分割，axis=1表示对列进行分割
b = np.split(a,3,axis=0)
b
b[0]
type(b[0])
c = np.array([1,2,3])
type(c)
c
b[0][0]
c[0]
b[0].shape
c.shape
type(b[0][0])


d = np.array_split(a,3,axis=1)
d
d = np.vsplit(a,3)
d
d = np.hsplit(a,2)
d
