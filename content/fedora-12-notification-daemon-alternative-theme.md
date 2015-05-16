Title: Fedora 12 通知区域主题更换
Date: 2009-11-01 04:56
Author: lovenemesis
Category: Desktop Stuff
Tags: Fedora, nodoka, notification-daemon
Slug: fedora-12-notification-daemon-alternative-theme

Fedora 12 Beta 发布以来，有不少朋友对新添加的 Notification-daemon
颇有微辞。固然统一化的通知区域管理有好处，但是黑色的巨大方块和 Fedora
默认的蓝色 Nodoka
主题十分不和。下面将介绍如何将其变得更好看（或者说正常）些～

**1.**需要安装与 Nodoka 配套的 Notification-daemon
主题及配置编辑器。在终端输入以下命令：

`su -c 'yum install notification-daemon-engine-nodoka gconf-editer'`

**2.** 安装完成后，启动“应用程序-系统工具-配置编辑器”，依次展开键值到
`/apps/notification-daemon`，之后双击右侧的 theme 值，将其从默认黑黑的
slider 改成 nodoka，回车确认。关闭配置编辑器即可。

**3.** 注销重新登录，现在 Notification-daemon
已经变成下面这个样子，怎么样，是不是和 Fedora 默认的 Nodoka
主题协调多了？

[![](http://i.linuxtoy.org/images/2009/11/notification_daemon_nodoka-400x135.png)](http://i.linuxtoy.org/images/2009/11/notification_daemon_nodoka.png)
