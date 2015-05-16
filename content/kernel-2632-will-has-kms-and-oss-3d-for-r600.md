Title: Kernel 2.6.32 将包含 R600 系列显卡 KMS 及开源 3D 加速支持
Date: 2009-09-09 10:33
Author: lovenemesis
Category: Drivers
Tags: drm, radeon
Slug: kernel-2632-will-has-kms-and-oss-3d-for-r600

来自 [Phoronix
消息](http://www.phoronix.com/scan.php?page=news_item&px=NzUxNg)表明，Linux
Kernel 2.6.32 将包括 AMD R600 系列显卡的 KMS 和开源 3D 支持。

开发者 David Airlie 在其个人博客上公布了关于即将进入 Kernel 2.6.32 的
DRM 模块的新消息。他在文中表明提到这个新的 DRM 模块允许 R600 系列显卡在
KMS 下获得完整的 2D/3D/Xv 加速和 DRI2，前提是同时拥有最新的 libdrm、ati
DDX 驱动和 Mesa。

此外，本次 DRM 还带了诸如 R128 系列固件载入和 KMS 支持、更好的 HDMI EDID
和 KMS 下 TV-out 输出支持等改进。

另外，在博客中还透露预计于12月初发布的 Fedora 12 将通过 Backport
的方式获得此 DRM 模块。  
好消息是届时 R600 系列显卡的 Fedora 粉丝可以提前获得 KMS 支持，坏消息是
R600 系列的 3D 加速由于 Mesa 和驱动的问题恐怕还要等待一段时间……

[Phoronix
原文](http://www.phoronix.com/scan.php?page=news_item&px=NzUxNg)  
[David Airlie 博客](http://airlied.livejournal.com/68097.html)
