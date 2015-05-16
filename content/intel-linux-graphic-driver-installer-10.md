Title: Intel Linux 显卡驱动安装器 1.0
Date: 2013-03-12 13:38
Author: lovenemesis
Category: Drivers
Tags: Intel
Slug: intel-linux-graphic-driver-installer-10

一直以来升级 Intel 开源显卡驱动都要涉及包括内核、DRM 库、Mesa 和 X.org
DDX 驱动等多个组件，其复杂程度程度甚至超越闭源显卡驱动升级。Intel
开源技术中心近日放出了适用于旗下显卡的驱动安装器，希望能简化该过程。

由于开源驱动涉及组件过多且分散，用“牵一发而动全身”形容毫不夸张。因此非滚动发行版都只在新版发布时提供开源驱动更新，绝少为已发布版本升级开源驱动。

Intel 此次提供的安装器实际上是一个针对**当下活跃的已发布 Linux
发行版本最新显卡驱动及其相关组件的仓库**。目前支持 Fedora 17/18，Ubuntu
12.04/12.10 发行版。

安装完成后可以在应用程序列表找到对应项，或者在终端运行：

`intel-linux-graphics-installer`

[官方下载](https://01.org/linuxgraphics/downloads/2013/intel-linux-graphics-installer)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTMyNDQ)
