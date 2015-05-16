Title: Linux Kernel 2.6.25 发布
Date: 2008-04-17 14:26
Author: toy
Category: News
Tags: Kernel, Releases
Slug: linux-kernel-2625

Linux Kernel 2.6.25 已经正式发布。作为 Linux 系统的内核，Linux Kernel
的每一次版本更新都会带来大量新增特性。自然，Linux Kernel 2.6.25
也不例外。

![Linux Kernel](http://i.linuxtoy.org/i/logo/linux.jpeg)

根据 [Kernel Newbies](http://kernelnewbies.org/Linux_2_6_25)
网站的总结，Linux Kernel 2.6.25 主要包括以下重要特性：

-   支持新的 MN10300/AM33 架构
-   能够更精确的检测进程的内存占用
-   用于控制进程组内存占用的内存资源控制器 (Memory Resource Controller)
-   实时分组调度
-   检测系统传输延迟的工具
    [Latencytop](http://linuxtoy.org/archives/latencytop.html)
-   ACPI 热量调节
-   timerfd() 系统调用
-   MAC 安全框架 SMACK
-   EXT4 文件系统得到了更新BRK 和 PIE 可执行地址空间随机化
-   RCU preemption 支持
-   针对 x86 的 FIFO spinlocks 支持
-   针对 x86\_64 的 EFI 支持
-   支持新的 Controller area network (CAN) 网络协议

此外，Linux Kernel 2.6.25 还对 ATI r500 提供了 DRI/DRM
的初步支持，并改善了硬件支持，以及更新了各种设备的驱动。

Linux Kernel 2.6.25 的源代码及补丁文件可从 [Linux Kernel
Archives](http://kernel.org/) 网站下载。
