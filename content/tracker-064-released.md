Title: Tracker 0.6.4 发布
Date: 2007-12-12 09:39
Author: toy
Category: Apps
Slug: tracker-064-released

Linux 平台上的桌面搜索工具
[Trakcer](http://linuxtoy.org/archives/tracker.html) 在昨天发布了新的
0.6.4 版。Tracker 0.6.4
能够使索引更健壮、可以限制日志文件大小、添加了新的 Tracker
applet、提供新的电源管理选项。此外，这个版本的 Tracker 也修正了许多
bug，从而确保了程序更加稳定可靠。

![Tracker logo](http://i.linuxtoy.org/i/2007/12/tracker.png)

**Tracker 0.6.4 更改日志：**

- Fixed memory leaks  
- Fixed several crashes  
- Made indexing more robust by pausing if disk space is low or index
grows too big  
- Limit log file size  
- New tracker applet - animates when indexing, provides ability to
pause indexing as well as viewing status and progress feedback from
indexer, statistics, prefs and of course search. Also provides
notification of warnings from tracker  
- New power management options enable much better customization  
- Ignored files fixes  
- Deskbar/tracker integration fixes  
- Made most prefs live and affect tracker in real time. Others will
prompt for restart and/or reindex where necessary  
- Shell script fixes  
- Fixed Imap bug with embedded Auth in URI  
- Built in corruption check and scan when tracker not shut down
cleanly  
- prevents infinite looping  
- Fix index deletions  
- many more bug fixes and stability improvements...

你可以从这里[下载 Tracker 0.6.4
的源代码](http://www.gnome.org/~jamiemcc/tracker/tracker-0.6.4.tar.bz2)。
