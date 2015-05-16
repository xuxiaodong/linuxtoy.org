Title: UniOS: 美好的幻想
Date: 2011-08-25 00:00
Author: lovenemesis
Category: Reviews
Tags: unios
Slug: unios-a-fairy-tale

不管你信还是不信，UniOS，一个德国 18
岁小伙发明的统一操作系统，宣称可以运行 Win， OS X 和 Linux 的应用程序。

根据当地媒体报道，一个 18 岁小伙 Maik Mixdorf
在朋友的帮助下，用三年的时间，五千两百万行代码，创造了一个可以运行任何
Win, OS X 和 Linux
应用程序的操作系统。在当地媒体的眼中，它已经俨然成为乔布斯和盖茨的竞争对手。

该系统宣称使用一个 **NT
层来解决驱动载入**的问题；并且使用**沙箱设计来隔离每一个应用程序**，从而不需要杀毒软件。  
它宣称可以运行 Microsoft Office 2010, Garage Band, iPhoto, Face Time,
或者 Dolphin 任意应用程序而无需担心驱动问题。

事实真的如此么？Jörg Thoma 采访了这个名叫 Maik Mixdorf
的小伙，终于揭露出了一些**真相：**

-   Ubuntu 10.10 + Wine
-   Avant Window Navigator + KDE4
-   仿造的 OS X Finder 的 Windows 程序，通过 Wine 运行。
-   来自 UC Berkly [Karthik](http://tharavaad.wordpress.com/) 的
    Picturebooth，使用 Flash 实现。

[朝内视频演示镜像](http://v.youku.com/v_show/id_XMjk3ODczOTky.html)

相信任何一个 Linux
爱好者都能穿如此简单的花样，为何当地媒体甚至学校的计算机老师都不愿面对呢？

笑过之余，请别忘记下面这些项目及他们的贡献者们，他们在某种程度上实现了跨系统的应用程序二进制兼容，还有它们面临的困难。

-   [ReactOS](http://www.reactos.org)：一个开源的在二进制兼容 Win
    的操作系统，目前处于 Alpha 阶段，无法解决驱动问题；
-   [Wine](http://www.winehq.org/)：运行在类 Unix 系统上的 Win16/32/64
    API 兼容层，经过十多年的发展，尚未做到运行全部 Win 程序；
-   [ndiswrapper](http://sourceforge.net/apps/mediawiki/ndiswrapper/index.php?title=Main_Page)：可以在
    Linux 系统上加载并使用部分 Win
    上的无线网卡驱动，面临着稳定性及维护性的问题。
-   [Linux
    兼容内核](http://www.longene.org/index.php)：本站[先前曾多次报道](http://linuxtoy.org/archives/linux-unifiedkernel-0241-released.html)，在这个多核时代面临着不支持多核的尴尬局面（最近有支持的迹象）。

*消息来源：*[golem.de](http://www.golem.de/1108/85776.html#gg1_anchor)
