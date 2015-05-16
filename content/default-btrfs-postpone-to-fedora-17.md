Title: 默认使用 BTRFS 文件系统的特性推迟到 Fedora 17 
Date: 2011-08-09 14:20
Author: liangsuilong
Category: Distros
Tags: Btrfs, Fedora
Slug: default-btrfs-postpone-to-fedora-17

Fedora 的 Josef Bacik
在[开发者邮件列表](http://lists.fedoraproject.org/pipermail/devel/2011-August/155349.html)上宣布，默认使用
BTRFS 文件系统的特性推迟到 Fedora 17。

推迟的原因很简单，就是因为 BTRFS 的查错工具 btrfsck 未能在 Fedora 16
特性冻结前推出，而且性能问题一直困扰着 BTRFS。同时部分 BTRFS
的特性仍然需要等待到 Linux 3.2
内核才能跟上。在经过谨慎且综合的考虑之下，Josef
Bacik 决定把这项特性推迟到 Fedora
17。他说他们已经很尽力很勤奋地工作，但是仍然无法使 BTRFS
达到稳定使用的阶段。部分特性的改进并不能完全由他控制，还要等待上游内核的审核。此外他还透露
btrfsck
会在几周内推出，至于具体需要等待几周，似乎暂时没有定论。一个字，就是等。最后，这项特性已经在
Fedora 16
新[特性列表](http://fedoraproject.org/wiki/Releases/16/FeatureList)删除了。所以
Fedora 16 依然会使用 EXT4 作为默认的文件系统。至于 MeeGo，它们的 BTRFS
默认文件系统的计划依然没有改变。

连同早前取消的 firewalld，Fedora 16 已经取消了 2
项特性。而在美国东部时间 8 月 10 日 17 点将会举行 Fedora 16 Go/No-Go
线上 IRC 会议，将会决定哪些特性未达到开发进度而放弃，同时决定 Fedora 16
Alpha 是否按时发布。最终会在 Fedora 16 Alpha
发布前完成所有特性的开发工作。
