# -*- coding:utf-8 -*-
from sklearn import linear_model
from sklearn import datasets
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
reg.intercept_

iris = datasets.load_iris()
iris
iris['data'][:5]
digit = datasets.load_digits()
digit['data']
digit.target
digit.images[0]
digit['data'].shape
digit['data'][0]
