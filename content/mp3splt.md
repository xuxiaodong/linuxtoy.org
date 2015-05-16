Title: Mp3Splt：MP3/OGG 分割器
Date: 2008-09-09 08:00
Author: toy
Category: Apps
Tags: MP3, Mp3Splt, OGG
Slug: mp3splt

因为某种原因，有时候我们需要将 MP3 或 OGG 格式的音频文件进行分割处理。在
Linux 上，你可以使用 Mp3Splt 这个程序来达成此目的。Mp3Splt
是一个专门用来分割 MP3 或 OGG 音频文件的工具。无需重新编码，Mp3Splt
直接基于时间点来分割，快速而方便。

**安装 Mp3Splt**

-   Archlinux：`# pacman -S mp3splt`
-   Debian/Ubuntu：`# apt-get install mp3splt`

你也可以从
[Mp3Splt](http://mp3splt.sourceforge.net/mp3splt_page/downloads.php)
网站获取其最新版来安装。

**使用实例**

假如我有一个名为 Yesterday Once More.ogg 的 OGG 文件，我想将 0 分 40
秒到 4 分半这部分分割下来，那么可以执行：

`mp3splt Yesterday\ Once\ More.ogg 0.40 4.30`

其中，

-   0.40 为开始分割点的时间，格式为分.秒
-   4.30 为结束分割点的时间

Mp3Splt 也支持同时进行多次分割，例如：

`mp3splt Yesterday\ Once\ More.ogg 0.40 2.20 4.30`

**GTK 界面**

如果你不喜欢使用命令行，Mp3Splt 也有一个 GTK
的图形化界面供你选择，不过需要另外安装。

[![Mp3Splt](http://i.linuxtoy.org/i/2008/09/mp3splt.png)](http://linuxtoy.org)

[Mp3Splt](http://mp3splt.sourceforge.net/mp3splt_page/home.php)
