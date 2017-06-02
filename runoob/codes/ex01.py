#  -*- coding: UTF-8 -*-
import time
import calendar
dict2 = { 'abc': 123, 98.6: 37 }
print dict2.items()
dict2.clear()
print dict2

dict2 = { 'abc': 123, 98.6: 37 }
del dict2
print dict2

dict = {['Name']: 'Zara', 'Age': 7};

print time.localtime(time.time())
print time.localtime()
print time.asctime()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print calendar.month(2017,6)
