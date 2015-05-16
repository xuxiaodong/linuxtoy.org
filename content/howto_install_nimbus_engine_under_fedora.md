Title: Fedora 下安装 Nimbus 主题引擎
Date: 2008-12-27 20:38
Author: lovenemesis
Category: Apps, Desktop Stuff
Tags: Fedora, nimbus, opensolaris
Slug: howto_install_nimbus_engine_under_fedora

Nimbus 是 OpenSolaris 下 GNOME 默认的主题引擎，本文将以 Fedora 11
为例介绍如何在 Fedora 下安装此主题引擎，使你的 Fedora 摇身一变成
OpenSolaris。  

因为 Fedora 仓库里并没有 Nimbus 引擎的 RPM
包，所以本文将采用下载源代码包自行编译的方式。如果你的发行版已经包括
Nimbus 引擎，无视此文通过包管理系统安装即可。

首先，需要从 Sun 的网站上下载最新的 Nimbus。目前最新的为 0.1.4
版本（2009年10月14日更新），下载地址见[这里](http://dlc.sun.com/osol/jds/downloads/extras/nimbus/nimbus-0.1.4.tar.bz2)。

然后，安装必要的编译工具：

`su -c 'yum install intltool gtk2-devel icon-naming-utils'`

输入 y 确定安装，等待安装完成。

之后解压缩下载的 Nimbus 源代码包到任意位置，进入解压缩后生成的目录。

在此目录中打开一个终端，接着输入以下命令：

`./configure --prefix=/usr`

`make`

`su -c 'make install'`

如果一切正常，此时你就可以在 “系统”-“首选项”-“观感”-“外观” 中找到 Nimbus
了，单击它即可启用。

最后来张截图。  

[![](http://i.linuxtoy.org/images/2008/12/screenshot.png)](http://i.linuxtoy.org/images/2008/12/screenshot.png)

想要 OpenSolaris 壁纸的朋友可以自行寻找，网上很多的，不再赘述。

本文得到了 [Linux 公社](http://www.linuxidc.com/Linux/2007-08/6638.htm)
和 [FedoraForum](http://forums.fedoraforum.org/showthread.php?t=155606)
上两篇文章的启发，在此向原作者表示感谢。
