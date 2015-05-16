Title: NVIDIA 290.03 Beta 驱动
Date: 2011-10-23 12:00
Author: lovenemesis
Category: Drivers
Tags: NVIDIA
Slug: nvidia-29003-beta-driver

NVIDIA 发布闭源二进制显卡驱动发布了290.XX 系列首个版本：
290.03，增加了可以关闭显卡加速的选项以及对于 GeForce 510 的支持。

主要改动有：

-   修正了部分包含集成显卡的系统上无法载入的情况。
-   增加了 "Accel" 选项，从而可以关闭显卡的 GPU 图形加速功能，将其保留给
    CUDA 等需要独占 GPU 的任务。
-   增加了 "GLShaderDiskCache" 选项，通过将编译过的 OpenGL Shaders
    缓存到磁盘的方式提升性能。
-   修正了在 x server 1.11 下老型号的 GPU 绘制梯形和三角形缓慢的错误。

[32位版本](ftp://download.nvidia.com/XFree86/Linux-x86/290.03/)

[64 位版本](ftp://download.nvidia.com/XFree86/Linux-x86_64/290.03/)

[详细内容](http://phoronix.com/forums/showthread.php?63584-290.03-%28beta%29-for-Linux-x86-x86_64-released)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTAwNDU)
