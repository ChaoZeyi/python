# -*- coding : utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
#Series
s = Series([1, 23, 'cc', 'whu'], index = [4, 3, 2, 1])
print s
print s.values

print type(s.values)
print s[1]
s[4] = 2
print s


#DataFrame
data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
f1 = DataFrame(data)
print f1
f2 = DataFrame(data, columns = ["name", "marks", "price", "delta"])
print f2
f3 = DataFrame(f2, index = [1, 2, 3, 4])
print f3
print f3.columns
print f3["name"][3]
f3["name"][3] = "yahoo"
print f3["name"][3]
f3["delta"] = 100
print f3
s3 = Series([50, 60], index = [1, 3])
f3["delta"] = s3
print f3
