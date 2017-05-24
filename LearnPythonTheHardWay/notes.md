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

print语句输出时，默认的会在后面加上换行，但加了逗号之后，换行就变成了空格：  

![03.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/03.jpg?raw=true)

#### 转义字符

\n：换行

\t：下一制表符

\'：表示'

\"：表示"

#### 输入输出

输入：raw_input()，返回值为字符串型（%r格式）

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

#### 函数

函数有多个输入参数时，可以使用*args接收，然后再进行解包，类似于命令行脚本的argv









