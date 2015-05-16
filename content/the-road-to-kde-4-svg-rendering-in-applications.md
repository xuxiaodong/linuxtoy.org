Title: 通向 KDE 4 之路（一）：SVG 透视技术
Date: 2007-02-07 21:41
Author: toy
Category: Apps
Slug: the-road-to-kde-4-svg-rendering-in-applications

Troy Unrau 在 [KDE.NEWS](http://dot.kde.org/) 上撰写的《通向 KDE 4
之路》系列文章，是我们了解 KDE 4
最新前沿技术的一扇窗口。现在，这些文章已被来自[云帆论坛](http://www.myswear.net/forum/)的
yuanjiayj 和千里孤坟网友翻译成了中文。那么，让我们从 SVG
透视技术开始了解吧。

自从 KDE 4 的开发全力进行，而 KDE 4.0
版将在今年稍后一点的某个时间发布。我想是时候整理出一个名叫通向 KDE 4
之路的每周栏目了。这个想法大致是把 KDE 4
有进步的几个特性分期做几个简短的回顾。这是第一期，目的是将伟大的 SVG
透视技术目前所得到的结果呈现于大家的面前。下面是详细内容。

很多的新特性已通过 KDE Planet
的众多个人博客为人所知，而我就打算写点大家不太知道或是需要大家多了解的内容。

首先我想要告诉大家的是 KDE
的构建，安装和运行等方面已相当好了，我已测试了很多从 KDE 3.x
中移植过去的程序了，大多数程序都非常稳定。当你亲眼看到底层技术的进步所引起的那些改变的时候，那是真正令人非常开心的。今天我将介绍的是由
Qt 4 中的 SVG 透视技术所带给人们的感观享受。

很多其它 KDE 程序正在运用 SVG
技术所带来的好处，这会让它们更令人愉快。你可以从
<http://tsdgeos.blogspot.com/2006/12/svg-meets-blinken.html> 和
<http://wiki.kde.org/tiki-index.php?page=KDE+Games+SVG+status>
找到很多有关信息。

今天我将把一些 KDE 3.5.5 中的一些软件和 KDE 4
中的对应软件的截图拿出来作个对比。

首先我们看到的是 KDE 系统守护软件（ KDE System Guard），它是 KDE
中一个很有用的工具。你可以输入“ksysguard”来运行它。它收集了各种简洁的底层信息，如内存和
CPU 使用表以及进程表等。

下面是 KDE 3.5.5 中它的样子：

[![Ksysguard](http://i.linuxtoy.org/i/2007/02/vol1_355_ksysguard_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_355_ksysguard.png)

而现在 KDE 4
的开发版中它是这样的（线条是抗锯齿的，图表是半透明的，背景是 SVG）：

[![Ksysguard](http://i.linuxtoy.org/i/2007/02/vol1_devel_ksysguard_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_devel_ksysguard.png)

看到了吧，这种改进是否很有意思呢！

下一个，我们看到的是 kdegames 中的几个软件。首先出场的是
KAtomic，这是个迷宫类的游戏，它很有趣，也有半教育性，它也用 SVG
技术改进了。看看对比吧。

[![KAtomic](http://i.linuxtoy.org/i/2007/02/vol1_355_katomic_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_355_katomic.png)

而在 KDE 4 中它具有了 oxygen 风格：

[![KAtomic](http://i.linuxtoy.org/i/2007/02/vol1_devel_katomic_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_devel_katomic.png)

接下去出场的是 KMahjongg，它也算是一个迷宫游戏吧。它在 KDE 3.5.5
中的样子与 Windows 娱乐包中的一个软件的样子很像。

[![KMahjongg](http://i.linuxtoy.org/i/2007/02/vol1_355_kmahjongg_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_355_kmahjongg.png)

而 KDE 4 中，经过 SVG 技术改进后，麻将牌变成了这个样子：

[![KMahjongg](http://i.linuxtoy.org/i/2007/02/vol1_devel_kmahjongg_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_devel_kmahjongg.png)

最后要介绍的是一个很常用的 KDE 组件：“运行命令”对话框（Alt－F2），KDE
3.5.5 中它是这样的：

[![Run](http://i.linuxtoy.org/i/2007/02/vol1_355_run_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_355_run.png)

而现在，在桌面界面设计中的大师 Aaron Seigo 的指导下，它成为了 Plasma
桌面中一个 SVG
主题式，优雅的组成部分。它还是个半成品，但下面的截图中会让你感受到这个创意的。

[![Run](http://i.linuxtoy.org/i/2007/02/vol1_devel_run_s.png)](http://i.linuxtoy.org/i/2007/02/vol1_devel_run.png)

下期我还会向大家介绍 KDE 4 中的另一个特性。祝大家开心。

原文：[The Road to KDE 4: SVG Rendering in
Applications](http://dot.kde.org/1167723426/)  
译文：[通向 KDE 4 之路（一）：SVG
透视技术](http://www.myswear.net/forum/viewthread.php?tid=7680)

（Troy Unrau／文 yuanjiayj／译）
