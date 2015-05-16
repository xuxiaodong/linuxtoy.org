Title: Deluge 更新到 0.5.6.2 版
Date: 2007-11-04 10:55
Author: toy
Category: Apps
Slug: deluge-updated-to-0562

BitTorrent 下载客户端 [Deluge](http://deluge-torrent.org/) 在近日将
0.5.6 稳定版更新到了 0.5.6.2。此版本修正了一系列的问题，如 WebUI
插件中的 bug、无效处理错误、程序关闭时的 bug 等。另外，TorrentCreator
插件中的默认 piece 大小被设为 256-KiB，并添加了一个 2048KiB
的选项。推荐仍在使用 Deluge 旧版本的朋友升级。

![Deluge](http://i.linuxtoy.org/i/logo/deluge.png)

Deluge 0.5.6.1~0.5.6.2 的更新记录为：

* Set default piece size to 256-KiB in TorrentCreator plugin and add
2048KiB as a size option.  
* Fix a bug in Debian package that caused the UI to completely freeze
when a torrent finished  
* Find and fix another shutdown bug that mostly Gutsy users were
incountering  
* Fix a couple of WebUI bugs, including the "index" page erroring out  
* Fix invalid handle error  
* Fix shutdown hang

- [Download Deluge 0.5.6.2](http://deluge-torrent.org/downloads)
