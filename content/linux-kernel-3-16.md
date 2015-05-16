Title: Linux Kernel 3.16
Date: 2014-08-04 09:13
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-16

Linux 内核 3.16 正式发布，大幅提升了开源显卡驱动的支持和性能。

[根据 Phoronix
的报道](http://www.phoronix.com/scan.php?page=news_item&px=MTcyMDU)，新版本的变化有：

-   Nouveau 驱动得到强化，包括 Tegra K1 SoC 的 GPU 以及桌面 Kelper 核心
    GPU 的重调速(re-clocking)支持。
-   Intel 驱动支持用于 HiDPI 设备的高精度指针，增加 Cherryview
    支持，改善 Broadwell 性能。
-   Radeon 驱动实现了 GPU VM 及 PTE 优化，大幅度提升 GCN
    架构显卡性能，HDMI 输出支持 Deep Color 且优化音频输出。
-   ARM 增加了 64位 EFI 支持，且扩展了单一内核的支持芯片范围到 Exynos
    SoC。
-   改善了 S390, PowerPC, 和 MIPS 的芯片 KVM 支持，ARM Xen
    虚拟化支持挂起及恢复。
-   功能完备的 blk-mq 首次发布，降低延迟，平衡多核 CPU 的 I/O
    负荷，支持多硬件队列等方式提升 SSD 的性能。
-   针对 XFS、Btrfs、F2FS 文件系统的改良。

[详细更新摘要](http://kernelnewbies.org/Linux_3.16)尚未就绪。

[官方源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.16.tar.xz)
