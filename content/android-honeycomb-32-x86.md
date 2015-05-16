Title: Android Honeycomb 3.2 X86
Date: 2011-11-21 23:10
Author: liangsuilong
Category: Embedded
Tags: Android, honeycomb
Slug: android-honeycomb-32-x86

还记得本站先前介绍的 [Android-x86
项目](http://linuxtoy.org/archives/android-x86-project.html)么？该项目近日将为平板电脑设计代号
Honeycomb 的 Android 3.2 移植到 X86 架构的机器上了。

以下是一些测试拍照：

[Honeycomb X86 系统设定页面](http://picplz.com/vGNF)

[Honeycomb X86 版本的 GTalk](http://picplz.com/vCF3)

[Honeycomb X86 版本的 GMail](http://picplz.com/vCnp)

[在 Honeycomb X86 上玩 Fruit Slice](http://picplz.com/vCcp)

[用 Honeycomb X86 访问本站](http://picplz.com/vC2Z)

本人的测试机是 Lenovo IdeaPad S205 (AMD E-450 预装 MeeGo 进不了 X
的那款)，运行 Honeycomb
相当流畅，但是鼠标移动的时候屏幕会轻微花屏，估计和本人倒了半瓶液晶清洁液到显示屏没有关系。Ralink
RT3090 无线网卡直接识别出连上 WiFi，这点比 Fedora 和 Ubuntu 都要强。玩
Fruit Slice 也十分流畅。

本人的 Intel 台式机是 Intel Core 2 Duo E6420 + AMD Radeon HD5550
比笔记本更加流畅，但是 Honeycomb
无法在图形界面管理有线网卡，所以只是略微体验了一下，移动鼠标没有花屏。在之前的
Gingerbread 是可以直接连上网的。

本人的 AMD 台式机是 AMD Athlon 64 X2 4200+ + ATi Radeon HD3650 无法启动
Honeycomb，启动时内核的 CPU microcode 无法识别 CPU
型号，故被认为是非华硕出产的电脑，无法启动。之前的 Gingerbread
是可以启动的。估计是 CPU 不支持 SSSE3 导致的。

整体的感觉比 Windows 8 Metro UI 实用和好用，如果平时习惯了 GNOME Shell
和 KDE Plasma Netbook 这种大图标的界面，你应该可以很快上手的。

如果感兴趣的朋友，可以[前往 Android X86
下载页面](http://code.google.com/p/android-x86/downloads/list)获取**适合您
CPU 类型的 LiveCD** 进行尝试。

此外，Android-x86
项目负责人[黄志伟](http://zh.wikipedia.org/wiki/%E9%BB%83%E5%BF%97%E5%81%89)先生已经在博客上放出[Ice
Cream Sandwich On VirtualBox
的截图](http://cwhuang.info/2011/11/ics-x86-screenshots)，暂时没有硬件加速。

[![](http://linuxtoy.org/img/2011/11/ics4.png)](http://linuxtoy.org/img/2011/11/ics4.png)
