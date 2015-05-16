Title: Linkage — 界面酷似 µTorrent 的 BitTorrent 下载软件
Date: 2007-08-22 08:00
Author: toy
Category: Apps
Slug: linkage

[Linkage](http://code.google.com/p/linkage/) 是一款新近刚出现的
BitTorrent 下载软件，它使用 C++ 并基于 libtorrent 库和 GTK+ 工具包（通过
gtkmm）开发而成。Linkage 在界面上酷似 µTorrent，同样小巧，且包含大多数
BitTorrent 下载软件所具有的功能。对于仍在寻找 µTorrent
替代品的朋友来说，Linkage 或许是一个不错的选择。

[![Linkage](http://i.linuxtoy.org/i/linkage/01_s.png)](http://i.linuxtoy.org/i/linkage/01.png)  
*Linkage 主窗口截图*

在试用 Linkage 过后，我发现它的主要功能包括：

-   支持同时下载/上传多个 Torrent 文件。当然这是 Linkage 的主要功能，但
    Linkage 既做到了列表化管理，也能够分组归类。
-   能够制作 Torrent 文件。
-   支持 DHT 和 PEX，可以设置最大连接数目、下载及上传速率。
-   可以显示有关 Torrent 的详细信息，如制作者、下载进度、连接
    IP、内含文件等。
-   具有插件系统，目前包括通知插件和托盘插件。当 Torrent
    下载完成时，前者可以及时通知你；后者可以让 Linkage 缩小到系统托盘。
-   支持使用代理。

另外，我也抓了一些 Linkage 的屏幕截图，也许你有兴趣会查看它们：

[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_02.png)](http://i.linuxtoy.org/i/linkage/02.png)[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_03.png)](http://i.linuxtoy.org/i/linkage/03.png)  

[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_04.png)](http://i.linuxtoy.org/i/linkage/04.png)[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_05.png)](http://i.linuxtoy.org/i/linkage/05.png)  

[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_06.png)](http://i.linuxtoy.org/i/linkage/06.png)[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_07.png)](http://i.linuxtoy.org/i/linkage/07.png)  

[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_08.png)](http://i.linuxtoy.org/i/linkage/08.png)[![Linkage](http://i.linuxtoy.org/i/linkage/thumb_09.png)](http://i.linuxtoy.org/i/linkage/09.png)

Linkage
目前还没有提供任何二进制包，仅有源码包可用。这意味着，如果你打算使用
Linkage，那么就必须从源代码安装它。好在作者针对 Fedora 和 Ubuntu
系统写了一篇[安装介绍](http://code.google.com/p/linkage/wiki/Installation)，可以作为参考。

- [Download Linkage
0.1.4](http://code.google.com/p/linkage/downloads/list)
