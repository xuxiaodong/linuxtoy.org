Title: 通向 KDE 4 之路（六）：令多媒体技术更轻松的 Phonon
Date: 2007-02-08 15:17
Author: toy
Category: Apps
Slug: the-road-to-kde-4-phonon-makes-multimedia-easier

继续我们的“通向 KDE 4 之路”栏目，今天我们要介绍的是精巧的新多媒体技术
[Phonon](http://phonon.kde.org/)。Phonon 的设计是为了在 KDE 4
中编写多媒体程序可以简单化，并保证这些程序可以在多个平台上及多种声音体系上工作。不走运的是，写这种关于声音类技术的文章很难配上相应的截图，所以呢，今天就多讲些技术细节吧。

Phonon 是一项新的 KDE
技术，它为多媒体程序播放音频或视频时提供了一套应用程序接口（API）。这套接口被设计成
Qt 函数的风格，这样 KDE 开发者们使用它时就不会觉得很陌生了。（如果您对
Phonon 的 API
感兴趣的话，请看看这些[在线文档](http://www.englishbreakfastnetwork.org/apidocs/apidox-kde-4.0/kdelibs-apidocs/phonon/html/index.html)，这些文档可能还是最近更新的，不过不能保证）。

首先要指出的是 Phonon 不是一个新的音乐系统服务器，它不会与
[xine](http://xinehq.de/)、[GStreamer](http://gstreamer.freedesktop.org/)、ESD、[aRts](http://www.arts-project.org/)
等构成竞争关系。相反，由于这些多媒体程序接口常常会不断变动，Phonon
以这些其它多媒体技术为后端，提供了一套不变的 API。这样就方便了，比如当
GStreamer 的 API 改变了，只要 Phonon 做相应的调整就可以了，其它使用
Phonon 的 KDE 程序都不会受到影响。

Phonon
的功能来源于开发者们所谓的“引擎”，每一种引擎支持一种后端。目前开发中的引擎有四种：xine、[NMM](http://www.networkmultimedia.org/)、GStreamer
以及
[avKode](http://websvn.kde.org/branches/work/avkode/)（[aKode](http://carewolf.com/akode/index.html)
的继承者）。可以肯定的是 aRts
光荣退休了，针对它的引擎是不会被开发的了。不过 aRts
还会在其它领域继续存在的。KDE 4.0
的目标是实现一个“保证可用”的引擎，外加一些可选用的引擎。

已被建议开发的引擎还有 MPlayer、DirectShow（在 Windows 平台上的）和
QuickTime（在 Mac OS X
平台上的）。这些额外的引擎的开发工作还没开始，因为 Phonon
的核心开发者们更关心的是确保目前开发的这个 API 功能完备。如果 Phonon
的开发者在当前这个 API
还很垃圾的情况下，就去忙于其它引擎的编写工作，那整个项目不乱套才怪呢（如果您想要出力编写一个引擎的话，请到
irc.freenode.org 的 #phonon 露个脸吧）。

当用户或程序选用了某个引擎之后，Phonon
就会使用这个已选中的引擎来确定各个后端所支持的文件格式和解码器，然后自动允许
KDE 程序播放多媒体文件。目前的 KDE 3
系列中，用户不得不手动在各个程序（如 Kaffeine、Amarok、Juk
等）中更改引擎，而不是通过 KDE 来选用引擎。

一旦 Phonon
选定了引擎，它就会使程序配合该引擎进行标准的多媒体运转。这里的标准的多媒体运转包括媒体播放器中常用操作，如播放、停止、暂停、寻找等。Phonon
也支持更高级的功能，如定义两个音轨之间跳转的方式等，这样不同的程序就可以共享这项功能而不用每次都去重新实现它。当然，一些程序想要在跳转时能有更多的控制，自己设计也没什么不可以的。

目前各个引擎中完成进度都好的是
xine，我在我的电脑上已经装上去并可以工作了。我也尝试过编译
NMM（出了名的难编译、难安装）和 GStreamer 引擎，可惜没有成功，另外那个
avKode 默认就是“停用”。我本来还想拿几张 Juk 或 Noatun 采用 Phonon
播放音频的截图出来贴一下，但它们与 KDE 3
系列版本中看起来也没什么两样（有些界面还更丑一点！）。等它们漂亮点的时候，我就在后续文章中把它们贴出来。

Matthias Kretz
提供了一个较短的[视频文件](http://static.kdenews.org/danimo/phonon_device_switching.ogm)，说的是在看电影时打开您的扬声器，验证设备的切换。Phonon
可以使您的原音频设备在切换后停止工作，从而您可以听到声音突从耳机中消失而在音箱中响起。

Matthias 也提供了下面这张使用 Phonon
设置模块选择输出设备的截图。这还在改进中，所以看起来还很粗糙。

[![Phonon](http://i.linuxtoy.org/i/2007/02/vol6_4x_kcmphonon_s.png)](http://i.linuxtoy.org/i/2007/02/vol6_4x_kcmphonon.png)

很难用截图来反映 Phonon
的工作情况（音频框架的截图实在难搞），但我可以描述下使用 Phonon
之后灵巧的一面：网络透明化。KDE 使用 KIOSlaves
来访问网络上的文件，这轻松的好像这些文件在自己的电脑上一样。多媒体程序如
JuK 或 Amarok
也能够在自己的收藏中非常透明地共享网络音频文件，开发者在实现这个功能时还不必去考虑后端引擎是否明白如何与
ioslaves 互操作这个问题。这项功能在 KDE 4
中已经部分地实现了，已可通过音频缩略图进行可视化操作了。很多人都可以使用任何
KIO 协议，包括 sftp:// 和 fish:// 这两个 KDE
强人们非常喜欢的协议进行文件共享。在我的电脑上自行编译的 fish://KIOslave
还很不稳定，不过据 #phonon IRC
上的开发者宣称，这个功能的将很快结束编写并投入使用，届时它的稳定性就没问题了。

正在开发中的 Phonon 将成为 KDE
程序的一项支柱性技术，它会使开发者的工作更轻松，并可避免多媒体后端的变动对各应用程序带来繁杂工作以及不稳定性，更使得
KDE
程序对其它平台的支持变得轻而易举。这就意味着那些开发者们可以在他们程序的其它部分花更多的时间，KDE
多媒体程序也将会变得比现在的更出色。

一些小消息：Amarok 的首席开发者 Mark Kretschmann 在本周正式开始了对
Amarok 2.0 的开发，而且他对 Phonon 对 Amarok 2.0
能起到的作用很感兴趣。Amarok 开发小组还是与他们在 1.4
系列版本中做的那样，还在开发自己的引擎。不过，就 Phonon
目前的开发状态来说，Phonon 还是可以通过调整来满足 Amarok 的需要的。

Phonon 开发者们的老大 Matthias Kretz 正在寻找有人可以为 Phonon
维护他们的网站，如果您想在非编程方面帮助 KDE 的话，不妨考虑一下。

原文：[The Road to KDE 4: Phonon Makes Multimedia
Easier](http://dot.kde.org/1170773239/)  
译文：[通向 KDE 4 之路（六）：令多媒体技术更轻松的 Phonon  
](http://www.myswear.net/forum/viewthread.php?tid=7844)  
（Troy Unrau／文 yuanjiayj／译）
