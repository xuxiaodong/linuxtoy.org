Title: X.Org 7.4 正式发布
Date: 2008-09-24 08:35
Author: toy
Category: News
Tags: X.Org
Slug: xorg-74

X.Org 是 X Window System 的开源实现版本，它支持 Linux、Solaris、以及 BSD
平台。X.Org 新的 7.4
版在今天得以正式发布。该版本加入了一些新的功能，并对原有的模块、输入和显示驱动进行了更新。与此同时，xorg-server
也发布了新的 1.5.1 版。

X.Org 7.4 的主要更改情况如下：

-   PciReworkProposal：使用 libpciaccess 替换了 PCI bus
    scanning/accessing 代码。
-   x11perf 1.5：添加了混合测试功能。
-   xtrans 1.1：在 Linux 下支持抽象套接字命名空间。
-   xf86-input-evdev 2.0.x：支持更广泛的设备，修正了稳定性方面的问题。
-   xf86-video-ati 6.9.x：添加了对 r5xx/r6xx/r7xx (RadeonHD
    1xxx/2xxx/3xxx) 设备的支持。另外，r5xx 支持纹理视频。所有芯片都支持
    RandR 1.2。
-   EXA：在速度上有所提升。
-   libX11 1.1.5：加入了更多国际化支持。
-   xorg-server 1.5：启动和关闭更快，EDID 1.4，安全的 RPC 认证，针对
    Xephyr 的 GLX 和 DRI passthrough 支持，更智能的自动配置，XACE
    安全框架，等待。

有关 X.Org 7.4
更详细的信息，可以查看其[发布注记](http://xorg.freedesktop.org/wiki/Releases/7.4)。

[X.Org 7.4](http://xorg.freedesktop.org/releases/X11R7.4/)
