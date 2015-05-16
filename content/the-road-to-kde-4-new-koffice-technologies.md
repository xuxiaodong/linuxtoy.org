Title: 通向 KDE 4 之路（二）：新 KOffice 技术
Date: 2007-02-08 09:48
Author: toy
Category: Apps
Slug: the-road-to-kde-4-new-koffice-technologies

本周的 KDE 之路栏目所要介绍的是 KOffice 项目中的 KWord 2.0。KWord 1.6.1
已经是一个强大的 KDE 集成的文字处理器，但应用了 KDE 4 技术之后的 KWord
2.0 将成为最强大的开源文字处理品之一。以下是详细内容。

KWord 与 Kexi 不同，作为一个 KDE 软件，它一直都被笼罩在巨大的
OpenOffice.org 组件的阴影之下。但这种情况将会得到改变，新的 KDE 4
技术将可使它作为原生程序的形式运行如 Windows 和 Mac OS X
等其它平台下。您可以从一些文件中找到 KDE 4
程序对其它平台的支持方面的详细情况。

KOffice 和 KWord 的最大的一个功能是对 OASIS OpenDocument
格式标准的支持，这种格式被众多办公软件（如 OpenOffice.org、Google
Docs）采用。目前开发者们正全力工作以求在 KWord 中获得对 ODF
格式的全面支持。

让我们看一下正在开发中的
KWord。请注意界面中各个方面中良好的图形保真效果。在我的系统中，它并不比
KOffice1.6.1 运行的慢。KWord 2
中获得最多改善的地方是它的文本格式与排版功能，这个功能也特别值得推荐。虽然它的开发还在继续中，但您从下面这张图中可以发现它比以前的版本要进步很多。您真的需要亲身体验一下新版本中移动、缩放以及旋转图层等操作时是多么地流畅。

[![KWord](http://i.linuxtoy.org/i/2007/02/vol2_devel_kword-flake_s.png)](http://i.linuxtoy.org/i/2007/02/vol2_devel_kword-flake.png)

添入 KWord 中的所有对象都会被转化为新的图层库，如 KFormula
所生成的公式，您可以在 KWord 中准确无误地插入做好的数学公式。这使得
KWord 可以像 KPresenter
那样轻松地进行页面排版，因为您不再受制于呆滞、规矩的文本格式。这些改变将使得
KWord 2 成为受注目的基础桌面排版程序。

另外在早期版本中缺少拼写检查支持的现象将得以改善，我们将使用 Sonnet
来完成拼写、语法检查。（在我的截图中没找到拼错了的单词吧？）

但这也不是 KOffice 2 中唯一的改进。例如在 KOffice 2
中我们还加入了新的扩展脚本嵌入框架
Kross。开发者们已为它做了很多的工作，而它也将是 KOffice 2
中的一个杀手级特性。

下图展示的是在 KWord 中新脚本菜单：

[![KWord](http://i.linuxtoy.org/i/2007/02/vol2_devel_kword-scripts_s.png)](http://i.linuxtoy.org/i/2007/02/vol2_devel_kword-scripts.png)

注意图中我是如何打开子工具栏的。我直接通过拖放就让它自动出现了。这是 Qt
的新特性，这样操作不会造成明显的界面不稳。

当然 KOffice 的其它组件也能应用脚本嵌入和图层特性。KSpread
和脚本功能结合的很好，对高级用户来说它实在是太强大了。

[![KSpread](http://i.linuxtoy.org/i/2007/02/vol2_devel_kspread_s.png)](http://i.linuxtoy.org/i/2007/02/vol2_devel_kspread.png)

对 Kross 有兴趣的朋友可以看看关于 KSpread 中 Kross
的开发与应用的这篇文章：<http://wiki.koffice.org/index.php?title=KSpread/Scripting>。

这只是运行于 KDE 4 平台上的 KWord 和 KOffice
中大量改进工作中的一些。当然这些截图展示的还只是开发中的版本，它还不太稳定，但在开发者的频道（如
irc.freenode.org 中的
#koffice）中稳定性是反复强调的。在新版本发布之前还有大量的幕后工作要做。

KOffice 有独立的发布时刻表，所以它也许不会与 KDE 4 同时发布。

原文：[The Road to KDE 4: New KOffice
Technologies](http://dot.kde.org/1168284615/)  
译文：[通向 KDE 4 之路（二）：新 KOffice
技术](http://www.myswear.net/forum/viewthread.php?tid=7705)

（Troy Unrau／文 yuanjiayj／译）
