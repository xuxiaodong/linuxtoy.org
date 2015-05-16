Title: 山寨版 GDrive！
Date: 2009-03-03 18:23
Author: toy
Category: Apps
Slug: gaedav

[撰文/Haoyu Bai]

为了能够支持 Zotero 1.5 的 WebDAV 文件同步，我把 PyFileServer 移植到了
Google App Engine 上。这样就能将 Google App Engine 作为 WebDAV
服务器，而 WebDAV 协议 Nautilus 和 Dolphin 都支持得很好，这样直接就把
GAE 变成 GDrive 了。 :-)

下面是在 Dolphin 中访问测试服务器的截图：

[![GaeDAV on
Dolphin](http://i.linuxtoy.org/images/2009/03/gaedav-thumb.png)](http://i.linuxtoy.org/images/2009/03/gaedav.png)

测试服务器在这里，欢迎试玩：

<http://gaedavtest.appspot.com/dav/>

在 KDE 的文件管理器中可以用 webdav://gaedavtest.appspot.com/dav/
访问，Gnome 应该也可以，不过没试过……

代码在这里：

<http://code.google.com/p/gaedav/>

目前只实现了最基本的功能。若有兴趣欢迎参与开发。：）

P.S. 本项目是 fork from PyFileServer 的。 PyFileServer 是 Google Summer
of Code 2005 的项目，原作者 Ho Chun Wei。
