Title: PC-BSD 9.0 beta
Date: 2011-08-08 13:50
Author: cheer_xiao
Category: Distros
Tags: BSD
Slug: pc-bsd-90-beta

严格来说……这不是一条 Linux 的新闻。首先，它不是
Linux；其次，它不是新闻（一周前的消息了）。  
FreeBSD 衍生操作系统 PC-BSD 发布 9.0 beta。主要看点：

-   基于尚未正式发布的 FreeBSD 9.0；
-   带来**多款 DE** 支持。PC-BSD 8 仅支持 KDE 4；PC-BSD 带来 GNOME
    2、KDE 4、Xfce 4 和 LXDE 支持；
-   安装程序多项更新，包括易用的 **ZFS 配置**、GELI 加密配置；
-   备份工具“Life-Preserver”多项更新，支持备份到 FreeNAS 或者任何远程
    ssh + rsync 服务器；
-   新的“PC-BSD 控制面板”，中心化、图形化的系统配置工具；
-   新的系统升级工具；现在可以使用 FreeBSD 的“freebsd-update”对 PC-BSD
    进行**跨次版本升级**（如 9.0 -> 9.1）；
-   新的软件中心“AppCafe”；
-   PBI 包管理系统得到改善，允许多个 PBI 包共享库文件。

[![PC-BSD
Logo](http://linuxtoy.org/img/2011/08/pcbsd.png)](http://linuxtoy.org/img/2011/08/pcbsd.png)

PC-BSD 是一个基于 FreeBSD 的面向桌面用户的操作系统。PBI (Push Button
Installer) 是 PC-BSD 自己的包管理系统和格式，采用类似于 Mac OS X
的“bundle”形式。PC-BSD
的开发者认为这种包更适合用于桌面。不过同时，PC-BSD 仍然可以使用 FreeBSD
的 ports 和 package 系统。

[发布公告](http://blog.pcbsd.org/2011/08/release-announcement-pc-bsd-9-0-beta1/)
[下载传送门](http://pcbsd.org/get-it/download-pc-bsd) (注意下载页上方是
PC-BSD 8，下方才是 9)
