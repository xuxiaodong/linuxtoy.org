Title: Linux Kernel 3.7
Date: 2012-12-11 16:29
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-7

Linus 刚刚宣布了 Linux 内核 3.7 版本的发布，本次升级带来了众多针对 ARM
平台的改善。

新版本的改善有：

-   改善了 Radeon 开源驱动的电源管理。
-   Intel 集显的模式设定部分得到重构。
-   增加对 64位 ARM 处理器 ARMv8 / AArch64 架构的支持。
-   在 ARM Cortex-A15 上支持 Xen 虚拟化。
-   允许构建适用于多个 ARM 设备的单一镜像。
-   优化了音频部分的电源管理，允许动态的休眠闲置控制器。
-   改善了 ext4 和 btrfs 文件系统，支持在 JFS 文件系统上运行 Trim 命令。

[参考更新内容](http://www.phoronix.com/scan.php?page=news_item&px=MTI0NzM)

[Kernel Newbies 详细内容(尚未更新)](http://kernelnewbies.org/Linux_3.7)

[内核源代码 XZ
压缩包下载](http://www.kernel.org/pub/linux/kernel/v3.x/linux-3.7.tar.xz)
