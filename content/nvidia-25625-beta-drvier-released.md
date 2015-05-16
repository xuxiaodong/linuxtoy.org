Title: NVIDIA 官方二进制 256.25 Beta 驱动发布
Date: 2010-05-22 21:49
Author: lovenemesis
Category: Drivers
Tags: driver, NVIDIA, proprietary
Slug: nvidia-25625-beta-drvier-released

NVIDIA 官方二进制驱动 2XX 系列发布首个公开 Beta 测试版本，改进颇多。

-   惯例一般地增加了若干非标准 GLX 协议支持。
-   改善对多个温度检测探针的支持。
-   VDPAU 支持 Xinerama
    扩展，可以在多头显示中的其中一个屏幕上进行高清解码渲染。
-   将 VDPAU 支持的 C 类显卡的错误渲染处理提升到和 B 类同样的水平。
-   增加新的VDPAU API 使其共用 OpenGL 和 CUDA 。
-   重命名 libGLcore.so.VERSION 文件，避免和 MESA GL 产生文件名冲突。
-   以前安装文件名字中迷惑的 -pkg# 后缀被废弃，同时增加移除 32
    位库的纯64位驱动包。
-   移除安装文件内几乎没用的预编译内核模块，将全部采取即时编译的方式，但是允许用户自行将内核模块添加进去。
-   改用 bz2 压缩安装文件，减少体积。

[英文完整更新日志及下载](http://www.nvnews.net/vbulletin/showthread.php?p=2255561)

*消息来源：
[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=ODI3Mw)*
