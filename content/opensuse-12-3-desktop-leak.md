Title: openSUSE 12.3 谍照之桌面篇
Date: 2013-03-10 13:40
Author: liangsuilong
Category: Distros
Tags: E17, Firefox, GNOME, KDE, openSUSE
Slug: opensuse-12-3-desktop-leak

本文是 Marguerite Su 翻译撰写介绍 openSUSE 12.3
的文章，文章比较长，不喜勿进。原文发自 <http://www.suse.ws/sneak-preview-i-opensuse-12-3-for-desktop-users/>

还有不到三天的时间，openSUSE 12.3
就会躺在您的门口啦。呃，就可以从镜像上下载使用啦，要是您很好奇它将搭载有哪些新东西，这个谍照就是给你写哒！我们将悄悄地告诉你桌面环境都有哪些更新：GNOME，KDE，XFCE
和 Enlightenment 都有！它们搭载的应用程序也有！享用吧！

桌面
----

 

让我们从桌面开始。openSUSE 是主要 Linux
发行版里面独一无二的，我们不偏不倚地分发所有主要的自由桌面：都是官方开发和官方支持的。这些桌面包括
GNOME Shell，KDE Plasma，Xfce，LXDE 和新鲜出炉的
E17。让我们浏览一下这些桌面的部分新特性吧！

GNOME Shell 3.6
---------------

GNOME Shell，仍是 GNOME
社区的一个比较新和二的项目，已经转职了四次。第一次转职都过去两年了，这个桌面仍然是一个火药桶。但是对于大多数用户来说，GNOME
Shell 已变成能为他们处理日常工作的畜生啦。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/Screenshot-from-2013-03-06-204014.png)](https://news.opensuse.org/wp-content/uploads/2013/03/Screenshot-from-2013-03-06-204014.png)

<div>

</div>

 

### 扩展介绍

GNOME Shell 团队创建了一个扩展系统，和 Firefox
非常像。虽然出于一些兼容问题导致的坏印象，笔者并不完全相信该系统，但是这种针对不同的人类无法避免的需求分歧的解决方案应该足够满足多数用户了。由于选择了
Javascript 进行 Shell（和扩展）开发，GNOME Shell
设计师能够让其用户界面十分干净有效，对扩展开发者的门槛也非常低。事实上，考虑到 ![](http://blogs.gnome.org/favicon.ico)[GNOME
扩展站点](https://extensions.gnome.org/)已经有了超过 300
个扩展，这一方案还算是矮子里面拔大个吧。GNOME 团队已经决定提升
Javascript 的地位使其成为神圣的 GNOME
开发语言。虽然一小撮人为这一决定想抓爆 GNOME
的蛋，它还是比较契合业内一切面向网络化的方向滴！

由于扩展可以修改 Shell 的任何一种行为，GNOME
设计师选择构建一个相对静态的默认
Shell，并针对他们认为是有效的工作模式进行优化。这得忍一时才能习惯，或者搜索（或制作）扩展来修改某些行为以符合您的诉求。但是这种影响据说比较小，因为他们已经明显注意为一系列常用动作创建平滑简单的工作流程了。针对「随用用」的优化还是有点效果的！

[![](https://news.opensuse.org/wp-content/uploads/2013/03/Favorite-extensions.png)](https://news.opensuse.org/wp-content/uploads/2013/03/Favorite-extensions.png)

Shell 和扩展

### 欢迎使用 GNOME Shell！

让我们看一下 GNOME Shell
的第一印象如何吧。您可能需要创建一个网络连接，如果您没插网线的话。点击右上角的无线图标，选择您的网络并输入密码。没法再简单了！您能在
GNOME Shell
各处都感觉到对细节的专注和对流程的聚焦：您就看不到不必要的选项（吐槽：想看也看不到）。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/clean-interfaces-in-GNOME.png)](https://news.opensuse.org/wp-content/uploads/2013/03/clean-interfaces-in-GNOME.png)

GNOME 干净的界面

### 保持联系

这都 2013 年了，「地球
Online」的在线时间一定要保证。所以啦，点击屏幕右上角您的用户名，并选择系统设置。在此您可以选择「在线账户」，点击添加一个账户，跟着向导走就可以。注意开启了两步式认证的
Google 账户不能用 —— 这种安全账户在 GNOME Shell 里就是不能用。

一旦您设置好了一个或多个账户，您可以在右上角设置您的状态。

既然我们都在系统设置这儿了，为啥不让我们那高贵冷艳的触摸板支持两个手指头呢？点击左上角格子里的图标返回到主视图，然后选择「鼠标和触摸板」。启用双指滚动。在系统设置里您还可以启用其它一些东西比如在「键盘
– 快捷键 –
输入」下可以设置组合键、额外字符键。你也能在通用访问下面找到隐藏的一些殘障人士选项。其它的残障人士选项在系统设置的辅助功能条目下。

如果您正在找一些复杂的主题设置，而不想仅仅满足于能换壁纸，您来错地方了
—— GNOME 没提供，openSUSE 默认搭载了一个这样的独立于 GNOME 的工具。

### 启动应用

现在我们来做点什么吧。按住鼠标拖到屏幕左上角或者点击那儿的「活动」文本。您将看到您的窗口以概览模式重组了。顶部是搜索栏。在此您可以查找文档和其它文件、应用和设置。点击启动或显示些东西吧。左侧是一个正在运行中的应用和喜爱的应用的停靠栏。下面发光表示它们正在运行。

右侧是“虚拟桌面”。您可以在上面排列您的应用，例如将它们根据活动分组。您可以拖动一个窗口并把它扔到右边，那个条目会展开，然后您可以调整应用程序在该窗口的位置。点击桌面将显示它们。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/Applications.png)](https://news.opensuse.org/wp-content/uploads/2013/03/Applications.png)

GNOME 应用程序

让我们开始搜索吧。输入「tweak」来找到之前提到的主题设置工具。在此您可以选择诸如是否在桌面上显示图标、合上笔记本上盖时或电量低时的动作，以及主题的细节设置。

等您玩够了，我们会继续介绍一些经典应用。

### 一些基础应用

最基础的当然是文件管理器 ——
鹦鹉螺，或者「文件」啦。鹦鹉螺提供了一个不俗的界面来处理您的文件。左侧是您喜爱的位置，上面是后退/前进按钮和一个地址栏，它的右边是一个搜索按钮，视图按钮，视图按钮的下拉菜单和一个选项菜单。搜索挺简单：点击按钮，输入，然后选择是搜索当前位置还是其它地方。地址栏是可点击的图标，如果您想查找某个位置的完整路径（比如您的一个设备，设备名通常都挺长挺怪的），按
ctrl-L
快捷键来在地址栏显示正常的文本。在任何文件夹中，您都可以从齿轮菜单中选择「添加书签」来把这个位置加入到左侧喜爱的位置。这些位置可以在「文件」菜单中编辑，文件菜单在屏幕左上角，您可以移除、重命名、编辑文件。文件菜单也提供了偏好设置和连接在线服务器选项。

您第一次使用「文档」可能会觉得震惊。它不是一个使用层级机制的文件浏览器，而是根据您最后使用文件的时间排序文件，也允许分组和查找，还能显示远程文件如在微软服务器上和
Google Drive
上的文件。另外，窗口右上角没有关闭按钮。您必须点击左上角的应用名称，在「活动」旁边的那个，然后选择「关闭」。一系列其它应用程序也都被这么干了。只要您有文件，它们就会自动显示在「文档」里。单击可查看这些文档，然后您可以使用右上角齿轮按钮下的菜单编辑它们。要组织文档，点击右上角的「选择条目」。「文档」现在将在文件前显示一个勾选框以供选择文件。单双击都不能启动程序来编辑它们，您必须得使用屏幕底部显示的那个工具条上的图标来这么干。那个工具条也能进行其它动作比如打印、查看属性、还有组织文件。组织按钮将会召唤出分组/标记功能。点击「添加」添加标签，完成后点击「关闭」。您选择的文档可以被加入到显示的分组里。您组织完毕后，请再次点击绿色的「好了」按钮。整体上来说，「文档」算是对
GNOME Shell
中应用程序集的一个有益的扩充。它的双头模式操作一开始可能挺恶心的，但您把您的文档组织好了以后，就能轻松地存活下去了。

Shotwell 是一个用来「照顾」您的相片的伟大的应用程序。Shotwell
为您的相片带来了一个「事件」视图，可以按日期排序它们。虽然这个应用程序看起来挺单薄的，它却提供了一系列惊艳的功能比如标记和基本编辑。而且编辑是非破坏性的，您在
Shotwell 中进行的修改不会修改原相片而是副本。虽然它尚未支持 GNOME
在线账户，在它里面单独配置一个账户还是可以轻松地将照片和视频发布出去的。

说到聊天，GNOME 携带了
Empathy。您对聊天应用的全部期待它都能满足。根据您连接的聊天网络，功能可能稍许不同（比如
lwqq
的功能现在就很单薄，不过谢虎成君已经找对方向了）。并且如果您已经设置了一个「在线账户」，那它直接就可以拿来用了。它那不讨人厌的通知和与
Shell
的深度整合让它变成了一个特别好用的工具。您可以在「账户设置」选择「附近的人」网络，它可以自动挖掘出本地网络中的妹子或抠脚大汉，让你与
TA
们聊天。设置头像功能也非常讚：您不但可以选择一张本地图片，还可以用摄像头照相！

[![](https://news.opensuse.org/wp-content/uploads/2013/03/stock-GNOME.png)](https://news.opensuse.org/wp-content/uploads/2013/03/stock-GNOME.png)

周到的 Empathy 可以帮你自拍

openSUSE 12.3 另外还搭载了 LibreOffice 帮您编辑文档，Rythmbox
为您播放音乐特典，Evolution 助您收发邮件和管理日程。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/LibreOffice_12.31.png)](https://news.opensuse.org/wp-content/uploads/2013/03/LibreOffice_12.31.png)

GNOME Shell 中的 LibreOffice

### 扩展

在使用 GNOME Shell 时，您可能会发现一些或许契合您的期待的细节。例如
Alt + Tab 切换的是应用程序而不是窗口。您可能想要尝试这种新活法 ——
也许它可能会让你「燃」起来。但是对于一些人来说，心灵鸡汤不甜。好在还有选择：扩展。它们通常是变更
GNOME Shell 部件行为的几行代码。

您可以用浏览器访问 ![](http://blogs.gnome.org/favicon.ico)[extensions.gnome.org](http://extensions.gnome.org/) 找到您的救命稻草。使用非常之简单，但请注意，扩展并不总是和您正在使用的
GNOME Shelll 或其它扩展兼容，可能会导致不稳定甚至废掉 GNOME Shell。

### 结论

显然，这是一个正在（重）造着的轮子：一些新秀应用肋骨还都露在外面，彼此之间也不配套，但是还是挺庆幸能看到
GNOME Shell
开发者们的视线正逐渐对焦：目前，许多不是太日用的功能不是一般的难找到，于是就有了 ![](http://blogs.gnome.org/favicon.ico)[GNOME
小抄](https://live.gnome.org/GnomeShell/CheatSheet)：GNOME
项目官方解说的一系列重要的快捷键和「你（丫）知道么」的东西。其它的技巧也可以在网上搜到。

一切的一切，openSUSE 12.3 的 GNOME Shell
还是值得试一试的（要是觉得我们的都不行，那 GNOME
就真的该死了）。通过我们默认搭载的扩展和折腾工具，调教它满足您的大多数需要还是挺简单的，另外那玄奥的「平滑的工作流程」可能体验也会不错。

KDE 4.10 等离子桌面
-------------------

由于在 openSUSE 用户中的受欢迎程度，KDE 被选为了默认桌面。KDE 的 Plasma
提供了一个远为经典的能够开箱即用的桌面设置。离上一次主要重构已经过去 5
年了，KDE
团队现在的代码库早已非常成熟了。然而这并不意味着改进不在进行。最吸引眼球的就有，准备迁移到下一代
Qt，移植到 Qt Quick 和 QML 等。openSUSE 12.3
中的这个版本，4.10，是一个相对沉寂的版本，再次肯定了 KDE
桌面和应用的「主力就是主力，那忧郁的眼神、稀疏的胡茬、伟岸的身影…」的观点。

### 等离子挂件

尽管人人都熟悉它的默认设置，Plasma
其实是一种极其灵活的技术。然而，与通过扩展修改一个排他性应用的功能不同，Plasma
的设计就是模块化的。每个部件都可以被替换，保证了独立部分之间不会相互干扰。这种设计允许将，例如，熟悉的带图标和挂件的背景和底部面板的设置，替换为针对上网本优化的设置，该设置中背景是一个启动器或者一系列按列排序的挂件和顶部一个自动隐藏的面板。针对平板呢，「Plasma
Active」也走在康庄大道上，虽然媒体中心和电话界面正处在早期开发阶段。但是这些行为大异的界面共享了大部分代码和精力，针对一个界面写部件在其它所有界面上跑的都会很好。在桌面独立区域显示天气的挂件到了上网本里就会自动变成定宽，到了平板里就会被放在格子里，到了手机上就会全屏运行，甚至在任意桌面都能放到面板里作为一个小的提示。当然，这种灵活性也不是完美无缺的。虽然挂件和其它部件可以用几乎任何一种语言写，大多数仍然还是
C++，需要的手艺比 Javascript
难多了。然而，目前很大的精力都放在将挂件迁移到基于 Javascript 的 QML
上，这使得折腾 Plasma
变得更加容易了。最新发布的 ![](http://kde.org/media/images/favicon.ico)[Plasmate
1.0](http://dot.kde.org/2013/03/05/plasmate-10-plasma-workspaces-sdk)，在 ![](https://static.opensuse.org/themes/bento/images/favicon.png)[software.opensuse.org](http://software.opensuse.org/package/plasmate?search_term=plasmate) 上已经有了，把这种简单提升到了一个新的高度。对于最终用户来讲，Plasma
可能在个人使用这块比 GNOME Shell 简单太多了 ——
当然代价也很明显，用户界面的复杂度提高了，大多数界面都是针对效率而不是好找优化的，这制造了一个更加陡峭的学习曲线。

### 欢迎使用等离子桌面！

和 GNOME
桌面一样，您可能需要先联网。这里您的体验可能不太平滑，因为对话框稍微有点复杂。在大多数情况下，在密码区输完密码就足以连上网了。然后提示您创建一个钱包，可以对钱包使用空密码，虽然它肯定会警告你
—— 但这至少不会在你已登入桌面的情况下还总是让你输密码了，对吧？

[![](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-wifi-dialoge.png)](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-wifi-dialoge.png)

无线稍微复杂了点儿

### 保持最新

即使您是跑在 Live CD 环境中，Apper，也会提示您几百个更新 ——
直接通过通知提示。有通知时，点击屏幕右下角的数字 1 或
2，将会弹出一个窗口显示最新的通知。如果您已经装好了
openSUSE，最好点击「复核」按钮来检查和安装更新。否则，点击‘x’会让它们滚蛋。注意和这些更新一起，您也会收到一些默认没有的好物比如
Adobe Flash 播放器等等。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-Notifications.png)](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-Notifications.png)

### 启动应用程序

要在等离子桌面中启动应用，您有两个主要选择可以做：使用左下角的菜单，或者使用快捷键是
alt + F2
的「命令启动器」。「命令启动器」是完全基于搜索结果的，比如当您搜索「音乐」时作为结果会返回音乐播放器
Amarok
和声音和视频配置程序。它也很长袖善舞啦，运用之妙存乎一心，比如计算器功能（输入一个算式，它能展示结果），控制音乐播放器，查单词（输入「define
tree」，将返回「tree」的定义），以及更多神鬼莫测的功能。当您点击了左边的扳手图标后，它的功能才会更加可见：您现在可以启用和禁用所有额外功能。与其它功能一起，维基百科、wikitravel
和 Youtube 搜索是默认禁用的，您可能想要试试它们！

菜单启动器默认显示了一些您收藏的应用程序，通过底部的标签页可以查看更多应用程序。点击分类您将看到该分类中的应用，点击右下的「全部应用程序」能把你带回来。在「我的电脑」标签页下您可以找到「设置」和「常用位置」以及「最近使用」和「离开」，顾名思义也没什么解释的。上面的搜索没有「命令启动器」那么多优雅的花样，只能尽职尽责地做好它的本职。

[![](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-menu-search.png)](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-menu-search.png)

两个菜单选择中的搜索

我推荐观看下面的视频来学习您桌面上的图标的作用，以及如何处理面板。荣耀归于 [Gameron
Wiebe](http://cameronwiebe.com/)（[G+](https://plus.google.com/106015123773137519616/posts)）。

### 专业技巧

既然 KDE
所有应用程序都是关于怎么帮你多快好省的，那我们就来看一些比较专业的花样吧。

**Konsole**

新鲜出炉的功能：在编辑下，您可以选择将您在一个标签页中输入的内容发送到所有其它标签页中去。需要登入
5 次服务器或在不同的地方执行同样的命令？重输甚至复制粘贴都不用了！

**Dolphin**

Dolphin 有一堆华丽的插件。首先在终端中输入 ‘sudo zypper in
dolphin-plugins’ 安装 Dolphin 插件，完成后，到「控制 – 配置
Dolphin」去选择服务。Dolphin 可以处理您的 Git 和 svn
仓库。在这里也可以下载其它服务 —— dropbox
服务超讚！您可以从![](http://kde.org/media/images/favicon.ico)[这个页面](http://opendesktop.org/content/show.php/kde-services?content=147065)下到一大堆服务。下载并解压那个
tarball，在那个文件夹里以 root 身份运行 ‘make’ 就可以啦！

如果您不喜欢 Dolphin
不默认显示您文件夹的预览（它当然没法记住设置啦，哪有设置可记呀！除非您在每个文件夹里都设一下预览），可以去「控制」或「视图」菜单修改设置。您可以勾选底部的选框来将您配置的东西设为默认。好吧，除了把默认调教的聪颖一些，您还可以调整特定文件夹的设置。如果你能想要显示更多文件类型的预览，可以去「Dolphin
偏好」-「常规」-「标签页预览」里面勾选。

![](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-Dolphin-Services.png)

配置服务

**语义搜索**

启用语义搜索（nepomuk）后，您将能在 Dolphin
中看到「最近文件」和一些搜索文件夹。请确保您的文件都被索引了。请注意
Nepomuk
需要一点时间才能索引完您的系统，但本版中这段时间被大刀阔斧地砍掉很多，无需等之前那么久。另外索引会在您使用电池供电是自动挂起。如果您遇到了性能问题，可以尝试运行
nepomukcleaner 命令。这个俏巧的工具可以清理一些东西，但是运行时间超长 ——
几个小时都不算事儿！但您可以随心所欲地暂停、停止和恢复。

如果您使用
KMail，您也许会注意到文件夹内容上面的快速搜索变得机敏了：它依然是根据您输入的词过滤您的邮件，但不再只搜索主题和收/发件人了，它现在也能检索邮件的全文了！

**图片和文档**

照片检视器 Gwenview 和文档检视器 Okular
分享了一些到世界末日您还在用却从来留意不到的杰出功能。打开一个大文档或图片，然后用鼠标到处拖拽。现在，别管应用程序或窗口的边缘了
——
是的，您的鼠标在到底时会自动在屏幕另一边绕出来！这个功能在滚动比你屏幕大的照片时非常优雅。

Gwenview 的简单编辑功能很不错，但是真正实现相片的高级编辑的是
Showfoto，DigiKam 软件包的一部分。享受 Showfoto
里那数不清的强力效果吧！这个应用真是太、太亮了。您的 KDE
系统默认就有装哦。

![](https://news.opensuse.org/wp-content/uploads/2013/03/KDE-showfoto.png)

**等离子桌面**

虽然等离子桌面不可思议地强，强到了禽兽的地步，它的技巧列出表格可能要好多页，最值得一提的肯定有
Pastebin
挂件。我把它仍在了屏幕右下角，当我想要把什么东西给别人看时，按下
PrintScren 键截图，然后直接把图片拖到 Pastebin
里，等它好了以后到聊天窗口或邮件里 Ctrl + V
（粘贴）就可以了。截图会自动上传到 Pastebin
服务器，然后把链接返回到您的剪切板里。文字也可以呦。其它任何方式都击败不了劳动人民的这种狡黠的智慧了。

**上网本用家**

如果您正在使用一个小屏幕的上网本或其它设备，可以看看 `Plasma Netbook`，这是标准
Plasma 界面的一个「重塑」，专门针对小屏幕优化。您可以在「系统设置 –
工作空间行为 –
工作空间视图」切换到「上网本」工作空间类型。点击「应用」后您的屏幕将翻天覆地：所有的应用程序都将全屏运行，您得把鼠标放在屏幕上边缘才能看到提供切换应用程序、时钟以及更多挂件的工具面板。鼠标移动到屏幕右上角，点击窗口标题可以切换应用程序，点击
X
可以关掉当前应用程序。顶部面板的「同一页」按钮可以让您把挂件并排放在一个页面里。您可以滚动查看
—— 这种方式能让挂件更漂亮和守序一些。

在桌面视图里您可以搜索并启动应用程序 ——
试试搜索栏吧！如果您不喜欢隐藏的顶部面板和最大化的应用程序而是这个「搜索并启动」界面，您可以在正常的带面板桌面里把它设成背景。返回您的正常桌面，点击腰果图标并选择「默认桌面设置」，然后在「布局」中选择「搜索并启动」。对了，多列滚动的报纸挂件布局也可以在这里选
—— Plasma 的哲学就是部件共享，任意组合、任君采撷。

### 结论

KDE
应用程序、等离子桌面和它的开发框架提供了一个强有力的效率优先兼顾公平的桌面体验。学习和配置过程可能有点跳脱，但一旦您搞定了，您未来大把的时间都可以省下来去扣脚或把妹！

E17
---

这是一个老瓶新酒，有 [swyear](http://swyear.blogspot.com/) 的雄文在前，就不献丑了:

-   [Enlightenment 17 所有事
    (1)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-1.html)
-   [Enlightenment 17 所有事
    (2)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-2.html)
-   [Enlightenment 17 所有事
    (3)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-3.html)
-   [Enlightenment 17 所有事
    (4)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-4.html)
-   [Enlightenment 17 所有事
    (5)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-5.html)
-   [Enlightenment 17 所有事
    (6)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-6.html)
-   [Enlightenment 17 所有事
    (7)](http://swyear.blogspot.com/2013/01/enlightenment-17-everything-7.html)

[![](https://lh4.googleusercontent.com/-y6iC6HMIuAQ/UOvdxUe3GgI/AAAAAAAAGTU/K3KHe1Pvdm0/d/fliemanager4.png)](https://lh4.googleusercontent.com/-y6iC6HMIuAQ/UOvdxUe3GgI/AAAAAAAAGTU/K3KHe1Pvdm0/d/fliemanager4.png)

MATE
----

这是 [hillwood](https://hillwoodhome.info/) 参与维护的 GNOME 2
派生，帮他宣传下。可以添加：

![](https://static.opensuse.org/themes/bento/images/favicon.png)[X11:MATE:Factory](http://download.opensuse.org/repositories/X11:/MATE:/Factory/openSUSE_12.3/)

软件源安装体验。

[![](https://lh6.googleusercontent.com/-9X0qvjEbm4o/UTBtbYTCFHI/AAAAAAAAEbM/gT7EQJgdcrs/s1022/2013-03-01+16%3A47%3A46%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)](https://lh6.googleusercontent.com/-9X0qvjEbm4o/UTBtbYTCFHI/AAAAAAAAEbM/gT7EQJgdcrs/s1022/2013-03-01+16%3A47%3A46%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

输入法
------

**Fcitx**

openSUSE 中的 Fcitx 直接跳了三个版本号，从 4.2.4 变成了 4.2.7。除了修复
bug
之外，还添加了一些新的输入法和一些「你不会注意到但是一旦注意到会觉得真心很碉堡哇靠这也可以」的功能，比如
Ctrl + ; 的剪切板，比如在英文键盘布局 Ctrl + ALt + H
的拼写提示和拼写检查，比如 Ctrl + Alt + Shift + U 直接输入 Unicode
字符，比如使用快速短语功能输入颜文字表情，比如在两个窗口各用一种输入法，等等。玛格丽特做了一个
Fcitx 隐藏彩蛋的演示视频：

**IBus**

前面想抓爆 GNOME 的蛋的一小撮人可能很想知道被 GNOME 作弄过的 IBus
究竟怎样[欲仙欲死](https://hillwoodhome.net/archives/232)了。

人家是上游大爷，要整合我们下游做小的没有办法，但是我们可以阴奉阳违：是的，openSUSE
并没有~~舔 GNOME 的腚沟~~开启整合，我们这儿连 IBus 都不是 1.5。

当然理由比较牵强：IBus
在日文环境总死。这个牛气冲天的理由让夹在维护者和开发者中间的 hillwood
很头痛，但是看官只要微笑就好了，当然 IBus
的开发者也不要介意，有时候人需要一个理由，既然日文维护者愿意抗压那就是日文了。

IBus 1.4 在 GNOME 3.6
中的托盘图标总是在下面的托盘区域，不方便设置（点名：GNOME），我们的日文开发者做了一个默认扩展。所以，太阳照常升起，银河依旧璀璨。

[![](http://www.suse.ws/wp-content/uploads/2013/03/%E9%BB%98%E8%AE%A4%E6%9C%AA%E5%BC%80%E5%90%AF%E6%89%A9%E5%B1%95.png)](http://www.suse.ws/wp-content/uploads/2013/03/%E9%BB%98%E8%AE%A4%E6%9C%AA%E5%BC%80%E5%90%AF%E6%89%A9%E5%B1%95.png)

默认未开启扩展

[![](http://www.suse.ws/wp-content/uploads/2013/03/2013-03-10-11_13_05%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)](http://www.suse.ws/wp-content/uploads/2013/03/2013-03-10-11_13_05%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

扩展设置界面

![](http://www.suse.ws/wp-content/uploads/2013/03/%E6%89%A9%E5%B1%95%E5%BC%80%E5%90%AF.png)

扩展开启后

**Mozc**

ACG 众一定不陌生了，Google 的开源日文输入法。现在 openSUSE
把它收纳到官方源里来了，可以通过 fcitx-mozc 或 ibus-mozc 体验。

更多
----

openSUSE 12.3 中还有一大堆其它的变化，一篇文章是写不完的。我只能说，等到
13 号您自己抓吧！

预祝大爷您玩的爽（Have a lot of fun）！

注意：文章中的所有图片来自 news.opensuse.org，swyear 博客和
suse.ws，所有图片版权归原版权人所有。
