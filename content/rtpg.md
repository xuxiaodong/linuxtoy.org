Title: RTPG: rTorrent 的 Web 界面
Date: 2009-02-01 17:53
Author: toy
Category: Apps
Tags: rTorrent, Web UI
Slug: rtpg

RTPG（Rtorrent Perl GUI）为命令行的 BitTorrent 下载客户端 rTorrent
提供基于 Web 的界面。通过这个 Web 界面，你不仅可以增删 torrent
文件，而且能够执行开始/停止下载、设定下载优先级以及控制上传/下载速度等操作。此外，该
Web 界面还包含诸如速率、进度、Peer 数量之类的信息供用户参考。

![rtpg](http://i.linuxtoy.org/images/2009/02/rtpg.png)

RTPG 需要
apache2、rtorrent、librpc-xml-perl、libjson-xs-perl、libjs-jquery、libtemplate-perl
等依赖。你可以通过 svn 获取 RTPG 的源代码：

`svn co http://svn.uvw.ru/rtpg/`

[RTPG](http://rtpg.uvw.ru/) [via [Debian Package of the
Day](http://debaday.debian.net/2009/02/01/wip-rtpg-www-please-your-dearest-with-rtorrents-power/)]
