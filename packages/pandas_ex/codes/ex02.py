# -*- coding : utf-8 -*-
import pandas as pd
import xlrd
#读取csv文件的问题
data = pd.read_csv("packages/pandas_ex/codes/test.csv")
data

data.shape
#data.index = ['first','second','third','forth']  改变DataFrame的索引值

#data.columns = ['first','second','third','forth','fifth']   改变DataFrame的列名
data['name'][1]
data.sort_values('physics', ascending=False)
data['math']
data[:1]
data[1:3]
dir(pd)
datas = pd.read_excel("packages/pandas_ex/codes/test.xlsx")
datas
datas.columns
datas.index
