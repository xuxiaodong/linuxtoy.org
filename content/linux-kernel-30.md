Title: Linux Kernel 3.0
Date: 2011-07-22 14:27
Author: lovenemesis
Category: Apps
Tags: Kernel
Slug: linux-kernel-30

Linus 正式宣布 Linux Kernel 3.0 版本正式发布。

新功能有：

-   Btrfs：实现自动碎片整理、数据校验和检查，并且提升了部分性能。
-   添加 sendmmsg()：提升约 UDP 发送性能 20%，接口发送性能 30%。
-   XEN dom0 支持。
-   增加 Cleancache 支持，
-   Berkeley 即时包过滤器，配合 libpcap/tcpdump
    提升包过滤规则的运行效率。
-   支持通过 WLAN 唤醒。
-   实现非特殊授权的 ICMP\_ECHO (ping 命令)。
-   setns() syscall 更好的命令空间处理。
-   添加 Alarm-timers，具有高精度计时器的特点，但是可以在通过 RFC
    设备唤醒挂起状态的系统。

[英文详细介绍](http://kernelnewbies.org/Linux_3.0)
