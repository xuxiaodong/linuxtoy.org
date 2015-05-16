Title: 下一代 Linux 文件系统: Btrfs
Date: 2010-08-30 00:45
Author: lovenemesis
Category: Featured
Tags: Btrfs
Slug: next-linux-filesystem-btrfs

翻译自LinuxPlanet的[Next Generation of Btrfs Linux Filesystem Nears
Prime Time](http://www.linuxplanet.com/linuxplanet/reports/7163/1/)  
我们再回过头来看看Btrfs方面的消息。*感谢 Petty 来稿！*

**Btrfs,未来的Linux标准文件系统（Future Linux Default Filesystem）**

至少从2008年起，[Btrfs就被人视作是下一代的存储技术](http://www.internetnews.com/dev-news/article.php/3781676/A-Better-File-System-for-Linux.htm)，现有的Linux文件系统的竞争者和取代者。自从2.6.29进入内核主线以来，每一次内核小版本的发布都包括了Btrfs的改进。

Btrfs项目的创始人，Chris Mason——现在是Oracle的Director of Software
Development表示，Btrfs虽然还未最终完成，但已经整体稳定和可用。但他同时承认，该文件系统仍有一些问题需要在接下来的开发中解决。Mason希望Btrfs能最终取代现有的Ext系文件系统。

在由Oracle赞助的关于Btrfs现状的webcast中，Mason指出了此项目的创立原因和技术特点。

由于现有的Linux文件系统的技术特点造成了某些Oracle关注的特性无法实现，所以他们决定另起炉灶，而不是在现有文件系统上扩展。

Btrfs的基本特点是使用了copy on write
(COW)，这意味着Btrfs在普通操作中不会直接覆盖数据，而是将元数据（metadata）和数据的新值写到别的地方，然后在文件系统中指向新的位置。  

这就提供了强大的一致性和完整性保证。在海量存储上，这对于保持数据的可管理非常重要。

在COW之外，Btrfs还提供了快照和调整文件系统大小的功能。为了方便现有的Ext3/4用户迁移，Btrfs提供了从Ext3/4离线转换（offline
conversion）的功能。在这种转换中，系统首先在Ext3/4的空闲空间上创建Btrfs，然后创建Btrfs的元数据（metadata），使其指向Ext3/4现存文件的数据块（data
blocks）（黑日白月注：[EXT4 到 BTRFS
的无损转换教程](http://linuxtoy.org/archives/use-livecd-to-allow-existing-fedora-13-use-btrfs-filesystem.html)）。

**仍有改进的余地（Room for Improvement）**

由于有上述优点，Btrfs迅速的获得了支持。如Meego、Fedora、OpenSUSE等发行版都包含了它。  
但目前Btrfs仍不是在每一个场合都优于Ext3/4。

例如，COW在有利于储存完整性的同时，它可能还不是对所有企业应用的场合都算理想。在回答InternetNews.com的问题时，Mason提到COW可能导致比其它文件系统更多的磁盘碎片（greater
disk
fragmentation），特别是在跑数据库和虚拟化的时候。因为在这两种环境下都会存在对一个特定文件的多次随机写入（数据库资料和虚拟机镜像），这是Btrfs表现最差的场合之一。但眼下Btrfs开发者正在努力寻找解决这一问题的途径（黑日白月注：个人使用体验是使用
sqlite 的程序性能受影响比较明显）。

而且至少还有另一个麻烦的问题——Mason警告说他们还没有什么管用的办法解决内核bug造成的文件系统损坏。当然同样，开发者现在正在做一个文件系统校验工具，以期缓解这一问题。他补充说，可能很快，他们的劳动就将结出果实——大约两个月，我们就能解决这些基本的问题，Btrfs将得到进一步的改进。
