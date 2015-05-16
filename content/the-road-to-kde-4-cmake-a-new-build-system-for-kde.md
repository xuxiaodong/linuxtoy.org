Title: 通向 KDE 4 之路（八）：CMake，新的 KDE 构建系统
Date: 2007-02-24 11:33
Author: toy
Category: Apps
Slug: the-road-to-kde-4-cmake-a-new-build-system-for-kde

当一个项目的规模发展到像 KDE
这样庞大的时候，对既定设计的变更比起十年前要困难多了。起初，KDE 依靠
autotools 工具集来构建大部分的项目，但从去年开始，KDE 4
将改用一个全新的构建系统，[CMake](http://cmake.org/)。我们认为它将很快成为世界上现存的各种构建系统中有力的竞争者之一。详情见下。

本文会着重介绍 CMake，CMake 不属于 KDE 项目，它是另一个独立开源软件小组
[Kitware](http://www.kitware.com/) 的产品，以 BSD
[授权协议](http://cmake.org/HTML/Copyright.html)发布。虽然我恐怕无法用截图这种形式来展现这种构建系统的特征，但是我将尽可能通过文字描述
CMake 之所以会受到 KDE 开发组欢迎的原因。

不过在正式开始讨论 CMake 之前，我打算先回顾一下 KDE 和 autotools
的关系史。KDE 创自 Qt，Qt
中有一个很棒的特性被称为元对象编译器（moc），而 autotools 若要支持 moc
作为大多数 KDE
头文件的预处理器必须在功能上进行一些拓展。这种状况只不过是个开始，为了在构建过程中自动生成并添加所需的文件类型，KDE
的开发者写了许多自用的 DCOP
通讯协议完成这一工作，比如加入文档编译器、语言包自动处理器、从 XML
中生成配置文件样本、Qt 用户界面编译器（就是那些 .ui
文件）等，我们希望构建系统能支持对这些操作的处理。更甚者，我们还企求 KDE
构建系统能支持预配置、编译选项等一系列完整的工程流水线。久而久之，现在的
KDE
构建系统已经演变得像一只由各种器官杂凑出来的怪兽，就算这样，autotools
也还是不能完全满足我们的需求。

在 KDE 3 时代，仅有极少数所谓“编译专家”才能通彻地熟悉整个 KDE
构建系统，不了解内情的 KDE
开发者若想把一个组件从某文件夹移到另一个文件夹里，别指望不花上几个小时就让这套代码能再次成功编译出来。甚至有时候，从头开始一个独立的
KDE 项目之前需要先部署 500K 左右的 autotools
配置，最终却只是为了支持一个简单的“hello world”类型程序。

事情很明显了，KDE 4 必须做些什么来摆脱这种窘境，在 Akademy 2005
会议中，我们决定要发掘其它可选用的构建系统。刚开始，SCons 一度成为新 KDE
构建系统的原型，但它还是太慢了，况且经过几个月的工作，我们都没能将
kdelibs 成功地从 autotools 完整迁移出去，其中一个很大的问题就是 SCons
在模块化上有显著的欠缺。

在这之后，有一名对 KDE 颇有贡献的人士，Alexander Neundorf 决定尝试将 KDE
迁移到 CMake 构建系统，这一流程居然相当顺利，~~而且他本人还是 CMake
开发者的技术支持~~他是在 CMake
开发者的支持下完成这一工作的。接下来，我们只用了几个星期就顺利地把 KDE
中大部分东西用 CMake 构建成功，这样 autotools 终于可以彻底地被驱逐了。

CMake 的开发者对 KDE 的迁移计划给予了很多的援助，他们还参与到针对 KDE
构建系统的邮件列表里一起帮忙，这种合作对彼此都有益处。就像 KDE
开发者会和 CMake 开发者展开交流，提出改进建议，这能促进 CMake
系统中某些落后设计加速进步──他们也很乐意提供反馈，这将使得 CMake
会对所有采用构建系统的项目都能及时给出有效的改进。

在我们的合作期间，CMake 为 KDE 的构建作出了大量的改良。使用 CMake
的项目可以花更少的时间完成构建系统的建设，开发者也一定希望用来折腾构建系统的精力越少越好。如一名
KDE 开发者所言：“CMake 不会再让你构建项目时烦得只想往自己脑袋上来一枪。”

CMake
的核心是~~读取一个容易理解的文本文件“CMakeLists.txt”，开发者可以往里面添加自己的源码目录~~把
CMakeLists.txt
这个文件放在源代码所在的目录中。当您运行“cmake”命令时，它会寻找这个文件，根据里面的内容生成标准的
Makefiles（UNIX 平台专用）或是利用命令行开关生成 XCode
项目文件（用于构建 OS X 系统上 XCode 开发工具所面向的 Mac
程序），甚至还能通过您的源代码生成 MSVC 项目。此外，CMake 中还有个 KDE
相关的特色功能，它可以基于 “CMakeLists.txt”自动创建出对应的
[KDevelop](http://www.kdevelop.org/)
项目文件，这里的“CMakefiles.txt”和用来生成 Makefiles 的文件是一致的。

KDE
的代码力图确保相当的可移植性（有少数部分例外），然而这并不足以让它能在
Windows 这样的其它系统上构建，因为受到了 autotools
的局限。但是现在，由于构建系统能在别的操作系统上运行，KDE
自身也同样可以了（当然，Qt 在其它平台上也已经是 GPL 了）。

在 KDE 3.x 中，推荐的 KDE 构建方式是像下面这样：  
` % ./configure --prefix=/foo --enable-debug % make # make install`  
如您所知，上面那是非常标准的 autotools
构建模式，只是，控制构建进程的那些脚本可是太难弄懂了。

使用 CMake
的话，构建语法有所改变（在开闭配置选项上比旧形式更加直观），但命令还是挺相似的，见下：  

` % cmake -DCMAKE_INSTALL_PREFIX=/foo \     -DCMAKE_BUILD_TYPE=debugfull . % make # make install`  
以上语法的变化幅度其实没多大，但却好懂多了。

CMake 搜索依赖对象的速度比“./configure”快了好几倍，用 CMake 构建
kdelibs4 比用 autotools 构建 KDE 3.5.6 的 kdelibs 所花的时间少了
40%，大概是拜 CMake 不使用 libtool 组织工具链所致吧。在 UNIX
平台上，CMake 使用的工具链是这样的：*cmake+make*，然后您再看看 KDE 3.5.6
的构建工具链：*automake+autoconf+libtool+make+sh+perl+m4*……伙计，对比一下吧。

这里我准备凭自己的个人经验来说明 CMake 到底有多好用：有一天 Aaron Seigo
向我讨教怎么把一些原属 kdesktop 的组件转移到 krunner 下，因为到 KDE 4
以后 kdesktop 将被全部清除。如果是在 KDE 3
下，我就得拟定一张待办事项清单，倒不是因为代码有多难懂，而是因为这构建系统太难应付。总之无论如何，我都不想再为
KDE 3 做这种事了。不过在 KDE 4 和 CMake
上，我只需要把代码换个存放位置，再改几个分类名字，这场代码迁移就在构建系统中顺利就绪了，整个过程里只需在
krunner 的 CMake
构建文件里修改两到三行而已。几分钟后，整个项目就可以重新构建，且成功完成了链接和安装。我对这件事印象很深，从此以后也致力于帮助别人做构建系统迁移的事务。反观在
KDE 3 时，我的脑子几乎要被构建系统弄垮，都打算放弃，不想再把代码往 KDE
SVN 上提交了（真的不是 KDE 代码本身的问题啊）。

事实可以表明，各位 KDE
编译专家以后可以少死些脑细胞了，每个人都可以较轻松地构建他们的项目并让其运行起来。或许有人有不同看法，但很多开发者都已经在对照了“CMakeLists.txt”和“autotools”语法之后直截表露出和我类似的感觉。当然了，几乎所有的
KDE 开发者现在还是 CMake 菜鸟，为此 CMake 开发者已经亲身进入 KDE
群体中帮助我们尽可能顺利地完成系统迁移。

这次 CMake 迁移并不是 KDE 项目第一次变更开发所需的核心技术了。在 KDE
开发早期，我们使用 CVS 实行源码版本控制，可惜 CVS
服务器维护者的脚步开始渐渐跟不上 KDE
发展的速度，我们这里还堆了一卡车访问时间记录比原始提交版本还要早的莫名其妙的代码文件。后来我们发现
Subversion （SVN）这个全新的并行版本控制系统更加有前途，更加适合 KDE
项目的需要，也更加容易维护。当时，还没有一个 KDE 这等规模的项目是用 SVN
管理的，对 Subversion 自己来说此次迁移也是个严峻的考验，最终的结果证明了
KDE 和 SVN 能协作得很好，自 KDE 先行之后，很多别的项目也都跟着往 SVN
上迁移了。

KDE 选用 CMake 构建系统也对公众起到了一定的示范作用，就像 Subversion
那样。一些其它项目也在迁移到 CMake 上，其中包括但不限于：
Scribus、Rosegarden（原本是 SCons）、PIPlot、ChickenScheme
等，另外我们还有项工作是让 KDE 3.x 程序也能使用 CMake（例如 KDE 3 上的
KPilot 就已经是了）。我认为，每一个试图支持多平台的项目都应该试试
CMake，往您的源码树里加一个“CMakeLists.txt”文件不会影响既有的构建系统，反能成为体验
CMake 能为您做些什么的良好契机。还有，和 KDE
一样，除非发生不可预料的意外，CMake 小组总会对产品的改进持以开放的态度。

这些链接可能对有兴趣知道更多的读者有用：

[The original post by Alex about the port to
CMake](http://lists.kde.org/?l=kde-core-devel&m=113734805302055&w=2)，一年多前的文章。

[An earlier article on KDE +
CMake](https://lwn.net/Articles/188693/)，曾发表在 Linux
每周新闻上的报道。

[KDE + CMake beginners
guide](http://wiki.kde.org/tiki-index.php?page=KDECMakeIntro)，来自 KDE
Wiki ~~的礼物~~。

这篇就到此为止。下星期，我答应给大家看些炫的东西……

原文：[The Road to KDE 4: CMake, a New Build System for
KDE](http://dot.kde.org/1172083974/)  
译文：[通向 KDE 4 之路（八）：CMake，新的 KDE
构建系统](http://www.myswear.net/forum/viewthread.php?tid=7889)

（Troy Unrau／文 | 千里孤坟／译）  
（感谢 jjgod 朋友的指正，本文已于 3/1/2007 更新。）
