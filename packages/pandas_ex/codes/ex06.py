# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#pandas的合并:concat
df1 = DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = DataFrame(np.ones((3,4))*1, columns=['a1','b1','c1','d1'])
df3 = DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
res = pd.concat([df1,df2,df3], axis = 0)
res
res1 =  pd.concat([df1,df2])
res1
res2 = pd.concat([df1,df2], join='inner')
res2
res3 = pd.concat([df1,df2], axis = 1,join_axes=[df1.index])
res3
