Title: Firefox 将使用 Cisco 提供的 H264 解码器
Date: 2013-11-01 14:01
Author: lovenemesis
Category: News
Tags: Firefox, h264
Slug: firefox-will-use-cisco-open-h264-decoder

Mozilla CTO Brendan Eich 发表博文，表示 Firefox 将在未来使用 Cisco
刚刚发布的开源 H264 解码器，并大力投入下一代无专利限制的视频编码格式
Daala 的开发。

博文要点：

-   [Cisco 将以 BSD 协议开放其 H264
    解码器](http://blogs.cisco.com/collaboration/open-source-h-264-removes-barriers-webrtc)实现，并提供针对主流操作系统的预编译库文件下载。**Cisco
    将负责承担 MPEG LA 的专利使用费**，并和 Mozilla 共同管理 OpenH264
    开源项目。
-   除非用户明确禁用，预计 2014 年初发布的 Firefox
    将会在**有必要的时候**，自动从 Cisco
    的站点下载预编译库文件并载入，从而允许运行在未内建 H264
    解码器的操作系统上(比如 XP)的 Firefox 支持 H264。
-   此举有利于改善 WebRTC
    视频通讯的跨平台互通性，但是依然还需要解决同样被专利困扰的 AAC
    音频解码器。
-   Firefox 依然支持 VP8 格式，并可在 WebRTC 中使用。Mozilla
    已经组成了开源编码器专家小组开发下一代[无专利限制视频编码格式
    Daala](http://www.xiph.org/daala/)，将以与 H265 和 VP9
    截然不同的方式绕过可能的专利雷区。

补充一些细节说明：

-   Cisco 开放的仅是 H264 解码器，不包含编码器。
-   该结果尽管是来自于 Mozilla 和 Cisco 在 WebRTC
    上的深度合作，不过并未仅限制 Mozilla
    使用，其他开源程序亦可通过类似方式使用该 H264 解码器
-   （合理推测）在已经内建 H264 支持的操作系统上，比如 Win7、OSX 和具备
    GStreamer H264 解码器的 Linux 发行版，将不会下载该解码器。

[博客原文](https://blog.mozilla.org/blog/2013/10/30/video-interoperability-on-the-web-gets-a-boost-from-ciscos-h-264-codec/)
