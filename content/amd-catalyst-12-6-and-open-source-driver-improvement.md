Title: AMD Catalyst 12.6 及开源驱动进展
Date: 2012-07-01 10:03
Author: lovenemesis
Category: Drivers
Tags: Catalyst, radeon
Slug: amd-catalyst-12-6-and-open-source-driver-improvement

AMD 发布了闭源显卡驱动 12.6 正式版本，同时也将开源驱动提升至 7.0 版本。

相比之前发布的 [Catalyst 12.6 Beta
版本](http://linuxtoy.org/archives/amd-catalyst-12-6-beta.html)，本次正式版本的变化有：

-   增加了对 Linux Kernel 3.4 的支持。
-   修复了一些 Beta 引入的错误。

[官方二进制 RUN
版本下载](http://www2.ati.com/drivers/linux/amd-driver-installer-12-6-x86.x86_64.run)

另外**适用于 Fedora 17 的 rpmfusion 版本**已经现身 updates-testing
仓库，Fedora 的用户可以使用如下命令在终端安装：

`yum --enablerepo=rpmfusion-nonfree-updates-testing install akmod-catalyst xorg-x11-drv-catalyst-libs`

之后可以参考先前在 12.6 Beta 提及的内容进行配置。

不知道是不是由于[从 NVIDIA
手中抢得大量订单](http://linuxtoy.org/archives/briefing-microsoft-canonical-nvidia.html)的关系，在**开源驱动方面**也有一些进展：

-   开源 2D 驱动 xf86-video-ati 发布**最后一个支持 UMS 的版本
    6.14.6**，之后的版本使用 **7.0 的分支，将仅支持
    KMS**。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTEyOTg)
-   一个适用于 Gallium3D Radeon 3D 开源驱动的补丁可以在不少情况下**提升
    OpenGL 性能约
    20%**。[消息来源](http://www.phoronix.com/vr.php?view=17560)
-   增加了大约有 2000 行的用于 Radeon
    内核驱动的文档说明，皆在帮助社区开发者尽快的了解 Radeon
    开源驱动。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTEzMDE)

