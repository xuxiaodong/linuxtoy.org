Title: Deluge 0.5.6 发布
Date: 2007-10-25 09:34
Author: toy
Category: Apps
Slug: deluge-056-released

全功能的 BitTorrent 下载客户端 [Deluge](http://deluge-torrent.org/)
已经发布了 0.5.6
版。这是一个值得为之升级的版本，其中包括添加了我们之前所提及的 [Web UI
功能](http://linuxtoy.org/archives/trying-out-deluge-web-interface.html)、修正了数据丢失必须重新下载的问题、使用新的完全分配方法来保留已下载的数据、托盘锁定密码不再存储在无格式文本文件中、更新了
Scheduler 插件、以及修正了许多 bug 等等。

![Deluge](http://i.linuxtoy.org/i/logo/deluge.png)

Deluge 0.5.6 的详细更改情况如下：

* Web Interface Plugin  
* Hopefully fix "losing data" and having to re-download parts (for
real this time)  
* Use new full allocation method which does not create files until one
of its pieces is downloaded  
* Tray lock password is no longer stored in plain text  
* Update the Scheduler plugin and fix a bunch of bugs on it  
* Double-clicking on a torrent opens up its containing folder  
* Fix SpeedLimiter plugin when setting upload limits  
* Fix MoveTorrent plugin when moving actively downloading torrents  
* Pause torrents while importing blocklist and resume them when
finished  
* Remove TorrentPieces and disable its use  
* A whole bunch of stuff for Win32  
* Add private flag to TorrentCreator plugin  
* Use SVG for internal logo usage (except on Win32)  
* Use theme for tray icon instead of hard-coded  
* Properly release port on shutdown  
* TorrentFiles plugin now has progress bars  
* Removing torrent files no longer deletes files that werent part of
the torrent  
* New max half-open connections setting to deal with cheap/broken
routers  
* Inherit UPnP fixes from libtorrent  
* Use threading for everything, instead of spawnning

除了源码包之外，Deluge 0.5.6 还为 Ubuntu、Debian、Gentoo 等 Linux
发行版准备有安装包。你可以从这里[下载 Deluge 0.5.6
的各种安装包](http://deluge-torrent.org/downloads)。

[Thanks zissan!]
