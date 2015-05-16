Title: Linux Kernel 3.11
Date: 2013-09-03 11:09
Author: lovenemesis
Category: Kernel
Slug: linux-kernel-3-11

Linux 内核 3.11 版本发布，带来了 Radeon 动态电源管理和 ARM
大内存页支持。

新内核带来的变化有

-   用于创建安全临时文件的标识位 `O_TMPFILE`。
-   实验性的 Radeon 显卡动态电源管理支持，需要传递 `radeon.dpm=1` 启用。
-   针对并行分布式文件系统 Lustre 的客户端支持。
-   初步支持 NFS 4.2 和具备 SELinux 标签的 NFS 分区。
-   详细的页面写入历史追踪。
-   ARM 大内存页支持，KVM 和 Xen 增加 ARM64 支持。
-   改善 SYSV IPC 消息队列扩展性。
-   允许应用程序请求低延迟网络 Polling
-   增加可压缩交换分区缓存 Zswap。

更多详情请参考 [Kernel Newbies](http://kernelnewbies.org/Linux_3.11)。

[内核源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.11.tar.xz)
