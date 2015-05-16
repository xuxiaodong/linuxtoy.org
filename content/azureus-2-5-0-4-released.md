Title: Azureus 2.5.0.4
Date: 2007-01-25 21:14
Author: toy
Category: Apps
Slug: azureus-2-5-0-4-released

跨平台的全功能型 BitTorrent 客户端程序 Azureus 已经放出了更新版本
2.5.0.4。该版本除了在核心部分和插件方面添加了少许新特性之外，也相应地作出了部分改进。另外，新的版本也修正了一些
bug。为了获得更为理想的 BitTorrent 下载体验，正在使用 Azureus
的朋友不妨考虑升级到最新版来。

Azureus 所列出的该版本的更新情况为：

> New Features:
>
> * Core | New users default save directory is now located in their "My
> Documents" directory, under "Azureus Downloads"  
>  * Core | Show alerts raised during closedown on next start as these
> often don't get displayed due to UI shutdown  
>  * Core | Allow plugin installs to place jars into the plugin-shared
> "shared/lib" directory  
>  * Plug | Unsafe config read/writing  
>  * Plug | Plugins can now open and close download bars
>
> Changes:
>
> * Core | Added scrape delay for stopped/errored torrents, and
> torrents with high share ratios  
>  * Core | Allow only one active scrape for each tracker  
>  * Core | Release piece-map when not required  
>  * Core | ASN lookup via DNS queries only  
>  * Core | Full recheck of torrent when part of torrent fails hash
> check on completion  
>  * Core | Take note of banned IPs when we have IP filter turned off -
> these are independent  
>  * Core | Disable download peer caching for private torrents  
>  * Core | Disconnect currently connected peers on tracker URL change
> for private torrents  
>  * Core | Remove unused download/upload specific stats from
> version-check message  
>  * Core | Include IP override in NAT check message for NAT check
> server to use  
>  * Plug | Timeout UPnP port releases during closedown to prevent
> Azureus hanging
>
> Corrected bugs:
>
> * Core | Fix choke/unchoke cycle bug for lan local peers  
>  * Core | Fix auto moving torrent data with DND files  
>  * Core | Fix NPE causing XML stats not to be written  
>  * UI | Fix crash when opening non-torrent URL when OS has no
> recognized HTML viewer  
>  * UI | Fix big icon in name column for OSes using GTK  
>  * UI | Make Download Basket work again for drag and dropping

Download [Azureus
2.5.0.4](http://prdownloads.sourceforge.net/azureus/Azureus2.5.0.4.jar)
