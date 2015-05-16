Title: gmusicbrowser — 音乐播放及管理软件
Date: 2007-09-13 08:00
Author: toy
Category: Apps
Slug: gmusicbrowser

[gmusicbrowser](http://squentin.free.fr/gmusicbrowser/gmusicbrowser.html)
是我最近发现的一款很不错的音乐播放及管理软件。它不仅功能完善，而且易于定制。如果你有海量的音乐收藏需要管理，那么不妨考虑选用
gmusicbrowser。

[![gmusicbrowser
player](http://i.linuxtoy.org/i/2007/09/gmusicbrowser-player_s.png)](http://i.linuxtoy.org/i/2007/09/gmusicbrowser-player.png)  
*gmusicbrowser 播放器*

**gmusicbrowser 的主要功能**

gmusicbrowser 具有丰富而完整的功能，主要包括下面这些：

-   在格式上，gmusicbrowser 主要支持播放 mp3、ogg、flac、mpc
    等音乐文件类型。由于 gmusicbrowser 可以选用
    mpg321/ogg123/flac123、gstreamer、mplayer
    等不同的音乐播放后端，所以还可能支持其他的格式。
-   gmusicbrowser 包含 tag 编辑器，并具有批量文件重命名功能。
-   gmusicbrowser 具有插件系统，目前提供支持
    last.fm、抓取专辑封面和歌词等功能。
-   你可以选用 gmusicbrowser
    预设的各种不同的界面布局方案，以满足个人的喜好。

**gmusicbrowser 的使用依赖**

因为 gmusicbrowser 是采用 Perl 语言编写的，所以要求你的系统必须具有
Perl。其他的使用依赖还包括：

-   gtk+2 及其 perl 绑定
-   gstreamer 及其 perl 绑定，或 mpg321/ogg123/flac123/amixer，或
    mplayer
-   Gtk2::Trayicon，可选依赖，如果你需要让 gmusicbrowser
    具有系统托盘图标功能，则要求此依赖。
-   Gtk2::MozEmbed，可选依赖。用于显示与艺术家相关的 Wikipedia
    页面及使用 Google 搜索歌词。

**安装 gmusicbrowser**

gmusicbrowser 当前最新稳定版为 0.960，提供有多种形式的安装包，如
Tarball、rpm、deb 等。

使用 Debian/Ubuntu 的朋友，可以将下列内容添加到 /etc/apt/sources.list
文件中：

`deb http://squentin.free.fr/gmusicbrowser ./`

然后使用下列命令来安装 gmusicbrowser：  
` sudo apt-get update sudo apt-get install gmusicbrowser`

或者，也可直接[下载 gmusicbrowser 的 deb
包](http://squentin.free.fr/gmusicbrowser/gmusicbrowser_0.960_all.deb)：

`sudo dpkg -i gmusicbrowser_0.960_all.deb`

对于使用基于 rpm 包管理器的 Linux 发行版用户，可以[下载 gmusicbrowser 的
rpm
包](http://squentin.free.fr/gmusicbrowser/gmusicbrowser-0.960-1.noarch.rpm)：

`sudo rpm -i gmusicbrowser-0.960-1.noarch.rpm`

其他 Linux 系统用户可以[下载 Tarball
包](http://squentin.free.fr/gmusicbrowser/gmusicbrowser-0.960.tar.gz)：  

` tar xzvf gmusicbrowser-0.960.tar.gz gmusicbrowser-0.960/gmusicbrowser.pl`

**运行 gmusicbrowser**

gmusicbrowser 可从“Applications → Sound & Video →
gmusicbrowser”启动运行。

[![gmusicbrowser
manager](http://i.linuxtoy.org/i/2007/09/gmusicbrowser-manager_s.png)](http://i.linuxtoy.org/i/2007/09/gmusicbrowser-manager.png)  
*gmusicbrowser 管理器*
