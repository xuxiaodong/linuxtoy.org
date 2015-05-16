Title: Azureus 2.5.0.2
Date: 2007-01-12 19:57
Author: toy
Category: Apps
Slug: azureus_2_5_0_2

[Azureus](http://azureus.sourceforge.net/) 是跨平台的 BitTorrent
下载客户端程序，在运行时需要 Java 运行环境的支持。Azureus 的更新版
2.5.0.2
在今日发布了。新的版本不仅添加了一些新的特性，而且也作出了不少改善。另外，许多的
bug 也得到了修复。

以下援引的是 Azureus 官方发布的更新列表：

> New features:  
>  · Core: Added method to XFS specific allocation of new files  
>  · Core: Added per-torrent max seeds parameter  
>  · Core: Added per-torrent max peers parameter  
>  · UI: Total file size added to Open Torrent Window  
>  · UI: Option to show complete downloads with incomplete "do not
> download" files in the download area  
>  · UI: Added custom user comment field  
>  · UI: Added file extension column in files view  
>  · UI: Spinners for config field that take numbers  
>  · UI: Setting for Minimum # of Simultaneous Active Downloads to have
> running at any given time  
>  · UI: Console UI NAT test  
>  · UI: Option to have separate rename and retarget menu items in Files
> view  
>  · Plug: Plugins can now create submenus.  
>  · Plug: Added code to allow plugins to get text input from a user in
> non-UI specific way.  
>  · Plug: Plugins now have better support to organise file data within
> default save directories.  
>  · Plug: Plugins can now easily add hyperlinks to config sections.
>
> Changes:  
>  · Core: Improve the "presence" handling for torrents created by
> ourselves  
>  · Core: Less memory footprint  
>  · Core: Faster startup for large torrent lists (and no naughty
> plugins)  
>  · Core: NAT test moved to separate server  
>  · Core: Download up/down idle counts now persisted over restart  
>  · UI: Open torrent windows now always has OK button enabled with
> warning message if pressed when in invalid state  
>  · UI: Remove nag/donation window  
>  · UI: Differentiate between libTorrent (Rakshasa) and libtorrent
> (Rasterbar)  
>  · UI: For multi-file torrents, icon in name column displays icon for
> largest file (+ a little folder icon)  
>  · UI: Faster filtering when torrent list is large  
>  · UI: Better logic when preventing a user deselecting files to
> download from Open Torrent window
>
> Bugs fixed:  
>  · Core: If clipboard has just a " or "" in it the open-torrents
> dialog won't open  
>  · Core: Setting of UDP port not working  
>  · Core: Less flipping of downloads from queued <--> downloading
> during the time a FP seed is forced active  
>  · Core: Fix memory leak causing slow, but eventual OOM and slow down
> of Azureus  
>  · Core: OSX: Handle volume not mounted on startup by erroring instead
> of creating a directory in /Volumes  
>  · Core: Fix to stop already complete downloads being moved by
> "move-on-completion" rules  
>  · UI: Fix (some) painting issues in pieces+files view  
>  · UI: Fix to allow negative values for Multi-monitor window
> positions  
>  · UI: Fixed memory leak in "Mr Slidey" code  
>  · UI: Fix UI loss when clicking delete from icon bar while in Details
> view  
>  · Plug: Fixed bug where some listeners for table columns were not
> registered properly.

Download link:

[Azureus
2.5.0.2](http://prdownloads.sourceforge.net/azureus/Azureus2.5.0.2.jar)
