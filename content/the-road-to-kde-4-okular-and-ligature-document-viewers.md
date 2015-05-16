Title: 通向 KDE 4 之路（七）：文档查看器 Okular 和 Ligature
Date: 2007-02-15 13:22
Author: toy
Category: Apps
Slug: the-road-to-kde-4-okular-and-ligature-document-viewers

本周的通向 KDE 4
之路栏目又将焦点转回到应用程序上来。今天要介绍的这两个极有前途的 KDE 4
软件是 [Okular](http://okular.org/) 和
[Ligature](http://websvn.kde.org/trunk/KDE/kdegraphics/ligature/)。虽然它们是
KDE 4 中出现的新星，但在 KDE 3 中都可以找到它们萌生的根基。下面是细节。

过去，KDE 中包含了各式各样的用于查看各种文件格式的程序，通过 KDE 的
KParts 技术，这些查看器在需要时可被嵌入到其它 KDE 程序（如 Konqueror
等）中。这些查看器支持的格式有 TIFF、PDF、PostScript、fax、DjVu
等等。Okular 和 Ligature
从那些早期的简单的查看器的设计中汲取了大量的营养，逐渐步向成熟。

KDE 中早就包含了一个叫作 KGhostView 的软件，它使用 GhostScript
作为后端，可同时查看 PDF 和 PostScript 格式的文件。 KDE
已经将其作为打印预览工具。下面就是 KDE 3.5.6 版中 KGhostScript
的一张截图。请注意图中有些文字渲染失真的情况可能是与我所用的发行版中所选的字体有关，而不一定是因为
KGhostScript 渲染文件的功能有缺陷。

[![KGhostScript](http://i.linuxtoy.org/i/2007/02/vol7_356_kghostview_s.png)](http://i.linuxtoy.org/i/2007/02/vol7_356_kghostview.png)

在 KDE 3 系列中，KGhostView 有了一个可用于查看 PDF
文件的竞争对手。这就是 KPDF，它在功能、速度等很多方面都令 KGhostView
黯然失色。现在许多发行版都将 KPDF 作为 KDE 中默认的 PDF
浏览器。下图就是显示与上图同一文件的 KPDF。

[![KPDF](http://i.linuxtoy.org/i/2007/02/vol7_356_kpdf_s.png)](http://i.linuxtoy.org/i/2007/02/vol7_356_kpdf.png)

就个人体验来说，KDE 中的 KPDF 表现的令人惊奇。当我点击网页中 PDF
文件的链接，并指定在浏览器中显示它时，KPDF 可快速而无缝地嵌入到
Konqueror 中，它表现地如此之好以至于我几乎会忘记当前页面不是 HTML
格式了。

还有一些高级功能如文本搜索，PDF 文件的拷贝与粘贴等 KGhostView
从来没真的实现过。在图层渲染，特别是加载的 PDF
文件中包含了大量矢量图像的时候，KPDF
要快上很多。在工作中，我用到大量的地图，这些地图大都是 PDF 格式的，使用
KGhostView
查看时慢的一塌糊涂，您甚至可以逐条地看到地图上那些矢量图慢慢地显现出来。而
KPDF 加载相同的地图时可以做到立即显现，这令我节省了大量的时间。

KPDF 不久前决定扩大它的文件支持范围，而不再仅仅支持 PDF 格式了，这得感谢
Google 公司的“代码之夏”活动的赞助。他们决定在 KPDF
中进行扩展而不是另起炉灶做个全新的软件的主要原因是 KPDF
已经具备了大量高级功能，而在查看其它格式的文件时这些功能就不需要重新实现了。为了更准确地反映
KPDF 演化为一个可以支持众多文件格式的查看器，它就被改名为“Okular”。

KDE 4 的用户们面临一个使用上的选择，即究竟是用 Okular 还是选用
Ligature，因为两者都被设计为支持大量的文件格式（有时它们的功能是重复的）。但因为它们都可被嵌入到其它应用程序中，无论用户用到哪一个都会同样觉得高兴。我将首先谈谈
Okular，因为我手上掌握了关于它的大量信息。在原本功能都很完备的 KPDF
的基础上，Okular 中有了引人注目的巨大改进。目前，它看来是 KDE 4
中最好的应用程序之一。

Pin Toscano (irc.freenode.org 上他叫 pinotree) 是 Okular
的开发领袖。目前它在 KDE SVN 中开发，有兴趣的朋友可以在
[/trunk/playground/graphics/okular](http://websvn.kde.org/trunk/playground/graphics/okular)
下找到它的源代码。它在 KDE 4 已相当稳定——实际上它是我所试用过的最稳定的
KDE 4 软件之一。它也已被纳为 KDE/Mac 软件包的一部分。 Benjamin Reed
提交了下面这张在 Mac 中运行的 Okular 的截图：

[![Okular](http://i.linuxtoy.org/i/2007/02/vol7_4x_mac_okular_s.png)](http://i.linuxtoy.org/i/2007/02/vol7_4x_mac_okular.png)

他提到：“真爽啊，Okular 在 OS X 中运行的很快。我可以把 Acrobat
扔掉了！:)”

我没有测试所有它支持的文件，但根据 Okular
网站中所列出的[支持格式](http://www.okular.org/formats.php)，它已能完全或部分支持以下
11
种文件格式：PDF、PS、TIFF、CHM、DjVu、DVI、XPS、OOo、FictionBook、ComicBook
和 s
标准图形文件。为了所有这些格式都可完美地支持，开发工作仍在继续中，更多的格式支持也已列上日程。Okular
将与 KDE 4
同时发布，届时不一定所有格式支持都启用，这取决于那时它们的稳定程度，当然您所用的发行版也可能会作出增删的决定。

下面这张图是查看 ComicBook 格式的
Okular，这种格式通常用于在线发行漫画。考虑到今后 KDE 4
可运行多个平台，Okular 甚至有可能成为最受欢迎的 ComicBook 查看程序。

[![Okular](http://i.linuxtoy.org/i/2007/02/vol7_4x_okular_s.png)](http://i.linuxtoy.org/i/2007/02/vol7_4x_okular.png)

Pino
很乐意与[易用性小组](http://www.okular.org/news.php#itemokularjoinsTheSeasonofUsabilityproject)的伙伴们共同工作以改进
Okular 的易用性，这也是 [Season of Usability
项目](http://dot.kde.org/1170202411/)的一部分。在 KDE 4.0
发布之前，它的很多界面部分都将会得到几乎是彻底地精细检查，以使得它可以做的更好。

KDE 4 中一个可作为竞争对手的文档查看器是 Ligature，其前身是
KViewShell。它存在于 kdegraphics
模块中，所以它目前是它所支持的各种格式的默认查看器。但对于那些更喜欢
Okular 的人们来说，这个默认随时都可以被推翻。我所能找到的可以使 Ligature
继续在 kdegraphics 模块中存在的唯一理由是“历史因素”：其前身 KViewShell
过去本来就是 kdegraphics 的一部分。但这也不意味着 Okular 就不会被 KDE
接受：如虽然 Amarok 从不曾放在正式的 kdemultimedia 包中，但 Amarok 仍是
KDE 最好的软件之一。

目前 Ligature 本身支持 PDF、PostScript、EPS、fax、Tiff、DjVu
等文件格式，同时 SVN 中也有支持 TeX 格式的插件。在我印象中“fax”格式与
TIFF 图片格式有很深的关系。Ligature 的前身 KViewShell 在其主 kdegraphics
分支中还不支持上述格式中的某几种，但在 KDE 3.5.x
分支中已加入了对上述几种格式的支持。

我试图弄一张显示 PDF 文件的 Ligature 的截图出来，但它却不能加载 PDF
文件。我试了一个 PostScript
文件，它加载后什么都没显示出来。所以我只好加载了一个实在无趣的 DVI
文件来展示 Ligature 当前的用户界面，但它的渲染功能也只是一般。

[![Ligature](http://i.linuxtoy.org/i/2007/02/vol7_4x_ligature_s.png)](http://i.linuxtoy.org/i/2007/02/vol7_4x_ligature.png)

看样子 Ligature 与 Okular
的用户界面很相像。这很大程度是由于它们都利用相同的标准 Qt 和 KDE
库来绘制用户界面部件。因为 Ligature
还不能显示一些文档，所以我就无法将之与 Okular
作实际的易用性对比。不过请注意，当前它还在开发状态下，出现一些低级失误也不必过于苛责。

关于 DVI 文件的说明：为了查看 DVI 文件，您需要安装一些 TeTeX
文件，在我的发行版上加起来总共是 85 Mb 左右——这可能是 DVI
文件不太受欢迎的原因之一吧，虽然它的渲染能力还是很出色的。当 Ligature 在
DVI
文件中找到一个超级链接时，它会在文本下显示一条下划线以示可被点击，这在某些场合下是很有用的，不过这种链接也使得文件很丑陋。Okular
就没有加上这种下划线，但也工作的很好。

Okular 与 Ligature
使用了不同的内部构架，实现了相似的效果，但它们内部所依赖的底层库是相同的（就像
MPlayer 和 xine
内部千差万别，但它们都使用相同的底层库来解码）。这就意味着它们不太容易合并为一个项目，而对底层库的跟进开发则可同时使得两个程序都受益。Okular
将会被各个发行版单独打包，而由于现在很多发行版最终都会把 kdegraphics
分解为若干个包，Ligature
就将会是这些软件包中的一个。当然了，只要也安装了必要的 KDE 库，GNOME
用户们也可以正常地使用 Okular 和 Ligature。但他们也可以使用共享底层库的
[Evince](http://www.gnome.org/projects/evince/)，而 Evince 与 GNOME
环境集成的更好。

本周的内容就是这些。希望可以澄清关于 Okular 和 Ligature 的混乱。

原文：[The Road to KDE 4: Okular and Ligature Document
Viewers](http://dot.kde.org/1171453163/)  
译文：[通向 KDE 4 之路（七）：文档查看器 Okular 和
Ligature](http://www.myswear.net/forum/viewthread.php?tid=7863)

（Troy Unrau／文）  
（yuanjiayj／译）
