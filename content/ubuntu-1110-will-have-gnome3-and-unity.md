Title: Ubuntu 11.10 将搭载 GNOME 3 + Unity
Date: 2011-05-01 22:03
Author: lovenemesis
Category: Desktop Environment
Tags: GNOME, Ubuntu
Slug: ubuntu-1110-will-have-gnome3-and-unity

因为 Ubuntu 11.04 "Natty Narwhal" 的开发重心在 Unity 上，故 11.04 搭载
GNOME 2.X。紧随其后的 Ubuntu 11.10 "Oneiric Ocelot"
的开发工作业已开始，其中值得关注的是 11.10 将**可能**搭载 GNOME 3 +
Unity，届时用户可以**选择使用 Unity 或者 GNOME Shell**。*感谢 xiaq 来稿*

[![](http://linuxtoy.org/img/2011/05/logo.png)](http://linuxtoy.org/img/2011/05/logo.png)
[![](http://linuxtoy.org/img/2011/05/unity-logo-64.png)](http://linuxtoy.org/img/2011/05/unity-logo-64.png)

开发人员表示让 Unity 和 GNOME Shell 共存的问题不大。现在主要的障碍是
Ubuntu 中不少软件包都打了补丁以支持 Ubuntu 自己的 AppIndicator
(替代系统托盘右键菜单的框架，[项目主页](http://unity.ubuntu.com/projects/appindicators/))，这个功能在
GNOME Shell 下会带来一些麻烦。开发人员将实现一个检测机制，让这些软件在非
Unity 环境下自动停用 AppIndicator 相关特性。

此外，基于 Metacity 和 Qt 的 Unity-2D (适用于不能运行 Compiz 的硬件)
也将在出现在 LiveCD 中。

*消息来源：*[OMGUbuntu](http://www.omgubuntu.co.uk/2011/04/gnome3-packages-begin-trickling-into-ubuntu-11-10)

**PS：**

此外带来两张包含 [Unity
操作方式的壁纸背景](http://www.omgubuntu.co.uk/2011/04/become-a-natty-power-user-in-no-time-using-this-unit-keyboard-shortcuts-wallpaper)两种：

[Ubuntu 紫色系背景](http://ubuntuone.com/p/pBs/)

[Eve
黑色系背景(墙外)](http://img220.imageshack.us/img220/9303/ubuntudefaultfinalen2.png)

**PSS：**

Indicator 框架，以及 GNOME Shell / Unity 之争：

下面的内容是我根据在 ~~LinuxTOY 看到的评论~~，加上自己 Google 后的总结。

Indicator 是 Ubuntu 实现的“系统托盘”服务框架。它基于
Dbus，相比传统的系统托盘，操作方式统一，支持更丰富的特性。Indicator
框架除了针对单个程序的 AppIndicator，还包括系统范围的 System
Indicator：例如 Sound Indicator
支持直接在菜单中查看专辑封面、控制播放器，Me Indicator 则支持设置 IM
的上下线状态等。Indicator 已经由 freedesktop.org 标准化，称为 [Status
Notifier
Specification](http://www.freedesktop.org/wiki/Specifications/StatusNotifierIcon)。目前
Ubuntu 的 Indicator 是 Status Notifier Specification
的参考实现，~~实际上也是唯一的实现。~~ 。

Ubuntu 的创始人 Mark Shuttleworth 曾经试图游说 GNOME 3
开发者采用这一标准，但被开发者拒绝，详情可以看 GNOME 3 核心开发者之一
Dave Neary
的[这篇文章](http://blogs.gnome.org/bolsh/2011/03/11/lessons-learned/)和
Mark Shuttleworth
的[回应](http://www.markshuttleworth.com/archives/661)。这在 GNOME Shell
和 Unity 之争中算是一个代表性的事件，Unity 团队和 GNOME Shell
团队就此分道扬镖。

不过值得注意的是，GNOME 3 不仅仅意味着 GNOME Shell，GNOME 3
的开发者不采用 Indicator 框架主要影响 GNOME Shell，因此 Unity 和 GNOME 3
的其它组件还是能够共处的，Ubuntu 11.10 搭载 GNOME 3 也是情理之中。

**UPDATE:** [csslayer](http://csslayer.tk/)在 ikde 指出 [KDE 也实现了
Status Notifier
Specification](http://www.ikde.org/discuss/quarrel-between-gnome-canonical-kde/)。
