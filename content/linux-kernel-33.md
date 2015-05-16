Title: Linux Kernel 3.3
Date: 2012-03-19 14:06
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-33

Linux 内核 3.3 发布，重新融合了来自 Android 的大量代码。

主要变化有：

-   合并了大量来自 Android
    内核分支树的代码和功能，未来还会继续。[本站过往报道](http://linuxtoy.org/archives/android-linux.html)
-   改善了 Btrfs 文件系统对 RAID 配置下的支持，增加了完整性除错工具。
-   合并 Open vSwitch 多层网络交换架构。
-   新的 teaming 网络接口，用于提供在用户态更简洁的以太网端口合并方式。
-   引入 Bufferbloat
    技术，尝试缓解在存在多层缓冲的情况下高速网络连接的数据包处理延迟问题。
-   允许针对某个控制组的进行 TCP 缓存限制。
-   增加网络优先级控制组。
-   更快更好的 Ext4 文件系统大小热缩放。
-   增加对德州仪器 C6X 架构的支持。
-   在 EFI 系统上支持直接引导。

驱动方面：

-   增加 ARMv7 上对大内存的 PAE 支持。
-   增加对 Intel 上网本系列所用 GMA500 系列显卡的支持。
-   增加对 iPhone 4S 的 USB 支持。
-   增加大量三星 Exynos4 相关驱动支持。

[更新详情](http://kernelnewbies.org/Linux_3.3)
