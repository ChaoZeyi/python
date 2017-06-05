# -*- coding : utf-8 -*-
import numpy as np
from pandas import Series, DataFrame
dates = pd.date_range('20130101', periods=6)
df = DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print df
df.index

df[2]['A']
