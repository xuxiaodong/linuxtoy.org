Title: NVIDIA Linux x86 Display Driver 1.0-9629
Date: 2006-11-08 09:02
Author: toy
Category: Apps
Slug: nvidia_1_0

[用于 Linux x86 平台的 NVIDIA 显示驱动程序
1.0-9629](http://www.nvidia.com/object/linux_display_ia32_1.0-9629.html)
于昨日发布，让我们来看看本次发布的主要亮点都有哪些？

-   增加了对于 GLX\_EXT\_texture\_from\_pixmap 的初步支持；
-   在 nvidia-settings 程序中新增了“显示配置”页；
-   改进了 Xinerama 中 OpenGL 的工作性能；
-   添加了针对 NVIDIA Quadro Plex 和 Quad SLI 的支持；
-   改进了 X 驱动错误恢复能力；
-   改进了 overlay 的工作性能；
-   增加了 SMBus 功能到 Linux/i2c 接口；
-   修正了 DFP 缩放支持的问题；
-   增加了对于 OpenGL 2.1 的支持；
-   新增了 TwinViewXineramaInfoOrder X 配置选项以便控制 TwinView
    中的显示设备次序；
-   修正了某些 TV 输出的相关问题；
-   新增了 NVIDIA 标志到 nvidia-settings 程序中，及 X 驱动程序闪屏，且在
    X 配置选项中可以使用新的 LogoPath 进行配置。

该驱动程序可从[这里](http://download.nvidia.com/XFree86/Linux-x86/1.0-9629/NVIDIA-Linux-x86-1.0-9629-pkg1.run)下载，并使用
`sh NVIDIA-Linux-x86-1.0-9629-pkg1.run` 安装。
