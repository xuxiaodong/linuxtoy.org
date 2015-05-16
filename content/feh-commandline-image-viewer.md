Title: feh: 命令行图片查看器
Date: 2011-08-23 00:00
Author: lovenemesis
Category: Image Viewer
Tags: feh, Terminal
Slug: feh-commandline-image-viewer

看到有人询问命令行下图片查看器，特将自己使用的 feh 分享一下。

它的功能有：

-   支持**多图幻灯片浏览**，可以读取文件夹以及播放列表。
-   **全屏模式**支持，并且可以像数码相框一样定时更换。
-   在指定浏览某路径时，会自动忽略非图片文件，并且**只将当前打开的图片加载入内存**。
-   支持**无损 JPG 旋转**。
-   支持**创建随机照片墙和缩略图**。
-   支持**显示动画 gif 文件**。

当然，经过简单的配置，feh 也可以和图形化的文件管理器如 Nautilus 和
Dolphin 协作，做为默认图片查看器。

*小贴士：*若想其出现在 GNOME 3 的默认应用程序列表中的话，复制已有的 eog
desktop 文件进行编辑即可。

[项目主页](http://feh.finalrewind.org/)

[源代码包下载](http://feh.finalrewind.org/feh-1.15.1.tar.bz2)

Fedora 15 下安装：`pkcon install feh`
