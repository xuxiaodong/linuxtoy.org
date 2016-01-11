Title: Linux Kernel 4.3
Author: lovenemesis
Date: 2015-11-02
Category: Kernel
Tags: kernel
Slug: linux-kernel-4-3
Summary: Linux 内核 4.3 版本正式发布，带来

详细的更新摘要尚未发布，来自 [Phoronix 的报道](http://www.phoronix.com/scan.php?page=article&item=linux-43-features&num=1)罗列了如下新特性：

* Intel Skylake 系列 CPU 支持
* Intel 下一代 Gen9 GPU 支持
* AMD Radeon Fury/Fiji 系列的开源驱动初步支持，不过由于尚未具备重调频支持，性能依然不及预期
* 重构了 Nouveau 驱动，为部分设备增添了重调频支持
* VMWare 现在支持 OpenGL 3.3
* Btrfs 文件系统的 RAID 5/6 改善，Ext3 的支持将转移给 Ext4 驱动向后兼容实现，以及其他 F2FS、Ext4 及 XFS 方面的错误修复

这一版内核依然没有包含争议颇多的 KDBUS，也没有太多新增功能。不过若是您拥有新款 Intel 处理器的话，升级到 Kernel 4.3 版本还是相当值得的。

[内核源代码下载](https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.3.tar.xz)
