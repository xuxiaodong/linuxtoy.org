Title: 在Windows下读取Ext4分区
Date: 2010-09-26 10:04
Author: Petty
Category: News
Tags: Ext2Fsd, Ext2Read, ext4
Slug: read-ext4-in-windows

本文介绍两个能在 Windows 下读取ext4分区的软件。

第一个是 [Ext2Read](http://sourceforge.net/projects/ext2read/)。它能查看
ext2/3/4 分区并从中拷贝文件和目录，支持 LVM2 和 EXT4 extent
，以及递归拷贝整个目录。

![ext2read](http://www.ubuntugeek.com/wp-content/uploads/2010/09/screenshot1.jpg)

第二个是[本站之前介绍过](http://linuxtoy.org/archives/ext2fsd.html)的
[Ext2Fsd](http://www.ext2fsd.com/) ，它是适用于Windows 2000, XP, Vista,
7的驱动程序，能使这些系统直接支持 ext2/3/4 分区的读写。但对 ext4
的支持是有限的——在创建/格式化 ext4 分区时， 必须加上 `-O ^extent`
参数来关掉 extent
特性，否则就无法支持。考虑到稳定性的问题，安装时最好去掉写入支持，以免数据损坏。同时在Windows
7中安装时必须使用 “Windows Vista Service Pack 2 兼容模式”。

[原文地址](http://www.ubuntugeek.com/how-to-read-ext3ext4-linux-partition-from-windows-7.html)
