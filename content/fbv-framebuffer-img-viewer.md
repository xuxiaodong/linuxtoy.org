Title: fbv: 控制台图片查看器
Date: 2011-08-23 15:08
Author: cheer_xiao
Category: Apps
Tags: fbv, framebuffer
Slug: fbv-framebuffer-img-viewer

fbv 是一款基于 framebuffer 的图片查看器，可以在**真正的终端**下查看
png/gif/jpeg/bmp 图片。

使用说明书：

1.  安装 fbv。
2.  按 Ctrl-Alt-F1~F6 中的某一个键切换到终端，登录。
3.  fbv /path/to/image
4.  键盘操作：

-   如果图片太大，使用 F 切换原大小/适合屏幕。
-   如果图片太大，也使用方向键或者 WAXD 滚动。
-   M 和 N 是旋转。
-   如果给定了多个文件，, 和 . 是翻页。
-   Q 是退出。
-   更多操作请自行摸索……欢迎补充 ^\_^

Arch 用户使用 pacman -S fbv 安装。其它发行版请补充。

PS. fbv
似乎只有一个临时的官方首页，在[这里](http://www.eclis.ch/fbv/ "fbv 临时主页")。源码库在[这里](http://repo.or.cz/w/fbv.git "fbv 源码库")。
