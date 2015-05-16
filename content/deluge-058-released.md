Title: Deluge 0.5.8 发布
Date: 2007-12-31 08:30
Author: toy
Category: Apps
Slug: deluge-058-released

如果你正在寻找 Linux 下功能全面的 GTK+ BitTorrent 下载软件，那么
[Deluge](http://linuxtoy.org/archives/deluge.html)
是一个不错的选择。Deluge
的开发非常活跃，时常更新以满足用户的需要。经过近一个月的开发，Deluge
于日前发布了 0.5.8
版。新版本为一些常用功能绑定了快捷键，引入了内置浏览器，并对某些插件进行了增强。

![Deluge](http://i.linuxtoy.org/i/logo/deluge.png)

**Deluge 0.5.8 更改日志**

Deluge 0.5.8 (29 December 2007)

- Fix handling of corrupt torrent files  
- Fix having two instances of Deluge running on Ubuntu  
- Fix problem relating to move torrent plugin not moving torrents
before they get cleared

Deluge 0.5.8RC2 (25 December 2007)

- Change add torrent to ctrl+n  
- Change notification plugin to not show the file list, but only the
torrent name  
- Allow removal of browser icon from toolbar  
- Add buttons to browser to launch the main and footer frames into an
external browser  
- Fix removing torrents from deluge template of webui - vonck7  
- Set the advanced webui template as default  
- Cut down significantly on the memory usage of the blocklist plugin  
- Fix some UPnP bugs  
- Fix "New version" alert from freezing sometimes  
- Prioritizes local peers over non-local ones when finding connect  
- Wish everyone a happy holiday :)

Deluge 0.5.8RC1 (22 December 2007)

- Key bindings:  
ctrl+a adds a torrent  
ctrl+l adds a torrent via URL ctrl+p pauses torrent(s)  
ctrl+r resumes torrent(s)  
delete removes torrent(s)  
- Fix total uploaded display bug  
- Fix seeding ratio stop on finished torrents  
- Fix zombie processes from occuring  
- Fix saying goodbye to trackers  
- Increase auto remove ratio to 100  
- Fix problem on Windows with filenames that have special characters  
- Fix saving of which columns to show  
- Fix init script error on exotic systems  
- Add web seed to Torrent Creator plugin  
- TorrentSearch is now built-in  
- Add internal anonymizing browser - Key bindings for that are as
follows:  
ctrl+l focus on location bar  
ctrl+k focus on search bar  
ctrl+r refreshes current page  
ctrl+enter adds 'www.' and '.com' to url string  
shift+enter adds 'www.' and '.net' to url string

Deluge 可在 Linux、Mac OS X 及 Windows 平台上运行，你可以从这里[下载
Deluge 0.5.8](http://deluge-torrent.org/downloads.php)。
