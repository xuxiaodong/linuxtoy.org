Title: 浅析三大主流显卡厂商对 Linux 的驱动支持
Date: 2012-06-27 17:21
Author: lovenemesis
Category: Drivers, Featured
Slug: compare-linux-driver-support-between-three-major-gpus

在挑选一台 Linux
兼容的电脑的时恐怕没有什么能比显卡更纠结了……本文将简要的比较 Intel、AMD
和 NVIDIA 显卡对于 Linux 的驱动支持情况。

以**常见的 i686/AMD64 架构**为例。

**Intel**

*开源驱动(以 Intel 2.19 Mesa 8.0.3 为例)*

**优点**

-   官方提供开源驱动支持。
-   对于最新产品的 0-day 支持。
-   不错的电源管理。
-   在 HD3000 及以后型号中通过 VAAPI 实现硬件解码支持。
-   在绝大多数发行版中开箱即用，无需额外配置。

**缺点**

-   性能大约只有 Win 平台的 80%。
-   没有 OpenCL 支持。
-   HDMI 输出在部分设备上存在问题。
-   并未使用新的 Gallium3D
    通用驱动架构，将吸收来自其他开源驱动方面进步上会有难度。
-   注意：早期上网本中配备的贴牌 Intel 显卡实为 PowerVR 的产品，Linux
    驱动情况糟糕，慎重选购。

*Intel 没有提供闭源驱动（PowerVR 的除外）*

*适用人群*：仅需要基本混成式桌面和上网需求的人群，由于 HDMI
的问题并不适合用作 HTPC。

**AMD**

*闭源 Catalyst 驱动（以当下最新的 [12.6 Beta
版本](http://linuxtoy.org/archives/amd-catalyst-12-6-beta.html)为例）*

**优点**

-   提供和 Win 平台几乎相近的性能。
-   对于最新产品的 0-day 支持。
-   提供对独立显卡和内置显卡的切换技术 PowerXpress 支持。
-   对具备 UVD2 以上显卡通过 XvBA 提供硬件解码支持。
-   对于 OpenCL 标准支持优秀。
-   具备较为齐全的调频调温及超频工具。

**缺点**

-   对于新版本 Kernel 和 X.org 支持的速度慢半拍。
-   当下直接调用 XvBA 实现硬件解码的程序有限（仅 [Fluendo
    Codec](http://linuxtoy.org/archives/fluendo-codec-pack-and-gstreamer-hardware-va-briefing.html)
    和
    [XBMC](http://www.phoronix.com/scan.php?page=news_item&px=MTAyODU)
    两个）。
-   当下 XvBA 不支持 H264 Level 5.1 的视频。
-   对于部分通过 Wine 运行的 3D 游戏兼容性不佳。
-   不再对 HD5000 之前的显卡提供支持。
-   目前不支持 KMS，短期内 Wayland 无望。

*开源驱动(以 ATI 6.14.4 Mesa 8.0.3 为例)*

**优点**

-   官方提供开源驱动支持。
-   具备一定的电源管理能力。
-   稳定的 HDMI 视频输出。
-   各种开源驱动新进展的试验场，比如 OpenCL、XTracker、VDPAU Tracker
    等。

**缺点**

-   性能仅有闭源 Catalyst 驱动的 20%～50% 左右。
-   对于最新发布的硬件尚不支持，需约半年左右。
-   动态电源管理存在闪屏缺陷。
-   部分功能如 HDMI 音频输出、PCI-E 2.0 和 HyperZ
    支持需要修改内核引导行才能启用。
-   不支持使用 UVD 组件进行硬件解码(仅能通过 Shader)。

*适用人群：*开源技术爱好者，OpenCL 开发者。若是用于游戏的话建议查询 Wine
的应用程序兼容性。

**NVIDIA**

*闭源驱动(以 [302.17
版本](http://linuxtoy.org/archives/briefing-about-nvidia.html)为例)*

**优点**

-   提供和 Win 平台几乎相近的性能。
-   对于最新产品 0-Day 支持。
-   对具备 PureVideo HD 的显卡通过 VDPAU 实现硬件解码支持。
-   存在大量支持通过 VDPAU 硬件解码程序，包括 Adobe Flash。
-   对于新内核和 X.org 支持响应及时。
-   绝佳的 CUDA 支持。
-   良好的 Wine 游戏支持。
-   对老显卡依然提供针对新内核和 X.org 的支持更新。

**缺点**

-   官方不支持独立显卡和内置显卡的切换暨 Optimus
    技术，需寻求社区解决方案 Bumblebee。
-   使用 PulseAudio 时需要手动配置 HDMI 音频输出。
-   不具备调频超频功能。
-   OpenCL 的性能和支持慢半拍。
-   恐怕永远都不会支持 KMS，Wayland 无望。

*开源驱动(以 Nouveau 0.16 Mesa 8.0.3 为例)*

**优点**

-   偶尔能带来些惊喜，比如对于 Kepler 核心显卡的支持。

**缺点**

-   没有任何来自官方的文档和支持，通过逆向工程得来，仅有一名来自 Red Hat
    全职开发者。
-   对于各代显卡的支持情况不稳定。
-   部分显卡需要手动从闭源驱动中提取 Firmware。
-   性能仅为闭源驱动的 20%～30%。
-   基本等同于没有的电源管理。
-   不具备 HDMI 音频输出功能。
-   不支持通过 PureVideo HD 实现硬件解码。

*适用人群*：高清视频爱好者，3D 游戏爱好者，CUDA 开发者。

希望本文能给正在选购显卡的朋友一个参考，正是因为没有完美的 Linux
驱动支持，所以更要**依据自身的需求理性选择并安装对应驱动程序**。
