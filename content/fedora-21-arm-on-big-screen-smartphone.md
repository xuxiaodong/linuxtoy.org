Title: 在大屏智能手机上运行 Fedora 21 ARM
Date: 2015-02-02 14:53
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-21-arm-on-big-screen-smartphone

[Fedora
社区的一名爱好者](http://nocomputerbutphone.blogspot.com/2014/10/running-home-pc-on-large-screen-phone.html)最近展示了在大屏智能手机上运行
Fedora 21 ARM 的效果，如果感兴趣且愿意折腾的不妨一试。

这位爱好者已经实现了在 Sony Xperia Z Ultra
运行，更多大屏亦可以通过类似方式实现。

[![fedora-21-on-big-screen-smartphone](http://lt-file.b0.upaiyun.com/files/2015/02/fedora-21-on-big-screen-smartphone-300x168.jpg)](http://lt-file.b0.upaiyun.com/files/2015/02/fedora-21-on-big-screen-smartphone.jpg)

和其他不刷机在 Android 智能手机上运行 Linux 的方式一致，也是通过
`chroot` 的方式实现的。除此之外，还需要以下工具辅助：

* [XServer
XSDL](https://play.google.com/store/apps/details?id=x.org.server)：Android
平台原生的 XServer 支持

* [AnTuTu CPU Master
Pro](https://play.google.com/store/apps/details?id=com.antutu.CpuMaster)：调整
CPU 频率，实现更高性能

* [Better Terminal Emulator
Pro](https://play.google.com/store/apps/details?id=com.magicandroidapps.bettertermpro)：更为全面的终端
Shell 工具集，方便执行引导脚本

当然您还需要可以用来 chroot 的[Fedora 21 ARM
镜像文件](https://drive.google.com/file/d/0B2NfHoyfFf1aalZHbENvMTAwVmc)本身。该镜像文件基于
Fedora 21 ARM 官方修改，预装了 Chromium、GIMP、rdesktop
等工具。需要将其解压到 `/data/local/fedora/` 路径下。

更多细节，请参考[博客原文及步骤说明](http://nocomputerbutphone.blogspot.com/2014/10/running-home-pc-on-large-screen-phone.html)
