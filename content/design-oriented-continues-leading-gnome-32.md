Title: 设计继续领着 GNOME 迈向 3.2 版本
Date: 2011-06-02 13:51
Author: lovenemesis
Category: Featured
Tags: gnome3
Slug: design-oriented-continues-leading-gnome-32

Gnome 2.x 系列中，GHIG 起到的作用是非常大的，但在这个系列，Gnome
还是个和大多数开源项目一样，是一个由代码 (Code) 驱动的项目。在 Gnome 3.0
的开发过程中，设计先行的理念得到了开发者社区的普遍认可，Gnome 3
的第一个版本 3.0 发布之后，该理念更是得到了来自用户层面的认可。*感谢
jcome 来稿。*

在接下来 GNOME 3.2
版本的开发中，[设计驱动](http://gitorious.org/gnome-design)这一开发模式继续发挥着其魅力：

将引入一个全新的 [GNOME Contacts
程序](https://live.gnome.org/Design/Apps/Contacts)，用于用户联系人的管理。这个程序的设计来自在
GNOME 3.0 开发中崭露头角的设计师 Allan Day，这次 Allan Day 同时也对
GNOME 程序外观主题做了一些尝试，Gnome 3.2 的主题将会更加细腻完善。目前
GNOME 社区的超级Hacker，Alexander Larsson 正在编程实现这个**全新的 GNOME
Contacts**。见下图：

[![](http://linuxtoy.org/img/2011/06/fig1-contacts.png "fig1-contacts")](http://linuxtoy.org/img/2011/06/fig1-contacts.png)

另外以 Allan Day 为主，GNOME
设计团队也在试图修改传统的[菜单栏设计](https://live.gnome.org/Design/Whiteboards/Menus)，极可能**在
GNOME 环境实现 Mega 菜单**。有了这个 Mega
菜单，您还需要菜单和程序窗口分离，有时甚至相隔万里之遥类 MacOS
的全局菜单吗？见下图：

[![](http://linuxtoy.org/img/2011/06/fig2-megamenu.png "fig2-megamenu")](http://linuxtoy.org/img/2011/06/fig2-megamenu.png)

当然作为最早进行 GNOME－Shell 设计的 Jon McCann 也没有停止对 GNOME
项目的贡献，在提出 GNOME OS 的概念之后，他开始了一系列的[GNOME OS
相关的设计工作](http://live.gnome.org/GnomeOS/Design/Whiteboards)。其成果之一的
**GTK+ Wizards 可能在出现在 3.2 版本**中。

另外，还可能在 3.2 版本出现的是 [GTK+
字体选取器](http://aruiz.synaptia.net/siliconisland/2011/04/gtk-fontselection-progress.html)。这是在  
Gnome/Fedora 设计团队和开发者 Alberto Ruiz 一道努力的成果。

Jimmac (惠及众多开源项目，甚至一些著名的商业软件，如著名的三维动画软件
Houdini 的 Tango 图标项目的发起人）也在继续的为 GNOME
桌面贡献其无穷创意，改进 Overview 模式下的 Windows 和 Applications
按钮的可用性。同时也在尝试**分页显示的 Applications 视图**。

[![](http://linuxtoy.org/img/2011/06/fig3-overview-application-picker.png "fig3-overview-application-picker")](http://linuxtoy.org/img/2011/06/fig3-overview-application-picker.png)

Control Center 方面，Jimmac 设计了一个用于[绘图板的 Control Center
面板](http://live.gnome.org/Design/SystemSettings/Tablet)；系统信息和网络面板也得到改良。还有由
Allan Day
提出的[把锁定按钮放到工具栏中的设计也在由开发者实现中](https://bugzilla.gnome.org/show_bug.cgi?id=650292)。

3.2 还将引进的一个非常大的特性是来自 Richard 的**色彩管理系统，也就是
[colord
模块](http://colord.hughsie.com/intro.html)**。相关的[用户体验设计](http://colord.hughsie.com/screenshots.html)也在紧锣密鼓的进行着。虽然
Richard 是来自 Redhat 的工程师，但是和其他的 GNOME 开发者一样，并没有把
colord 工作局限于 GNOME 这个圈子里，而是和众多的上游项目 如
CUPS，GohstScript，Foomatic 等等一道去完善 Linux
桌面的软肋：色彩管理。这个项目并不是 Fedora only: colord
的开发者们积极的帮助诸如 openSUSE、Ubuntu 之类的发行版实现对 colord
的支持。相信不久的将来不只是 Fedora，不只是 GNOME，其他发行版如
Ubuntu，Gentoo，Arch；其他桌面环境如 KDE，XFCE
等都将迈入具有色彩管理系统行列，缩小 Linux 和
Windows（WCS），OSX（ColorSync），等商业操作系统缩的差距。

Nautilus
方面，进化速度也在加快。比如，一个很容易引起用户注意到的改进：通过
JavaScript （UI 部分），C
实现的[**快速文件预览支持**](http://blogs.gnome.org/cosimoc/2011/04/29/sushi/)，它一方面给桌面用户更好的桌面使用体验，另一方面也体现了
GNOME 3 全新架构的强大。该新特性将不只局限在
Nautilus，在文件选择器和桌面的其他地方也会有其身影出现。  
[**朝内视频说明**](http://v.youku.com/v_show/id_XMjcyNDAwNTg4.html)

通过 **GNOME-Shell, Zeitgeist 和 Tracker 的协同工作**，在 3.2
中用户查找管理回想自己的数据内容会变得会简单，高效。大家可能还记得当初因为没有好的设计方案和
GNOME，特别是 GNOME-Shell 紧密融合，Zeitgeist 没能作为 GNOME
的依赖模块，导致其开发者产生抱怨，部分高级用户的误解。现在 Zeitgeist
终于明白设计是 GNOME 一个必不可少的部分，GNOME
不是一个堆放先进功能，新奇软件的环境。现在 Zeitgeist 开发团队正和 GNOME
开发团队一道把这个漂亮创意融入到 GNOME 桌面环境中去。

除了引入新设计，新功能，开发者们也在**积极修复 GNOME 3.0
遗留的一些问题**，如过高的窗口标题栏（已经在最新稳定版本 3.0.1
中修复）等等。当前如雨后春笋般涌现的用户自定扩展有过度使用 Topbar
的趋势，这 GNOME-Shell 的设计造成了某种程度的冲突，此类问题也是摆在
GNOME 设计师，开发者们前面的挑战。

本文主要参考了[这篇文章](http://afaikblog.wordpress.com/2011/05/27/recent-goings-on-in-gnome-design/)和网上其他相关资源.
