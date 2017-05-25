## 软件安装

### atom

下载很方便，直接在官网下载最新版本https://atom.io/

一路next，然后安装一些必要的包![10.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/10.jpg?raw=true)

由于没有翻墙，无法在atom本地的安装库安装，采用的方法是：

安装node.js，使用其中的分支命令npm：npm install url

http://www.jianshu.com/p/9c8cd894d22d

其中最重要的是要找到你所要安装包的url地址，一般是github地址，可以在https://atom.io/packages搜索，例如，当你需要下载autocomplete-python的时候：

![11.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/11.jpg?raw=true)

选择github仓库地址

![12.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/12.jpg?raw=true)

然后进行安装，默认安装路径为C:\Users\Administrator\\.atom\packages

![13.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/13.jpg?raw=true)

需要安装的有如下几种包：

- linter    （编辑时若有语法错误，会有黄色警告或者红色报错信息）

- git-plus   （更方便的和git交互）

- autocomplete-python    （自动补全）

- highlight-selected        （选择部分高亮）

- highlight-line      （整行高亮）

- markdown-preview        （markdown的预览）

- script       

- ask-stack   （直接跳转，在stack-flow提问）

- Hydrogens(ipython,pip,jupyter)      （单步执行，需要先安装pip、ipython、jupyter）

  > 安装pip：https://pypi.python.org/pypi/pip#downloads
  >
  > 然后在解压之后的文件目录下执行python setup.py install
  >
  > 步骤参考：http://www.cnblogs.com/yuanzm/p/4089856.html
  >
  > 不需要配置环境

- minimap      (小窗图)

#### pydev+myEclipse

> 一直无法在eclipse商店在线下载
>
> 采用离线下载时，各种因为python2.x，python3.x版本问题，安装失败

### pyCharm

> 安装成功
>
> 下载地址：https://www.jetbrains.com/pycharm/download/#section=windows