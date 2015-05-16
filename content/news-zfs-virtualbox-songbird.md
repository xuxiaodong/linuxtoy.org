Title: 短消息： ZFS, VirtualBox, Songbird
Date: 2010-06-08 05:49
Author: lovenemesis
Category: Music Player
Tags: Songbird, VirtualBox, zfs
Slug: news-zfs-virtualbox-songbird

三则短消息：ZFS 文件系统的 Linux 原生支持，VirtualBox 3.2.4 发布，
Songbird 1.7.2 Linux 版本同步发布。

ZFS 文件系统由于协议和 GPL 不兼容，在 Linux 系统上一直停留在 FUSE
状态。最近 Lawrence Livermore National Laboratory 的研究者们成功将 **ZFS
做成内核模块**的方式，避免了协议纠纷，可喜可贺。但是目前 **POSIX
访问接口还没实现**，挂载不能，用户态只能通过 zvol
访问。[详情](http://www.osnews.com/story/23416/Native_ZFS_Port_for_Linux)

距离上一个版本不到一周，VirtualBox 3.2.4 紧急发布，修复了
**Host-only/bridged 网络、Win64 Page Fusion 和 3D
加速**相关的错误。[详情](http://www.virtualbox.org/wiki/Changelog)

Songbird 1.7.2 正式发布，带来了**照片同步和视频播放**的功能，Linux
版本依然提供，但不再由官方 QA。 同时 5 月底时 Nightly Build 迁移到
xulrunner 1.9.2 平台，运行效率有不小提升，版本号也随着升级到
2.0.0。[1.7.2 Linux
版本下载](http://wiki.songbirdnest.com/Developer/Articles/Builds/Contributed_Builds#Linux)
[Nightly Build
版本下载](http://wiki.songbirdnest.com/Developer/Articles/Builds/Nightly_Builds)
