Title: Florence：虚拟键盘软件
Date: 2008-02-26 09:54
Author: toy
Category: Apps
Slug: florence

[Florence](http://florence.sourceforge.net/english.html) 是一款为 GNOME
桌面环境而开发的虚拟键盘软件。如果你的键盘因为损坏而使某些按键失灵的话，那么可以使用这款软件暂时顶替。

[![Florence
截图](http://i.linuxtoy.org/i/2008/02/florence-thumb.jpg)](http://i.linuxtoy.org/i/2008/02/florence.jpg)

目前，Florence 还没有为 Linux
发行版准备预编译的二进制包。要使用它，你必须从源代码编译安装。Florence
依赖于 libgnomecanvas 和
at-spi，在编译之前需准备好。然后，在下载其源代码后，可以按如下指令编译安装：

` $ tar jxvf florence-0.0.3.tar.bz2 $ cd florence && ./configure $ make $ su # make install`

你可以从这里[下载 Florence 的最新版
0.0.3](http://sourceforge.net/project/platformdownload.php?group_id=217749)。

**更新**

Arch Linux 用户可以使用由 rainy 朋友所提供的
[PKGBUILD](http://linuxtoy.org/archives/florence.html#comment-78436)。

[感谢 Gundamdriver 朋友推荐]
