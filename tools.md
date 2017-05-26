## 软件安装

### atom

下载很方便，直接在官网下载最新版本https://atom.io/

一路next，然后安装一些必要的包![10.jpg](https://github.com/ChaoZeyi/python/blob/master/LearnPythonTheHardWay/photos/10.jpg?raw=true)

由于没有翻墙，无法在atom本地的安装库安装，采用的方法是：

安装node.js，使用其中的分支命令apm：apm install url

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
  > 可能会出现如下情况： pip不是内部或外部命令，也不是可执行程序  
  > 需要配置环境变量，步骤参考：  
  > http://www.crifan.com/run_pip_install_django_error_pip_is_not_recognized_as_an_internal_or_external_command_operable_program_or_batch_file/
  >
  > 安装ipython: pip install ipython，如果直接这样安装会报错，需要 Microsoft Visual C++ 9.0环境：
  >
  > error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
  >
  > 解决方法：在https://www.microsoft.com/en-us/download/details.aspx?id=44266下载安装
  >
  > ​



- minimap      (小窗图)

- Platformio Ide Terminal      （终端，命令行执行）

  > 解决无法下载安装的问题
  >
  > https://www.thjiang.com/2016/07/17/atom-%E6%97%A0%E6%B3%95%E5%AE%89%E8%A3%85%E6%8F%92%E4%BB%B6%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/  



#### pydev+myEclipse

> 一直无法在eclipse商店在线下载
>
> 采用离线下载时，各种因为python2.x，python3.x版本问题，安装失败

### pyCharm

> 安装成功
>
> 下载地址：https://www.jetbrains.com/pycharm/download/#section=windows
