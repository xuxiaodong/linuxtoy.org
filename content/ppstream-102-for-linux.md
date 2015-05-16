Title: PPStream 1.0.2 for Linux
Date: 2011-09-04 10:41
Author: lovenemesis
Category: Movie Player
Tags: Fedora, ppstream
Slug: ppstream-102-for-linux

距离[上一次发布](http://linuxtoy.org/archives/pps-back-again.html)又快一年了，
PPS 网络电视悄悄的发布了 Linux 平台下的 1.0.2
正式版本(2011年8月26日创建)，解决了上个版本中部分令 Linux
用户纠结的问题。

改进有：

-   不再需要 Root 权限运行。
-   自带 mplayer
-   提供 desktop 文件
-   提供 RPM 和 DEB 两种二进制包。

实测运行截图：

[![](http://linuxtoy.org/img/2011/09/pps-102-linux.png "pps-102-linux")](http://linuxtoy.org/img/2011/09/pps-102-linux.png)

Fedora 15 下安装方法：

1.  首先需要[启用 RPMFusion
    仓库](http://www.rpmfusion.org/Configuration)。
2.  下载 [PPStream Fedora
    RPM](http://download.ppstream.com/linux/PPStream.rpm)。
3.  双击 RPM 安装，或者使用 `pkcon install-local PPStream.rpm`
    命令行安装。
4.  安装后最好注销重登陆，或者运行
    `update-desktop-database`，这样才能在应用程序菜单中找到 PPStream。
5.  默认视频输出不知为何是 X11，建议更换成 Xv；音频输出貌似只有 alsa
    有效果，pulse 没声音。

[官方下载](http://dl.pps.tv/pps_linux_download.html)（提供 [Fedora
RPM](http://download.ppstream.com/linux/PPStream.rpm) 和 [Ubuntu
DEB](http://download.ppstream.com/linux/PPStream.deb)）

**PS：**PPS 还同时发布了 [Android
版本](http://dl.pps.tv/pps_android_download.html)。
