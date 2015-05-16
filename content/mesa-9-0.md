Title: Mesa 9.0
Date: 2012-10-09 10:54
Author: lovenemesis
Category: Drivers
Tags: Mesa
Slug: mesa-9-0

开源 3D 驱动集合 Mesa 正式发布 9.0 版本，带来了部分硬件的 OpenGL 3.1
支持。

本次大版本升级的亮点有：

-   Intel 驱动实现 OpenGL 3.1 支持，Radeon 和 Nouveau 正在跟进，预计在
    9.1 实现。
-   增加了对 Nvidia 老显卡的 NV30 驱动和对 Radeon HD 7000 系列 RadeonSI
    驱动。
-   将 Gallium3D OpenCL Tracker Clover
    合并入主干，不过成熟度尚不如闭源驱动。
-   Gallium3D VDPAU Trakcer 完善，可以使用显卡的 Shader 进行 MPEG1 和
    MPEG2 的硬件加速解码。
-   Radeon R600 Gallium3D 现在支持 MSAA 多重采样抗锯齿。

[邮件列表发布公告](http://lists.freedesktop.org/archives/mesa-dev/2012-October/028420.html)

即将在年底发布的 [Fedora 18 已经确定搭载 Mesa
9.0](https://apps.fedoraproject.org/packages/mesa)。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTIwMjE)
