Title: Raspberry Pi 2 获得试验性 VC4 开源驱动支持
Author: lovenemesis
Date: 2016-02-11
Category: Embedded
Tags: raspberrypi2
Slug: raspberrypi2-gets-experimental-vc4-opensource-driver-support
Summary: 近日适用于树莓派的 Linux 发行版 Raspbian 发布了新版本，包含了试验性的 VC4 开源驱动支持，意味着树莓派上可以有 OpenGL 加速了。

如果您跟进本站关于内核方面的报道的话，便会知道 Raspberry Pi 所用 GPU 的开源驱动方面在最近一两年进展喜人。KMS 的支持能合并入主线的一大要求便是要有用户态对应的驱动可用，Raspbian 的最新版本便搭载了启用 VC4 开源驱动的 Mesa 11.1 版本。终于，Raspberry Pi 有和其他 PC 平台 Linux 桌面版相符的 OpenGL 加速支持了。

根据 [Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=Trying-VC4-On-Raspbian-RPi2)的报道来看，打开此试验性支持仅需要升级下 Raspbian 并在 `rpi-config` 工具中启用即可，重启后便可以在 `glxinfo` 汇报其支持 OpenGL 2.1 版本。不过至少在现阶段，该试验性支持会导致相机模块异常，且无法调用 GPU 硬件 H264 解码。

目前笔者正在更新手头的 Raspbian ，稍后更新体验。注意目前**仅适用于 Raspberry Pi 2**，不支持 Raspberry Pi 1 代和 Zero 。

[Raspbian 最新版下载](https://www.raspberrypi.org/downloads/raspbian/)

*消息来源*:[TweakTown](http://www.tweaktown.com/news/50280/raspberry-pi-gets-experimental-gpu-acceleration-games-now-playable/index.html?utm_campaign=trueAnthem:+Trending+Content&utm_content=56bc815f04d3011aa27c89b3&utm_medium=trueAnthem&utm_source=twitter)


