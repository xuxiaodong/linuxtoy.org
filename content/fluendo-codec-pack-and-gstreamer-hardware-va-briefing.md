Title: Fluendo Codec Pack 及 GStreamer 硬件加速简述
Date: 2012-06-22 10:55
Author: lovenemesis
Category: Featured
Slug: fluendo-codec-pack-and-gstreamer-hardware-va-briefing

[Fluendo Codec
Pack](http://www.fluendo.com/shop/product/complete-set-of-playback-plugins/)
是来自于 GStreamer 主要开发者之一 Fluendo
发布的多媒体解码包集合，可以提供在 GStreamer
框架下**合法的版权媒体格式播放**以及**各类显卡的硬件加速**支持。

先看看来自官方的产品说明：

-   完整的 Windows Media 音视频支持，包括**无损音频**和 **VC1
    高清视频**以及对应的分离器。
-   完整的 MPEG2 和 MPEG4 Part 2 解码，并包含 Divx 3.11 Alpha 支持。
-   支持 H264/AVC 高清解码。
-   MP3/AAC/LPCM/iLBC/ADPCM/Dolby Digital plus 音频解码支持。
-   流媒体支持。
-   在一个二进制包中提供对 **AMD XvBA, Intel VAAPI & NVIDIA VDPAU GPU
    硬件加速**的即插即用支持。

值得注意的是解码包中并不包含 Real Media
的内容，若需要播放此类媒体仍需要安装 gstreamer-ffmpeg
插件。该插件可以和此解码包同时安装，在遇到两者都可播放的格式时会优先使用
Fluendo 解码包。

目前最新版本是 17（尽管页面上是标明的是 16），产品[定价 28
欧元（(延长升级费用每年仅为 5～7
欧元)）](http://www.fluendo.com/shop/product/complete-set-of-playback-plugins/)，可以**使用
PayPal 银联卡付款**。购买后可以选择下载 32 位、64 位的通用二进制包，或者
DEB 及 RPM 包，甚至提供 OpenSolaris 安装包，不限次数。

经过近两周的使用以及和客服的沟通(态度和响应时间都很赞)，结合对于散布于论坛中对于
**GStreamer 硬件加速**的讨论，大致总结一下。

目前 GStreamer 领域的硬件加速方案有两种，[来自 Splitted Desktop Systems
的开源 gstreamer-vaapi
方案](http://www.phoronix.com/scan.php?page=news_item&px=ODIzNA) 和来自
Fluendo 的闭源 fluva 方案（应用于上文的 Codec Pack 中）。

gstreamer-vaapi 可以用过 vdpau-vaapi 或者 xvba-vaapi 的方式实现对于
NVIDIA 或者 AMD
闭源驱动下的硬件加速支持，不过恐怕是由于**间接调用**，至少 xvba-vaapi
的效果不甚理想。

Fluendo 的 fluva 则是**直接调用** VAPAU 或者 XvBA 实现 NVIDIA 或者 AMD
闭源驱动下硬件加速，保证了高性能的解码。

但是现阶段的两款 GStreamer 硬件加速都有以下两个局限：

-   目前 [Totem 3.4 使用的 clutter-gst 有
    Bug](http://gstreamer-devel.966125.n4.nabble.com/Gstreamer-VAAPI-and-Totem-td4655188.html)，会导致
    fluva 的硬件加速无法启用。该问题已经在上游解决，将随 Totem 3.6
    发布。目前可以暂用不依赖 clutter-gst 的 GStreamer 播放器如
    [Parole](http://goodies.xfce.org/projects/applications/parole)
    替代。使用 Totem 3.2 的 Ubuntu 12.04 不受该问题影响。
-   由于当初 GStreamer
    的字幕插件设计考虑不周，目前在加载字幕后将无法使用硬件加速。该问题
    Fluendo 正在开发[新的 GStreamer
    字幕插件](http://forums.gentoo.org/viewtopic-t-912868-start-0.html)解决此问题，并且允许将字幕的渲染也交给
    GPU 硬件加速。

*假如显卡不支持硬件加速或者硬件加速性能不理想，那么这个 Codec Pack
对我有意义么？*

于是在下退回到 Radeon Gallium3D 驱动，使用下列样片与 gstreamer-ffmpeg
ffdec\_h264、mplayer 1.1 ffmpeg 和 VLC 2.0.2 libav
进行**软件解码比较**。

测试样片信息：

-   源..........: Evangelion 2.22: You Can (Not) Advance 2009 Blu-ray
    1080p AVC TrueHD/DTS-MA 6.1
-   视频位率...: x264 @ 9337 Kbps High Profile Level 4.1
-   色彩空间...: YUV
-   子采样...: 4:2:0
-   帧速......: 23.976 fps
-   音频.........: JPN DTS-ES6.1 768 Kbps
-   片长 ........: 01:52:09 (h:m:s)
-   分辨率......: 1920 X 1080

[测试平台硬件信息](http://www.smolts.org/client/show/pub_79c55d9b-ea8d-45f5-8159-fb546e8d06f6)

结果：

-   使用 gstreamer-ffmpeg ffdec\_h264 的 Totem/Parole
    音视频不同步，音频流畅但是视频卡住。
-   VLC 2.0.2 libav
    可以实现音视频同步，但是视频马赛克十分严重，完全不能观看。
-   Mplayer 1.1 ffmpeg 音视频部分不同步，视频每隔 10 秒左右就卡住了。
-   使用 Fluendo fluh264dec 的 Totem/Parole
    可以**十分流畅的播放该片，没有马赛克。**

由此可见 Fluendo 的 H264
软解码器效率非常出色。不过就算如此，也难以避免软解码时 CPU
占有率过高的通病。

**总结**

Fluendo Codec Pack 适用于什么群体呢？

-   懒得折腾，希望获得开箱即用的 GPU 硬件加速支持的 Linux 用户。
-   想在不具备硬件加速条件的设备上观看 1080P 高清视频的 Linux 用户。

如果您符合以上两类群体之一，不妨考虑下 Fluendo Codec Pack。

**PS：**在此感谢 @doublechou 在初期提供早期版本测试。
