Title: 使用 Byzanz 录制 Gif 动画或 Ogv 视频
Date: 2012-12-24 17:12
Author: toy
Category: Apps
Slug: byzanz

想要录制 Linux 桌面？Byzanz 是一个不错的选择。Byzanz
简单小巧，容易使用，既能录制 Gif 动画，又可录制 Ogv 视频。

![byzanz](http://lt-file.b0.upaiyun.com/files/2012/12/byzanz-demo.gif)

**安装 Byzanz**

可执行下列指令来安装 Byzanz，注意需要 root 权限：

aptitude install byzanz # Debian/Ubuntu  
yum install byzanz # Fedora  
emerge -av byzanz # Gentoo/Funtoo

Arch Linux 用户可在 AUR 中找到 Byzanz。如果你不能在自己所用的 Linux
发行版包仓库中找到 Byzanz，那么可以获取其[源代码][s]，自行编译。

**Byzanz 用法**

以本文的 byzanz-demo.gif 为例，你可以通过如下命令来完成录制过程：

byzanz-record -d 40 -x 0 -y 0 -w 400 -h 320 byzanz-demo.gif

其中：

* `-d 40` 为录制的时长为 40 秒  
* `-x 0` 录制区域的横坐标  
* `-y 0` 录制区域的纵坐标，记住：屏幕右上角为原点（0,0）  
* `-w 400` 录制区域的宽度  
* `-h 320` 录制区域的高度  
* `byzanz-demo.gif` 保存的文件名

BTW: Byzanz 还带有一个 GNOME panel applet，感兴趣的同学可自行尝试。

[s]: http://git.gnome.org/browse/byzanz/
