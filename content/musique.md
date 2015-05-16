Title: Musique
Date: 2011-11-10 00:00
Author: lovenemesis
Category: Music Player
Tags: musique, Qt
Slug: musique

Musique 是一款基于 Qt 4.6 的跨平台音乐播放器，可运行在 Win、OS X 和
Linux 系统上。*感谢 @shellex 提供消息*

[![](http://linuxtoy.org/img/2011/11/musique.png "musique")](http://linuxtoy.org/img/2011/11/musique.png)

特点有：

-   从 Last.fm 抓取艺术家、专辑和歌词信息。
-   在 Win 和 OS X 平台上支持导入 iTunes 音乐库，特别支持 Lion
    引入的全屏模式。
-   简洁的播放列表设计，按照艺术家、专辑或文件夹选择并拖拽即播放。
-   搜索方式支持自动补全。

Musique 的源代码按照 GPLv2 发布，但是其 Win 和 OS X
的预编译二进制版本是需要支付少量费用的，而 32 位 Linux
预编译二进制版本则是免费的。

**PS：**Musique 需要使用 Phonon GStreamer 后端才能工作，**和 Xine
后端存在兼容性问题**。依据发行版打包情况，可能需要手动创建将其插件从
KDE4 连结至 Qt4 目录下，例如在 Fedora 16 i686 下：

    sudo ln -vs /usr/lib/kde4/plugins/phonon_backend/phonon_gstreamer.so /usr/lib/qt4/plugins/phonon_backend/phonon_gstreamer.so

**PS2：**Musique 的简体中文化已经完成，将随下一个版本发布。

[官方网站及下载](http://flavio.tordini.org/musique)
