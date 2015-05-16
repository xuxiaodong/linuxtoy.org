Title: Btrfs 文件系统现状
Date: 2014-11-09 21:32
Author: lovenemesis
Category: Featured
Tags: Btrfs
Slug: btrfs-current-status

随着默认搭载 Btrfs 文件系统的 openSUSE 13.2 发布，这个备受期待的 Linux
系统下一代文件系统距离生活近了不少。来自富士通的开发者 Satoru Takeuchi
在 LinuxCon 2014 上分享了 Btrfs 文件系统的发展现状，表示当下 Btrfs
已经可以在生产环境下部署使用了。

隶属富士通 Linux 开发部门的 Satoru Takeuchi 表示富士通从 2010
年开始就开始进行 Btrfs
的相关开发，因为这是唯一能满足关键任务系统的稳定及健壮需求的文件系统。摘录其[演示文稿](https://events.linuxfoundation.org/sites/events/files/slides/Btrfs\_Current%20status\_and\_future\_prospects\_0.pdf)的中的一些要点如下：

* 通过示意图方式快速介绍了 Btrfs 的功能特点，简洁易懂。还搞不清 CoW
和子卷概念的童鞋别错过啊～

* CoW 方式的文件极大的提高了健壮性，在富士通的测试中完胜 Ext4 及 XFS。

* 文件卷的性能胜过 LVM 及 dm-thinp 。

* 从 Kernel 3.0 到现在，每个版本 150 个左右和 Btrfs
相关的补丁，其中错误修复占大多数，不过几乎每次发布都会引入新功能。其中也有富士通的一部分贡献。

* 在与 Ext4 及 XFS 的性能测试方面， Btrfs
不是胜出就是不相上下。从这个角度看性能方面令人满意。

* 目前 Btrfs 已经可以适用于除 RAID 5/6 以外的所有环境，特别适合 RAID 1
和 RAID 10 。推荐搭配最新的稳定版内核使用。

* 接下来将继续完善 RAID 5/6 的支持，丰富 Btrfs 文件系统的用户态工具。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTgzMzM)

PS：本站[首次报道 Btrfs 文件系统于 2009
年](https://linuxtoy.org/archives/linux-kernel-2629-rc-1.html)，后来本人亦分享了[将
Ext4 转换成 Btrfs
文件系统的方法](https://linuxtoy.org/archives/use-livecd-to-allow-existing-fedora-13-use-btrfs-filesystem.html)。

前段时间在为新本本装系统时，考虑到 SSD 支持选择了 Btrfs
文件系统，立刻被其优秀的特性所打动，子卷方式特别适合空间有限的固态硬盘。现正谋划着在台式机上也全面切换至
Btrfs 。

如果您还不了解 Btrfs
文件系统，本文所谈到的演示文稿是个很好的图文介绍。如果您也在使用 Btrfs
文件系统，不妨在此分享下您的经验～
