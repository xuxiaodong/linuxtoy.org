Title: Arch Linux 2011.08.19 安装介质
Date: 2011-08-20 20:34
Author: cheer_xiao
Category: Distros
Tags: Archlinux
Slug: archlinux-2011-08-19

15 个月之后，极简主义哲学的滚动发行版 Arch Linux 发布了新版的安装介质。

发布的直接原因是 Linux 内核包的 kernel 和 initramfs
[文件名改动](http://www.archlinux.org/news/changes-to-kernel-package-and-filenames/)导致原来的安装介质不能正常网络安装了。以下译自官方发布公告，翻译不完整。

本次主要带来以下新特性：

[AIF](http://projects.archlinux.org/aif.git/) (ArchLinux Installation
Framework):

-   对 Btrfs 和 NILFS2 的实验性支持
-   支持 syslinux 作为 bootloader 选项。Grub 依然支持，Don't panic :)
-   新的配置文件格式，以支持新的 rc.conf 和 linux 3.0
-   选择安装源更加灵活（支持多个本地/远程仓库作为安装源）
-   安装包的时候显示包的描述信息
-   默认开启调试和日志。增加了脚本 /arch/report-issues
-   移除了 tcp\\\_wrappers 的支持。

[Archiso](http://projects.archlinux.org/archiso.git/) (Arch 安装镜像):

-   使用当前 [core] 中的包：kernel 3.0.3-1, pacman 3.5.4-3, glibc
    2.14-4, mkinitcpio 0.7.2-1, initscripts 2011.07.3-1 and netcfg
    2.6.7-1
-   使用 dm-snapshot 取代了 aufs2
-   启动定制 USB 镜像所需文件均安装在 /arch
-   允许修改 NBD 导出名
-   允许使用串口终端（内核参数 console）
-   允许启动定制脚本（内核参数 script）；tty1 自动登录
-   增加了自我完整性测试（内核参数 checksum=y）
-   支持用把 iso 挂载成回环(loopback)设备
-   添加包：btrfs-progs-unstable crda curl dhclient dialog dnsmasq
    hdparm netcfg nilfs-utils openconnect rp-pppoe rsync vpnc
    wpa\_actiond
-   移除包：aufs2 aufs2-util joe ndiswrapper ndiswrapper-utils tiacx
    tiacx-firmware
-   移除 x86test；syslinux 菜单中添加了 HDT (Hardware Detection Tool)
-   支持从 memdisk 启动
-   SquashFS 和 initramfs 使用 XZ 压缩。

Arch Linux 用户使用 pacman -Syu 即可更新到最新。

Arch
的官方安装指南已经更新至新版，猛击[这里](http://wiki.archlinux.org/index.php/Official_Arch_Linux_Install_Guide "Arch Linux 官方安装向导")阅读。

*消息来源*：[官方发布公告](http://www.archlinux.org/news/20110819-installation-media/ "Arch Linux 2011-08-19 官方发布公告")

PS. cheerXiao 就是 xiaq，我刚才发现 WordPress 可以改昵称的……
