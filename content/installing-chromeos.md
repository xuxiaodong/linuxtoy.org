Title: 安装 ChromeOS 至本地硬盘
Date: 2009-12-09 14:51
Author: toy
Category: Tips
Tags: ChromeOS
Slug: installing-chromeos

{ 撰文/[yang](http://www.sgtalk.cn) }

先[编译镜像](http://www.sgtalk.cn/656868.html)，编译完后，挂载编译好的  
rootfs.image，然后开始后续的工作了。

分出两个空闲的 ext3 分区，分别设置卷标为
C-STATE（hd0,7）、C-ROOT（hd0,8），第一个是 home
目录（可写），第二个是根目录。将挂载的 rootfs.image 下面的文件通通拷贝到
C-ROOT 下面，然后再将其中的 home 目录拷贝到 C-STATE 下面。ChromeOS
系统已经被我们写入到物理磁盘中了，然后我们再用 GRUB 来引导，下面：

[bash]  
title chrome OS-fix  
root (hd0,8)  
kernel /boot/vmlinuz init=/sbin/init boot=local rootwait
root=LABEL=C-ROOT ro noresume noswap i915.modeset=1 loglevel=1  
initrd /boot/initrd.img  
[/bash]

上面的引导实际上是根据 rootfs.image/boot/extlinux.conf 来写的。

OK，现在重启系统，就可以从 GRUB 来启动本地磁盘中的 ChromeOS
了。其实先不着急重启，我们可以顺便修改下网络，因为像我这里上网并不是
DHCP 分配 IP 的，而需要手动设置，不然只能登录毫无意义的脱机用户了。正如
ChromeOS 是基于 Debian 的，可以直接修改 /etc/network/interfaces
文件，顺便修改 /etc/resolv.conf，添加 DNS。另外，也可以[修改下默认的 GTK
主题](http://www.sgtalk.cn/656972.html)，直接修改
/etc/gtk2.0/gtkrc。如果需要安装部分软件包，请直接 chroot 进入，然后
dpkg。

以上仅供测试。

补充，根目录是只读系统，可能是 Google
为了防止用户糟蹋乱了系统的缘故？就好像把 Debian 5.0 升级到 Ubuntu 9.10
一样？home 目录是可写的，但在 U
盘中却会重启后清理干净，本地磁盘不会。还有就是，无法挂载 NTFS。

{ [Source](http://www.sgtalk.cn/657020.html). Thanks yang. }
