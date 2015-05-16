Title: 如何在 Ubuntu 启用 Radeon 开源驱动的 UVD 硬件解码(补充)
Date: 2013-04-19 13:48
Author: liangsuilong
Category: Movie Player, Tutorials
Tags: AMD, radeon, Ubuntu
Slug: how-to-useopen-source-radeon-uvd-on-ubuntu

Phoronix 今天公布了在 Ubuntu 启用 Radeon 开源驱动 UVD 硬件解码的方法。

首先，你需要一块 Radeon HD 4000
系列或更新的显卡。然后，可以按照以下步骤逐步安装：

-   安装 VPDAU 的头文件：`sudo apt-get install libvdpau-dev`
-   从[Mesa 的 Git
    仓库](http://cgit.freedesktop.org/mesa/mesa/)抓取最新代码，加上` --with-gallium-drivers=r600 --enable-vdpau `
    编译参数进行编译安装。
-   在 `/etc/ld.so.conf.d/z.conf` 加上 `/usr/local/lib/vdpau`
    参数，没有这个配置文件可自行创建，然后执行 ldconfig 命令。
-   安装 drm-next 分支的 3.10 内核，可以从 Ubuntu Mainline Kernel PPA
    下载安装。[下载地址](http://kernel.ubuntu.com/~kernel-ppa/mainline/drm-next/2013-04-18-raring/)
-   下载 GPU 对应型号的 UVD Firmware 并放入到 `/lib/firmware`
    目录，若不清楚显卡型号，可以全部下载。[下载地址 ](http://people.freedesktop.org/~agd5f/radeon_ucode/)
-   重启电脑，选择新内核进入系统。
-   使用兼容 VDPAU 接口的播放器进行播放即可。

提示一：Linux 版本的 Flash Player 是通过 VDPAU 获得 GPU
硬件解码的，理论上 Flash Player 也可以利用 UVD 进行播放视频。

提示二：其他发行版可以参考以上指南，根据实际环境配置和调整。

结合早前 Phoronix 进行的[Radeon Gallium3D
性能测试](http://www.phoronix.com/scan.php?page=article&item=amd_linux_april2013&num=1)，AMD
的 Radeon 开源驱动进展良好，某程度上开源驱动和 Catalyst
闭源驱动的差距越来越小。有组建 Linux HTPC
的朋友可以考虑一下。使用笔记本的朋友，还是先安抚一下电池君，给多一点耐心吧。

[Phoronix
原文链接](http://www.phoronix.com/scan.php?page=news_item&px=MTM1NDk)

补充：

1. 在  Ubuntu 13.04 AMD64 里，Radeon 的内核 Firmware 应该放在
`/lib/firmare/radeon` 目录内，否则会在开机启动引导的时候出线无法加载 UVD
Firmware 的错误，进入系统后也无法使用 UVD 播放视频。

2. 在 Core 2 Duo E6420 和 4GB 内存下，使用 CPU 软解播放 Transformer
Prime 拍摄w的码率为约 16Mbps 的 1080P H.264 视频，CPU 占用了
60%～80%。在使用 Radeon HD 5550 的 UVD 硬解下，mplayer 只占用不超过 5%
的 CPU 资源。另外一个 40Mbps 的 1080P H.264 视频，硬解下 CPU
依然占用不到 5%。不过在 UVD 硬解下，拖动视频可能会导致 mplayer
卡住和崩溃。这可能是内核和 Mesa 的 Bug，等待正式版本时修复。

[![](http://lt-file.b0.upaiyun.com/files/2013/04/amd-uvd-vdpau-300x168.png)](http://lt-file.b0.upaiyun.com/files/2013/04/amd-uvd-vdpau.png)
