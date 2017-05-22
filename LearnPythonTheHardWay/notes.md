#### 数据解析

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










