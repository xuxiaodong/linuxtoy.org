Title: PLaunch：快捷方式管理工具
Date: 2008-11-27 13:49
Author: toy
Category: Apps
Tags: PLaunch, Python
Slug: plaunch

[作者/volans]

Windows 和 Linux
系统都支持全局快捷键，你可以把常用的程序和快捷键绑定，需要的时候快捷键一按，一切近在眼前，设计真是方便啊。但是有时候我们也面临各种各样的困扰：

1.  快捷键冲突，自己定义的快捷键已经被使用；
2.  想快速运行的程序太多，快捷键用完了；
3.  快捷键太多了，记不起来那么多，有违初衷；

如果你也为这样的问题烦恼，那 PLaunch 是一个新的选择。PLaunch
是一个快捷方式管理工具，它是一个快捷方式的集合，你可以通过它快速呼叫任何你设定的程序，再也不用担心冲突、快捷方式庞大和遗忘。

![PLaunch](http://i.linuxtoy.org/images/2008/11/plaunch.png)  
*PLaunch 主窗口*

PLaunch 是用 Python 和 Pygtk 实现的，可在 Linux 及 Windows
系统中运行。另外在 Windows 和 Linux 下有着不同的需求库文件。 其中，在
Linux 下需要 pygtk 和 xlib；Windows 下则需 pygtk、pywin32 及 pyhook。

项目主页：<http://code.google.com/p/plaunch/>  
下载地址：<http://code.google.com/p/plaunch/downloads/list>  
使用说明：<http://code.google.com/p/plaunch/wiki/Quickstart>
