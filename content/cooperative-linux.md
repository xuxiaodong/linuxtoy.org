Title: Cooperative Linux
Date: 2008-11-22 17:30
Author: toy
Category: Apps
Tags: coLinux
Slug: cooperative-linux

[作者：[yang](http://www.shouguang.org/yang/)]

想使用 Linux，但是，说实话，我从 Ubuntu 6.06 开始到现在的 Ubuntu
8.10，我的感觉是 Ubuntu 变得越来越慢了。

只是针对我的老笔记本而言，发行版本越来越高，而我的笔记本的硬件却还是老样子的，同样运行
Ubuntu 6.06 很快，但是运行 8.10 却是“卡的很”。

有人推荐我使用别的 WM，我当然试过了，去掉 GNOME，使用非常轻量级的
Openbox（Fluxbox）依然是卡的很，正如
[littlebat](http://www.learndiary.com/)
所说的：“这些现代的内核和图形库等相对于老旧电脑来说是很笨重的”——真是非常准确且现实的说法。

但是，我还是非常喜欢——非常非常喜欢 Linux 中的一些小而专的软件，比方
w3m，Irssi，或者 Dillo，这是一些非常优秀的软件。但是在 Windows
下却没法使用它们——虽然有 Dillo 的 win
版本，但实在是太粗糙了——所以我选择了 [Cooperative
Linux](http://www.colinux.org/)（简称 coLinux）。

[![coLinux](http://i.linuxtoy.org/images/2008/11/colinux-thumb.png)](http://i.linuxtoy.org/images/2008/11/colinux.png)  
*coLinux 使用截图*

相信不少人使用过 coLinux，这是个非常快速的 Linux 类虚拟机，可以在
Windows 下快速的运行，速度非常非常的快速！虽然对 X
支持不好，但是在控制台下，和一般使用 Linux
的操作是完全相同的。它可以运行 Debian，Arch，Gentoo，FC 等，好多的 Linux
版本都可以在 coLinux 下快速的运行。如果你对 X 要求不高，且埋怨 VMware
的效率的话，不妨尝试下 coLinux——我经常在 Linux 做 Web
服务的测试，非常安全且快速。

关于 coLinux 的具体安装我就不一一介绍了，安装非常简便：在 Windows 下使用
coLinux 专门的 vmlinux 内核来引导 ext3 的磁盘镜像。具体的安装请看官方的
wiki
或者[这篇文章](http://www.shouguang.org/yang/2008/11/install-debian40rc5-on-cooperative-linux/)吧，或者是这篇[较老的安装教程](http://www.shouguang.org/yang/2008/11/install-debian40rc5-on-cooperative-linux/)（已经不适合最新版的
coLinux）。

这里我只是想介绍下这个优秀的 Linux 模拟器。
可以非常非常的快速，非常非常稳定的运行
Linux，很稳定很实用的软件。我尝试在 coLinux 下安装了
[Debian](http://www.shouguang.org/yang/2008/11/install-debian40rc5-on-cooperative-linux/)
和
[Arch](http://www.shouguang.org/yang/2008/02/colinux%E4%B8%AD%E5%AE%89%E8%A3%85colinux/)。

希望大家尝试下这个东东，的确不错的说。

尝试在 coLinux 下使用 GUI 的程序，需要
[Xming](http://www.shouguang.org/yang/2008/11/cooperative-linuxxming/)。

coLinux 的默认控制台并不支持中文，可以使用
[SSH](http://www.shouguang.org/yang/2008/11/%E4%B8%8A%E7%BD%91%EF%BC%8C%E4%BD%BF%E7%94%A8colinux/)
来完美的显示和输入中文。

感谢 toy 推荐了 vitetris，相当之好玩，比
[tetris-bsd](http://www.shouguang.org/yang/2008/11/%E5%87%A0%E4%B8%AA%E6%9C%89%E8%B6%A3%E7%9A%84bsd%E7%BB%8F%E5%85%B8game/)
有趣多了。

另外 toy 曾经介绍的
[andLinux](http://linuxtoy.org/archives/andlinux.html) 也是借助 coLinux
实现的。嫌安装 coLinux 麻烦的同学使用 andLinux 或许更方便些吧。

[[原文链接](http://www.shouguang.org/yang/2008/11/cooperative-linux/)]
