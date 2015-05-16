Title: Fedora 17 支持在 EFI 系统上原生引导
Date: 2012-05-28 17:54
Author: lovenemesis
Category: News
Tags: Fedora
Slug: fedora-17-supports-native-efi-boot

想在 Apple Mac 系统上使用安装 Linux 系统但是却苦于问题多多的 BIOS
兼容模式？ Fedora 17 将是首个默认安装介质支持在 EFI 系统上原生引导的
Linux 发行版。

Matthew Garrett
在[他的博客中](http://mjg59.dreamwidth.org/11285.html)详细介绍了 Fedora
17 在安装介质

首先是效仿其他发行版，使用
[isohybrid](http://www.syslinux.org/wiki/index.php/Doc/isolinux#HYBRID_CD-ROM.2FHARD_DISK_MODE)
创建可以直接 `dd ` 到 U 盘的 ISO 镜像。毫不奇怪。

接下来的就是一些独特的地方了：

1.  声明存在 Apple 格式的分区表，于是可以在 Apple 设备上直接识别。
2.  增加覆盖范围为整个镜像的，类型为 0， MBR 分区格式。
3.  引入 EFI 引导分区。
4.  为内嵌的 HFS+ 分区增加对应的分区信息。

结果就是一个可以**同时支持在 BIOS, UEFI 和 Mac EFI
系统下引导，并且支持从 CD 或者 U 盘直接写入引导的光盘镜像**。

在 Mac 设备上使用原生 EFI 模式带来的一大好处就是避免使用 BIOS
兼容模式带来的诸多驱动方面的烦恼。

注意事项：

-   请在 Mac 系统中关闭 BIOS 兼容模式后再引导。
-   部分使用 Radeon 系统显卡的机器存在初始化问题，目前仍在修复。

[在 MacBook Air 上引导 Fedora 17
的视频演示](http://www.youtube.com/watch?v=SEa7xI0tdcY)([朝内镜像](http://v.youku.com/v_show/id_XNDAzODM0NjIw.html))
