Title: Aptitude 有了 GTK+ GUI
Date: 2008-07-11 08:05
Author: toy
Category: Apps
Tags: Aptitude, Debian, GTK+
Slug: gtk-gui-for-aptitude

熟悉 [Debian](http://linuxtoy.org/tag/debian) 的朋友都知道，Aptitude
是其中重要的包管理工具。不过，Aptitude
仅有文本模式和命令行界面。最近，作为一名 Google 代码之夏的参与者，[Obey
Arthur Liu](http://www.milliways.fr/) 为
[Debian](http://linuxtoy.org/tag/debian) 项目中的 Aptitude 带来了一个
[GTK+ 的图形用户界面
(GUI)](http://www.milliways.fr/2008/07/09/state-of-the-aptitude-week-7/)，以改善其可用性。

[![Aptitude GTK+
GUI](http://i.linuxtoy.org/i/2008/07/aptitude-thumb.png)](http://i.linuxtoy.org/i/2008/07/aptitude.png)

目前，这个 GTK+ 界面的 Aptitude 能够更新/显示包列表、搜索包、标记包
(安装、删除、保留等)、显示冲突、执行包操作等。其他一些缺少的特性将在后续开发中添加，如包依赖、高级搜索、Tags
支持等。

开发者 Obey Arthur Liu 希望 Aptitude GTK+ GUI 成为
[Debian](http://linuxtoy.org/tag/debian) 中另一个图形化的包管理工具
Synaptic 的替代品，让我们拭目以待。

Aptitude GTK+ GUI 的源代码位于：<http://dev.graffit.net/aptitude/trac>。
