Title: Linux下使用的GCC编译器图形前端软件wxgcc
Date: 2011-03-23 13:21
Author: lovenemesis
Category: Development
Tags: GCC, wxpython
Slug: wxgcc-gcc-gui-frontend-in-linux

wxgcc 的全称是：wxpython gcc compiling toolkit
，它是一个在Linux环境下使用的，基于 wxpython 的GCC
编译器图形前端软件，可以用来快速的编译验证一个 C/C++ 程序，适合 C/C++
初学者使用！*感谢 wzc0066 来稿！*

对于Linux用户（尤其是C/C++初学者），不知您是否遇到过这种情况：在进行C/C++编程或是研究他人源代码的时候，发现对于某个C/C++语言特性不是很明确，于是就想自己创建一个小程序编译测试一下。一般需要进行如下操作（以C语言的helloworld为例）：

$ vi helloworld.c  
$ gcc helloworld.c -o helloworld  
$ ./helloworld

偶尔操作一回当然是没什么问题的，但如果需要频繁这么操作就会让人有些不耐烦了，wxgcc正是为解决这种问题而诞生。

**软件下载：**

-   可以下载最新版本的压缩包：<http://code.google.com/p/wxgcc/downloads/list>
-   或者直接从SVN获取最新的源代码：`svn checkout http://wxgcc.googlecode.com/svn/trunk/ wxgcc-read-only`

**软件依赖：**

-   wxpython 2.8
-   gcc编译环境

GCC一般Linux发行版都会默认安装的，对于Ubuntu用户可通过如下命令安装wxpython
2.8：

-   `$ sudo aptitude install python-wxgtk2.8 libwxgtk2.8-dev python-wxtools libwxbase2.8-0 libwxgtk2.8-0 python-wxglade`

**使用方法：**下载解压后执行里面的"wxgcc"启动脚本，或者参照README.txt文件！

**常用快捷键：**

-   F5 - 编译并执行
-   F11 - 全屏显示
-   Ctrl + L - 锁屏进入只读状态
-   Ctrl + F/R - 查找/替换
-   其它的见程序的菜单栏

**使用技巧：**

-   多使用tab键进行代码对齐
-   语法高亮在按下空格键或是Enter键时变更

**[更多信息](http://www.ucrobotics.com/?q=cn/forum/13)**

**软件截图：**

![](http://www.ucrobotics.com/downloads/wxgcc/c.jpg)

![](http://www.ucrobotics.com/downloads/wxgcc/cpp.jpg)

![](http://www.ucrobotics.com/downloads/wxgcc/help.jpg)
