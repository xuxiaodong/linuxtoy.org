Title: Linux Kernel 4.2
Author: lovenemesis
Date: 2015-08-31
Category: Kernel
Tags: kernel
Slug: linux-kernel-4-2
Summary: 在短暂的一周延期后，Linux 内核发布 4.2 正式版本，带来了统一架构下 AMDGPU 内核态组件和  UEFI 固件更新支持。

根据 [Phoronix 上的报道](http://www.phoronix.com/scan.php?page=article&item=linux-42-features)来看，新版本的变化有：

* 首次包含 AMD 统一驱动架构下的 `amdgpu` 内核态模块，目前支持 Tongo 、Carrizo 及 Fiji 核心的 GPU，不过注意重调速支持需要等到下个版本
* 对于 AMD GCN 1.0 的显卡用户来说，可以使用 VCE1 的视频编码核心了
* 新增 VirtIO GPU 驱动，奠定 QEMU/KVM 虚拟环境下 GPU 加速的基础
* NCQ TRIM 允许强制开启或关闭，方便维护较早的 SSD
* 针对 Btrfs, Ext4, F2FS 的修复及改善
* 新增对 PS Move 的支持，同时 XBox 控制器上的 LED 现在可正常工作了
* 提供对 UEFI ESRT 的支持从而可以在 Linux 下更新 UEFI 固件，其用户态工具将随着 Fedora 23 面世


[详细更新内容](http://kernelnewbies.org/Linux_4.2)

[邮件列表发布公告](http://lkml.iu.edu/hypermail/linux/kernel/1508.3/04416.html)

[官方源代码下载](https://kernel.org/pub/linux/kernel/v4.x/linux-4.2.tar.xz)