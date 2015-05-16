Title: 基于 GTK2 的飞信客户端： OpenFetion
Date: 2010-06-03 07:53
Author: lovenemesis
Category: Instant Messenger
Tags: openfetion
Slug: gtk2-based-fetion-client-openfetion

[LibFetion](http://linuxtoy.org/archives/linux-fetion-1-3-released.html)
近半年没有动静了，不知去向如何。现在
[levin108](http://code.google.com/u/levin108/) 开发了 OpenFetion， 使用
GTK2 ，并且使用最新的 v4 协议，是不错的替代品。

与 LibFetion 相比， OpenFetion 有如下特点：

-   使用 GTK2+ 实现图形界面，与 GNOME 系统风格更加协调。
-   完全开源，没有链接非开源库。
-   使用 v4 协议，实现了直接发送短信、自定义头像等功能。

目前 OpenFetion 的最新版本是 1.5 。

[作者博客](http://basiccoder.com/openfetion)

[源代码下载](https://sourceforge.net/projects/ofetion/)

[源代码及各种版本二进制包下载](http://code.google.com/p/ofetion/)

**PS：**Fedora 13 上通过源代码编译安装方法：

安装依赖组件（gstreamer-devel 可选，提供消息提示声功能）

`su -c 'yum install gstreamer-devel gtk2-devel libxml2-devel openssl-devel'`

之后都懂得……

`./configure --prefix=/usr`

`make`

`su -c 'make install'`
