Title: GameConqueror 0.09 -- Linux 游戏作弊工具
Date: 2010-01-11 10:59
Author: toy
Category: Games
Tags: GameConqueror
Slug: gameconqueror-0-0-9

{ 撰文/[Wang Lu](http://coolwanglu.blogspot.com) }

你是否喜欢游戏修改？你是否一直在寻找“CheatEngine for Linux”?  
那么你不该错过 GameConqueror。

GameConqueror 是一款 Linux 游戏修改工具，用 PyGTK 写成，以 scanmem
作为后端。

[![GameConqueror](http://i.linuxtoy.org/images/2010/01/gameconqueror-thumb.png)](http://i.linuxtoy.org/images/2010/01/gameconqueror.png)

我的目标是实现 CheatEngine 的大多数功能，成为名副其实的“CheatEngine  
for Linux”。

现在已经实现了基本的搜索功能，支持不同的数据类型和搜索类型，如下：

+ 数据类型：

- 不同长度的类型：int{8/16/32/64}、float{32/64}  
- 未知长度的类型：int、float  
- 未知类型：number  
- 字节串和字符串：bytearray、string

+ 搜索类型：相等、大于、小于、变化、未变、增大、减少

### 下载

PPA：  

我只在 64 bit Karmic
下进行了测试，其他环境如果不能正常使用请告知，谢谢。

SVN：  
svn checkout http://scanmem.googlecode.com/svn/trunk/ scanmem

主页：  

下载时注意选择 0.09 版本。

运行需要 Python 和 Python-GTK2，编译需要  
libreadline（大多数发行版应该都默认安装吧）。

GameConqueror 的 bug
或者不恰当的使用会导致程序崩溃，请务必注意备份数据、资料等等。

安装后应该在“游戏”类别里出现菜单项，也可以直接运行  
gameconqueror（请在终端内运行，见下）。

查看 Value 的悬停提示（tooltip）可以了解各种搜索语法，参考了金山游侠。

至于那个烦人的终端窗口，现在只能在这里看到搜索进度和出错信息。我之前主要是实现  
scanmem 的各种功能，界面改进则是下个版本的目标。

未来考虑实现的功能：

+ 界面改进（搜索进度条，出错提示，用户交互等等）  
+ 指针搜索  
+ 可选的浮点数取整方式  
+ 十六进制内存查看/编辑器

不会实现的功能：

+ 变速（类似变速齿轮，这个不是不想写，而是不会写，有谁能教教我？）  
+ 反汇编器

欢迎使用，感谢反馈。

{ Thanks Wang Lu. }
