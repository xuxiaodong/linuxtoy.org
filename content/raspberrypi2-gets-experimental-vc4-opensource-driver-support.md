Title: Raspberry Pi 2 获得试验性 VC4 开源驱动支持
Author: lovenemesis
Date: 2016-02-11
Category: Embedded
Tags: raspberrypi2
Slug: raspberrypi2-gets-experimental-vc4-opensource-driver-support
Summary: 近日适用于树莓派的 Linux 发行版 Raspbian 发布了新版本，包含了试验性的 VC4 开源驱动支持，意味着树莓派上可以有 OpenGL 加速了。

如果您跟进本站关于内核方面的报道的话，便会知道 Raspberry Pi 所用 GPU 的开源驱动方面在最近一两年进展喜人。KMS 的支持能合并入主线的一大要求便是要有用户态对应的驱动可用，Raspbian 的最新版本便搭载了启用 VC4 开源驱动的 Mesa 11.1 版本。终于，Raspberry Pi 有和其他 PC 平台 Linux 桌面版相符的 OpenGL 加速支持了。

根据 [Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=Trying-VC4-On-Raspbian-RPi2)的报道来看，打开此试验性支持仅需要升级下 Raspbian 并在 `rpi-config` 工具中启用即可，重启后便可以在 `glxinfo` 汇报其支持 OpenGL 2.1 版本。不过至少在现阶段，该试验性支持会导致相机模块异常，且无法调用 GPU 硬件 H264 解码。

注意目前**仅适用于 Raspberry Pi 2**，不支持 Raspberry Pi 1 代和 Zero 。

更新下体验：

1. 对于老版本用户来说，除了更新以外，在 `rpi-config` 中启用加速时还需要安装 `libgl1-mesa-dri` 及 `xcompmgr` 两个安装包
2. 安装后需要重启，不过至少本人的测试中重启的意思其实是断电重启动……
3. 具体应用场景中 Iceweasel 汇报有 Basic 加速了，WebGL 渲染器也被识别
4. GNOME 3 的应用在非全屏状态下的阴影显示不正常


[Raspbian 最新版下载](https://www.raspberrypi.org/downloads/raspbian/)

*消息来源*:[TweakTown](http://www.tweaktown.com/news/50280/raspberry-pi-gets-experimental-gpu-acceleration-games-now-playable/index.html?utm_campaign=trueAnthem:+Trending+Content&utm_content=56bc815f04d3011aa27c89b3&utm_medium=trueAnthem&utm_source=twitter)


