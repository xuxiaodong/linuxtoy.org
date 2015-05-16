Title: Transmission 1.22 发布
Date: 2008-06-16 14:35
Author: toy
Category: Apps
Tags: Releases, Transmission
Slug: transmission-122-released

Transmission 是一款适合在 Linux 及 Mac OS X 平台下使用的 BitTorrent
下载工具，该工具以其简洁、轻量及高效的特点赢得了不少用户。近日，Transmission
的作者 John Clay 发布了最新的 1.22 版，作为 Transmission
的忠实使用者，当然立即进行更新。

![Transmission](http://i.linuxtoy.org/i/2007/04/transmission.png)

自 [Transmission
1.1x](http://linuxtoy.org/archives/transmission-110-released.html)
以来，新版本增加了支持 https tracker 连接、可以使用 Bluetack Level1
列表来锁定 IP、更好的支持多 tracker 的 torrent 文件等功能。同时，在 GTK+
接口方面，也有一些改进，如针对配置文件使用 XDG
目录规范、提高了可用性等。除此之外，Transmission 1.22
还修正了先前版本中所存在的一些缺陷。

[Transmission 1.22
的源代码](http://www.transmissionbt.com/download.php)可以从这里找到。若需编译安装则可按如下步骤进行：  

` tar xvjf transmission-1.22.tar.bz2 cd transmission-1.22 ./configure -q && make -s make install (需要 root 权限)`
