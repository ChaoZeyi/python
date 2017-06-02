#  -*- coding: UTF-8 -*-
#函数的值传递
def changeNun(a):
    a += 1
    return a
b = 10
print changeNun(b)
print b



def changeList(list_a):
    list_a.append('a')
    return list_a
list_b = [1,2,3]
print changeList(list_b)
print list_b


#关键字参数
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
printinfo( age=50, name="miki" )
printinfo("miki",40)


#缺省参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
printinfo( age=50, name="miki")
printinfo("miki",40)
printinfo( name="miki" )


#不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
printinfo()
printinfo( 10 )
printinfo( 70, 60, 50 )

#lambda函数
sum = lambda arg1, arg2, arg3: arg1 + arg2;
print "相加后的值为 : ", sum( 10, 20, 30)
print "相加后的值为 : ", sum( 20, 20, 20)


def reverse(li):
    for i in range(0, len(li)/2):
        temp = li[i]
        li[i] = li[-i-1]
        li[-i-1] = temp

l = [1, 2, 3, 4, 5]
reverse(l)
print(l)


globvar = 0

def set_globvar_to_one():
    global globvar
    globvar = 1
def set_globvar_to_two():
    # global globvar
    globvar = 2

def print_globvar():
    print(globvar)

print_globvar()
set_globvar_to_one()
print  globvar        # 输出 1
print_globvar()
set_globvar_to_two()
print  globvar        # 输出 1
print_globvar()  # 输出 1，函数内的 globvar 已经是全局变量


num = 100
def func():
    num += 1
    print num
func()
