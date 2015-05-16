Title: AMD 发布开源 UVD 支持
Date: 2013-04-03 11:38
Author: lovenemesis
Category: Drivers
Tags: AMD, uvd, vdpau
Slug: amd-releases-open-source-uvd-support

AMD 放出了 Radeon 系列显卡 UVD 视频解码单元的开源驱动支持。

由于 UVD
硬件解码单元的开源驱动支持可能会牵扯到其他系统中数字版权管理(DRM)，这方面的进展一直非常缓慢，以至于大多数人都觉得不可能了。在此期间
AMD 发布了 XvBA 接口，允许使用 Catalyst 闭源驱动访问 UVD
硬件解码单元，不过该 XvBA 仅有少数几个程序使用（Fluendo Codec Pack 及
XMBC），接受度很低。

直到今天 AMD 发出了 UVD 硬件解码单元的开源驱动支持：

-   **支持 Radeon 4000 及以后显卡的中的 UVD2
    及以后的硬件解码单元**，Radeon 2000 中的 UVD 和 Radeon 3000 中的
    UVD+ 单元亦可使用但支持有限。
-   H.264、VC-1 及 MPEG2/4 的解码工作将由 UVD 单元完成，显著降低 CPU
    占有率。
-   UVD 硬件解码单元将通过目前应用最为广泛的 VDPAU
    接口访问，意味着现有支持 VDPAU 接口的媒体播放程序将可以直接使用 UVD
    硬件解码单元。
-   该支持涉及内核、DRM 及 Mesa 方面的变更，将合并入 Kernel 3.10 及 Mesa
    9.1/10.0。

目前适用于 Radeon 7000 系列开源显卡驱动 RadeonSI 中的 UVD3
支持补丁已经现身，更多的 UVD
支持将陆续发布。这意味着在今年下半年的发行版中 AMD
用户很有可能得到开箱即用的开源高清视频硬件解码支持。

[各代 Radeon 显卡中的 UVD
硬件解码单元](https://en.wikipedia.org/wiki/Unified_Video_Decoder#UVD_enabled_GPUs)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=article&item=amd_opensource_uvd#=1)
