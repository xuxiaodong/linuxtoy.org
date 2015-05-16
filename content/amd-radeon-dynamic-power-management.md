Title: AMD 开源 Radeon 驱动动态电源管理
Date: 2013-06-28 11:52
Author: lovenemesis
Category: Drivers
Tags: AMD, radeon
Slug: amd-radeon-dynamic-power-management

AMD 发布了用于开源 Radeon 驱动的动态电源管理补丁，预期将收录于 Linux
Kernel 3.11 版本。此外还增加了对尚未发布的 Radeon 8000 系列显卡的支持。

如果您还记得 [Phoronix 在 2
年前的报道](http://www.phoronix.com/scan.php?page=news_item&px=OTI1OQ)，今天
AMD 实践了当年的宣言：Radeon 8000
将成为开源驱动支持的一个里程碑。之前发布的[开源 Radeon 驱动 UVD
硬件解码](http://linuxtoy.org/archives/amd-releases-open-source-uvd-support.html)支持将很快随着
Linux Kernel 3.10 与公众见面。而在 Linux Kernel 3.11
中将带来期待已久的动态电源管理实现。

早先 AMD Radeon
开源驱动仅支持较为有限的电源管理，其中[动态调节部分实现的并不完善](http://linuxtoy.org/archives/power-management-for-open-sourced-radeon-driver.html)。而本次新发布的补丁，则为从
Radeon 2000 到 7000
系列的显卡实现了动态核心/显存频率调整、动态电压调整和 PCI-E 1.0/2.0
切换，以及 ASPM 支持。

针对预期下半年发布的 Radeon 8000 ，目前已经实现了 KMS、通过 GLAMOR
实现的 2D 加速、Gallium 3D 加速、OpenCL 通用计算和 UVD
解码支持，其对应的动态电源管理补丁也将很快释出。

另外，现有 [Radeon 7000 用户已经可以在 Fedora 19 上体验开箱即用的
RadeonSI
开源驱动](http://www.phoronix.com/scan.php?page=news_item&px=MTM5Nzg)了。按照以往
Fedora 内核升级的节奏，Radeon 8000 系列的支持及本动态电源管理补丁也将在
3.11 内核发布后的一个月内通过更新推送。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTM5NjE)
