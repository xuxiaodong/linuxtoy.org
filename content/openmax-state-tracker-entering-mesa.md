Title: OpenMAX State Tracker 进入 Mesa
Date: 2014-02-08 09:26
Author: lovenemesis
Category: Drivers
Tags: AMD, OpenMAX, radeon
Slug: openmax-state-tracker-entering-mesa

AMD 最近将 OpenMAX 的 State Tracker 提交至 Mesa 主线，将在未来随 Mesa
10.2 版本发布，之后开源的 Radeon UVD 将可以使用OpenMAX 将为**提供 H264
Hi10P 解码**支持，而整合有 VCE 的 AMD APU 和 GPU 将可以实现**硬件加速
H264 编码**。

OpenMAX 是一个由 Khronos Group 开发的平台中立无专利风险的媒体加速
API，尤其得到嵌入式厂商欢迎，也是 Android
系统的硬件编解码的标准接口。不过在桌面 Linux 领域目前似乎仅有 Gstreamer
实现了 OpenMAX 支持。

AMD 此次为 Mesa 增加 OpenMAX State Tracker 主要是为了实现 VCE
视频编码，配合相应的 libdrm 和至少 3.15 版内核，具备 VCE 模块的 AMD
APU/GPU 将可以实现具有硬件加速的 H264 编码。对于最终软件来讲，使用
[Gstreamer 的 OpenMAX
插件](http://cgit.freedesktop.org/gstreamer/gst-omx/)即可。注意当下暂时仅支持
VCE2 模块。

额外的，Radeon UVD 亦可使用 OpenMAX 实现视频解码操作。相比已有的 [VDPAU
接口](https://linuxtoy.org/archives/amd-releases-open-source-uvd-support.html)，最大的好处就是可以实现
[H264 Hi10P
的解码](http://www.phoronix.com/scan.php?page=news_item&px=MTQ5NjU)（动漫宅们，欢呼吧！）。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTU5NDc)
