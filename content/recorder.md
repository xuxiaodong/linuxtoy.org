Title: Recorder - 超简单的 GTK+ 光盘烧录器
Date: 2008-07-23 15:21
Author: toy
Category: Apps
Tags: GTK+, Recorder
Slug: recorder

Recorder 真是一个超简单的 GTK+ 光盘烧录工具。与
[Brasero](http://linuxtoy.org/tag/brasero)
相比，没有那么多依赖。其实，大多数时候，我们需要的就是能够烧录 ISO
映像文件、数据 CD/DVD 什么的而已。使用 Recorder 足矣。

![recorder.png](http://i.linuxtoy.org/i/2008/07/recorder.png)

**安装 Recorder**

Recorder 要求 pygtk、cdrkit (或 cdrtools)、dvd+rw-tools，需先行安装好。

Archlinux：可以使用
[AUR](http://aur.archlinux.org/packages.php?ID=16501)，`yaourt -S recorder`。

Gentoo：[ebuild
文件](http://recorder.googlecode.com/files/recorder-1.3.1.ebuild)到这里取用。

其他 Linux 发行版，先[下载 tar.bz2
文件](http://code.google.com/p/recorder/downloads/list)，然后执行：  

` tar jxvf recorder-1.3.3.tar.bz2 cd recorder-1.3.3 make install #这一步需要 root 权限`

**配置**

当首次启动 Recorder 后，需要配置“Path to your drive”，在其中输入
`/dev/cdrom` 即可。

[Recorder](http://code.google.com/p/recorder/)
