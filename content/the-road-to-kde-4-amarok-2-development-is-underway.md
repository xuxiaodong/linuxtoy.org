Title: 通向 KDE 4 之路（十一）：Amarok 2 开发起步
Date: 2007-03-15 21:21
Author: toy
Category: Apps
Slug: the-road-to-kde-4-amarok-2-development-is-underway

本周我们将来看看 Amarok 2 将出现的众多特性中的一部分，Amarok 2 是 KDE 4
中的 [Amarok](http://amarok.kde.org/)
开发分支。我们在此所讨论的所有特性的开发已接近完成。下面是关于 Amarok
的引擎（包括
[Phonon](http://phonon.kde.org/)），用户界面的改变，Magnatune
音乐商店，OS X 支持以及其它内容的详细情况。

几周前，通向 KDE 4 之路栏目介绍了 Phonon。当那篇文章放出之时，Amarok 2
的开发工作还没开始，但 Phonon 开发者们在设计 Phonon 库的时候总是照顾到了
Amarok 的需要。

在 Amarok 1.x 中，开发者们不得不分出力量去维护分别针对
xine、gstreamer、aKode
等后端的引擎。到现在这些引擎仍然麻烦不断，在某些情况下，维护所有引擎实在是种奢望，于是现实迫使开发者们将重点只放在
xine 引擎上了。而像其它程序，如 Noatun
等不得不一次一次地重复没有效率的劳动来实现这些后端的功能。而在 KDE 4
中，Phonon 接口的设计就让 Amarok
这样的程序不必再去担忧引擎的事情了，只要集中精力把程序的其它方面做好就行。根据
Amarok 开发者们的经验，只要花上 90 分钟就可以使 Amarok 的 Phonon
后端可用，然后再加几个小时就能完善它。而且使用了 Phonon
之后，各种应用程序都可以通过 KIO
技术播放支持某些网络协议的音乐，然后我们就等着看 Amarok 如何去挖掘
Phonon 的潜力了。

Amarok 2 对 Phonon 的支持正在进行中。老的引擎也已移植完毕，特别是老的
xine 引擎仍然被积极地开发着，开发者们也没有决定废弃老的引擎。因为 Amarok
2 的开发只进行了几周而已，决定是否废弃如 xine
等现有引擎还为时过早，这些引擎在过去干的很不错。

在 Amarok 中使用 Phonon 的一个额外好处是它可以让 Amarok
获得访问底层引擎即 Phonon-xine 引擎中具备的视频播放功能。开发者们已经在
Amarok
中加入了初步的视频播放支持，但它目前只是作为音频播放功能的补充，而不是想替代其它更出色的视频播放器如
Kaffeine。其想法是假设在你的音乐库中有视频文件，而你又想用 Amarok
来播放它，则 Amarok 将会将视频流看作是音乐的可视化。Amarok
中加入了视频的支持并不会扰乱 Amarok 2 的音频体验。据 Dan Meltzer
所说，通过 Phonon 在 Amarok 中加入视频支持其实总共只用了 7 行代码。

当然了，KDE 4 的跨平台特性也使得 Amarok 将可运行于其它平台，不再限于
Unix/X11 了。Benjamin Reed 的努力使开发中的 Amarok 2 成功地首次出现在 OS
X 中。向 Windows 的移植也在起步中，不过我还没搞到截图。

[![Amarok](http://i.linuxtoy.org/i/2007/03/vol12_4x_mac_s.png)](http://i.linuxtoy.org/i/2007/03/vol12_4x_mac.png)

我个人认为 Amarok 在这些平台上的出现，Amarok 将成为其它平台用户了解 KDE
这个跨操作系统的开发平台的最佳窗口，Amarok 的作用是其它 KDE
上的程序无法替代的。因为 Amarok
是世界上最优秀最出色的媒体播放器，它是这一领域的最强者。

如果只有跨平台与 Phonon 支持这两项特性的话，Amarok 的新版还不足以升到
2.0，它的变化多着呢。

XMMS 与 Winamp 有许多相似之处，而 Amarok 也在很多方面受到 XMMS
的启发。基本的东西如音乐播放器的多栏播放列表，它显示了媒体文件中包含的标签信息。现在虽然不同的程序添加了有趣的方式对列表进行分类，过滤以及编辑，但这些多栏播放列表在
10 多年中也没真正的改变过了。Amarok
在分类和过滤方面做的特别出色，在标签编辑方式就稍逊色了点（JuK
则拥有一个惊人的标签编辑器）。但是除非是由于延续传统的关系，这些功能中没有一个真正地限制
Amarok 以一种死板音乐栏的格式来显示播放列表。随着 Amarok 2
的用户界面的重新设计，播放列表也有了革新。虽然它仍然列出了音轨，名称以及其它标签内容，但它已不再受限于旧式的播放列表栏格式。

这时就需要一张图来说明描述，这里是一张概念模拟图。

[![Amarok
Mockup](http://i.linuxtoy.org/i/2007/03/vol12_mockup_s.png)](http://i.linuxtoy.org/i/2007/03/vol12_mockup.png)

你也许首先想知道的是“播放列表到哪儿去了？”最初我和我的一些伙伴在 IRC
上也这么问过，但如果你仔细地看了，就会发现其实右侧的列表就是播放列表，它只是在旧式的播放列表中解决出来了。而现在如果你的文件上少了一些标签的话，播放列表将简单地对那些缺少的标签进行调整，漂亮地显示文件中所含的信息。

截图中最显著的就是中间部分。这个中间部分是 Amarok 2
的焦点，开发者们试图向你提供当前所播放的文件的更多的信息，并使您能“重新发现您的音乐”，这也是开发者们的口号。除了“内容”信息被移到了中间，最左边的一栏仍然保留了它原有的功能。当然，按照
KDE 的传统，界面上很多部分都可以设置的。

这是张 Amarok 1.4.5
的截图，将它与上面的模拟图进行对比可以显示用户界面各组成部分的改进。上面那张模拟图是开发者们试图做到的用户界面目标图，但究竟是好是坏，他们会在权衡之后作出调整与改变。

[![Amarok
1.4.5](http://i.linuxtoy.org/i/2007/03/vol12_356_amarok_s.png)](http://i.linuxtoy.org/i/2007/03/vol12_356_amarok.png)

现在给出的是开发中的运行于 Linux 的 Amarok 的截图。请注意 Amarok 2
的开发仅仅进行了一个月，工作仍在继续中。

[![Amarok
2](http://i.linuxtoy.org/i/2007/03/vol12_4x_amarok_s.png)](http://i.linuxtoy.org/i/2007/03/vol12_4x_amarok.png)

Amarok 中最有前途的一个特性是 [Magnatune](http://magnatune.com/)
商店的集成。维基百科中的解释是：Magnatune
是一个中立的唱片品牌，它公平地对待音乐家和用户。用户可以在决定是否购买之前，不用付费地在线收听并下载
Mp3 格式的音乐。Magnatune
售出的音乐文件没有任何形式的阻止顾客复制文件的数字版权，相反 Magnatune
还彭励购买者与朋友们分享三份拷贝。

Amarok 在 1.4.4 版中首次加入对 Magnatune 的支持。从那时开始，Amarok
团队就从其它商店收到了许多封邮件，表示有兴趣与 Amarok 合作。但在 Amarok
1.4 中，开发者们忙于改善对 Magnatune 的支持而无力开启更大的项目。在
Amarok 1.4.5 中，Magnatune
商店的第二个版本放出，开发者们对这个版本非常满意。它工作的很好，并为
Magnatune 带来了少量但不断增长的销售额。

前进正当其时，Magnatune 的主要开发者 Nikolaj Hald Nielsen
计划提供一个面对所有流媒体音乐商店的服务框架，把成果推进到一个更高的水平。这个服务框架可作为并有意作为添加其它音乐商店的起点，它将会提供大量的基础函数（购买，网站信息分解等），这些基础函数都是较为简单的因为每个商店都有其特定的操作这些函数的办法。尽管如此，这也是
Amarok 向统一的流媒体音乐支持方面迈出的一大步，事实上
[CoolStreams](http://musicsojourn.com/Cat/Streams/index.htm)
服务已移植到这个新框架上（用一个 ruby 脚本），同时还有了一个 Shoutcast
浏览器。

这是一张关于实验中的“Cool Streams” ruby 脚本运行于服务框架的截图。

[![Cool
Streams](http://i.linuxtoy.org/i/2007/03/vol12_4x_services_s.png)](http://i.linuxtoy.org/i/2007/03/vol12_4x_services.png)

如果你想要参于 Amarok 2 的开发的话，你需要安装一个 KDE 4 的开发环境。在
[KDE TechBase
网站](http://techbase.kde.org/Getting_Started/Build/KDE4)你可以找到使用
SVN 库的指南，或者你也可以使用
[kdesvn-build](http://kdesvn-build.kde.org/)
程序来自动完成这一切。Amarok 开发者们接受补丁包，如果你需要 SVN
访问权限加入开发的话，他们也会乐意提供的。他们也需要美术工作者们，测试者们的帮助，有意提供帮助的人们可以通过
freenode 的 #amarok 频道与他们联系。

女士们先生们，Amarok 2 的开发进展非常迅速。引用 Amarok 开发者们的领袖
Mark Kretschmann 的话“如果开发以这种速度继续的话，在 KDE 4
发布的时候我们已经在做 Amarok 3 了”对将来的惊喜有点心理准备，请期待
Amarok 团队。

想及时了解 Amarok 的新闻的话，请察看 Ljubomir Simin 的 [Amarok
通讯](http://ljubomir.simin.googlepages.com/awn)。特别感谢他对本文的帮助。我第一次尝试与人合作，非常顺利。

[原文](http://dot.kde.org/1173761811/) by Troy Unrau  
翻译 by yuanjiayj
