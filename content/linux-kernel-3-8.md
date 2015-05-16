Title: Linux Kernel 3.8
Date: 2013-02-19 11:00
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-8

Linux 内核 3.8 发布，带来了新的针对固态硬盘设计的文件系统 F2FS。

新内核带来的功能和改善有：

-   Ext4 文件系统现在允许在 inode 中保存超小文件，可节省 1%～3%
    左右的磁盘空间。
-   Btrfs 文件系统新增专门的磁盘替换命令，大幅度加快的转换速度。
-   新增针对固态硬盘设计的文件系统 F2FS，更多的利用了 FTL 带来的优势。
-   允许非特权用户安全的查看并使用进程专属命名空间。
-   XFS 文件系统增加日志校验和。
-   内存 Huge Page 增加全零页支持。
-   内存控制器增加内核内存使用审计功能，允许设定命中上限。
-   自动化 NUMA 平衡，更好的利用距离处理器最近的缓存。
-   停止对于 386 处理器的支持。
-   真正实现 CPU 热拔插。
-   改善了开源显卡驱动的性能。

[Kernel Newbies 详细介绍](http://kernelnewbies.org/Linux_3.8)

[官方源代码包下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.8.tar.xz)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTMwNTQ)
