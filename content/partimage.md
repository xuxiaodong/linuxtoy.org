Title: Partimage — 分区克隆工具
Date: 2007-08-16 10:37
Author: toy
Category: Apps
Slug: partimage

[Partimage](http://www.partimage.org/) 是一款与 Ghost
类似的备份工具，它通过将硬盘分区保存为映像文件，从而达到备份数据的目的。目前，Partimage
所支持备份的文件系统包括
Ext2/Ext3、Reiser3、FAT16/32、NTFS、HPFS、JFS、XFS、UFS、HFS
等类型，囊括了 Linux、Unix、Mac OS、Windows 等平台。

[![Partimage](http://i.linuxtoy.org/i/2007/08/partimage_s.png)](http://i.linuxtoy.org/i/2007/08/partimage.png)

在使用 Partimage 保存映像文件时，你可以使用 gzip/bzip2
程序对其进行压缩，以便节省磁盘空间。你也可以将大的映像文件分割成多个较小的文件，从而烧录成
CD 或 DVD。Partimage 还支持通过网络来保存映像文件，比如在使用 Samba、NFS
的环境中。

[Partimage 当前最新版本为
0.6.6](http://www.partimage.org/Download)，支持 Linux 2.2/2.4/2.6
内核。如果你不想安装 Partimage，那么可以下载包含了它的
SystemRescueCd，烧录后便可直接加以使用。
