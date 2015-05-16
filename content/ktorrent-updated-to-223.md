Title: KTorrent 更新到 2.2.3 版
Date: 2007-11-15 11:19
Author: toy
Category: Apps
Slug: ktorrent-updated-to-223

KDE 桌面环境下的 BitTorrent 下载软件 [KTorrent](http://ktorrent.org/)
于今日更新到了 2.2.3 版。这是一个 bug
修订版本，其中主要针对之前版本中所存在的各种 bug
进行了修订。同时，该版本也添加了一些由社区会员所贡献的补丁。

![KTorrent](http://i.linuxtoy.org/i/logo/ktorrent.jpg)

引用 KTorrent 2.2.3 的更改记录如下，以供大家参考：

- Fix datacheck of 4GB+ files on 32 bit systems  
- Prioritise at least 1 % of multimedia files instead of 1 chunk  
- Fix crashes caused by SIGXFSZ (BUG: 149747)  
- Make sure body tag is OK in 404 and 500 error defines in webgui (BUG:
150023)  
- Fix bug which allows clients to trick KT in enabling PEX on private
torrents  
- If do not use KDE proxy is enabled and no alternative proxy is set,
make sure we use no proxy at all for HTTP tracker connections. (BUG:
150284)  
- Removed slashes which prevent opening torrents to work in ktshell  
- Fix broken preexsting file check, which can result in files being
deleted when the user deselects them and they already exist. (BUG:
150563)  
- When stop all and start all is pressed, make sure that start and stop
buttons are updated properly (BUG: 149549)  
- Make URL of tracker selectable in tracker tab  
- Fix issue with speed calculating, causing the displayed speed to grow
enormously  
- Updated Peer ID list with more clients  
- Fix crash when trying to download an empty link with the RSS plugin
(BUG: 150879)  
- Fix crash at exit when the RSS plugin was loaded  
- Make TrayHoverPopup dissapear faster (BUG: 148243)  
- Sort IP addresses by their actual value and not by their string
representation (BUG: 150328)  
- Added patch from Jaak Ristioja, which updates the FileView in a
separate thread.  
- Make sure only the files of a torrent are moved when the data
directory is changed.  
- Make sure window is not hidden when hidden\_on\_exit is true and the
system tray icon is not enabled  
- Added patch from Stefan Monov to hide the menubar (BUG: 151450)  
- Fix crash at exit (BUG: 149827)  
- Added patch from The\_Kernel, which allows you to change file
priorities in the webgui  
- Backported fix for refresh bug from KDE4 version  
- Added option to limit the number of outgoing connection setups, so
that people can limit the number of TCP connections in SYN\_SENT state,
should their router not be able to handle to much  
- Replaced TOS setting by DSCP setting  
- Added several patches from Rafael Mileki which fix and improve some
things in the webgui  
- Change buttons in recreate popup to Recreate and Do Not Recreate
(BUG: 151805)  
- Added patch from Lukasz Fibinger which adds a filter bar to search
for torrents  
- Make sure that day and month names are not translated in HTTP
headers.

你可以从这里[下载 KTorrent 2.2.3
的源代码](http://ktorrent.org/index.php?page=downloads)。
