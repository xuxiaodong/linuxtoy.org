Title: Debian Installer 6.0 Beta1
Date: 2010-10-31 22:02
Author: lovenemesis
Category: Apps
Tags: Debian, installer
Slug: debian-installer-60-beta1

Debian Installer 6.0 Beta1
宣布发布，增加**软件包架构自动检测**，并且**关闭 ReiserFS 默认支持**。

本次新的 Debian 安装器有如下改善：

-   为 PS3 自动内核检测。
-   正确**识别 M$ Windows 的恢复分区**。
-   内核更新至 2.6.32。
-   parted 更新至 2.2，
-   增加对 Marvell GuruPlug、Marvell OpenRD-Ultimate 和 HP t5325 Thin
    Client（部分）平台的支持。
-   支持**ISO/USB混合式 ISO**。
-   在安装过程将**检索安装介质上的固件 Deb
    包**，方便执行包含驱动固件的光盘安装或网络安装。
-   部分语言文件更新及移除。

此外，新版本将启用 udhcpc 作为默认 DHCP 客户端（除 kFreeBSD），关闭了
ReiserFS 支持（若打开需添加`modules?=partman-reiserfs`）以及停止创建
/cdrom 符号连接。

[发布公告原文](http://www.debian.org/devel/debian-installer/News/2010/20101030)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=ODczOA)
