# -*- coding : utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
dates = pd.date_range('20130101', periods=6)
df = DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print df
type(df['A'])
df['A'][2]
df['A','20130103']
df[2]
df['20130103']
df['20130101':'20130104']
df[0:2]
df['20130101':'20130101']
df.loc['20130101']
df.loc['20130101',['A','B']]
df.loc['20130101':'20130103']
df.iloc[0]
df.iloc[0:2]
df.ix[0, ['A','B']]
df[df.A > 10]
