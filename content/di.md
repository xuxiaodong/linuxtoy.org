Title: di: 查看磁盘使用情况
Date: 2012-12-26 15:10
Author: toy
Category: Cli
Slug: di

[di][d] 即 disk information
之意，利用它你可以查看挂载文件系统的磁盘使用情况。与 `df` 相比，`di`
的结果更为详细，同时你能对输出有更多控制，如过滤、排序等。另外，`di`
也支持检查用户及组配额。

**`di` 用法举例**

di -a # 查看所有挂载文件系统的磁盘使用情况

Filesystem Mount Size Used Avail %Used fs Type  
rootfs / 5.1G 2.4G 2.5G 52% rootfs  
/dev/mapper/debian / 5.1G 2.4G 2.5G 52% ext3  
/dev/sda1 /boot 227.7M 18.8M 196.8M 14% ext2  
udev /dev 10.0M 0.0M 10.0M 0% devtmpfs  
devpts /dev/pts 0.0M 0.0M 0.0M 0% devpts  
/dev/mapper/debian /home 13.7G 1.2G 11.8G 14% ext3  
none /home/xuxiaodon 0.0M 0.0M 0.0M 0% vboxsf  
none /media/sf\_wind 0.0M 0.0M 0.0M 0% vboxsf  
proc /proc 0.0M 0.0M 0.0M 0% proc  
tmpfs /run 101.0M 0.5M 100.5M 1% tmpfs  
tmpfs /run/lock 5.0M 0.0M 5.0M 0% tmpfs  
tmpfs /run/shm 202.0M 0.0M 202.0M 0% tmpfs  
sysfs /sys 0.0M 0.0M 0.0M 0% sysfs  
tmpfs /tmp 1000.0M 199.5M 800.5M 20% tmpfs  
rpc\_pipefs /var/lib/nfs/rp 0.0M 0.0M 0.0M 0% rpc\_pipefs

di -x proc,tmpfs,sysfs # 排除 proc、tmpfs、sysfs 等

Filesystem Mount Size Used Avail %Used fs Type  
rootfs / 5.1G 2.4G 2.5G 52% rootfs  
/dev/mapper/debian / 5.1G 2.4G 2.5G 52% ext3  
/dev/sda1 /boot 227.7M 18.8M 196.8M 14% ext2  
udev /dev 10.0M 0.0M 10.0M 0% devtmpfs  
devpts /dev/pts 0.0M 0.0M 0.0M 0% devpts  
/dev/mapper/debian /home 13.7G 1.2G 11.8G 14% ext3  
none /home/xuxiaodon 0.0M 0.0M 0.0M 0% vboxsf  
none /media/sf\_wind 0.0M 0.0M 0.0M 0% vboxsf  
rpc\_pipefs /var/lib/nfs/rp 0.0M 0.0M 0.0M 0% rpc\_pipefs

di -I ext3 # 只显示 ext3 文件系统

Filesystem Mount Size Used Avail %Used fs Type  
/dev/mapper/debian / 5.1G 2.4G 2.5G 52% ext3  
/dev/mapper/debian /home 13.7G 1.2G 11.8G 14% ext3

更多用法，可 `man di` 了解。

[d]: http://www.gentoo.com/di/
