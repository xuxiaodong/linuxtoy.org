Title: GStreamer 1.4
Date: 2014-07-22 16:05
Author: lovenemesis
Category: Movie Player
Tags: Gstreamer
Slug: gstreamer-1-4

广泛应用于 Linux 平台的多媒体框架 GStreamer 发布 1.4 版本，在保持 1.X
API 兼容性的前提下带来了不少变化。

新功能有：

-   可以直接使用 OpenGL 作为视频作业流水线的一部分，无需 Clutter。
-   引入 `v4l2videodec` 元素用来访问通过 V4L2
    接口暴露出来的硬件解码器，比如 Exynos 系列 SoC。
-   重新设计了下载缓冲元素。
-   引入 `audiomixer` 元素可以将多个音频流混音成一个且保持音画同步。
-   增加 OpenNI2 以支持 Kinect，OpenEXR 以支持 EXR 图像。
-   增加 `curlsshsink` 及 `curlsftpsink` 从而实现 SSH/SFTP 文件写入。
-   将一些 0.10 时期的插件迁移到 1.X 架构。
-   gst-libav 升级至 libav 10.2 版本，增加 H265/HEVC 支持。
-   重新设计了 `waylandsink`，未来将进一步改善以更好地支持 Wayland。
-   包含 800+ 处错误修复。

如无意外，GStreamer 1.4 将随着年底发布的各大发行版与最终用户见面。

[官方邮件列表发布公告及源代码下载](http://lists.freedesktop.org/archives/gstreamer-announce/2014-July/000322.html)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTc0NTg)
