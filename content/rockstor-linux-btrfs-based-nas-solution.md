Title: Rockstor：基于 Linux 和 Btrfs 的 NAS 方案
Date: 2015-12-25
Author: lovenemesis
Category: Distro
Tags: nas, btrfs, centos
Slug: rockstor-linux-btrfs-based-nas-solution
Summary: 如果您打算自行组建 NAS，除了 BSD 阵营的 FreeNAS 与 ZFS 的传统组合，不妨尝试下 Linux 与 Btrfs 的组合方案 Rockstor。

Rockstor 的特点有：

* 基于 CentOS 订制，为 NAS 应用特别订制的 Linux 发行版
* 使用前沿的 Btrfs 文件系统
* 提供基于 Web 的管理界面以及 RESTful 的 API
* 支持所有 NAS 的标准功能，包括 Samba、NFS、SSH、FTP
* 基于 Docker 的插件机制，可以扩充 Rockstor 的功能，比如 OwnCloud 集成
* 允许以虚拟机方式安装，方便体验

Rockstor 以 GPLv2 协议分发，上层应用以 Stable 和 Testing 两种渠道**滚动升级**，其中 Testing 渠道完全免费，而 Stable 则收取每年 $15 的订阅费用。

在从其[下载页面](http://rockstor.com/download.html)获得安装介质后便可以类似 CentOS 的方式安装，亦可以从其[商店订购](http://shop.rockstor.com/)预装好系统的 U 盘或 PCI-E SSD

[Rockstor 首页](http://rockstor.com/)
