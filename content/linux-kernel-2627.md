Title: Linux Kernel 2.6.27 发布
Date: 2008-10-10 10:20
Author: toy
Category: News
Tags: Kernel
Slug: linux-kernel-2627

Linux Kernel 2.6.27 稳定版已正式发布啦。与上一个版本
[2.6.26](http://linuxtoy.org/archives/linux-kernel-2626-final-is-out.html)
一样，2.6.27 也为各位 Linux 用户带来了许多突出的特性，主要有：

-   无锁（Lockless）页面缓存及 get\_user\_pages()
-   Ext4 添加了延时分配（Delayed Allocation）功能
-   Kexec jump：基于休眠的 kexec/kdump
-   UBIFS 与 OMFS：前者是为闪存设备设计的新文件系统，后者为 Sonicblue
    Optimized MPEG File System support 的简称
-   Block layer 数据完整性支持
-   多队列网络
-   ftrace、sysprof 支持
-   Mmiotrace
-   外置固件支持
-   改进了 gspca 驱动对视频摄像头的支持
-   可扩展的文件描述符系统调用
-   电压及电流调节器

此外，Linux Kernel 2.6.27 还为各种硬件设备提供了新的驱动，比如：Intel
wireless 5000 系列、RTL8187B 网卡、Atheros AR5008 及 AR9001
芯片系列等等。

Linux Kernel 2.6.27 的源代码及补丁可从 Kernel.org 网站获取。

[Linux Kernel 2.6.27](http://kernel.org/) [via [Linux Kernel
Newbies](http://kernelnewbies.org/Linux_2_6_27), thanks bingyuan!]
