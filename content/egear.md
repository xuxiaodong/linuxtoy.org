Title: eGear：基于 Qt 4 的下载管理软件
Date: 2008-10-28 10:43
Author: toy
Category: Apps
Tags: eGear, Qt
Slug: egear

eGear 是由 LinuxSir
论坛会员夕角利用空闲时间开发的一款下载管理软件。该软件基于 Qt
4，并用到了 Curl
库，目前已经基本实现了一般下载管理软件所应具有的功能，比如：支持 HTTP 及
FTP 的多线程下载、支持监视剪贴板、提供任务 log
等。感兴趣的同学可下载尝试，并向作者反馈。

![eGear](http://i.linuxtoy.org/i/2008/10/egear.png)

安装 eGear 需要 curl 和
qt-gui，在获取源代码并解压后，可进入目录执行以下命令编译：

`qmake && make`

然后，要启动 eGear，可以执行：

`./egear`

另外，作者也为 Gentoo 用户提供了
ebuild，需要的同学可从[这里获取](http://www.linuxsir.org/bbs/thread336805.html)。

[eGear](http://code.google.com/p/egear/) [via
[LinuxSir](http://www.linuxsir.org/bbs/thread336805.html)]
