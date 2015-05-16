Title: Linux Kernel 3.18
Date: 2014-12-08 15:29
Author: lovenemesis
Category: Kernel
Tags: Kernel
Slug: linux-kernel-3-18

代号 “Diseased Newt” 的 Linux 内核 3.18
发布，带来了开源显卡驱动的重调频改善。

详细的[更新日志](http://kernelnewbies.org/Linux\_3.18)尚未就绪，[大略更新亮点](http://www.phoronix.com/scan.php?page=news\_item&px=MTg1NjA)有：

* 针对早期 Radeon R600 系列集成显卡的 UVD1 硬件解码支持。

* 针对 R9 290
系列的显卡重调频支持，解决过去由于主频过低导致的性能问题。

* Nouveau 驱动添加 DisplayPort 音频输出支持，并进一步优化重调频。

* 大幅缩短在多 CPU 节点情况下的从休眠到唤醒的时间。

* 改善 Btrfs 及 F2FS 文件系统，收录 OverlayFS。

[源代码包下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.18.tar.xz)

[邮件列表发布公告](http://lkml.iu.edu/hypermail/linux/kernel/1412.0/05308.html)

*消息来源*：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTg1NjY)
