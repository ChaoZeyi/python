from sklearn import datasets
from sklearn import svm
import pickle
clf =  svm.SVC(gamma=0.001, C=100)
iris = datasets.load_iris()
iris
###############手写数字识别系统#########################
digits = datasets.load_digits()
digits
x = digits.data
y = digits.target
clf.fit(x[:-1], y[:-1])
clf.predict(x[-1])

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(x[-1])
