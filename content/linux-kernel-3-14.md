Title: Linux Kernel 3.14
Date: 2014-03-31 14:24
Author: lovenemesis
Category: Kernel
Slug: linux-kernel-3-14

Linus 宣布 Kernel 3.14 版本发布，带来了 Deadline 调度器和 Broadwell
初步支持等新特性。

[新版本的详细更新日志](http://kernelnewbies.org/Linux_3.14)尚未就绪，根据
[Phoronix
的相关报道](http://www.phoronix.com/scan.php?page=news_item&px=MTYzNDg)，新特性有：

-   对 Intel Broadwell 和 GeForce 780/TITIAN 系列的初步支持，启用 AMD
    GCN 架构显卡的 UVD 硬件解码。
-   支持 AMD CPP 加密协处理器，支持 MIPS interAptiv 及 proAptiv
    设计，支持 Intel 新的移动处理器 Merrifield 。
-   将适用于实时操作领域的 Deadline 调度器合并入主线，改善了 CPUfreq
    的效率。
-   实现 TCP 自动封塞的功能。
-   改善了 F2FS 文件系统的性能，众多 Btrfs 文件系统优化，将 Sysfs 转变为
    Kernfs。

[邮件列表发布公告](http://lkml.iu.edu/hypermail/linux/kernel/1403.3/03023.html)

[官方源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.14.tar.xz)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTY0ODQ)
