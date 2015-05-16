Title: 轻松启用 Radeon 开源驱动 UVD VDPAU 支持
Date: 2013-08-04 10:25
Author: lovenemesis
Category: Drivers, Featured
Tags: arch, Fedora, radeon, uvd, vdpau
Slug: easy-enable-radeon-opensource-uvd-vdpau-support

Kernel 3.10 在视频方面带来的一个重大变化就是允许开源 Radeon 驱动使用 UVD
进行高清硬件解码。

要实现 Radeon UVD 硬件解码需要满足以下几点：

-   内核 3.10+
-   Libdrm 2.4.45+
-   Mesa 9.2 Git+ 且使用 --enable-vdpau
-   支持 VDPAU 的视频播放器：mplayer, XBMC, VLC 2.1.X

**Fedora 19**

下面先以 Fedora 19 为例说明如何启用，非常简单：

`pkcon install mesa-vdpau-drivers vdpauinfo`

之后可以首先运行 `vdpauinfo` 查看运行结果，比如在 A10-5800K 上：

    display: :0   screen: 0
    API version: 1
    Information string: G3DVL VDPAU Driver Shared Library version 1.0

    Video surface:

    name   width height types
    -------------------------------------------
    420    16384 16384  NV12 
    422    16384 16384  NV12 
    444    16384 16384  NV12 

    Decoder capabilities:

    name               level macbs width height
    -------------------------------------------
    MPEG1                16  9216  2048  1152
    MPEG2_SIMPLE         16  9216  2048  1152
    MPEG2_MAIN           16  9216  2048  1152
    H264_BASELINE        16  9216  2048  1152
    H264_MAIN            16  9216  2048  1152
    H264_HIGH            16  9216  2048  1152
    VC1_SIMPLE           16  9216  2048  1152
    VC1_MAIN             16  9216  2048  1152
    VC1_ADVANCED         16  9216  2048  1152
    MPEG4_PART2_SP       16  9216  2048  1152
    MPEG4_PART2_ASP      16  9216  2048  1152

    Output surface:

    name              width height nat types
    ----------------------------------------------------
    B8G8R8A8         16384 16384    y  NV12 
    R8G8B8A8         16384 16384    y  NV12 
    R10G10B10A2      16384 16384    y  NV12 
    B10G10R10A2      16384 16384    y  NV12 

    Bitmap surface:

    name              width height
    ------------------------------
    B8G8R8A8         16384 16384
    R8G8B8A8         16384 16384
    R10G10B10A2      16384 16384
    B10G10R10A2      16384 16384
    A8               16384 16384

    Video mixer:

    feature name                    sup
    ------------------------------------
    DEINTERLACE_TEMPORAL             -
    DEINTERLACE_TEMPORAL_SPATIAL     -
    INVERSE_TELECINE                 -
    NOISE_REDUCTION                  y
    SHARPNESS                        y
    LUMA_KEY                         -
    HIGH QUALITY SCALING - L1        -
    HIGH QUALITY SCALING - L2        -
    HIGH QUALITY SCALING - L3        -
    HIGH QUALITY SCALING - L4        -
    HIGH QUALITY SCALING - L5        -
    HIGH QUALITY SCALING - L6        -
    HIGH QUALITY SCALING - L7        -
    HIGH QUALITY SCALING - L8        -
    HIGH QUALITY SCALING - L9        -

    parameter name                  sup      min      max
    -----------------------------------------------------
    VIDEO_SURFACE_WIDTH              y        48     2048
    VIDEO_SURFACE_HEIGHT             y        48     1152
    CHROMA_TYPE                      y  
    LAYERS                           y         0        4

    attribute name                  sup      min      max
    -----------------------------------------------------
    BACKGROUND_COLOR                 y  
    CSC_MATRIX                       y  
    NOISE_REDUCTION_LEVEL            y      0.00     1.00
    SHARPNESS_LEVEL                  y     -1.00     1.00
    LUMA_KEY_MIN_LUMA                y  
    LUMA_KEY_MAX_LUMA                y  

**Arch Linux**

<http://pkgbuild.com/~lcarlier/mesa-git/>

**Ubuntu 13.04**

鉴于 Ubuntu 在内核和 Mesa 方面的保守策略，使用 13.04
版本的童鞋请依然参照[本站早先教程自行编译配置](http://linuxtoy.org/archives/how-to-useopen-source-radeon-uvd-on-ubuntu.html)。

由于条件所限，**希望使用其他发行版的童鞋们能在评论中分享所用发行版启用
Radeon UVD VDPAU 的方式**，我将汇总到此文中方便日后参考。
