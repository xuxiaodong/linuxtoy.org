Title: KTorrent for KDE 4 已抵达
Date: 2007-12-24 16:07
Author: toy
Category: Apps
Slug: ktorrent-for-kde-4

[KTorrent](http://linuxtoy.org/archives/ktorrent.html) 是 KDE
桌面环境下一款功能强大的 BitTorrent 下载软件。经过 KTorrent
开发者数月的努力，面向 KDE 4 平台的第一个发布版本 KTorrent 3.0 Beta 1
在今天诞生了。KTorrent 3.0 Beta 1 不是纯粹从 KDE 3
版本的移植，其中也添加了很多新功能。

[![KTorrent for KDE
4](http://i.linuxtoy.org/i/2007/12/ktorrent-for-kde4-thumb.png)](http://i.linuxtoy.org/i/2007/12/ktorrent-for-kde4.png)  
*KTorrent for KDE 4 截图*

KTorrent 3.0 Beta 1 主要添加了下列新特性：

-   IPv6 支持
-   SOCKSv4 和 v5 支持
-   能够选择要使用的网络接口
-   提供 flat 列表模式以显示 torrent 文件
-   重新组织了配置对话框
-   可以移动个别的 torrent 文件
-   新的 queuemanager 界面

KTorrent 3.0 Beta 1 需要最新的 KDE 4 ([KDE 4 RC
2](http://linuxtoy.org/archives/kde-40-rc-2-released.html))，其[源代码](http://ktorrent.pwsp.net/index.php?page=downloads)可从
KTorrent 网站获取。

如果你想安装 KTorrent 3.0 Beta 1，在准备好 cmake 及所需的开发包
(Qt、KDE、libgmp、QCA2) 之后，那么可按如下步骤进行编译：  

` tar -xvjf ktorrent-3.0beta1.tar.bz2 cd ktorrent-3.0beta1 mkdir build cd build cmake -DCMAKE_INSTALL_PREFIX=/path/to/prefix/of/kde4/installation .. make sudo make install`
