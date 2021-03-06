#### 格式化字符

%d：整型

%f：浮点型

%s ：解析字符串，但对于整型、浮点型同样可以解析，可以看做是先把整形和浮点型转换成了字符型，再进行解析

![01.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/01.jpg?raw=true)

%r：可解析整型、浮点型、字符型，但需要注意和%s的区别，会打印出所有的字符：

![02.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/02.jpg?raw=true)

#### 单引号、双引号、三引号

都可以用来表示字符串。

当我用单引号来表示一个字符串时，如果要表示 Let's go 这个字符串，必须这样：s4 = 'Let\'s go'，要使用转义符 \ , 如果你的字符串中有一大堆的转义符，看起来肯定不舒服，如果用双引号可以解决这个问题，如下：s5 = "Let's go"。这时，python知道你是用 " 来表示字符串，所以python就把字符串中的那个单引号 ' , 当成普通的字符处理了。是不是很简单。对于双引号，也是一样的，下面举个例子s6 = 'I realy like "python"!'，如果我使用“I realy like "python"!”，就会报语法错误，这时就需要用到单引号了。

单引号和双引号表示的字符通常要写成一行，如果要写成多行，那么就要使用\ (“连行符”)吧，如
s2 = "hello,\
world"
如果你用3个双引号的话，就可以直接写了，如下：
s3 = """hello,
world,
hahaha."""

其中，"""......."""，'''....'''，都可用于多行注释

#### 逗号的使用

print语句输出时，默认的会在后面加上换行，跳到下一行，但加了逗号之后，换行就变成了空格：  

![03.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/03.jpg?raw=true)

#### 转义字符

\n：换行

\t：下一制表符

\'：表示'

\"：表示"

#### 输入输出

输入：raw_input()，返回值为字符串型（%r格式）

**如何判断raw_input方法接收到的字符串是否为数字**

str = raw_input("please input the number: ")
str.isalnum() 所有字符都是数字或者字母
str.isalpha() 所有字符都是字母
str.isdigit() 所有字符都是数字
str.islower() 所有字符都是小写
str.isupper() 所有字符都是大写
str.istitle() 所有单词（以空格分隔）都是首字母大写，像标题
str.isspace() 所有字符都是空白字符、\t、\n、\r

**字符串索引，从左到右默认从0开始，从右到左默认从-1开始**

上述的主要是针对整型的数字，但是对于浮点数来说就不适用了，那么浮点数怎么判断呢，一直在纠结这个问题，为什么非要区分整型和浮点数呢，既然都是参与运算的，全部适用浮点数不是一样吗，在得到结果后，直接转换为int型不是一样吗，为什么非要纠结在前期去判断是否整型或者浮点数呢，有了这样的思路，下面就好做了，例如：
我们可以通过异常来判断，异常语法如下：
try:
{statements}
exception: {Exception Objects}
{statements}

str = raw_input("please input the number:")
try:
f = float(str)
exception ValueError:
print("输入的不是数字！")

还有一种纯粹判断是否为浮点数的方法，使用正则表达式：

1. 引用re正则模块
   import re
   float_number = str(input("Please input the number:"))
2. 调用正则
   value = re.compile(r'^[-+]?[0-9]+.[0-9]+$')       r表示以%r原生字符串形式，不考虑字符的转义
   result = value.match(float_number)
   if result:
   print "Number is a float."
   else:
   print "Number is not a float."
3. 关于这个正则表达式，解释一下：
   ^[-+]?[0-9]+.[0-9]+$
   ^表示以这个字符开头，也就是以[-+]开头，[-+]表示字符-或者+之一， ?表示0个或1个，也就是说符号是可选的。 同理[0-9]表示0到9的一个数字，+表示1个或多个，也就是整数部分。 .表示的是小数点，\是转义字符因为.是特殊符号（匹配任意单个除\r\n之外的字符）， 所以需要转义。 小数部分同理，$表示字符串以此结尾

给命令行脚本传递变量：

![04.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/04.jpg?raw=true)

![05.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/05.jpg?raw=true)

`argv`是所谓的“参数变量(argument variable)”，这个变量包含了你传递给 Python 的参数。第 3 行将 `argv` “解包(unpack)”，与其将所有参数放到同一个变量下面，我们将每个参数赋予一个变量名： `script`, `first`, `second`, 以及 `third`，将所有的参数依次赋予左边的变量名。

#### 文档生成工具

pydoc：只能在命令行中使用，IPython、script中都不行；![06.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/06.jpg?raw=true)

#### 读写文件

![07.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/07.jpg?raw=true)

处理完文件后，需要将其关闭：txt.close()

`1` read：读取文件内容，返回的是一个字符串

`2` readline：读取文件内容的一行，返回的是一个字符串

`3` write(stuff)：将stuff（通常是字符串）写入文件

`4` truncate：清空文件

`5` close：关闭文件

![08.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/08.jpg?raw=true)

**需要注意的：** 当需要对文件对象进行操作时，必须以写的形式打开文件：open(..，'w')；用write()向文件写入内容时，没有自带换行，如需换行，需要自己加上’‘\n''；默认的write是覆盖写，就算没有对文件清空，最后得到的文件也只有write进去的内容；如果需要追加写，要用追加的形式打开文件：open(..，'a')，同样可以进行清空、写入等一些列操作。

在读写文件时，有一个文件操作指针，对文件read()完一遍之后，该指针已经处于文件末了，如果再次进行read(),则得到空，此时需要把该指针移至文件起始位置，用seek()函数。类似的，当用w形式写文件时，文件操作指针位于文件起始位置，而以a形式写文件时，文件操作指针位于文件末尾。

> tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。
>
> seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
>
> 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。如果from缺省，则默认是0，以文件的开头作为参开位置。

#### 函数

函数有多个输入参数时，可以使用*args接收，然后再进行解包，类似于命令行脚本的argv：

![09.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/09.jpg?raw=true)

编译：需要调用其他py文件的函数时，需要import ***（没有.py后缀），此时相当于.py文件编译成.pyc文件，调用方法为：文件名.函数名。

内置sorted()函数，如果待排序的是字符串，则默认使用每个字符串第一个字母的ASCII码值来排序。

#### 快捷键

ctrl+d：退出Python环境

ctrl+c：退出当前运行程序

#### 标识符

- **\_\_foo\_\_**: 定义的是特殊方法，类似 \_\_init\_\_() 之类的。
- **_foo**: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
- **__foo**: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
- Python不允许实例化的类访问私有数据，但你可以使用 **object._className__attrName** 访问私有属性

####关键字（非0即为真）

| 关键字      | 作用                                       |
| -------- | ---------------------------------------- |
| and      | 逻辑与操作， x and y， 如果 x 为 False，x and y 返回 x 的计算值，否则它返回 y 的计算值。 |
| del      | 用于List列表操作，删除一个或者连续几个元素，del a[0]，del a   |
| from     | 用于导入相应的模块，from ... import                |
| not      | 逻辑非，not x，如果 x 为 True，返回 False 。如果 x 为 False，它返回 True，返回的是bool值 |
| while    | while循环                                  |
| as       | 与其他关键字合用，import xx as xxx                |
| elif     | 和if配合使用                                  |
| global   | 定义全局变量（想要给全局变量赋值，先global一下）              |
| or       | 逻辑或，x or y， 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值 |
| with     | 和as一起使用                                  |
| assert   | 表示断言                                     |
| else     | 与if一起使用                                  |
| if       | if语句选择分支                                 |
| pass     | 意思就是什么都不做                                |
| yield    | 类似return，它返回的是一个生成器                      |
| break    | 终止循环                                     |
| except   | 和try一起使用，用来捕获异常                          |
| import   | 用来导入模块                                   |
| print    | 打印                                       |
| class    | 定义类                                      |
| exec     | 用来执行存储在字符串或者文件中的python语句                 |
| in       | 查找列表中是否包含某个元素，或者字符串a是否包含字符串b             |
| raise    | 显示地引发异常                                  |
| continue | 跳过continue后面循环块中的语句，继续执行下一次循环            |
| finally  | 看到finally语句，必然执行finally语句的代码             |
| is       | python中的对象包含三要素：id、type、value。id用来唯一标识一个对象，type标识对象的类型，value是对象的值。is判断的是a对象是否就是b对象，是用id来判断的，==判断的是a对象的值是都和b对象的值相等，是通过value来判断的 |
| return   | 跳出函数，返回值                                 |
| def      | 定义方法                                     |
| for      | 循环                                       |
| lambda   | 匿名函数                                     |
| try      | try except处理异常                           |

#### 数据类型

| 数据类型   | 意义   |
| ------ | ---- |
| True   | 真    |
| False  | 假    |
| None   | 空    |
| string | 字符串  |
| number | 数字   |
| float  | 浮点   |
| list   | 列表   |

#### 操作符号

| 操作符号 | 意义                                  |
| ---- | ----------------------------------- |
| +    | 加                                   |
| -    | 减                                   |
| *    | 乘，对于非数字类型，表示重复操作，‘a'*2 = 'aa'       |
| **   | 幂 2**3 = 8                          |
| /    | 除                                   |
| //   | 取整除，9//2=4，9.0//2.0=4.0，9.0/2.0=4.5 |
| %    | 取模                                  |
| <    | 小于                                  |
| >    | 大于                                  |
| <=   | 小于等于                                |
| >=   | 大于等于                                |
| ==   | 等于                                  |
| !=   | 不等于                                 |
| <>   | 不等于，类似!=                            |
| @    | 函数修饰符                               |
| ;    | 用于在一行中书写多条语句                        |
| +=   | a= a+b                              |
| -=   | a= a-b                              |
| *=   | a*=b a=a*b                          |
| /=   | a=a/b                               |
| //=  | a=a//b                              |
| %=   | a=a%b                               |
| **=  | a=a**b                              |

#### 数据结构

- #### List（列表）  可当做是list

  [  ,  ,  ,]

  pop

  append

  del

  join

  len(list)


- #### dict（字典） 可当做是HashMap

  a = {  key : value , key : value ,}

  无序的对象集合，只能通过Key来获取

  del

  > 注意del和clear()的区别：
  >
  > del是直接删除这个对象，而clear()是清空内容

  ![02.jpg](https://github.com/ChaoZeyi/python/blob/master/%E8%8F%9C%E9%B8%9F%E6%95%99%E7%A8%8B/photos/02.jpg?raw=true)

  ​

  items(),得到的是list类型

  for key in a （只能通过key来遍历，不能通过value）

- #### tuple（元祖）  不可二次赋值，也不能删除，相当于只读列表

  （  ,  ,   ,   ,）

- #### class（类）

  ​  声明对象时，相当于执行的\_\_ init\_\_函数（构造函数），self表示的是类的对象     

#### 数据类型转换

| 函数                    | 描述                              |
| --------------------- | ------------------------------- |
| int(x [,base])        | 将x转换为一个整数                       |
| long(x [,base] )      | 将x转换为一个长整数                      |
| float(x)              | 将x转换到一个浮点数                      |
| complex(real [,imag]) | 创建一个复数                          |
| str(x)                | 将对象 x 转换为字符串                    |
| repr(x)               | 将对象 x 转换为表达式字符串                 |
| eval(str)             | 用来计算在字符串中的有效Python表达式,并返回一个对象   |
| tuple(s)              | 将序列 s 转换为一个元组                   |
| list(s)               | 将序列 s 转换为一个列表                   |
| set(s)                | 转换为可变集合                         |
| dict(d)               | 创建一个字典。d 必须是一个序列 (key,value)元组。 |
| frozenset(s)          | 转换为不可变集合                        |
| chr(x)                | 将一个整数转换为一个字符                    |
| unichr(x)             | 将一个整数转换为Unicode字符               |
| ord(x)                | 将一个字符转换为它的整数值                   |
| hex(x)                | 将一个整数转换为一个十六进制字符串               |
| oct(x)                | 将一个整数转换为一个八进制字符串                |

#### is 与 == 区别

> is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
>
> is判断为真时，==判断就一定为真，但反过来，==判断为真时，is判断就不一定为真

![01.jpg](https://github.com/ChaoZeyi/python/blob/master/%E8%8F%9C%E9%B8%9F%E6%95%99%E7%A8%8B/photos/01.jpg?raw=true)

python 不支持 switch 语句，所以多个条件判断，只能用 elif 来实现

在atom中，如果存在raw_input()，不能用script来运行，必须用ctrl+alt+shift+enter，或者直接使用命令行，如果用script，会出现堵塞

> random.uniform(a,b)   随机生成给定范围的浮点数，a可以是上限，也可以是下限
>
> random.randint(a,b)     随机生成给定范围的整数，a必须是下限（a < b）

#### input()和raw_input()区别

> raw_input()是把用户输入的所有都当做字符串类型（%r）
>
> input()接收数字输入时，返回的就是数字类型
>
> a = input()
>
> 》1 
>
> type(a)
>
> 》int
>
> 而且可以接收表达式，相当于执行了eval()函数
>
> a = input()
>
> 》1 +2 
>
> a = 3
>
> 而且当input()接收字符串时，必须使用引号
>
> a = input()
>
> 》'ab' 
>
> a = 'ab'

while.....else

for......else

只有当while/for 正常运行结束时，才会运行else语句，如果是用break退出循环，就不会运行else语句

#### python 创建二维列表

```
list2d = [ [3 for i in range(3)] for i in range(4)]
list2d = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]
```

> 代码理解：对于i = 0、1、2、3，list2d[i]都是[3 for i in range(3)]，而[3 for i in range(3)]表示的是一个列表，[3,3,3]，所以对于i = 0、1、2、3，list2d[i] = [3,3,3]

#### 参数传递

在 python 中，类型属于对象，变量是没有类型的：

```
a=[1,2,3]

a="Runoob"
```

以上代码中，**[1,2,3]** 是 List 类型，**"Runoob"** 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。

### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

#### python 函数的参数传递：

- **不可变类型：**值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
- **可变类型：**引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

#### 全局变量与局部变量

一个程序的所有的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

在函数体中如果需要改变全局变量的值，需要申明global ###

> 函数内部的变量名如果第一次出现，且出现在=前面，即被视为定义一个局部变量，不管全局域中有没有用到该变量名，函数中使用的将是局部变量；
>
> 函数内部的变量名如果第一次出现，且出现在=后面，且该变量在全局域中已定义，则这里将引用全局变量，如果该变量在全局域中没有定义，当然会出现“变量未定义”的错误。

![03.jpg](https://github.com/ChaoZeyi/python/blob/master/%E8%8F%9C%E9%B8%9F%E6%95%99%E7%A8%8B/photos/03.jpg?raw=true)

#### package

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 \_\_init\_\_.py 文件！！！！该文件的内容可以为空。\_\_int\_\_.py用于标识当前文件夹是一个包。

考虑一个在 **package_runoob** 目录下的 **runoob1.py、runoob2.py、__init__.py **文件，test.py 为测试调用包的代码，目录结构如下：

```
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py
```

```
test.py
# coding: UTF-8 
# 导入 Phone 包
from package_runoob.runoob1 import runoob_1    
#（import的是函数名，可以直接import *，表示导入了该.py文件的所有函数）
from package_runoob.runoob2 import runoob_2 
runoob_1()
runoob_2()
```

