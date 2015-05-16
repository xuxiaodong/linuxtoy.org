Title: gsnapshot－小巧的截屏程序
Date: 2006-12-14 18:45
Author: toy
Category: Apps
Slug: gsnapshot

经常撰写软件教程的朋友，身边总是离不开截屏程序。今天，我发现了一个名叫
[gsnapshot](http://www.softcraft.org/gsnapshot/)
的程序，它的主要作用就是截取屏幕，并将其保存为图片。gsnapshot 使用 GTK2
编写，依赖很少，使用起来感觉不错。

在功能方面，gsnapshot
当前支持截取整个屏幕、窗口、区域这几种类型，可以将截取的屏幕保存为
PNG、JPEG、BMP 格式。同时，gsnapshot
也具有延时截屏功能。如果有打印机，也可以在 gsnapshot
中直接将截取的屏幕打印输出。

![gsnapshot](http://i.linuxtoy.org/i/2006/12/gsnapshot.jpg)  
*gsnapshot 截图*

目前，使用 gsnapshot，需要自己编译，不过，仅需 `make -f Makefile.unix`
这一步。还算简单吧。

[ [Download
gsnapshot](http://www.softcraft.org/gsnapshot/downloads.html) ]
