Title: 通向 KDE 4 之路（三）：完全的 Mac OS X 支持
Date: 2007-02-08 10:47
Author: toy
Category: Apps
Slug: the-road-to-kde-4-full-mac-os-x-support

虽然 KDE 的设计在 Linux、FreeBSD 以及其它 UNIX/X11
平台上均可成功移植，但这并不表示它在其它平台上就没有突破。奇趣公司在 GPL
协议之下发布了面向 Mac、Windows 甚至是嵌入式平台上的 Qt 新版本——Qt 4。Qt
是 KDE 开发的基础，因此 KDE
现在也获得了在这些平台上的原生支持。今天我主要讲的是 KDE/Mac
的开发情况。下面是详细内容。

在我讲述之前，我想先讨论几个 KDE 必将面对的一些问题。在 KDE 3 中，KDE
这个术语指的是 K 桌面环境（Kwin、Kicker、kdesktop 等），由此当它面向 Mac
OS X 的版本中不再出现这些组件时它还有理由被称为“KDE”吗？或者 KDE
是指这整个项目，按这种说法，无论 Konqueror 是否运行于 Mac、Windows 或者
Enlightenment 等平台，它都可被称为一个“KDE 程序”。

有一些关于 KDE 4
的问题已被讨论过了。讨论的结果是“KDE”就像一把大伞，它包括 KDE
的所有东西。也就是说 KDE 应用程序，KDE 开发环境（库以及技术），KDE
工作空间（由 KWin、Plasma 等组成），这三个主要部分组成了 KDE
软件。当我们谈及 KDE 时，它所指的就是全部。

这种说法也解决了一些有着独立发布时刻表的软件所带来的问题。例如 Amarok
有一个与 KDE 不同的时刻表，于是有一些人就不把它看作是 KDE
整体的一部分。在 KDE 4 中的 Amarok
清楚地被标为是一个可限制性运行于某桌面环境中的“KDE
程序”，而不存在任何的隐晦。在 KDE 4 中，虽然 Amarok
有独立的开发周期，但它仍是一个 KDE 产品。正如 Amarok 的首席开发者 Mark
Kretschmann 所说的，“如果 Amarok 使得更多的用户去使用 KDE
技术的话，那就很理想了。如果有人在其它平台上如 GNOME 或 Mac
上使用它的话，对我们来说也不错。”

本文说的是非运行于 X11 平台上的 KDE，所以我们需要先将 KDE/X11 与 KDE/Mac
区分一下。在询问了一些开发者后，我采用这种说法：KDE/X11 指的是所有 KDE
程序运行于 X11 上，开发环境搭建在 X11 上，KDE 工作空间也在 X11
上。同样的，KDE/Mac 是指 KDE 程序运行于 Mac 上，KDE 开发环境搭建在 Mac
上，而 KDE 工作空间则不存在于 Mac 上，这里没有包括它。以上说法同样适用于
Windows 平台。然而必须知道的是这些所谓的区别仅仅在于平台不同，最重要的是
KDE
源代码是相同的，并没有为某个平台将代码树分开。不存在分支或者异样的端口。

新的 KDE 开发环境技术如 Phonon 和 Solid
可使移植变的轻松，因为与平台的整合工作发生在库的水平上。KDE
程序的开发不必太在意操作平台的不同。

什么是 KDE/Mac？

KDE/Mac 是可原生运行于 Mac 操作系统上的 KDE 程序的集合，包括使这些 KDE
程序工作的底层技术，库等。KDE/X11 与 KDE/Mac
只有略微的不同。最大的不同是 KDE 工作空间如 KWin 和 Plasma 等不会在 Mac
上出现。原因是 KWin 和 Plasma 的功能在 OS X 系统中已经存在，强行地在 Mac
系统上实现它们会造成 KDE 程序与其它 Mac 程序不能很好的整合在一起。因此
KDE 就没有把 KDE/X11 移植到 Mac 中去了。

在 KDE 设计之初就考虑到 KDE 程序与其它 UNIX 桌面环境（早期是指 Window
Maker，后来是 GNOME 和 Enlightenment）共存的问题。KDE
程序用的是共享的标准（如 FreeDesktop.org
的成果），可共享剪贴板数据、系统托盘，所以与其它平台的兼容问题较少。而现在由于
Qt 4 所带来的高度可移植性，在如 Mac 等非 X11 环境中 KDE 的兼容性也很好。

KDE 程序以前就能运行于 Mac 平台上，它可使用苹果公司建立在 OS X 系统上的
X11 服务层，但因为 KDE 仍然使用 Qt/X11，所以这些程序看起来与运行在普通
X11 平台上的样子差不多。事实上它们能良好的运行， Fink
项目的出色成果功不可没。如果您有兴趣在 OS X 系统运行其它 UNIX
程序的话，去看看 Fink 项目吧。

（其实也存在一个 Qt/Mac 的自由软件版本可以在 Mac 平台上使用 KDE 3.x
系列的程序，但由于稳定性的原因，通常还是使用包含 Fink 技术的 KDE/X11。）

下面是一张用 Fink 技术将 KDE 3.5 运行于 Mac 系统的截图。

[![KDE](http://i.linuxtoy.org/i/2007/02/vol3_3x_small_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_3x_small.png)

由于建立在 Qt/X11 平台上，这使整个 KDE 环境都能够运行。但可明显的发现
KDE 与 Mac
系统没什么协调性，就好像是在一个屏幕上运行了两个完全不同的计算机系统。

KDE 4 则在移植工作中取得了巨大的进步，这很大部分要归功于 Qt 4，还有基于
CMake 的新的 KDE 构建系统。在“KDE on Mac OS X”网站上 KDE/Mac 程序的 .dmg
文件已作为一个标准发布包提供下载。多亏了 KDE/Mac 项目的头儿 Benjamin
Reed，KDE 开发快照版可以很容易地运行在 Mac 平台上。请访问
irc.freenode.org 的 #kde-darwin 频道帮助报告和解决问题。现在 KDE 4
还远没到可发布的程度，它还很可能崩溃。

已下载的软件包被打开并被安装之后，KDE/Mac 程序可以使用 OS X 的 Finder
运行，如下：

[![Finder](http://i.linuxtoy.org/i/2007/02/vol3_mac_finder_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_finder.png)

从上图可以看到大量的 KDE 程序已可以在 Mac
上使用。由于这还是一个开发中的版本，有些程序很容易崩溃（就像使用 SSL
的程序）还有些东西看起来很丑陋。在这点上，目前运行于 X11 上的 KDE 4
也是同样的，希望 KDE 4 的开发可以在这两点可以同时改进。

在移植的同时，一些非常重要的工作也发生在 KDE/Mac
的整合中。例如，剪贴板，键盘快捷键，其它语言输入等。还有鼠标拖放仍然很粗糙。KDE/Mac
的开发者们需要任何了解 KDE 和 Mac 技术的伙伴来帮助他们解决这样的小问题。

这就是你们所期待的：在截图中大家都看到了目前 KDE 4
移植工作的进展情况。Mac 用户对其中的一些程序也是赞赏有加。

由于我们使用 SVG 技术，我就先贴一张在 Mac 平台上的 SVG 截图。下面是
Shisen Sho，这是一个板块游戏。Shisen Sho 与 KMahjongg 共享了 SVG
板块。这个游戏在 Mac 上看起来很漂亮，风格也很一致。

[![Shisen
Sho](http://i.linuxtoy.org/i/2007/02/vol3_mac_kshishen_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_kshishen.png)

上周有人问起 KOffice
是否也支持其它平台。我现在可以愉快地告诉你们，KWord、KSpread 以及
KOffice 的其它组件在 KDE/Mac 上运行的很好。我在上周测试了开发中的
KOffice 2，KWord 与它在 KDE/X11
中的版本运行的一样好。同时我还运行了其它一些 KOffice
程序看它们是否工作。下面是一张运行于 Mac 系统上的 KSpread 向导及 KDE4
文件对话框的截图。

[![KSpread](http://i.linuxtoy.org/i/2007/02/vol3_mac_kspread_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_kspread.png)

还请注意下 KSpread 图标在 OS X 底栏上的显示。它可不像运行于 Fink
技术上的 KDE 那样（在桌面左方会出现一个 KDE
边栏），可调置为自动隐藏。已运行的程序图标显示在边栏上。

当然也许有人会问：Konqueror 能运行吗？答案是可以。KDE 4 版本的 Konqueror
主要是 KDE 3.5 中的 Konqueror 的移植工作，但其后端库如 KHTML 渲染引擎和
Javascript 支持都获得了大量的改进。在 Mac 上，由于 Qt 4 实现的 OS X
风格，我们使用的是当中的标签浏览，如下：

[![Konqueror](http://i.linuxtoy.org/i/2007/02/vol3_mac_konq_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_konq.png)

Mac 自称是图形与多媒体程序第一平台。但此快照版中没有找到 KDE
图形包，所以我就不能抓张图出来看看了。

但 education 包里的小程序还是可以让 Mac 显露一点锋芒的。下面是包含在
KDE-Edu 项目中的两个优秀的程序：Kalzium 和 KStars。在 KDE-Edu
项目中的新特性容我以后介绍。现在还是让我们看看 KDE/Mac
中的这两个华丽而又功能完备的程序。

[![Kalzium](http://i.linuxtoy.org/i/2007/02/vol3_mac_kalzium_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_kalzium.png)

[![KStars](http://i.linuxtoy.org/i/2007/02/vol3_mac_kstars_s.png)](http://i.linuxtoy.org/i/2007/02/vol3_mac_kstars.png)

图片就贴到这里了，当 KDE 运行于其它平台时，就总会出现一些其它问题的。

当我考虑这篇文章的时候，我遇到很多人，它们反对在一个非自由平台上运行 KDE
程序。他们在 IRC
上露出这样的情绪“无论何时你在一个非自由的平台上运行自由软件，上帝就会杀死一只小动物。甚至会杀死一只伶俐的小动物。”

但 KDE
有其支持其它平台的好理由：吸引开发者，鼓励互操作性以及形成标准。世界上有大量的
Mac 和 Windows 的开发者，支持了 Mac 和 Windows 就可以使大量的程序利用
KDE 技术。支持其它平台使 KDE 技术受益的最好例子是
KHTML/WebKit。现在世界上有很多用户使用基于 KHTML
的网络浏览器，各网站不得不提高他们与标准的兼容性，这就意味着更多的网站使用
Konqueror。同样的事也将会发生，如 KOffice 之与 OpenDocument
格式，Kontact 之与自由软件组件系统，这都将是双赢的。

原文：[The Road to KDE 4: Full Mac OS X
Support](http://dot.kde.org/1168899755/)  
译文：[通向 KDE 4 之路（三）：完全的 Mac OS X
支持](http://www.myswear.net/forum/viewthread.php?tid=7767)

（Troy Unrau／文 yuanjiayj／译）
