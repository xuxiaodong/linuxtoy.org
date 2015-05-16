Title: 通向 KDE 4 之路（九）：Dolphin 与 Konqueror
Date: 2007-03-03 14:33
Author: toy
Category: Apps
Slug: the-road-to-kde-4-dolphin-and-konqueror

经常看 KDE 新闻的朋友也许已经注意到了，最近在 kdebase
模块中多了一个新东西。[Dolphin
文件管理器](http://enzosworld.gmxhome.de/)作为 Konqueror 的补充被加入了
kdebase。以下是这个新的文件管理器以及它与 Konqueror 和 KDE
相关部分的关系的详细内容。

首先大家对 KDE 中的文件管理器作一个回顾：出现在 KDE 1.x 中的是 KFM（KDE
文件管理器），它是一个初步的拥有一定网络浏览功能的文件管理器。下面是一张
KFM 的截图（从 kde.org
的截图库里找出来的），从图中您可以对它的操作方式有一个了解。

[![KFM](http://i.linuxtoy.org/i/2007/03/vol10_1x_kfm_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_1x_kfm.png)

虽然从 KDE 1.x 开始，KDE 已发展了很多年了，但仍然可以很容易地发现 KFM
的某些部分启发了 Konqueror 的设计，那些设计就被加入了当时的 KDE 2.0
中。KParts 技术为我们的文件管理程序带来了新的革命，同时也造就了
Konqueror 这个集网络浏览器、文件管理器等功能为一体的强大程序。下面是张
KDE 3.5.6 中 Konqueror
的截图，您可以看到虽然界面改进了很多，但依然可以看到当年 KFM 的影子。

[![Konqueror](http://i.linuxtoy.org/i/2007/03/vol10_356_konq_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_356_konq.png)

Konqueror 实为 KDE 2.x 和 3.x 系列中 KDE 技术的代表作，它展示了 KDE
技术中最优秀的部分。Konqueror 显示了 KDE 的 IOslaves
技术的强大，这个技术使得您通过 FTP、fish（SSH）、HTTP
以及其它协议进行文件操作时实现网络的透明化（网络操作时与在本机操作一样方便）。Konqueror
是如此的先进，只要您在地址栏填上 FTP
位置，您就可以像在本机上一样操作它（据我所知，只有 Konqueror
能做到这点）。它的 KParts
功能可以令它嵌入各种所需的查看器，如可以直接在它的界面中嵌入如
[KPDF](http://kpdf.kde.org/)、[KWord](http://koffice.kde.org/kword/)、图像查看器，当然还有我们最重要的
[KHTML](http://www.khtml.info/) 网页翻译引擎。有了 KParts，Konqueror
的图标查看功能也可作为一个插件来实现。

Konqueror
真是个强大的工具，它可以完成您或您的系统想做的任何事，并且可以通过模块和插件无限制地对它进行定制和扩展。当
Konqueror
用作网络浏览器的时候，它仍然可以以一个文件管理器的方式工作。看看
Konqueror
的工具栏上的按钮吧，您可以轻松地注意到这种独特的运转方式。例如工具栏的那个“向上”按钮在您浏览
Google
地图的时候仍然可用。但它与网页内容一点关系也没有，另一个例子是当您在排列
/home/ 里的图标时，它的网络书签依然可用。

Dolphin 的介绍：Dolphin 是 KDE 4
中的新文件管理器，它百分之百地专注于文件管理功能而并不想成为一个如
Konqueror 那样万能的程序。它试图优化与文件管理相关的工作，并为 KDE
用户提供一个易于使用的灵活的文件管理器。这并不意味着它功能匮乏或无法定制，这只是表示
Dolphin 是为单一目的而构建的。

Dolphin 也不是完全重写的新项目，也没有与 Konqueror
竞争的打算，这两个程序都将得到喝彩。Dolphin 使用 KDE 平台上已存在的 IO
slave
来完成远程或本地文件管理，也就是说它可以胜任所有“远程”管理之类的任务，而此功能正是得益于
Konqueror。Dolphin 将不会显示网页或像 Konqueror 那样嵌入式地显示 PDF
文件。

Konqueror 也将从 Dolphin 中受益。虽然 Konqueror
的用户界面会有所调整，它也不再是 KDE 4 的默认文件管理器了，但是它不会在
KDE 4 中消失。Konqueror
的文件管理功能仍然会得到保留，其功能与过去一致没有改变。在 Dolphin
的开发而带来的对 KDE 的图标查看部分的改进也将被用于改进 Konqueror
的图标显示，因为他们共享同样的底层库。前面提到的 Konqueror 使用 KParts
实现图标查看功能，对于底层的 KParts 的改进将使 Konqueror 的用户受益。

现在让我们看看 [KDE SVN 库](http://websvn.kde.org/)中的 Dolphin 和
Konqueror
的截图吧。请注意这些截图代表的是开发者目前所构建的样子，而并不表示它最终就是这样了或是功能已定型了，也不表示推荐大家编译
SVN 中的这两个软件作日常使用。

[![Konqueror](http://i.linuxtoy.org/i/2007/03/vol10_4x_konq_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_4x_konq.png)

您可以将 Konqueror
设置为默认使用标签浏览，也可以定制其它相关界面。它目前常作为一个网络浏览器来使用，只是偶尔被用于作文件管理。
Konqueror 最初就是由文件管理器衍生而来，现在它却越来越多地被 KDE
用户们用作网络浏览器。作为一个网络浏览器，Konqueror 工作的很好，它对
[CSS 3
的兼容性](http://www.css3.info/khtml-356-is-the-most-css3-compliant-of-all/)非常出色，包括对高度期望的“不透明标签”的支持也很好。

在 KDE 3.x 中 Konqueror
的网络浏览器功能不断改进的同时，其标准的文件管理功能也将得到维护。而它文件管理部分的代码与
Dolphin 共享，从而也从 Dolphin 的开发中获益。

Dolphin 与 Konqueror
完全不同，它是一个“真正”的文件管理器，它的界面中的大量元素是专门为文件管理开发的，它也不会由于要作为一个网络浏览器而被迫调整。可以用一个截图来证明：

[![Dolphin](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_breadcrumb_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_breadcrumb.png)

请注意 Dolphin
的“breadcrumb”式的目录选择器，这个东西对于文件管理时非常有用，但如果您需要使用浏览器的
URL
地址时它就没什么用了，因此它就是那种只用于层次文件处理的窗口小部件。对于用过
OS X 的 Finder 或 GNOME 的 Nautilus 的朋友来说，breadcrumb
部件应该不陌生吧。对上面这张截图的另一个注明是：点击并按住一个
breadcrumb
目录条时，它会出现一个下拉的目录表，这个目录表显示的是与其目录同级的文件夹，这就提供了更高效的文件导航了。

[![Dolphin](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_alt_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_alt.png)

不过 breadcrumb 部件也不一定需要，如果您更喜欢 Konqueror
式的地址栏的话，在设置中做个更改就行了。Dolphin 的定制度也很高，看下面。

[![Dolphin](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_options_s.png)](http://i.linuxtoy.org/i/2007/03/vol10_4x_dolphin_options.png)

这张截图证明了 KDE
在设置排版方面花了大力气，它提供了尽可能需要的选项但设置条款的排布上却清清楚楚。请注意
KDE 4
的设置对话框的改进。当然对某些屏幕来说，它的对话框显得过于高大了，有些地方尚需修改。等
Oxygen 图像组件齐备之后，这个对话框也会更容易看了。

Dolphin 的功能也不完全是新的，它只是换了个新的方式而已。它可以看作是
Konqueror 功能和 Nautilus 框架的混同体。Dolphin 构建于壮健的 KDE
基础之上，它重新利用了如 KIO slaves 等现有技术，并有所创新。在 Konqueror
中常用的右键操作仍然会最大限度的保留（只是 Donphin 不会像 Konqueror
那样嵌入查看器，它会在外部启动程序）。Konqueror
现在的开发关注于其网络浏览体验，而在 KDE 2.0
时代就具备的文件管理功能仍将支持。

当 KDE 4 发布的时候，Dolphin 将设为本地 file:/
协议的默认程序，在程序菜单中它也将被设为是默认的文件管理器。Konqueror
则是默认的网络浏览器，照顾到长期以来的用户习惯，它的文件管理器功能仍然可用。，就像
KDE 3.x 中用户也可以将第三方的程序如 Krusader
作为默认的文件管理器那样，用户也可以设置他们喜欢的程序作为默认文件管理器。请继续关注
Dolphin 和 KDE 的消息，下周见。

原文：[The Road to KDE 4: Dolphin and
Konqueror](http://dot.kde.org/1172721427/) by Troy Unrau  
译文：[通向 KDE 4 之路（九）：Dolphin 与
Konqueror](http://www.myswear.net/forum/viewthread.php?tid=7910) by
yuanjiayj
