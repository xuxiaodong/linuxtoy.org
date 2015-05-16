Title: Wine 1.1.7 发布，Direct3D 10 起步
Date: 2008-10-25 23:26
Author: lovenemesis
Category: Apps
Tags: Wine
Slug: wine-117-direct3d10

开源的 Win32 API 实现 Wine 昨日发布了开发版本的又一次更新 1.1.7。
这次例行更新中最引人注目的就是 Wine 开发小组开始了对 Direct3D 10
的实现。

相比之前版本，此次更新有如下变化：

-   提升了对 DOS 驱动器的设备管理。
-   很多对应 Richedit 的修正。
-   修正了很多安装文件错误，尤其是对于 **IE 7**。
-   开始着手对于 Direct3D 10 的实现。
-   修正了 Adobe Dreamweaver 8 使用中的细节问题。
-   修正了魔兽争霸3地图编辑器无法启动的错误。
-   修正了 Google Chrome 地址栏中选择总是从最先开始的问题。
-   修正了使用 GNOME 时魔兽世界无法全屏运行的错误。

详细英文更新日志请见[这里](http://www.winehq.org/?announce=1.1.7)。

下载见[这里](http://prdownloads.sourceforge.net/wine/wine-1.1.7.tar.bz2)。

*Tips*：

若是使用 gcc 4.3.0 无法正常编译源代码包的话，不妨在 ./configure
之前先运行 ulimit -s unlimited 。
