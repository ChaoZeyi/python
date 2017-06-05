# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dates = pd.date_range('20130101', periods=6)
df = DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print df
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
df
df.dropna(axis=1,how='all')
#df.fillna(value=0)
df.isnull()
np.any(df.isnull())
s = Series(['False','True'])
s
list1 = ['True', 'False']
np.any(list1)
