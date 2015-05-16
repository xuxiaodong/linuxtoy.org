Title: Mesa 10.4 正式发布
Date: 2014-12-15 14:27
Author: lovenemesis
Category: Drivers
Tags: Mesa, OpenGL, Wine
Slug: mesa-10-4-final-release

开源 3D/OpenGL 库 Mesa 在短暂延期后发布 10.4 正式版，带来了 Direct3D 9
State Tracker 支持。

本次新版本的变化有：

* 名为 *Gallium Nine* 的 Direct3D State Tracker，配合[打过补丁的 Wine
](https://github.com/iXit/wine)及 AMD 开源驱动(不支持
Intel)可以大幅度提升 Direct3D 9 游戏的性能。

* 重新默认启用 AMD HyperZ。

* 提升 Clover/OpenCL 的性能。

* 显著提升了 Freedreno Gallium3D 驱动的性能。

* Intel Sandy Bridge 上的几何 Shaders 支持。

* 进一步实现了更多 OpenGL 4.X 扩展。

[邮件列表发布公告](http://lists.freedesktop.org/archives/mesa-dev/2014-December/072630.html)

[官方 FTP 源代码包下载](ftp://freedesktop.org/pub/mesa/10.4.0/)

*消息来源*：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTg2Mjc)
