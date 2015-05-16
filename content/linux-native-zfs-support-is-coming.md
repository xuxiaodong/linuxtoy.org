Title: Linux 原生 ZFS 支持即将到来
Date: 2010-08-29 19:03
Author: lovenemesis
Category: Featured
Tags: zfs
Slug: linux-native-zfs-support-is-coming

翻译自Phoronix的[Native ZFS Is Coming To Linux Next
Month](http://www.phoronix.com/scan.php?page=article&item=zfs_linux_coming&num=1)、[LLNL
Talks To Us About Their Linux ZFS
Port](http://www.phoronix.com/scan.php?page=news_item&px=ODU1MA)。*感谢
Petty 来稿！*

**来自Linux文件系统部门的利好消息：**

还记得本站之前报道过的[Linux的ZFS原生支持](http://linuxtoy.org/archives/news-zfs-virtualbox-songbird.html)吗？美国Lawrence  
Livermore National
Laboratory依据该实验室安全部门和美国能源部的一份协议开发了ZFS的Linux的原生支持，但此项目的代码并不可以直接使用——因其不提供POSIX接口。印度的Knowledge
Quest
Infotech公司则达到了该目标，[他们从去年开始自己的移植工作](http://kqinfotech.wordpress.com/2009/10/23/hello-world/)。

早些时候KQ Infotech的Business Manager, Darshin
Vyas，[在Phonronix论坛中发出声明](http://www.phoronix.com/forums/showthread.php?t=25570)（此链接指向的讨论包含了比本文更加详尽的信息），该项目已接近Beta状态。

由于Solaris自身发布协议和专利纠纷的限制，此项目的代码仍是基于CDDL发布的，因而**不会进入主线内核**，故他们只会提供可以编译为内核模块的源代码，由最终用户自行“嵌入”GPL的内核，并且不使用任何GPL-only
symbols，规避了GPL的Copyleft条款要求将非GPL程序嵌入GPL程序的行为人（此场合下即最终用户，无再发布的需要）分发程序必须以GPL发布的协议冲突问题（这是常见的GPL规避手段之一）。同时该公司似乎确信Oracle不会对他们采取法律行动。

代码预计在九月15日发布，将**只能支持64位内核**，同时将提供用于Fedora
12和Red Hat Enterprise Linux 6  
Beta
2的RPM包。Ubuntu10.04亦可安装，但需自行编译，期待届时的Phoronnix的Ext4 &
Btrfs V.S. ZFS on
Linux测评。(译者私心希望有Reiser4出场，但按其进度——2.6.37才能进主线——来讲，属不可能。）

**存在的问题：**

KQ Infotech记的ZFS on
Linux虽好，但不能确定其未来的法律风险，也不能指望得到Oracle/Sun的许可。由于上述的许可证纠纷，无论是官方内核还是主要的发行版都不可能采用它，任何人想用ZFS作为Linux的根文件系统的人都**必须自己编译内核并自行处理安装问题**。

同时其基于ZFS Pool 18，虽然较新，但非最新的21，故仍**缺乏de-duplication
support**和其他一些在OpenSolaris解散前加入的更新颖的功能。只有X86-64支持，也进一步限制了其应用。同样令其前景模糊不清的是——KQ
Infotech一直在关门开发，至今外界无法得到一行代码——该公司是会一直以自由许可提供该模块，还是会将其拿来用商业许可套现。

由于功能上与向ZFS看齐的Btrfs日趋完善，并正在成为Linux的下一代“标准”文件系统，所以如果这项工作早个两三年完成的话，重要性可能会比现在大。在Phoronix上个月进行的一系列测试：[Running
ZFS with CAM-based ATA](http://www.phoronix.com/vr.php?view=15148)、[ZFS
On FreeBSD vs. EXT4 & Btrfs On
Linux](http://www.phoronix.com/vr.php?view=15150)、[Btrfs, EXT4, & ZFS
On  
A Solid-State
Drive](http://www.phoronix.com/vr.php?view=15187)中，Ext4/Btrfs on
Linux无论是机械硬盘还是固态硬盘性能都把ZFS on FreeBSD
8.1甩开了好几条街。虽然可以将之归咎为FreeBSD自身的瓶颈，但也很难指望ZFS在Linux上能比EXT4/Btrfs有什么性能优势（如果不说完全不可能的话）。

考虑到以上几点，这个模块可能用于尝鲜会很有趣，但不可能改变Linux文件系统的前景，它自身估计也只会在小范围内应用。

**LLNL方面的情况：**

劳伦斯—利物浦国家实验室（Lawrence Livermore National
Laboratories）的Linux ZFS移植项目的领导人Brian
Behlendorf向Phoronix方面提供了以下信息：

1.**KQ
Infotech的工作是基于LLNL的基础上的**，具体来说是该实验室[发布在Github上的](http://github.com/behlendorf/zfs/wiki/disclaimer)SPL
ZFS 0.4.9源代码。

2.Brian Behlendorf打算把KQ Infotech的**改进合并回自己方面的代码库**。

3.LLNL的**ZFS移植最终会升级到onnv\_147**——Oracle废弃OpenSolaris之前的最后一版，不过这之前要花些时间，因为他们需要“维持现有的稳定性和Linux内核的可移植性。

4.虽然KQ Infotech方面在Phoronix论坛上放言：ZFS是“ by far the best file
system”，并且甩下了诸如“Thats why its long awaited, am not just
bullshitting here, arival lot of storage companies are keenly looking
forward to this solution and only if you are related to the storage
industry, will you know the real gem ZFS is! Nothing to laugh on ZFS
being the best file system, hell it
is!!!”这样的狠话，但Behlendorf仍警告说ZFS for
Linux仍在开发中，还有大量工作要做，它目前的状况并不是那么乐观。

不管怎么说，好在有LLNL的技术支持和美国能源部的合同在那里，Linux的原生ZFS支持还是可以期待的。
