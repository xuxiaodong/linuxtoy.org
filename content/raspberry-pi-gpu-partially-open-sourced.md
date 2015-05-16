Title: Raspberry Pi GPU 驱动部分开源
Date: 2012-10-25 13:14
Author: lovenemesis
Category: Drivers
Tags: arm, Raspberry Pi
Slug: raspberry-pi-gpu-partially-open-sourced

微型 ARM 电脑 Raspberry Pi 的 GPU 驱动开源了，至少部分是。

Raspberry Pi 基金会[今早宣布了旗下同名微型电脑所用 GPU Broadcom
VideoCore 4 驱动开源](http://www.raspberrypi.org/archives/2221)。

初来看着是个很好的消息，因为在 Linux 世界中能比桌面 x86/64 GPU
驱动还要糟糕的只有 ARM SoC 的 GPU 驱动了，Broadcom
此举无疑是为其他厂商如 Samsung 和 NVIDIA 树立了一个好榜样。目前**在 ARM
阵营中没有任何一家厂商提供开源驱动支持**，相比之下 x86 阵营的 Intel 和
AMD 对开源界简直太友好了。近年来由于 ARM
的流行，有了一些第三方逆向工程的 GPU
驱动，不过全部处于非常早期的试验阶段。

不过，貌似现实依然残酷。

来自 [Phoronix
的进一步报道](http://www.phoronix.com/scan.php?page=news_item&px=MTIxNDk)显示这个**所谓开源的驱动需要导入二进制的闭源固件/微代码才能使用**。

好吧，二进制固件/微代码在开源 GPU 驱动中也不算稀奇。有 AMD
官方支持的开源的 Radeon
驱动在运行时可以自动生成显卡所需的微代码，社区主导的 NVIDIA Nouveau
开源驱动在部分型号上则需要用户手动从官方闭源驱动提取固件。

只是这次 VideoCore 4 的闭源二进制固件/微代码甚至代劳了 OpenGL ES
的实现。意味着**开发者完全无法借助公开的 GPU 驱动改善 VideoCore 4 的
OpenGL ES 实现或者将其合并入 Mesa/Gallium3D 框架**。

如果 Raspberry Pi 基金会和 Broadcom 方面在 ARM GPU
驱动开源的止步于此，这种开源只能勉强评价为“聊胜于无”了。
