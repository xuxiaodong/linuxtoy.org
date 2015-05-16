Title: Azureus 3.0.5.0 发布
Date: 2008-03-07 17:15
Author: toy
Category: Apps
Slug: azureus-3050-released

跨平台的 Java BitTorrent 客户端
[Azureus](http://azureus.sourceforge.net/) 在近日发布了 3.0.5.0
版。与旧版本相比，Azureus 3.0.5.0
不管是在核心功能方面，还是在用户界面上都有所改进和增强。比如，新版本添加了对
uTorrent PEX 的支持，提供了强制绑定 IP 的选项，在 UI
方面添加了一些菜单和选项等。

![Azureus](http://i.linuxtoy.org/i/logo/azureus.jpg)

以下引用 Azureus 3.0.5.0 的详细更改记录，供参考：

> New Features:
>
> * Core | Added uTorrent PEX support  
>  * Core | Azureus probes trackers for UDP-capabilities on first
> scrape/announce now and uses udp instead of http where available  
>  * Core | Added option to enforce IP bindings even when the specified
> interfaces are not available (useful when Azureus should not use
> certain network interfaces)  
>  * Core | Intervene with http seeds if progressive stall imminent  
>  * Core | Message user on startup if they have installed Azureus to
> read-only location  
>  * Core | Added dnd status to XML stats  
>  * UI | Added option for "Open Containing Folder" menu action - which
> may integrate better with non-standard file browsers  
>  * UI | Added option for "Show Torrent Menu" -- Users can now decide
> to see the Torrent menu in the menubar or not  
>  * UI | Fast Renaming (not moving) in the Files tab (click on name
> column) and Open Torrent dialog (click on dest. name column)  
>  * UI | Completed downloaders column  
>  * UI | Added start/stop to category menu  
>  * UI | Added per-category speed limits  
>  * UI | Added per-category option setting  
>  * UI | Added multiple-torrent options setting to MyTorrents view  
>  * UIv3 | New menu configuration for Vuze and Vuze Advanced UI's  
>  * UIv3 | Activity Tab  
>  * UIv3 | Vuze Login from client  
>  * Plug | Added Network Status plugin to perform some basic network
> tests  
>  * Plug | Allow plugins to specify their minimum JDK requirements
>
> Changes:
>
> * Core | Further memory footprint reductions; for additional tweaks
> see http://www.azureuswiki.com/index.php/Reduce\_memory\_usage  
>  * Core | Reimplemented LT extension protocol code  
>  * Core | DND/Compact (aka Delete) priority now deletes all files
> that do not share pieces with normal/high priority files  
>  * Core | Queuing rules now don't start any further torrents if the
> global up/download speed limits are reached  
>  * Core | Made the crypto handshake a bit less predictable  
>  * Core | Added support for IPv6 compact announces (client) and
> udp-multiscrapes (client+server)  
>  * Core | Take note of more peer-source selections  
>  * Plug | Added support for plugins which implement mainline DHT
>
> Corrected bugs:
>
> * Core | Request limiting/Priorities no longer pinch off LAN peers if
> seperate LAN speeds are enabled  
>  * Core | Increase time Azureus holds open listen socket on close to
> reduce dual-start window  
>  * Core | Allow ~ character in tracker addresses to support I2P  
>  * Core | Determine app name correctly on OSX so that restart works
> for renamed apps  
>  * UI | Shells no longer use the low-res frog icon, the normal main
> window icon is now used instead  
>  * UI | Limiting comments in General View to 5k characters under
> WinXP to avoid crashes due to faulty comctl32.dll  
>  * UI | Setting speed parameters manually now disables autospeed  
>  * Plug | Encode spaces correctly in get-right web seed urls

你可以从这里[下载 Azureus
3.0.5.0](http://azureus.sourceforge.net/download.php)。
