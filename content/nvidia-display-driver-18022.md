Title: NVIDIA 发布 Linux 显示驱动 180.22
Date: 2009-01-09 09:38
Author: toy
Category: Drivers
Tags: NVIDIA
Slug: nvidia-display-driver-18022

NVIDIA 已经发布了一个新的 Linux 显示驱动，其版本号为
[180.22](http://www.nvidia.com/object/linux_display_ia32_180.22.html)。这是
180 系列的第一个稳定版驱动，适用于 32 位和 64 位 Linux 平台。

NVIDIA 180.22 主要包括以下改进和增强：

-   添加了对 Quadro FX 2700M、GeForce 9400M G、GeForce 9800 GT、GeForce
    9800 GT、GeForce 8200M G、GeForce Go 7700、GeForce 9800M
    GTX、GeForce 9800M GT、GeForce 9800M GS、GeForce 9500 GT、GeForce
    9700M GT、GeForce 9650M GT、GeForce 9500 GT 等系列 GPU 的支持。
-   通过新 VDPAU API，添加针对类似 PureVideo 功能的原生支持。
-   添加针对 CUDA 2.1 的支持。
-   添加针对 OpenGL 3.0 的初级支持。
-   添加新的 OpenGL 工作站性能优化程序。
-   默认状态下自动开启 glyph 缓存，并使之支持所有可支持的 GPU。
-   默认状态下自动关闭存储 X pixmap。
-   添加针对 SDI 全范围色彩的支持。

此外，该版本还改善了驱动的稳定性及与 Linux
内核的兼容性，并修正了一些缺陷。

[NVIDIA 180.22 32
位](http://us.download.nvidia.com/XFree86/Linux-x86/180.22/NVIDIA-Linux-x86-180.22-pkg1.run)
& [64
位](http://us.download.nvidia.com/XFree86/Linux-x86_64/180.22/NVIDIA-Linux-x86_64-180.22-pkg2.run)
