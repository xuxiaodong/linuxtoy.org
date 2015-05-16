Title: 如何在 Fedora 下安装 PPStream 网络电视
Date: 2009-12-12 05:14
Author: lovenemesis
Category: Movie Player
Tags: Fedora, ppstream, totem
Slug: how-to-setup-ppstream-on-fedora

本文将介绍如何在 Fedora 下安装 PPStream 网络电视 Linux 版本。

网上有很多关于 PPStream Linux 版本安装的教程，不过绝大多数都是基于
Ubuntu 的。本文参考 [totem-pps 上的
Wiki](http://code.google.com/p/totem-pps/wiki/HowToInstall) 为例在
Fedora 12 i686 重做这个过程。

**1.** 下载所有必需软件包

首先是 PPS for Linux 本身：
[点击此下载](http://download.ppstream.com/linux/release_for_ubuntu.tgz)

然后是由 [sunmoon1997](http://code.google.com/u/sunmoon1997/) 制作的
PPStream Totem 插件，包含三部分：
[libppswarpper](http://people.freedesktop.org/~jinghua/distfiles/libppswrapper-0.0.18.1.tar.gz),
[gst-plugins-pps](http://people.freedesktop.org/~jinghua/distfiles/gst-plugins-pps-0.0.18.tar.gz)
和
[totem-pps](http://people.freedesktop.org/~jinghua/distfiles/totem-pps-0.0.18.tar.gz)
。（[totem-pps
下载主页](http://people.freedesktop.org/~jinghua/distfiles/)）

在[配置好 rpmfusion
仓库](http://rpmfusion.org/Configuration/)后，安装必须的依赖软件和编译工具：

*在终端中运行以下命令*

`su -c 'yum install gcc-c++ glibc-devel intltool python-devel gstreamer-devel gstreamer-ffmpeg gstreamer-plugins-bad gstreamer-plugins-ugly'`

**2.** 安装 PPStream for Linux

*在放置 release\_for\_ubuntu.tgz 的目录打开终端依次执行以下命令*

`tar xf release_for_ubuntu.tgz`

`cd release_for_ubuntu/`

`su -c 'cp -v ppscdn_config.ini /etc'`

`tar xf libs_for_ubuntu.tgz`

`su -c 'cp -av libs/libpps*so* /usr/lib'`

**3.** 编译并安装 PPS 封装库 libppswarpper

*在放置 libppswarpper 的目录打开终端依次执行以下命令*

`tar xf libppswrapper-*.tar.gz`

`cd libppswrapper-*`

`./configure --prefix=/usr`

`make`

`su -c 'make install'`

**4.** 编译并安装 Gstreamer PPS 插件 gst-plugins-pps

*在放置 gst-plugins-pps 的目录打开终端依次执行以下命令*

`tar xf gst-plugins-pps-*.tar.gz`

`cd gst-plugins-pps-*`

`./configure --prefix=/usr`

`make`

`su -c 'make install'`

**5.** 编译并安装 Totem 电影播放机 PPS 插件 totem-pps

*在放置 totem-pps 的目录打开终端依次执行以下命令*

`tar xf totem-pps-*.tar.gz`

`cd totem-pps-*`

`./configure --prefix=/usr`

`make`

`su -c 'make install'`

**6.** 在 Totem 电影播放机里启用 PPStream 侧栏

打开电影播放机，在“编辑”-“插件”里即可找到“PPStream
浏览器”，在它前面打勾即可。

此时点击侧边栏，在下拉菜单中即可看到 PPStream 内容。

**至此安装完成。**

**如何播放？**

*方法一：*在电影播放机里的 PPStream 寻找感兴趣的内容，双击即可播放。

*方法二：*在 [PPS 在线视频看看](http://kan.pps.tv/)
网站上选择感兴趣的内容，在播放窗口右下角右键点击“客户端播放”，选择“复制链接地址”。然后打开电影播放机，选择“电影”-“打开位置”，刚才的链接地址会自动复制到里面，点击打开即可。

*方法三：*为 Firefox 安装 Greasemonkey 扩展，然后使用由 liu.wanfang
写的[这个脚本](http://userscripts.org/scripts/source/59991.user.js)即可直接在[PPS
在线视频看看](http://kan.pps.tv/) 网站上观看。

**感谢 PPStream，sunmoon1997 和 liu.wanfang，是他们为 Linux
平台带来了更好的影音体验！**
