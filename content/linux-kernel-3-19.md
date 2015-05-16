Title: Linux Kernel 3.19
Date: 2015-02-09 13:19
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-19

Linux 内核 3.19 如约而至，带来 AMD HSA 初步支持及 Btrfs RAID 5/6 改善。

目前 Linus 本人尚未在邮件列表中发出更新摘要，不过根据
[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Linux-3.19-Kernel-Features)的报道来看，新版本的改善有：

* 收录 AMDKFD 驱动，配合用户态程序可以实现 AMD 异构计算支持。  
* Intel Skylake GPU 的初步支持  
* 为 AMD Radeon 开源驱动增加动态风扇转速调节支持  
* GeForce 900 系列的初步支持，不过仅是能识别了，尚无任何加速支持  
* Btrfs RAID 5/6 的改善  
* SquashFS 增加 LZ4 压缩支持  
* 为多种触控板增加多点触控支持

[官方源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.19.tar.xz)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Linux-3.19-Kernel-Released)
