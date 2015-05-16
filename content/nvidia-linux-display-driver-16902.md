Title: NVIDIA 发布 Linux 显卡驱动 169.12
Date: 2008-02-27 11:22
Author: toy
Category: Apps
Slug: nvidia-linux-display-driver-16902

NVIDIA 在今天面向 Linux
平台发布了一个新的显卡驱动程序──169.12。该驱动延续自上一次的
[169.09](http://linuxtoy.org/archives/nvidia-display-driver-updated-to-16909.html)，同属一个稳定系列。而中间出现的
[171.05](http://linuxtoy.org/archives/nvidia-releases-new-display-driver.html)
测试版，目前还没有下文。

![NVIDIA](http://i.linuxtoy.org/i/logo/nvidia.png)

此版本的显卡驱动程序主要改进了 GeForce 8 GPU
的电源管理支持和稳定性。同时，对于 GLX\_EXT\_texture\_from\_pixmap
的内存不足处理及 nvidia-xconfig 工具也有所改善。此外，一些 bug
也得到了修正。具体内容可以参考其[发布公告](http://www.nvidia.com/object/linux_display_ia32_169.12.html)。

你可以从这里[下载该版本的显卡驱动程序](http://us.download.nvidia.com/XFree86/Linux-x86/169.12/NVIDIA-Linux-x86-169.12-pkg1.run)
([64
位](http://us.download.nvidia.com/XFree86/Linux-x86_64/169.12/NVIDIA-Linux-x86_64-169.12-pkg2.run))。
