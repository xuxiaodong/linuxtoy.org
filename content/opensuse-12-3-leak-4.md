Title: openSUSE 12.3 谍照四：去而复归：一个发行版的传说
Date: 2013-03-12 23:08
Author: liangsuilong
Category: Distros
Tags: OBS, openSUSE, Qt
Slug: opensuse-12-3-leak-4

# openSUSE 谍照四：去而复归：一个发行版的传说

这是玛格学姐贡献的又一雌文，继续为我们介绍 openSUSE 12.3

原文：[http://www.suse.ws/sneak-preview-iiii-there-and-back-again-a-distros-tale/](http://www.suse.ws/sneak-preview-iiii-there-and-back-again-a-distros-tale/)

英文原文：[https://news.opensuse.org/2013/03/11/sneak-preview-iii-there-and-back-again-a-distros-tale/](https://news.opensuse.org/2013/03/11/sneak-preview-iii-there-and-back-again-a-distros-tale/)

Qt5, Linux 3.8 和 LibreOffice
有什么相通之处？它们的发布时间都超过了我们开发的 deadline，但都在
openSUSE 12.3 的支持周期内。别怕：Open Build Service 拯救世界！大于
35000 个在册打包者为 openSUSE 12.3
构建了多种多样的软件包，本文中将着重说明其中一些。

## openSUSE 12.3

首先，我们来谈谈 openSUSE 12.3。去年 12 月 20 日，我们的开发分支
‘Factory'，包含了那时最新最棒的自由软件，进入了’维稳冻结‘期。该冻结的目的是为了修复残破不能编译的软件并拿给测试团队进行压力测试。从那时起，就不再允许向
openSUSE
中再推送软件的主要版本更新了，除非打包者能够自证该版本至少是和前个版本同样稳定的。翻译团队也从此时开始更新翻译。当然了，该冻结肯定也是为了消融软件包冲突，确保相互协作，而且协作得稳定。没有这个阶段，我们也没法为您带来
openSUSE 12.3 这一以稳定为主打的发行版。对于主流用户来说，openSUSE 12.3
是一个伟大的产品，提供了他们恰恰需要的：**把该死的活儿干了**。稳定可依赖，这是大多数
openSUSE
用户的要求。（表看我，我最早是看它是最漂亮的发行版，后来看它是最灵活的折腾不死的发行版，再后来，I'm
a part of the project.）

![](https://news.opensuse.org/wp-content/uploads/2012/06/geekos.jpg)

## 啥？你不求稳？

但有时候，您需要一个比发行版搭载的还新的软件包或应用程序，人之常情。可能您在
[Planet KDE](http://planetkde.org) 上看到了一个很帅气的东西比如
[kscreen](http://www.afiestas.org/kscreen-supporting-the-old-and-new-xrandr1-1-backend/)，然后想要试试看;
或者您想帮助测试新的 [小企鹅输入法 Fcitx](https://github.com/fcitx);
或者您喜欢的应用程序 beta 一万年比如
[Hotot](https://github.com/lyricat/Hotot);
或者您就喜欢在悬崖边缘结庐而居，就要那个范儿，比如 yue 就总是
[KDE:Unstable:SC](https://build.opensuse.org/project/show?project=KDE%3AUnstable%3ASC)...

![](https://news.opensuse.org/wp-content/uploads/2013/03/dister\_mechanic\_small-300x300.png)

你当然可以在 openSUSE
里这么干，但是蜘蛛侠他叔讲了，「屁股越大，责任越大」。稳定版本的
openSUSE
经过了重重测试，来保证每个部分都没毛病，至少别让你开门见血。但是您从其它软件源安装的软件包越多，您离「绝对中立」的稳定版就越远，就更加的偏向「混乱邪恶」，软件包可能彼此都会打架。我们的软件包管理器
zypper 和我们的 [Open Build
Service](https://build.opensuse.org)或许是业内最好的在启用了一篮子软件源的情况下还能让你保持稳定的一个平台
—— 一般 openSUSE 用户都添加了 10
个以上的软件源，但风险完全可控。但别说我没警告过你呦，正如我在论坛上说，我修的「大部分都不是
openSUSE 自己的问题，而是被用户玩坏的 openSUSE 的问题」。

![](https://lh6.googleusercontent.com/-inPyBHQ5sFc/UT7CqRkCtRI/AAAAAAABKhk/lzcSh0\_7tQA/s766/%E5%8F%91%E8%A1%8C%E7%89%88%E5%96%84%E6%81%B6.png)

安全贴士：

* 稳定性 —— 拴好你的软件包管理员 ——
当你叫它安装软件包时，它做事的原则是「主人最高」，绞尽脑汁地想出一个方法来帮主人装上这个软件包;
哪怕卸载 700
个冲突包只要主人高兴世界崩塌了又怎样。所以如果选上一个软件包，弹出来一个方案说要把你系统卸掉一半，这时候在它请求主人许可的时候，您最好摸摸它的头，微笑就好了，千万别点「确定」。

* 可维护性 —— 如果你有选择的话，请从 devel 开头的工程选择软件包而不是从
home 开头的工程里选。Devel
工程是发行版打包者制作软件包的地方，它们都会被推送到 ’Factory‘。home
工程类似于
PPA，是用户自己的后院，他把你杀了埋了半年都没人发现！虽然两者都没官方保证，但是一般情况下，devel
的维护程度较高，更加可信！

* 安全性 ——
当您使用「一键安装」安装软件包时，将添加软件源，并且您必须信任那个开发者的
GPG 密钥。但如果您搞了一大堆软件源，`zypper dup`
命令可能就会把软件包从主源切换成其它添加的源里的版本。这可能直接把后果甩你脸上，甚至可能会有安全性问题。所以在执行发行版升级前请确认禁用了其它源，如果水平不是很高也请关掉软件管理中的「允许厂商变更」选项，最后提醒一下，「软件源」中把主源的优先级设置为
10 可以有效防止这种情况的发生。

## Open Build Service

好么，新鲜出炉的软件包是怎么来的？怎么得到它们？

![](https://news.opensuse.org/wp-content/uploads/2013/03/categories.png)

[Open Build Service](http://openbuildservice.org/)
是一个「以一个自动、协调和可重复的方式从源代码编译和分发软件包的通用系统」。说人话就是：OBS
就是一个服务器，编译软件，打包软件，然后丢到一个下载服务器上，可以在网页上手动下载，也可以加源更新。而且它是自由的
—— GPL 授权，开源开发，也可以在
[build.opensuse.org](https://build.opensuse.org)
免费使用。我们用前面这个服务器开发
openSUSE，我们和其他打包侠在上面打了十万个包。从编译服务安装软件也很简单，我们有一键安装技术。您甚至不需要许多其它姊妹发行版要求您输入的命令
—— 它啥都不用，就点一下。您可以在
[software.opensuse.org](https://software.opensuse.org)
上查找软件，每个软件都有一键安装。使用方法见下面的视频！

[油管子视频](http://www.youtube.com/watch?v=hmW0156G810)  
墙内 YouTudou 版本正在上传审核

## 软件混搭

有一些比较常用的软件的新版本很遗憾由于时间问题没进入 openSUSE
12.3。这包括 Qt 5,LibreOffice 和最新的 3.8
内核。也有一些软件出于体积和/或其它原因不是很适合放在官方 openSUSE
源里。游戏就是比较典型的例子。但是它们都能通过
[software.opensuse.org](https://software.opensuse.org)
安装。让我们通过几个例子来见识一下。

### LibreOffice 和其它应用

特性冻结不久，新版 LibreOffice 就出来了。4.0
版里有很多[耀眼的功能](http://www.libreoffice.org/download/4-0-new-features-and-fixes)，比如
Personas（支援 Firefox 主题），多媒体加速预览，使用 Android
设备远程控制您的幻灯片等。也有一些改进，诸如更高质量的 RTF，支援导入
Visio，或导入许多格式时的性能提升。如果您没有这些特性就不能活，或者等待了好几年没法再等了，您可以尝试使用
OBS 上的 LibreOffice 软件源。openSUSE 的 LibreOffice
团队维护了一个如何升级的[维基](https://en.opensuse.org/LibreOffice#Update\_to\_Latest\_Version)页面，当然您也可以直接从
[s.o.o/libreoffice](http://software.opensuse.org/package/libreoffice)
上面抓！

### 游戏

游戏是一类发行版很不好囊括的东西。一方面，离线游戏的数据包都超大，另一方面，MMOG
游戏要联网，必须使用最新
API，因此也必须得经常更新。这两类都不太适合成为正常的发行版软件包的候选。但别担心，openSUS
游戏还是没问题啦，只是放在一个独立的软件源里了。最方便的方法是查看
[openSUSE 游戏黄页](http://software.opensuse.org/packages/Games)。

![](https://news.opensuse.org/wp-content/uploads/2013/03/game-category.png)

### 更加新锐的桌面环境：GNOME，KDE 和它们的 Devel 开发源

你是 Gnome 的粉丝吗？不装最新 KDE
软件看看新玩具就不舒服会死星人？我们有[Gnome](http://en.opensuse.org/GNOME\_repositories)和[KDE](http://en.opensuse.org/KDE\_repositories)软件源。所以您是可以使用您喜欢的桌面环境的最新版的，甚至在我们将它标记为稳定，或者弄完圈内著名的「SuSE
调教」之前就可以用。但是请注意。KDE 和 GNOME
都包含/依赖了一大堆新的函数库，所以你玩的太 High
您的系统可能起不来床。上面的维基页面有如何添加 GNOME/KDE
软件源的技巧和提示 —— 记住，带 Factory 的源可以是非常不稳定的！

不只是桌面环境才有这样的 Devel 开发源，其它东西也有。您可以在
[software.opensuse.org](https://software.opensuse.org)
上搜索时点击「show unstable packages」，也可以来
opensuse\_zh@im.partych.at 上问一句。

### 最新的 Linux 内核

Linux 内核的开发很稳健，平均 3-4 个月发布一次，目前最新的稳定版本是
3.8。但是 openSUSE 12.3 特性冻结的时候，它还是
RC，好多问题也没解决。所以我们搭载的是我们那时认为更加稳定，并经过了完整测试的
3.7 版。但是升级内核的理由太多了 —— 多数都是硬件相关的。视频和无线驱动占
Linux 内核比重极高，如果您的笔记本是新买的，运行 OBS
的[最新稳定版内核](http://kernel.opensuse.org/packages/stable)源中的内核可能主意不坏。请注意，内核，作为您的作业系统非常核心的一块，只有在必须升级的时候才应该被升级
——
乱升级会有稳定性问题。另外如果您出于各种原因必须停留在某个老版本上，可以看[这些技巧](http://en.opensuse.org/SDB:Keep\_multiple\_kernel\_versions)。

### Qt 5 和开发工具

您是一个开发者，想做一些面向未来的迁移？或者您想要使用只有最新版本的库里才有的杀手级功能？心放宽，特性冻结没进去也把心放宽。Open
Build Service
上新版本海了去了。例如[这](http://en.opensuse.org/KDE\_repositories#Qt\_5.0\_Development\_Snapshots)
就是一个 Qt 5 的实验源。您可以现在就玩最新的 QML
或者其它的功能啦，或者可以看看 Qt 项目当初承诺的 4 到 5
无缝迁移是不是真的。如果您再好好搜搜，您可能会发现某人已经在他的 [home
源](http://software.opensuse.org/package/ruby20)里开搞 Ruby 2.0
了。复习一下，前面说 home 源怎样了？高度实验性，可能会挂，可能有严重
bug。但换句话说，至少有个盼头了啊，既然都有人搞起了，进非 home
源只是时间问题了嘛。

另外如果您遇到了问题，Open Build Service 就跟面向软件包的 Github
一样：派生、修理，就跟把大饼挂脖子上咬一口那么简单！或者有个专有名词叫，[BURPing](https://lizards.opensuse.org/2011/05/16/have-you-burped-yet-today/)，细节看[这篇文章](https://news.opensuse.org/2011/09/27/get-your-package-in-factory-for-12-1/)！

或者您想要玩嵌入开发？OBS 上有最新版的 [AVR
交叉编译器](http://software.opensuse.org/package/avr-libc-gcc47)，在一些
home 源里你还能找到
[msp430](http://software.opensuse.org/package/cross-msp430-gcc)
的开发工具。Android？ 中文圈的 Douglarek
就在玩这个，你们会有得聊的。但要是你是一个开发者，你开发的软件需要特定的库，那最好还是注册一个账户，把所有您需要的库嫁接到您的
home
里，打包自己的软件，然后和外界[分享](http://openbuildservice.org/help/manuals/obs-best-practices/cha.obs.best-practices.upstream.html)！

## 中毒已深？

所以呀，你得到了它。许多选择 —— 毕竟我们是尊重 Linux
哲学，绝对中立的呀（见前图）！再等一天，openSUSE
就有了。如果您手别太滑，把持的住，您会从
[software.opensuse.org](https://software.opensuse.org) 和 OBS
上的软件包中找到很多乐子的。

预祝大爷您玩的爽（Have a lot of fun）！
