Title: Fedora 13 下安装 NVIDIA 二进制驱动
Date: 2010-03-09 19:06
Author: lovenemesis
Category: Drivers
Tags: Fedora, NVIDIA
Slug: howto-install-nvidia-binary-driver-under-fedora-13

Fedora 13 如同前作 Fedora 12 一样，默认开启了 Nouveau 的 KMS
模块，尽管已经可以通过 Gallium3D 获得完整 3D
加速支持，但肯定还有一些追求性能和希望用高清视频加速的朋友需要 NVIDIA
的二进制驱动。

本文以使用 rpmfusion 打包的 NVIDIA 的二进制驱动为例，若需要安装 Nvidia
官方站点提供的版本，请参考[Fedora 12
的文章](http://linuxtoy.org/archives/howto-install-nvidia-official-driver-under-fedora-12.html)
并依照此文做出相应修改。

**1.** 添加 rpmfusion 仓库：

`su -c 'rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm'`

**2.** 使用 yum 安装驱动：

`su -c 'yum --nogpgcheck install xorg-x11-drv-nvidia akmod-nvidia'`

**3.** 屏蔽 initrd 中的 nouveau 模块：

`su -c 'sed -i '/root=/s|$| rdblacklist=nouveau|' /etc/grub.conf'`

**4.** 重启

**非常必要！**

在此感谢 FedoraForm 的 **leigh123linux 大**的
[HowTo](http://forums.fedoraforum.org/showthread.php?t=240860) 。
