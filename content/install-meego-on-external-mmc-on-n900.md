Title: 在 N900 上外置存储卡上安装 MeeGo
Date: 2010-08-07 19:39
Author: lovenemesis
Category: Gadget
Tags: MeeGo
Slug: install-meego-on-external-mmc-on-n900

如果你很期待 MeeGo Handset 版本而又恰好拥有 N900 及一个空闲的 MMC
卡的话，那么现在已经可以尝试啦！*感谢 gbraad Redent !*

首先前往 [Nokia
开发站](http://tablets-dev.nokia.com/meego-codedrop.php)下载需要的RAW镜像和内核包，注意需要输入
N900 的 IMEI 号才可以。

然后用 dd 将 RAW 镜像做到空闲的 MMC 卡上。之后将做好的 MMC 卡插回到 N900
里，记得装上背盖。

最后，像通常刷 N900 一样参照如下命令用 Flasher
将内核包刷入，不过不同的是用 -l 选项只加载，这样就不会覆盖原先 Maemo 5
的内核了：

`flasher-3.5 -l -b -k `

之后系统就会用这个内核从 MMC 引导入 MeeGo Handset
系统了！体验完后，再次重启就可恢复 Maemo 5 系统，完全无痛~

**警告：珍爱生命，谨慎折腾！**

[英文原文](http://forum.meego.com/showthread.php?p=6642#post6642)
