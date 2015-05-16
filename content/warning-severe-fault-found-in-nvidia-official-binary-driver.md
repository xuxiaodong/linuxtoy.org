Title: 警告：Nvidia 官方二进制驱动严重问题
Date: 2010-03-07 20:50
Author: lovenemesis
Category: Drivers
Tags: fault, NVIDIA
Slug: warning-severe-fault-found-in-nvidia-official-binary-driver

昨日 Nvidia 官方闭源驱动爆出重大缺陷，可能导致显卡风扇停转继而导致 GPU
核心温度过高。

该问题出现在 Win32 196.75 版和 Unix 系列 195.36.08 和 195.36.03
驱动上。对于 Unix 类系统的驱动， Nvidia 建议用户降级至 190.53 或 195.30
驱动。

对于部分新近的发行版，可以先使用开源的 Nouveau 驱动。在 Fedora 13 Alpha
上，该驱动已经可以通过 Gallium3D 提供基本的 3D 加速支持，可以运行
Compiz，QuakeLive 和 Wine (Warcraft III) 等 3D 应用。

消息来源：
[FedoraForum](http://forums.fedoraforum.org/showthread.php?t=241786)
