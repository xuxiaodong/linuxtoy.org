Title: Linux Kernel 3.15
Date: 2014-06-09 14:42
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-15

Linux 内核 3.15 版本刚刚发布，带来更快的唤醒时间及初步 LLVM 支持。

新版本的详细发布日志尚未就绪，从目前得知的改善有：

-   处理器方面增加对使用 CPS 系统的 MIPS 架构处理器支持。
-   音频方面增加对使用 Intel Smart Sound Technology 的等设备的支持。
-   网络方面增加对 Realtek RTL8723AU/RTL8723BE 无线网卡的支持。
-   KGDB 现在支持 ARM64 架构。
-   大幅度降低在使用 SATA
    驱动器的情况下系统从待机唤醒的时间，试验中单驱动器配置可缩减至 1
    秒钟。
-   合并部分支持 LLVM 编译的补丁，更多将随着下一个 3.16 版本合并。

[详细 Kernel Newbies
说明（尚未就绪）](http://kernelnewbies.org/Linux_3.15)

[官方源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.15.tar.xz)
