Title: Linux Kernel 2.6.37
Date: 2011-01-05 18:36
Author: lovenemesis
Category: News
Tags: Kernel
Slug: linux-kernel-2637

Linux 内核 2.6.37 发布，带来 **Ext4 性能提升**及 **I/O 节流控制**支持。

-   Ext4 文件系统**默认使用Block I/O
    模式**，实现更好的多核系统扩展支持；同时延期创建节点列表，提高文件系统创建速度。
-   XFS 文件系统扩展性提升。
-   全面移除[BKL (Big Kernel
    Lock)](http://en.wikipedia.org/wiki/Giant_lock)，允许编译一个完全没有
    BKL 的内核。
-   为 Ceph 分布式网络文件系统引入 RBD(Rados block
    device)从而实现类似块设备的功能。
-   **I/O节流阀支持**：允许为一个或一组进程指定可以使用的最大的 I/O 值。
-   "Jump label"：被禁用的静态跟踪点将不会对性能产生任何影响。
-   Btrfs
    更新：支持将空闲空间缓存到硬盘上，支持异步建立快照，快分配时支持元数据及数据混合。
-   提升了 Perf 的探测能力。
-   电源管理改善：休眠景象的 LZO 压缩及设备延迟挂起支持。
-   支持 PPP over IPv4：显著提升 PPTP VPN 的连接速度，并大幅度降低 CPU
    占有率。

详情请参考 [KernelNewbies](http://kernelnewbies.org/Linux_2_6_37)

*消息来源：*[LWN](http://lwn.net/Articles/421638/)
