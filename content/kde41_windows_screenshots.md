Title: Conquer your M$：KDE 4.1 for Windows 图文教程
Date: 2008-08-15 16:26
Author: lovenemesis
Category: Apps
Tags: crossplatform, KDE
Slug: kde41_windows_screenshots

上个月底，万众期待的 KDE 4.1 如约发布。相比KDE 4.0
，在更加华丽的外表之下，还有很多底层上的改变，其中之一就是在 Qt 4.4
的支持下强化了跨平台的能力。现在，基于 KDE 的应用程序也可以在 WIndows 和
Mac OSX 平台上运行了。今天就先展示一下 Windows 平台上 KDE 4.1
的风采。期待有条件的朋友也能分享下 Mac OSX 上运行情况。

**KDE 在 Windows
平台上的安装**采取的是在线安装的方式。首先需要下载一个[安装管理器](http://winkde.org/pub/kde/ports/win32/installer/kdewin-installer-gui-latest.exe)，保存到任意位置之后双击启动它，即可开始安装。

![](http://i.linuxtoy.org/i/2008/08/kde1-340x218.png)

首次安装的时候注意不要勾上下面的小勾！点击 Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde2-340x218.png)

这一步是选择 KDE 应用程序的安装位置，所有的 KDE
程序都保存在这个目录下，只有个性化配置保存在用户的个人目录下。点击 Next
继续。

![](http://i.linuxtoy.org/i/2008/08/kde3-340x218.png)

这一步是选择安装类型，如果没有意图做 KDE 在 WIndows 下的开发工作的话选择
End User 最终用户模式即可，此时的运行时环境被限定为 MSVC。如果想使用
MinGW 做为运行时环境的话必须选择 Developer 开发者模式。点击 Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde4-340x218.png)

这一步是选择下载的安装文件临时存储位置，推荐与第二步中设定的安装位置选在同一个分区下的不同目录，避免稍候无意义的跨分区复制操作。点击
Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde5-340x218.png)

这一步是设定连接到互联网的方式，从上到下分别是“直接连接”，“使用IE的连接设定”，“使用FIrefox的连接设定”，“手动设定代理服务器”。一般的，
使用电信/网通/铁通的 ADSL 接入的用户选择"直接连接"即可。点击 Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde6-340x218.png)

这一步是选择从哪个镜像服务器下载，从列表中选择离你最近的地区即可。有时中国的镜像会无相应，此时推荐使用澳大利亚的。点击
Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde7-340x218.png)

这一步是选择需要安装的组件，根据右侧的描述选择勾选自己感兴趣的软件包即可。很可惜，目前还没有
KDE 的中文语言包。点击 Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde8-340x218.png)

这一步是提醒你还有这些软件包因为依赖关系的原因也即将被一起下载安装。点击
Next 继续。

![](http://i.linuxtoy.org/i/2008/08/kde9-340x218.png)

开始下载，之后会自动开始安装。除了在安装 Ogg Vorbis DirectX Filter
的时候需要确认一下弹出窗口外，没有什么可操作的。

![](http://i.linuxtoy.org/i/2008/08/kde11-340x218.png)

至此安装完成。之后就可以在"开始"-"所有程序"菜单中找到"KDE 4.1
Release"了，在其中就可以找到刚才安装的 KDE
应用程序了。安装信息保存在与安装管理器同一目录下的新建的etc目录下。

另：如果以后要更新或安装其他 KDE
程序，只需要再次运行此安装管理器，在第一步勾选下方的小勾即可。

**下面是一些 KDE 应用程序的屏幕截图**

首先，是**音乐播放器 Amarok 2** Alpha 1。

![](http://i.linuxtoy.org/i/2008/08/amarok01-340x279.png)

以上是主窗口，从以前的两栏竖向拆分变成三栏，只是不太清除中间的分栏是做什么的，从未有任何东西出现过……

![](http://i.linuxtoy.org/i/2008/08/amarok02-340x235.png)

这是重新设计的服务配置页面，从中可以看到默认已经包括了不少有用的服务插件。

![](http://i.linuxtoy.org/i/2008/08/amarok03-290x340.png)

Amarok 关于页面。另外，OSD
也可以正常显示，也可以自定义显示位置。再另外，估计是由于附带的 Ogg
Vorbis DirectX Filter 的问题，反正它是没把任何一首音乐发出声音来，无论是
ogg 还是 mp3 ……

下来是 KDE 4 的**文件管理器 Dolphin**。

![](http://i.linuxtoy.org/i/2008/08/dolphin01-340x236.png)

以上是主界面，可以正常显示中文。但是估计是由于 Kio
的问题，信息右侧栏并不能正常预览图片文件。同时并没有针对 Windows
的多根文件系统结构进行调整，于是我怎么都到不了其他分区……

![](http://i.linuxtoy.org/i/2008/08/dolphin02-286x340.png)

Dolpihn 关于页面。很遗憾的是，老牌的多功能的网页浏览文件管理软件
Konqueror 就没有 Dolphin 的脑容量高了，完全启动不起来。

下来是还处在开发中的 **KDE 办公套件 KOffice** 。

![](http://i.linuxtoy.org/i/2008/08/kword01-340x263.png)

这个是其中的字处理器 KWord，目前并不能打开 MS Word 格式的文件。KWord 与
Openoffice.org Writer 的不同在于它是 Frame-based 的字处理器。

![](http://i.linuxtoy.org/i/2008/08/kspread01-340x263.png)

这是其中负责表格计算的 KSpread，同样不能打开 MS Excel 格式的文件。

![](http://i.linuxtoy.org/i/2008/08/kpresenter01-316x340.png)

这是其中幻灯片演示程序 KPresenter，也不能打开 MS Powerpoint 格式文件。

![](http://i.linuxtoy.org/i/2008/08/krita01-340x271.png)

这个是其中的像素绘图程序 Krita，它融合了 Openoffice.org Draw 和 GIMP
的部分功能，是个不错的程序。

![](http://i.linuxtoy.org/i/2008/08/krita02-286x340.png)

Krtia 的关于页面，从中可以看出整个 KOffice 还处于 alpha 阶段。其实
KOffice 包含的组件远不止这几个，像数据库管理工具 Kexi ， 公式编辑器
KFormula 等都是相当不错的软件。相比 Openoffice.org 来言，KOffice
组件的启动速度要快很多，在界面设计上也有独到之处，缺点是目前在 Windows
平台上还不支持 MS Office 文件格式的打开和保存。

下来是**下载管理器 KGet**。

![](http://i.linuxtoy.org/i/2008/08/kget01-340x190.png)

以上是 KGet 主界面，可以看到拖放栏显示是正常的。遗憾的是，本人偏好的
BitTorrent 客户端  KTorrent 完全无法启动。

下来是**多协议即时消息程序 Kopete**。

![](http://i.linuxtoy.org/i/2008/08/kopete01-222x340.png)

这个是 Kopete  的主窗口，点击最下方的提示就可以创建新账户。

[![](http://i.linuxtoy.org/i/2008/08/kopete02-340x326.png)](http://i.linuxtoy.org/i/2008/08/kopete02.png)

这个是选择要创建账户使用的即时通讯协议，MSN、Jabber、Yahoo
都在其中，甚至还有QQ！不过 QQ 经过测试是登录不上的……

下来是 **KDE 教育组件中的天文馆 KStars**。

![](http://i.linuxtoy.org/i/2008/08/kstars01-329x340.png)

应该是星相图……

![](http://i.linuxtoy.org/i/2008/08/kstars02-327x340.png)

这个是太阳系行星轨迹图。

![](http://i.linuxtoy.org/i/2008/08/kstars03-194x340.png)

感谢31楼oldherl指教，这个是关于木星卫星的某某图……

![](http://i.linuxtoy.org/i/2008/08/kstars04-330x340.png)

KStars 的关于页面。 除了 KStars 以外，KDE
教育组件里还包含了适用于化学、数学、物理、语言等学科的教育辅助软件，十分有趣。遗憾的是，KDE
4 引入的桌面地球仪 Marble 无法启动。

下面是 **KDE 游戏**组件部分。

![](http://i.linuxtoy.org/i/2008/08/kdiamond01-245x340.png)

这个是 KDE4.1 新增加的类似钻石迷情的 KDiamond，很适合同女友一起玩。

![](http://i.linuxtoy.org/i/2008/08/kbreakout01-340x236.png)

这个是经久不衰的打砖块 KBreakOut，背景图很有动感。除了这两款以外， KDE
还附带了数独 Ksudoku 等众多有趣的小游戏，无论数量和质量都远远超过
Windows 附带的小游戏。

下来是 KDE 中一些辅助性工具。

![](http://i.linuxtoy.org/i/2008/08/kwrite01-340x243.png)

简单的**可视化文本编辑器 Kwrite** 。如果需要语法加亮等功能的话可以使用
kdesdk 软件包中的高级文本编辑器 Kate 。

![](http://i.linuxtoy.org/i/2008/08/okteta-273x340.png)

这个是**十六进制编辑器 Okteta**。

![](http://i.linuxtoy.org/i/2008/08/kdehelpcenter01-340x263.png)

这个是 **KDE 帮助中心**，只是里面还是以在 POSIX
系统版本的帮助内容为主，并没有增加 Windows 平台上的特殊内容。

以上截图所用 Windows 系统为 深度XP 6.2 SP3 版本。

以上就是 KDE 4.1 在 WIndows
系统上的安装方法及部分软件的截图，更多的留待自己去发现吧～ 当初 KDE 4
宣布时就以强大的跨平台能力为目标，从现在看来已经成功的迈出了第一步。尽管还有不少不尽人意之处，不过相信到
KDE 4.5 的时候，无论是哪个系统平台的用户，都可以享受到诸如 Amarok、
KTorrent、KOffice 等优秀的开发源代码软件了。

[KDE on Windows Project 主页](http://windows.kde.org/)
