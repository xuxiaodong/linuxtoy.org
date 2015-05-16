Title: Gimmie 在 Ubuntu 下的安装使用
Date: 2006-10-22 15:08
Author: toy
Category: Tutorials
Slug: gimmie_install_and_use

在 [linuxtoy](http://linuxtoy.org/archives/gimmie.html) 上看到了 Gimmie
这个小东西，想要试试。在安装的过程中也遇到了一点问题，现在写来与大家分享。

一、安装

1.按照英文论坛上我们需要安装如下包：

> * build-essential  
>  * python-dev  
>  * python-gtk2-dev  
>  * python-gnome2-dev  
>  * python-gnome2-desktop  
>  * python-gnome2-extras-dev  
>  * libgnome-desktop-dev  
>  * libgnomecups1.0-dev  
>  * libwnck-dev

在我的系统中实际安装的包有：

> libart-2.0-dev libavahi-client-dev libavahi-common-dev
> libavahi-glib-dev  
>  libbonobo2-dev libbonoboui2-dev libcupsys2-dev libgconf2-dev
> libgcrypt11-dev  
>  libgnome-desktop-dev libgnome-keyring-dev libgnome2-dev
> libgnomecanvas2-dev  
>  libgnomecups1.0-dev libgnomeui-dev libgnomevfs2-dev libgnutls-dev  
>  libgpg-error-dev libidl-dev libopencdk8-dev liborbit2-dev
> libselinux1-dev  
>  libsepol1-dev libtasn1-3-dev libwnck-dev libxres-dev
> python-gnome2-dev  
>  python-gnome2-extras-dev x11proto-resource-dev

2.到 <http://beatnik.infogami.com/Gimmie> 下载源代码包
[gimmie-0.1.1.tar.gz](http://www.beatniksoftware.com/gimmie/releases/gimmie-0.1.1.tar.gz)，并解压缩。

3.进入解压缩后的目录执行：  
` ./configure && make`

4.程序有一点小问题，模块没有被复制到合适的目录。我们手动调整一下。在软件目录下执行：  

` cp egg/.libs/_egg.so .. cp gdmclient/.libs/_gdmclient.so .. cp gnomecups/.libs/_gnomecups.so .. cp gnomedesktop/.libs/_gnomedesktop.so .. cp iconentry/.libs/_iconentry.so .. cp sexy/.libs/_sexy.so .. cp wnck/.libs/wnck.so ..`

5.运行命令启动程序：  
` ./gimmie.py`

6.如果你希望每次开机时都能自动启动，在
**菜单-系统-首选项-会话-启动程序** 处添加 gimmie.py 的地址即可。

[![Gimmie](http://i.linuxtoy.org/i/gimmie_s.jpg)](http://i.linuxtoy.org/i/gimmie.jpg)

二、使用

在 bar 上端我们可以看到分别有
Applications、Documents、Peple、Computer，只要左键单击这几个字就可以打开相应的配置菜单。

[![Gimmie](http://i.linuxtoy.org/i/gimmie2_s.jpg)](http://i.linuxtoy.org/i/gimmie2.jpg)

在任何窗口里面，右键点击一个图标就会出现选项。选择 Keep Around
就可以让图标作为快捷方式显示在 bar 上。

[![Gimmie](http://i.linuxtoy.org/i/gimmie3_s.jpg)](http://i.linuxtoy.org/i/gimmie3.jpg)

People 是和 Gaim
相互关联的，你可以把你经常联系的朋友图标作为快捷方式添加。也可以快速的进行分组、添加好友的动作。另外似乎还可以监视
Gmail（有那个图标，但是我这里是灰色的。）。

在 Computer 字符上点击右键可以快速打开系统设置菜单。

在 Documents 字符上点击右键可以快速的新建文本文件。打开标签目录。

状态栏图标：比如 Gaim、amule，他们曾经也显示在 gimmie
的右侧，但是在写此文的时候他们依然还是在 Gnome 的任务栏上。

如果你知道更多的 gimmie 设置方法，希望分享。

（注：此文作者为 latteye，由其本人投递到 linuxtoy
与大家分享，[原始链接](http://www.laroea.cn/read.php/64.htm)，非常感谢
latteye 朋友的支持）
