Title: Mini Howto: Fubuntu
Date: 2006-08-13 20:35
Author: toy
Category: Tutorials
Tags: fluxbox
Slug: fubuntu

对于 Ubuntu、Kubuntu、Xubuntu 大家都比较熟悉了，那 Fubuntu 又是什么呢？我把 [Fluxbox](http://www.fluxbox.org)+Ubuntu 称为 Fubuntu。:)

<!-- PELICAN_END_SUMMARY -->

[![Fubuntu](http://i.linuxtoy.org/i/fubuntu_s.png)](http://i.linuxtoy.org/i/fubuntu.png)

这几天时间我对原有的系统进行了彻底地改造，抛弃了一惯使用的 GNOME，原因十分明显，我需要一个轻量而灵活的系统，选择 Fluxbox 是个不错的主意。Fluxbox 这个窗口管理器相当轻量，而且可配置性也是非常高。目前，我对 Fluxbox 的表现很满意，整个系统反应迅速，运行稳定，感觉非常舒服。

需要说明的是，对于 Fluxbox 的安装与配置是一个详细而漫长的过程，也许本文不能给你全部的答案，但我还是十分乐意写出来，为有兴趣的朋友提供一些参考。

下面我将开始简述 Fubuntu 的整个安装过程。

首先需要确定的一件事情是，映像文件的选择。在 Ubuntu 官方网站上列出的有 Desktop CD、Server install CD 和 Alternate install CD 三种。其中，Desktop CD 是一个包含图形化安装程序的 Live CD，不是我们所需要的。至于后两种，二者择其一皆可。

在安装之初，选择 Server 模式进行安装，按照一般的安装过程把基本系统安装好。之后，重新启动系统，并登录，这时候还是文本界面模式。现在要做的就是修改 /etc/apt/sources.list 文件，将其中 deb http:// 和 deb-src http:// 前面的 # 符号去掉。保存后执行指令 `sudo apt-get update`。

现在我们就可以安装图形化环境了，执行指令 `sudo apt-get install x-window-system-core fluxbox xdm xterm`。这个指令将安装 X 窗口系统、Fluxbox 窗口管理器、图形登录管理器和终端。你可以根据自己的喜好对该指令作出部分调整，比如最后两者。

再次重启系统，使用图形登录管理器进入即可完全置身 Fluxbox 环境了。这时候，可以对 Fluxbox 进行一些配置，如：通过下列操作来生成一个菜单：

    cd /usr/share/doc/fluxbox
    sudo gzip -d fluxbox-generate_menu.gz
    sudo cp fluxbox-generate_menu /usr/bin
    fluxbox-generate_menu

如果要对 Fluxbox 进行更多的配置，建议去阅读使用手册。

最后，就是安装你喜欢的应用程序了，像 Firefox、XMMS、Gaim 等等。
