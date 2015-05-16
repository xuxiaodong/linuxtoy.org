Title: VirtualBox 2.0.4 发布
Date: 2008-10-25 23:09
Author: lovenemesis
Category: Apps
Tags: VirtualBox
Slug: virtualbox-204

昨日，开源的虚拟化软件 VirtualBox 发布了其 2.0.X 稳定系列的修正版
2.0.4。经过 2.0.2 和 2.0.4 两个修正版本，VirualBox 2.0.X
系列已经比较稳定了，还在坚守 1.9.6 的用户可以放心升级了。

该版本对于 **Linux 用户**来讲有如下变化：

-   修正了虚拟机会在主机启动300秒后停止相应的错误。
-   Windows 增强工具:
    修正了访问共享文件夹中的深层次目录结构时崩溃的错误。
-   Windows 增强工具: 提升共享文件夹名称的解析 (bug
    [#1728](http://www.virtualbox.org/ticket/1728 "Slow performance of shared folders XP guest with Ubuntu 7.10 Host (reopened)"))
-   Windows 增强工具: 修正 Windows 2000 关机时错误 (bug
    [#2254](http://www.virtualbox.org/ticket/2254 "Win2000 Guest Additions Shutdown problem -> fixed in 2.0.4 (closed)"))
-   Windows 增强工具: 修正当目标存在时 `MoveFile()` 的错误代码 (bug
    [#2350](http://www.virtualbox.org/ticket/2350 "MoveFile does not report failure when the target exists => Fixed in 2.0.4 (closed)"))
-   Linux 增强工具: 修复 `seek()` 对于超过 2GB 文件时的错误 (bug
    [#2379](http://www.virtualbox.org/ticket/2379 "Shared folders - unable to seek beyond 2GB => Fixed in SVN (closed)"))
-   Linux 增强工具: 支持 Ubuntu 8.10
-   Linux 增强工具: 修正剪贴板Bug (bug
    [#2015](http://www.virtualbox.org/ticket/2015 "Clipboard bad replaces memory => fixed in next version (closed)"))

完整的英文更新日志请看[这里](http://www.virtualbox.org/wiki/Changelog)。

下载请看[这里](http://www.virtualbox.org/wiki/Downloads)。
