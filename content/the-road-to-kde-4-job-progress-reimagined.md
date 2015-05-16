Title: 通向 KDE 4 之路（四）：新的工作进度管理器
Date: 2007-02-08 11:31
Author: toy
Category: Apps
Slug: the-road-to-kde-4-job-progress-reimagined

你有过这样的经历了吗，10
个程序的任务栏同时出现在你的桌面上，只有等某个任务结束时其任务栏才会消失？文档打印进度，K3b
CD 烧制对话框，KAudioCreator 的音频编码器，Konqueror
的文件传输，Kopete，KTorrent，KMail 正在检查邮件……而 KDE 4
中新的工作进度管理器将统一显示这些任务了，这将使您更轻松地查看和管理你的系统中正在进行的任务。下面是详细内容。

设想下 Firefox 的下载管理器与 KDE
的打印队列管理器，除了工作类型外并没有什么实质上的差别。每个 KDE 4
程序在有任务时都会在一个进度管理器对话框内添加一个叫作观察器（Observer）的标记。然后这个独立的程序就能观察到任何正在进行中的任务了，并且能像原来的进度对话框那样显示进度甚至添加某些可回馈到原程序的操作按钮（如“取消下载”等）。有些程序如
K3b，它已具备了非常良好的进度报告系统，那它们的对话框就会保留下来，但其进度仍将被新的进度管理器观察到，于是所有的任务进度条都被放在了同一个地方。

在 [Rafael Fernandez Lopez](http://ereslibre.livejournal.com/)
的努力下，工作进度管理器原本作为一项[虚拟的 KDE 4
改进设想](http://www.kde-look.org/content/show.php?content=33673)通过
[KDE-Look.org](http://www.kde-look.org/) 逐渐成为一个功能完备的 KDE 4
整合项目。大量程序已通过修改支持了这个新管理器，很多的进度条集合在了一起。上周二的“二进制不兼容变化”日中，大量的改变被正式地提交到
KDE 4 仓库中了。

下图是 KDE 用户及 KDE-look.org 的贡献者 kiras 所制的原始模拟图。

[![Mockup](http://i.linuxtoy.org/i/2007/02/vol4_mockup_small_s.jpg)](http://i.linuxtoy.org/i/2007/02/vol4_mockup_small.jpg)

应注意的是上图还只是个模拟图，并不是 KDE 4、Plasma 或 Konqueror
的最终的真正的样子。

目前它已被做成一个标准的系统托盘程序（就像 KDE 3.5.5
中的打印队列管理器那样），它与 GNOME
的托盘可相互配合使用。但它目前还只能观察到 KDE 程序，所以目前监视
Firefox 的下载进度还不支持。不过也不能说以后不会支持，因为使用 D-Bus
交互进程通讯构架后非 KDE 程序的进度应该是能被观察到的。目前已有意向与
GNOME 下的 [Mathusalem](http://tw.apinc.org/weblog/2006/08/22)
团队合作开发了，这是个类似的项目。

下图是目前已实现的监视程序的截图，只要点击下托盘图标，它就会显示出来。您可以看到，它已经相当实用了。

[![Uiserver](http://i.linuxtoy.org/i/2007/02/vol4_devel_uiserver_s.png)](http://i.linuxtoy.org/i/2007/02/vol4_devel_uiserver.png)

您可以看到 Kopete
的按钮位置已被预留住了，它还没什么意义只是为了做测试用的。不过只要你点击某个按钮中的，它就会回传给
Kopete 一个信号，然后 Kopete 就跳出一个更小的对话框。

您所看到的 Konqueror 的下载进度条显示的是一个真实文件的下载进度。当
Konqueror
关闭后，它们仍会继续工作。而像“中断下载”之类有用的操作按钮正在实现中。

如果您想要参与 KDE 4 的开发工作，为 KDE 程序添加新的 Kjobs
进度监视支持是相当容易的切入点。它只需要几行代码就可以使得应用程序在进度管理器上显示进度，也只要几行代码就可以实现操作按钮的功能。

这个新的进度监视技术将整合入
Konqueror（如模型中的那样）、桌面托盘程序，其它程序将直接使用
D-Bus。我甚至可以想像到一个小的网络程序可以让您远程监测进度……

Rafael
的目标是在最初的功能实现之后，就添加项目保留功能，这样当一个工作结束之后，它就可以随意地保留在队列中直到被用户关闭为止。他也在寻求人们对这个工具的反馈以及可实现的改进。

期待有更多的文章罗列出 KDE 4 伟大的技术。

*方法论上的一个小便条：我确保在我的截图上使用 KDE
默认的风格，即使它很丑陋我也要这么做，因为这样你就可以对 KDE
的进展有一个更好的理解并可以清晰地看到它的进步。另外作为一种准则，我到目前为止所演示的各种特性都是可用的，任何人都可以通过下载
SVN
上的源代码进行编译安装重现我的演示。而今天的文章，我不得不弄了一些简单的代码以使这个正在开发中的程序可用，这是我一直坚守的准则的一个例外。另外，Kopete
进度支持还没放入官方的 SVN 库，但 Rafael 已用它来测试特性了。*

原文：[The Road to KDE 4: Job Progress
Reimagined](http://dot.kde.org/1169588301/)  
译文：[通向 KDE 4
之路（四）：新的工作进度管理器](http://www.myswear.net/forum/viewthread.php?tid=7796)

（Troy Unrau／文 yuanjiayj／译）
