Title: Linux DLNA
Date: 2011-08-22 00:00
Author: lovenemesis
Category: Featured, Movie Player, Music Player, Network, Reviews
Tags: dlna, Fedora
Slug: linux-dlna

DLNA 是 “Digital Living Network Alliance
数字生活网络联盟”的缩写。随着消费电子产品的发展，有越来越多的 DLNA
兼容设备出现在生活中。那么 Linux 下对这个技术的支持情况如何呢？

DLNA 采取 C/S 的架构设计，于是存在 **“Digital Media Server 媒体服务器”**
和 **“Digital Media Player 媒体播放器”** 两个角色。后续的 1.5
版本又增加了对于手机等移动设备的支持，与前两者的兼容格式要有些差异。

本文大致列举了一些在 Linux 平台上的**开源 DMS 和 DMP
产品**，希望能起到抛砖引玉的效果。

**媒体中心 Media Center：DMS + DMP**

[XBMC](http://www.xbmc.org)

老牌的开源跨平台媒体中心解决方案，当然包括对 DLNA
的支持，可用于媒体提供及播放。提供免安装的 Live 镜像可供尝试。

Fedora 15 下安装（需启用 RPMFusion）： `pkcon install xbmc`

[GeeXboX](http://www.geexbox.org/)

一个专注于 HTPC 的 Linux 发行版，有 X86, PPC 和 ARM 架构版本，它是 Linux
世界中 DLNA 的核心，引领了多个 DLNA 相关开源实现。

值得一提的是它的媒体中心界面 Enna 是使用 Enlightenment 技术实现的。

**媒体服务器：DMS**

[uShare](http://ushare.geexbox.org/)

最早实现 DLNA 支持的 UPnP 媒体服务器，源自 GeeXboX，**同时提供对 XBox
360 (`-x` 选项)和 DLNA/PS3 (`-d` 选项)的支持**。

Fedora 15 下安装（需启用 RPMFusion）： `pkcon install ushare-freeworld`

[Coherence](http://coherence.beebits.net/)

使用 Python 编写的媒体服务器和 DLNA 实现框架，提供有 **D-Bus
访问接口以及多种媒体后端**，可以使用现有 Rhythmbox 音乐库的内容。

Fedora 15 下安装： `pkcon install python-Coherence`

[ps3mediaserver](http://code.google.com/p/ps3mediaserver/)

使用 Java 编写的跨平台 DLNA 媒体服务器，特别为 PS3
优化，提供**实时媒体格式转换**功能，解压缩即可使用。

**媒体播放器：DMP**

[Totem DLNA/UPnP](http://coherence.beebits.net/wiki/Totem)

基于 Coherence 框架创建，调用 GStreamer。

Fedora 15 下安装： `pkcon install totem-upnp`

[Rhythmbox DLNA/UPnP](http://coherence.beebits.net/wiki/RhythmBox)

同样基于 Coherence 框架创建，调用 GStreamer。

Fedora 15 下安装： `pkcon install rhythmbox-upnp`

*目前还没找到在 Linux 平台下支持 DLNA 访问的照片管理软件。*

*目前看来 VLC 和 MPlayer 似乎对于 DLNA 并没有很好的支持。*

**实用工具**

[UPnP Inspector](http://coherence.beebits.net/wiki/UPnP-Inspector)

用来探测网络中的 DLNA 设备的实用工具，也是基于 Coherence 的。

Fedora 15 下安装： `pkcon install upnp-inspector`

*延伸阅读：*[这篇文章](http://jorgenmodin.net/index_html/archive/2009/12/26/list-of-open-source-dlnaupnp-av-software-devices/weblogentry_view)也总结了一些开源
DLNA 产品。

*参考链接：*[维基百科](http://zh.wikipedia.org/wiki/DLNA)

**PS：**

受部分来自火星的读者朋友要求，特地补充两个使用样例。

**1. PS3MediaServer + PS3**

在偶 Fedora 15 的本本上运行上文介绍的 ps3mediaserver 做为
DMS，同一局域网下的 PS3 开启 DLNA 做为 DMP。

于是我就可以用 PS3 在电视上浏览本本中的照片、音乐和视频了。甚至原先 PS3
不能播放的格式比如 OGG 和 RMVB，在经过 ps3mediaserver
的实时转换后也可以在播放了。

此外由于偶的手机 Xperia Neo 也支持
DPMS，可以随时将手机中的照片和音乐通过无线网络在 PS3 上浏览。

**2. My Book Live + Rhythmbox/Totem**

西数的这款外置硬盘内置 Twonky 的 DLNA DMS。通过 LAN
链接至无线路由器，将音乐、视频等拷贝进去后，就可以使用 Rhythmbox/Totem
去访问其中的内容了，在多台设备间也可共享。

同样的在 Android 手机上也可以使用
[UPnPlayer](https://market.android.com/details?id=cx.hoohol.silanoid)访问其中存储的音乐和视频。
