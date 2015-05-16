Title: Firefox 实现 HTML5 音视频 GStreamer 后端
Date: 2012-04-23 05:52
Author: lovenemesis
Category: Web Browser
Tags: Firefox, html5
Slug: firefox-implement-html5-audio-video-gstreamer-backend

得益于 GStreamer 后端的实现，未来 Firefox 将可以使用系统内置解码器实现
HTML5 音视频的解码和播放工作。

根据[该 Mozilla Bugzilla
上的追踪](https://bugzilla.mozilla.org/show_bug.cgi?id=422540)，目前用于
HTML5 音视频标签播放的 GStreamer 后端支持已经实现并且得到合并许可。

此举意味着 Firefox 将可以通过 GStreamer
作为中介，使用操作系统已经具备的解码包完成 HTML5
音视频的处理工作，带来了如下好处：

-   Firefox 的 HTML5
    音视频格式支持将不再局限由于专利限制的几种。若是用户主系统已经具备
    H264/AAC 解码能力，Firefox 亦可自由使用。
-   避免类似 Google Chrome
    捆绑自有的格式解码器带来的授权和分发协议复杂化，不会给打包者带来额外烦恼。
-   和本地视频一样可以享受用户主系统上的一切优化调优，实现更佳的播放效果，比如硬件解码支持。
-   通过 GStreamer 可以方便的支持包含 B2G 移动版本和 Windows
    平台在内的全部系统，减少针对不同平台内置编码器的维护成本。
-   在具备多个回放设备的系统上（Linux），GStreamer
    的设备侦测和选择更为可靠。

目前还不清楚该后端将会在随哪个 Firefox 版本发布，请留意本站的后续报道。
