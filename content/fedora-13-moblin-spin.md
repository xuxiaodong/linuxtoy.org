Title: Fedora 13 Moblin Spin 发布
Date: 2010-05-29 04:12
Author: lovenemesis
Category: Distros
Tags: Fedora, Moblin
Slug: fedora-13-moblin-spin

如果想在非 Intel 平台的计算机上体验类似 MeeGo 的桌面环境，那么刚刚发布的
MeeGo 上游 Fedora 13 Moblin Spin 或许就是你最好的选择。

[![](http://i.linuxtoy.org/images/2010/05/moblin-screenshot-01-sm.png)](http://i.linuxtoy.org/images/2010/05/moblin-screenshot-01-sm.png)

与先前发布的 MeeGo 相似，Fedora 13 Moblin Spin 同样提供了
[Clutter](http://www.clutter-project.org/)
混合特效界面，[GUPnP](http://www.gupnp.org/) 通用即插即用服务和 Bisho
社交网络聚合套件。

在下大概把玩了下，注意到以下与 [MeeGo 1.0
上网本平台](http://linuxtoy.org/archives/meego-10-core-platform-with-netbook-experience-released.html)不同之处：

-   支持 AMD 平台的 CPU 及显卡，不再局限 Intel
    平台，但是要求显卡驱动要有 3D 加速支持
-   Intel 平台显卡的运行明显比 MeeGo 流畅，估计是 Fedora 13
    的显卡驱动比较新的缘故
-   采取 ext4 文件系统，而不是 Btrfs
-   采取 Firefox 作为默认浏览器，而不是 Chroium 或者 Chrome

已经安装了 Fedora 13 的朋友，可以通过在终端运行如下命令将 Moblin
添加到桌面环境中：

`su -c 'yum groupinstall "Moblin Desktop Environment"'`

**注意：** 由于 Mutter 的冲突问题，不能和 GNOME Shell 同时安装。

[英文主页及32/64位版本 LiveCD 下载（经测试可以制成 LiveUSB
方便无光驱的上网本使用）](http://spins.fedoraproject.org/moblin/)
