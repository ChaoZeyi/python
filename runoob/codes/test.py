#  -*- coding: UTF-8 -*-
# import runoob.codes.package_python.hello1
# from runoob.codes.package_python import hello1
# from runoob.codes.package_python.hello1 import *
# 这三种用法在单步执行时效果都是一样的
from package_python.hello1 import *
# 在script中只能用这种方式，且从.py文件的同级目录开始
from package_python.hello2 import *

hello_1()
hello2()
hello_11()
