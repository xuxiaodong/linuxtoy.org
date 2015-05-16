Title: Deluge 0.5.7 发布
Date: 2007-11-28 09:40
Author: toy
Category: Apps
Slug: deluge-057-released

BitTorrent 下载软件 [Deluge](http://deluge-torrent.org/) 在今天发布了
0.5.7 版。该版本主要包括添加了 Scrape 支持、手动强制复查、本地 peer
发现、高级的进度栏、自动载入文件夹、以及设置选项等。此外，Deluge 0.5.7
也改进了 WebUI 和 Scheduler 插件，并修正了许多 bug。

![Deluge](http://i.linuxtoy.org/i/logo/deluge.png)

**Deluge 0.5.7 更改日志**

- Scrape support  
- Manual force-recheck  
- Add local peer discovery (aka local service discovery)  
- Blocklist plugin will now display errors, instead of just crashing on
a bad list or wrong type  
- Add torrent in paused state option  
- Add advanced progress bar  
- Fix bug in merging trackers  
- Various updates to WebUI, including https support and advanced
template by vonck7  
- Add maximum connection attempts per second preference  
- Fix bug where loaded plugins were forgotten if Deluge crashed  
- Fix ratio bugs (hopefully for the last time)  
- Add preference to only show file selection popup if torrent has
multiple files  
- Fix pause all and resume all bugs  
- Fix client not loading if our website goes down (new version check
failing)  
- Allow torrent creation with no trackers  
- Scheduler plugin revamp by Ben Klein  
- Fix ETA from going backwards  
- UI warning on full HD - no longer just silently pauses torrents  
- Replace SimpleRSS with FlexRSS  
- Add preference for the location of torrent files  
- Add autoload folder  
- Copy translator credits from Launchpad to our about->credits  
- Differentiate between queued and paused torrents. Able to pause
queued torrents - patch by yobbobandana  
- Show error when writing/permission problems occur  
- Fix invalid handle error  
- Fix toolbar icon/text issue  
- Fix more invalid handle errors  
- Fix Portuguese encryption drop-down boxes  
- Fix some translation issues with gtk stock

你可以从这里[下载 Deluge
0.5.7](http://deluge-torrent.org/downloads)，包括[源代码](http://deluge-torrent.org/downloads-source)及适用于
[Ubuntu](http://deluge-torrent.org/downloads-ubuntu)、[Debian](http://deluge-torrent.org/downloads-debian)、[Gentoo](http://deluge-torrent.org/downloads-gentoo)
等 Linux 发行版的安装包。
