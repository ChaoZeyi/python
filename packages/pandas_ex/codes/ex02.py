# -*- coding : utf-8 -*-
import pandas as pd
import xlrd
#读取csv文件的问题
data = pd.read_csv("pandas_ex/codes/test.csv")
data
data.shape
data.index
data.columns
data['name'][1]
data.sort_values('physics', ascending=False)
data
data['math']
data[:1]
data[1:3]
dir(pd)
datas = pd.read_excel("pandas_ex/codes/test.xlsx")
datas
datas.columns
