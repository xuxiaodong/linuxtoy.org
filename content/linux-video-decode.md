Title: Linux 下的显卡硬解码混战
Date: 2008-11-15 15:35
Author: toy
Category: News
Slug: linux-video-decode

[撰文/guest]

Windows 下有
DXVA，符合规范的解码器能够利用显卡的运算能力进行视频的部分甚至全部解码工作。现在
ATI 的 UVD2 和 NVIDIA 的 PureVideoHD 已经趋于成熟了。Intel 的 ClearVideo
也在进步中。总之使用 Windows 的用户可以尽情享受新型显卡带来的好处。但是
Linux 下的用户就惨了，Linux 下最常用的视频输出就是
xv，能够提供快速的显示，但是对于 UVD2 和 PureVideoHD
的新特性是没有对应的使用方法的。有能力使用显卡进行部分解码的东东是
XvMC。问题是这个东东设计的时候只考虑了 Mpeg2 的完全硬解码。对于
H264，VC1 没有部分对应的解码方法，因此无法对 H264 和 VC1
进行完全硬解码。使用起来也不方便。估计很多的 mplayer
使用者没有指定过 -vo xvmc -vc ffmpeg12mc 来看 mpeg
吧。针对这种情况，多种的解决方案也相应提出来，可是还没有哪个已经成气候。结果就是...现在的
Linux 的显卡硬解码方案是群雄混战……

因为内容都是提供 Linux 下的显卡解码 API，所以下面仅给出链接。

-   **Intel**：
    提出了
    [VA-API](http://www.freedesktop.org/wiki/Software/vaapi)。可是社区讨论认为基本是重复了
    DXVA 的那一套，所以……社区又提出要扩展 XvMC
    以支持更多格式...这个大家去找邮件列表看吧，我不太了解。
-   **ATI**：
    新的 Linux
    驱动中出现了几个使用意图未明的库文件，经过符号分析，发现了 UVD
    字样和 XvBA
    字样。详情看[链接](%20http://www.phoronix.com/scan.php?page=news_item&px=NjcwMA)。UVD
    很清楚了，但是 XvBA 是什么呢？X-Video Bitstream Acceleration
    ([XvBA](http://en.wikipedia.org/wiki/X-Video_Bitstream_Acceleration))
    就是 AMD 扩展 Xv 令其能够执行 Bitstream
    解码，而这个是现在的高清格式解码中很重要的一部分。原来的 GPU
    对于整数运算和位运算基本没有能力，所以早期的显卡很难完成高清格式的完全解码。新的
    ATI 和 NVIDIA
    显卡都针对这种情况内置了相应的硬件。这才能使显卡完全解码成为可能。但是
    AMD
    没有发布相关的说明，驱动也没有相应的头文件，无法调用。因此现阶段只是推测。但是既然库文件中有了这个符号，应该不会有错吧。
-   **Generic GPU-Accelerated Video Decoding**：
    一个 [Google code
    项目](http://code.google.com/soc/2008/xorg/appinfo.html?csaid=ACD6AA025594454A)，也可见于
    <http://www.bitblit.org/gsoc/g3dvl/index.shtml>。一般性的显卡视频解码加速，部分使用了
    OpenGL shader
    来解码，目前发展当中。似乎是没有特定的硬件要求，说明是只要基于
    Gallium3D 的驱动框架就能解码 (Mesa3D 就是用这个的)。目前已经用他自己
    API 实现了 XvMC，这样就提供了兼容性和过渡性方案。
-   今天又有新发现 **[NVIDIA Driver Brings PureVideo Features To
    Linux](http://www.phoronix.com/scan.php?page=article&item=nvidia_180_vdpau#=1)**：
    NVIDIA 的 8 系列显卡的 Linux 驱动将不再支持
    Xvmc，这个激起了相当大的民愤。可是没有想到!!NVIDIA 发出了 180.06
    Linux 驱动，有了个视频解码 API!! VDPAU API (The Video Decode and
    Presentation API for
    Unix)，这个不光有解码，还有解码后处理，如降噪等功能!!更绝的是驱动连同头文件和文档都发布了，更有
    NVIDIA 为 mplayer
    写的开启相关功能的补丁在网站上可供下载!!之后就是[这个页面](http://www.phoronix.com/scan.php?page=article&item=nvidia_vdpau#=1)太厉害了，刚发布就有了
    Benchmarks。结果是使用打过补丁的 mplayer 用 -vo vdpau -vc
    ffh264vdpau 参数来播放高清 H264，结果是降频到 1.8G 的 CPU
    占用率基本为 10%，完全可以证明其硬件加速的能力!

这些消息说明了厂商对 Linux
开发的逐渐重视。但是现在确实是一场大混战...Linux
界尤为明显的一个规律就是优胜劣汰。好东东写出来 N
年后也有人用，糟糕的昙花一现...不知这场大战最终会是个什么结果...但是对于
Linux 用户来说，体验是大大增强了。
