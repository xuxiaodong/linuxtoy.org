Title: AMD 和 NVIDIA 显卡驱动双获更新
Date: 2007-12-21 11:29
Author: toy
Category: Apps
Slug: amd-and-nvidia-display-driver

最近，AMD 和 NVIDIA 针对 Linux
平台的显卡驱动程序先后获得了更新。其中，AMD 将旗下的 ATI Catalyst Linux
显卡驱动程序更新到了 7.12，而在 NVIDIA 这边也不肯示弱，继续推出了新的
169.07 测试版显卡驱动程序。

新版本的 ATI Catalyst 显卡驱动程序为 FireGL
V3600/V5600/V7600/V8600/V8650 系列的新产品提供了支持，并引入了对 RedFlag
DT 6.0、openSUSE 10.3 这两个 Linux
操作系统的支持。同时，这个版本还修复了当运行 OpenGL
应用程序时内存泄漏、执行 X -configure 时段错误及 fglrxinfo 报告 OpenGL
渲染字符串等问题。

不过，该 ATI Catalyst
版仍有一些已知问题存在，具体内容可以查看其[发布注记](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/catalyst_712_linux.html)。

ATI Catalyst 7.12 可用于 x86 和 x86\_64
架构，你可以从[这里获取其安装文件](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/ati-driver-installer-7-12-x86.x86_64.run)。

NVIDIA 的 169.07 测试驱动添加了对 GeForce 8800 GT、GeForce 8800 GTS 512
和 GeForce 8800M 的支持，在 .run 文件中添加了 CUDA 驱动，改进了
Quadro/GeForce 8 系列 GPU 及交互 DVI、HDMI 和 HDTV
的模式设置支持。同时，该版本也改进了热键切换支持、渲染性能、显示设备检测、NVIDIA-settings
的可用性、GLX visual consolidation 等等。

此外，NVIDIA 169.07 也修正了一些问题，包括 X
渲染问题、稳定问题等。你可以阅读[发布注记](http://www.nvidia.com/object/linux_display_ia32_169.07.html)了解详细情形。

NVIDIA 169.07
可从[这里下载](http://us.download.nvidia.com/XFree86/Linux-x86/169.07/NVIDIA-Linux-x86-169.07-pkg1.run)
([x86\_64](http://us.download.nvidia.com/XFree86/Linux-x86_64/169.07/NVIDIA-Linux-x86_64-169.07-pkg2.run))。
