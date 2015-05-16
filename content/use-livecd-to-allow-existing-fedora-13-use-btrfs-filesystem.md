Title: 用 LiveCD 让现有 Fedora 13 使用 Btrfs 文件系统
Date: 2010-06-06 06:09
Author: lovenemesis
Category: Tips
Tags: Btrfs, Fedora
Slug: use-livecd-to-allow-existing-fedora-13-use-btrfs-filesystem

[Fedora 13](http://linuxtoy.org/archives/fedora-13-final-released.html)
引入了 Anaconda 安装器对于新一代 Btrfs
文件系统的支持，不过这个安装选项仅限使用 DVD
安装时使用。本人简单介绍下在用其他方式（比如 LiveCD）安装或者用
PreUpgrade 升级上来之后，怎样使用 LiveCD 让已有的系统使用 Btrfs
分区而**不影响其中已保存的数据**。

鉴于想这样折腾的童鞋都是已经对于 Linux
系统有一定了解的，于是在下在这里只是说下过程，经过测试目前正常。

*需要工具：*

-   Fedora 13 LveCD 或者相应的 LiveUSB。
-   硬盘上已经安装好的 Fedora 13 系统，使用 ext3 或者 ext4 文件系统。
-   独立 /boot 分区，因为 grub 不支持从 btrfs
    引导（**一会儿也不要转换**）。

*步骤说明：*

1.  在已安装到硬盘的 Fedora 13 系统上安装 btrfs-progs 软件包，提供必要的
    btrfs 维护工具。
2.  重新启动电脑，从 LiveCD 或者 LiveUSB 引导。
3.  在 Live 环境中也安装 btrfs-progs，使用其中的 btrfs-convert
    工具将硬盘上的分区转换为 btrfs 文件系统。
4.  使用 blkid 获得分区新的 UUID 编号，修改 fstab 和 grub.conf
    文件中对应的 UUID 值。
5.  挂载硬盘系统的 / 分区，进入后使用 `touch .autorelabel`
    ，请求在下次重启时 SELinux 对整个文件系统进行重新标注。
6.  重新启动系统，从硬盘引导，等待 SELinux 重新标注完成。

若是一切顺利，那么恭喜你可以开始体验下一代 Linux 平台文件系统 Btrfs 了。

这种方法的好处的是原先系统会以子卷的方式保留在硬盘上，意味着可以随时返回到
ext3/ext4 文件系统上，转换过程也不会丢失任何数据。

恢复 ext4 的方法和上面类似，只是在第三步使用 btrfs-convert 时增加 -r
恢复选项。注意这样**使用 Btrfs 文件系统时的一切更改将丢失**！

如果对于 Btrfs 文件系统感觉满意，那么可以使用 `btrfs subvolume delete `
将备份子卷删除，释放所占空间。

[FedoraForum
教程](http://forums.fedoraforum.org/showthread.php?t=246520)

[参考 Btrfs
Wiki](https://btrfs.wiki.kernel.org/index.php/Conversion_from_Ext3)

*PS:* 使用 Ubuntu
的朋友可以参考这篇[教程](http://ubuntuforums.org/showthread.php?t=1389279)去体验
Btrfs，但是要复杂不少：需要给 grub2 打补丁，需要添加 btrfs 模块的
initramfs 生成规则。
