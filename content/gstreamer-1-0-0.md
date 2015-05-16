Title: GStreamer 1.0.0
Date: 2012-09-26 10:19
Author: lovenemesis
Category: Movie Player
Tags: Gstreamer
Slug: gstreamer-1-0-0

经过漫长的开发，GStreamer 终于发布了 1.X 稳定分支的首个版本 1.0.0 。

新的 1.0.0 版本带来的特性有：

-   改善缓冲及事件管理，元数据支持扩展及协商。
-   可以自动重新发送动态流水线的状态。
-   更佳清晰的音视频流水线描述。
-   改进对时间戳的支持。
-   增加对 gobject-inspection 语言绑定的支持。
-   增加视频上叠加层的混成 API
    （编者注：更好的解决字幕显示，并可实现“弹幕”效果）。

**1.X 和现有的 0.10.X API 和 ABI
不兼容，但两者可以同时安装而互不影响**。由于主要的变化影响的是插件开发者，应用程序开发者按照其[迁移指南](http://cgit.freedesktop.org/gstreamer/gstreamer/tree/docs/random/porting-to-1.0.txt)做少量变更即可迁移到
1.X 系列。即将发布的 GNOME 3.6 将依赖 GStreamer 1.0。

[发布公告及源代码包](http://lists.freedesktop.org/archives/gstreamer-announce/2012-September/000265.html)
