Title: GNOME Shell 软件渲染
Date: 2011-11-07 11:47
Author: lovenemesis
Category: News
Tags: Fedora, Gallium3D, gnomeshell, LLVM
Slug: gnome-shell-software-rendering

利用基于 Gallium3D 的 LLVMpipe 驱动，**GNOME Shell
将实现无需显卡加速的软件渲染模式**。

LLVMpipe 是一个基于 LLVM 的 Gallium3D 驱动，利用 CPU 的实现 OpenGL
加速效果。尽管该驱动运行 3D 游戏颇为吃力，但是在现代的 CPU
上实现混合桌面特效还是绰绰有余的。

[![](http://linuxtoy.org/img/2011/11/small-heck-of-yes.png "small-heck-of-yes")](http://linuxtoy.org/img/2011/11/small-heck-of-yes.png)

如上图所示，该功能一方面可以**在不具备 3D
加速的设备（虚拟机或者显卡驱动有问题）上提供良好的 GNOME Shell
体验**，另一方面也**将开发资源从维护仅用于 GNOME Fallback
模式的组件中解放出来**，集中精力完善 GNOME 3。

还需要从事的工作包括更新 GNOME Shell 支持驱动名单、增加内核伪 GEM
模块等。

该功能计划在 **Fedora 17 GNOME 3.4** 中实现，预期届时包括 Unity
在内等**依赖 3D 加速的其他桌面环境亦将从中受益**。

[Fedora
Wiki（包含大图）](https://fedoraproject.org/wiki/Features/Gnome_shell_software_rendering)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTAxMTI)
