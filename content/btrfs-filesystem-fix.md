Title: Btrfs 文件系统修复技巧
Date: 2015-05-06 16:11
Author: lovenemesis
Category: Tips
Tags: Btrfs
Slug: btrfs-filesystem-fix

Btrfs
文件系统工具随着内核版本的进步在逐步成熟，不过难免在使用过程有会有一些意外发生，遇到**无法挂载**的情况怎么办？

若是在其他文件系统异常的情况下，第一反应当然是 `fsck`
系列工具咯～不过若是在终端运行它的话，会得到这样的结果：

* 什么都没有发生……  
* 告诉你若是想修复文件系统，请使用 `btrfs check` 子命令

慢！在撞墙或果断调用 `btrfs check` 之前，请注意 btrfs
文件系统不像其他文件系统，大多数情况下是不需要 `fsck` 的，这个不干活的
`fsck` 其实是为了兼容在 `fstab` 中错误的非0 `fs_passno`
设置而生的。

再慢！`btrfs check`
是个猛药，草率使用可能会适得其反。那么接下来应该怎么办？

#### 使用最新内核挂载

Btrfs
在磁盘上的文件系统格式已经稳定下来了，但是各种内核态和用户态的工具还在发展。不少错误或问题可以通过使用包含修复的新内核解决。

假设您已经通过无论何种方式引导了包含最新内核的 Live
环境，那么此时可以首先尝试以 `recovery,ro` 选项挂载 btrfs 文件。

之后观察下 `dmesg` 或 `journalctl -k` 的输出，有没有 btrfs 相关的
kernel oops。

没有什么异常的话，可以先检查下最后访问的文件什么的，看是否存在。由于
Btrfs 的 COW 机制，大部分情况应该是都在的。

若**有且仅有** kernel oops 的情况下，使用 `btrfs-zero-log`
去尝试修复下。

#### 重新挂载，检查异常

若是上一步通过只读挂载正常且又没有 kernel
oops，那么就可以尝试正常的**读写挂载**了。

运气好的话，没什么问题，可能意味着之前遇到的挂载异常问题已经在新的内核中修复了。  
但尽管如此，依然推荐执行 `btrfs scrub start`
命令，开始检查全部文件及其校验和。

`btrfs scrub` 是一个在后台运行的命令，耗时比较长，在下一个普通的
Seagate 500G SATA3 7200rpm 的硬盘完成这个工作需要约 26
分钟。期间可以随时使用 `btrfs scrub status` 查看进度。

请注意对于**非 RAID 环境**来讲，`btrfs
scrub`仅能检查出文件错误但无法修复问题（木有未损坏的文件拷贝啊……），对于
RAID 1 等级别，这个过程也可以自动使用来自冗余盘的信息进行修复，除非加上
`-r`参数。

#### 挽救重要数据

只有**下列两种情况**需要执行 `btrfs rescue`
命令，因为它扫描磁盘文件簇的方式**真的非常费时**，不过相对应的，它**不要求分区挂载**：

1. 最开始连只读挂载都失败的情形  
2. 只读挂载成功，但是读写挂载使用 `btrfs scrub`
时提示大量错误，而且又是单盘环境

#### 重建文件系统

当你挽救了重要数据之后，最后又回到 `btrfs check`
这里了，它会尝试修复文件系统。注意为了避免误操作，**仅在加上
`--repair` 选项**时才真正执行修复。

个人觉得，若是重要数据不多的话，离线恢复不难的话，还不如重新格式化得了……

#### 总结及提醒

Btrfs
文件系统本身健壮性还是不错的，不过由于工具集还在发展，偶尔出些小状况，通过上述的修复手段也都能应对。

此外，提醒下若是突然遇到挂载异常又排出了硬件问题，可以**到 IRC
频道或者 [Wiki
的页面](https://btrfs.wiki.kernel.org/index.php/Gotchas)看看**是不是最近工具集导致的，有时可以节省不少绕弯的精力。

文中所述命令的详情可以通过 `man -k btrfs` 查阅

参考资料：

* [Btrfs Problem FAQ](https://btrfs.wiki.kernel.org/index.php/Problem_FAQ)  
* [Btrfs FAQ](https://btrfs.wiki.kernel.org/index.php/FAQ)  
* [Btrfs Tips](http://marc.merlins.org/perso/btrfs/post_2014-03-19_Btrfs-Tips_-Btrfs-Scrub-and-Btrfs-Filesystem-Repair.html)
