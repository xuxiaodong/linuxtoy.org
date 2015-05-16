Title: webcam-server-dialog: webcam-server 的简单图形前端
Date: 2010-09-26 18:18
Author: Petty
Category: News
Tags: webcam
Slug: webcam-server-dialog

之前[本站曾介绍过](http://linuxtoy.org/archives/linux-camera-monitor.html)如何在
Linux 下用摄像头做简单的监控系统。其中
[web-server](http://webcamserver.sourceforge.net/) 是最简单的解决方案。
但它是个命令行程序，使用时可能略有不便。这里介绍一个简单的 GUI。

事实上，这个 GUI 程序只是一个30多K的 bash 脚本，通过调用dialog,
whiptail, Xdialog, xmessage, gxmessage, kdialog, 或 Zentiy 实现
GUI。[文件下载](http://www.mediafire.com/?opu79isz45ir28p)在 MediaFire
上。原作者还提供了配套的 [XDG destop menu item
供下载](http://www.mediafire.com/?en19j3z5dnt536o)。

具体使用请参考[原文](http://jhansonxi.blogspot.com/2010/09/webcam-server-dialog-basic-front-end-to.html)（需翻墙）。
