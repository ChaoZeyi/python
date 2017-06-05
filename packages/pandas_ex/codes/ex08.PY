# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#pandas的绘图

data = Series(np.arange(100))
data
data.plot()
plt.show()
data = DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data
data.plot()
plt.show()
ax = data.plot.scatter(x = 'A', y = 'B', label = 'class1',color="lightblue")
ax1 = data.plot.scatter(x = 'A', y = 'D', label = 'class2',ax = ax)
data.plot.scatter(x = 'A', y = 'C', label = 'class3',color="r",ax = ax1)
plt.show()
