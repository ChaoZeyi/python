# -*- coding: UTF-8 -*-

class Employee(object):
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):    #构造函数
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

em1 = Employee("aa", 1000)
print hasattr(em1, "name")
del em1.name
print setattr(em1, "name", "bb")

print Employee.__bases__
print Employee.__doc__;


class Point(object):
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "销毁"

pt1 = Point()
pt2 = Point()
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # 打印对象的id
del pt1
del pt2
del pt3
class Point1(Point):
     def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
print issubclass(Point1, Point)



class JustCounter(object):
    __secretCount = 0  # 私有变量
    _secretCount = 0
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        self._secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter._secretCount
print counter._JustCounter__secretCount
