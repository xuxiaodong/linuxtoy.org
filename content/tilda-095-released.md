Title: Tilda 0.9.5 发布
Date: 2007-12-14 10:46
Author: toy
Category: Apps
Tags: Tilda
Slug: tilda-095-released

下拉终端程序
[Tilda](http://linuxtoy.org/archives/tilda-and-yakuake.html)
于昨日发布了 0.9.5
版。新版本对主要代码进行了重新整理，具有更好的动画支持，添加了真透明特性，支持
Tab 键循环切换，更新了文档等。此外，Tilda 0.9.5 也修正了一些 bug。

![Tilda](http://i.linuxtoy.org/i/2007/12/tilda.png)  
*Tilda 0.9.5 屏幕截图*

Tilda 需要 GLib (>= 2.8 版)、Glade (>= 2.0 版)、VTE、libConfuse
等使用依赖。在准备好依赖并[下载源代码](http://downloads.sourceforge.net/tilda/tilda-0.9.5.tar.gz)之后，可按如下指令编译安装：  

` tar zxvf tilda-0.9.5.tar.gz cd tilda-0.9.5/ ./configure make make install`

值得注意的是最后一步要求 root 权限。
