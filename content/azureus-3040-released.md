Title: Azureus 3.0.4.0 发布
Date: 2007-12-08 10:02
Author: toy
Category: Apps
Slug: azureus-3040-released

[Azureus](http://azureus.sourceforge.net/) 是一款使用 Java
语言开发而成的跨平台的 BitTorrent 下载软件。最近，Azureus 发布了 3.0.4.0
版，该版本在核心模块、用户界面、以及插件等方面有所改进和增强。

![Azureus](http://i.linuxtoy.org/i/logo/azureus.jpg)

以下为 Azureus 3.0.4.0 的详细更新记录，供参考：

**Feature**  
- Core: Reconnect to peers after unexpected disconnect / recover stats
of recently disconnected peers [Parg,The 8472]  
- Core: Global download speed limit can also limit the number of
outgoing requests, this should improve TCP performance [The 8472]  
- does not work with auto-speed since an explicit download speed-limit
must be set  
- downloads from as few peers as possible when the global limit is
reached  
- prioritizes downloads which are on the head of the queue  
- Core: IP binding now provides primitive round-robin load balancing
for users with multiple internet connections; accepts interface names
and IPv6 binding (if supported on the platform) [The 8472]  
- Core: Embed ChangeLog.txt in release jar [Nolar]  
- UI: Column menu option to automatically put contents of cell into the
tooltip [amc1]  
- UI: Piece distribution view is now also available as a peer subview
[The 8472]  
- UI: Added 'time remaining' column to peers view [Parg]  
- UI: Added option to suppress file download dialog [khai]  
- UI: Various progress reports have been unified; main status bar can
display progress for certain processes now [khai]  
- Plug: Plugins can now change the color of rows [amc1]  
- Plug: Plugins can add configuration colour parameters [amc1]

**Change**  
- Core: Attempt to re-open a file when access fails to try and recover
from a transient error [Parg]  
- Core: Auto speed default is now the new 'beta' (v2) algorithm
[ranul]  
- Core: Revised piece picking code to deal better with some edge cases
and snubbed peers [The 8472]  
- Core: Share Ratio/min Seeds ignore rule now applies even when no
tracker scrape is available [The 8472]  
- UI: Added private torrent indicator to the general tab [The 8472]  
- UI: Logging Consoles now have regex-based filters [The 8472]  
- UI: Tweaked table views to use a bit less memory and run better when
items are being quickly removed/added [TuxPaper]

**Bugfix**  
- UI: Don't hang UI redraw if file access is slow [Parg]  
- UI: Fixed inconsistencies in the Torrent Open Dialog related to
renaming and retargeting files and directories [The 8472]

你可以从这里[下载 Azureus
3.0.4.0](http://sourceforge.net/project/showfiles.php?group_id=84122&package_id=215453&release_id=559852)。
