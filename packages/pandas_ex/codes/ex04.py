# -*- coding = utf-8 -*-
import numpy as pd
from pandas import Series, DataFrame
import pandas as pd
#修改指定位置的值
dates = pd.date_range('20130101', periods=6)
df = DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print df
df['A'] = 10
df
df.iloc[2,0] = 30
df
df.loc['20130101','A'] = 20
df
df.B[df.A > 10] = 5
df
df['E'] = np.nan
df
s = Series([1,2,3,4,5,6], index=df.index)enenenenenen1hzizhi
s
df['F'] = s
df
df['E'] = s
df
s1 = Series([11,21,31,41,51,61])
s1
df['E'] = s1
df
df['G'] = s1
df
