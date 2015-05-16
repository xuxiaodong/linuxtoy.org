Title: Paint Mono — Paint.NET for Linux
Date: 2007-12-23 15:19
Author: toy
Category: Apps
Slug: paint-mono

可能很多使用 Windows 的朋友都知道这款名为
[Paint.NET](http://www.getpaint.net/) 的图像编辑软件。目前，针对该软件的
Linux 平台移植已经出现──[Paint
Mono](http://code.google.com/p/paint-mono/)。从名称上即可看出，Paint
Mono 是采用 Mono 将 Paint.NET 移植到 Linux 系统上的。

[![Paint Mono
截图](http://i.linuxtoy.org/i/2007/12/paint-mono-thumb.png)](http://i.linuxtoy.org/i/2007/12/paint-mono.png)  
*Paint Mono 截图*

虽然这是一起由开源社区成员完成的非官方移植行为，但在 Paint Mono
中已经实现了 Paint.NET 的大多数特性。如果你想要在自己的 Linux 系统中尝试
Paint Mono，那么你将需要 Mono 1.2.6 和一个 SVN
客户端。然后，执行下列步骤：  

` $ svn co http://paint-mono.googlecode.com/svn/trunk/src paint-mono $ cd paint-mono $ ./configure $ make $ make install`

[[via](http://tirania.org/blog/archive/2007/Dec-21.html)]
