# -*- coding : utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#pandas的合并:merge
left = DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],'key2':['K0','K1','K0','K1']})
right = DataFrame({'key1': ['K0', 'K1', 'K2', 'K3','K4'],
                              'C': ['C0', 'C1', 'C2', 'C3','C4'],
                              'D': ['D0', 'D1', 'D2', 'D3','D4'],'key2':['K0','K1','K2','K0','K0']})
left
right
res = pd.merge(left,right,on='key1')
res
res = pd.merge(left,right,how="outer")
res
res = pd.merge(left,right,how="left")
res
res = pd.merge(left, right, how="outer", indicator=True)
res
res = pd.merge(left, right, how="outer", indicator='indicator_name')
res
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
left
right
res = pd.merge(left, right, right_index=True, left_index=True)
res
res = pd.merge(left, right, right_index=True, left_index=True, how="outer")
res
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
boys
girls
res = pd.merge(boys, girls, on="k", suffixes=['_boy','_girl'])
res
