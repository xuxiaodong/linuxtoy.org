Title: Debian Lenny 终于到来
Date: 2008-12-18 19:45
Author: toy
Category: News
Tags: Debian, Lenny
Slug: debian-lenny-has-arrived

[撰文/yjwork]

经历了两天的无更新后，终于迎来了三个软件更新，其中包括 base-files
，其版本号为 5。base-files 是“Debian 基本系统文件，本软件包包含 Debian
系统的基本文件系统树和一些重要的文件，例如
/etc/debian\_version、/etc/host.conf、/etc/issue、/etc/motd、/etc/profile、/etc/nsswitch.conf
及其它文件，还包括 Debian 系统中常用的几种许可协议的文本。”

以下是相关输出信息：

debian:/home/yjwork# cat /etc/debian\_version  
5.0  
debian:/home/yjwork# uname -a  
Linux debian 2.6.26-1-amd64 #1 SMP Wed Nov 26 18:26:02 UTC 2008
x86\_64 GNU/Linux  
debian:/home/yjwork# cat /proc/version  
Linux version 2.6.26-1-amd64 (Debian 2.6.26-11) (waldi@debian.org) (gcc
version 4.1.3 20080623 (prerelease) (Debian 4.1.2-23)) #1 SMP Wed Nov
26 18:26:02 UTC 2008  
debian:/home/yjwork# cat /etc/issue  
Debian GNU/Linux 5.0 \\n \\l

debian:/home/yjwork# ls /boot  
config-2.6.26-1-amd64 initrd.img-2.6.26-1-amd64
System.map-2.6.26-1-amd64  
grub initrd.img-2.6.26-1-amd64.bak vmlinuz-2.6.26-1-amd64  
debian:/home/yjwork#

重启电脑后，你会发现，在终端的登录界面上出现的是：

Debian GNU/Linux 5.0 debian tty1

而以前是 Debian GNU/Linux lenny/sid debian tty1。

正在使用 Debian Lenny
测试版的同学可通过其内置的包管理工具更新。其他同学就等 Debian
官方的正式公布吧。
