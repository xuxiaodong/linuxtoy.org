Title: NVIDIA 发布显卡驱动 185.13 Beta
Date: 2009-03-15 15:27
Author: toy
Category: Apps
Tags: NVIDIA
Slug: nvidia-18513-beta-released

{撰文/[liangsuilong](http://liangsuilong.blogspot.com/)}

据 [Phoronix](http://phoronix.com/) 报道，NVIDIA 针对 Linux
平台秘密发布了显卡驱动 185.13 Beta 测试版。之所以用到“秘密”这个词，因为
NVIDIA 没有跟随驱动发布 Changelog，就连在 NV News
也找不到相关的更新信息。

目前已经知道的改进是，X
配置文件增加了两个选项：AllowUnofficialGLXProtocol 和 PanAllDisplays。

> The AllowUnofficialGLXProtocol option will expose the GLX protocol on
> GL commands where the protocol is incomplete.
>
> The PanAllDisplays option will enable panning on all displays as the
> cursor is moved.

而 VDPAU 也有所改进。

另外，据 NV News 说，NVIDIA
驱动的控制面板上的频率检测是跳动的，有别于以前的固定不变。可能 NVIDIA
改进了显卡的电源管理。

不过这个驱动有风险。求稳定的最好就不要尝试了，喜欢追新的朋友可以当一下小白鼠。

下载地址：

x86: <ftp://download.nvidia.com/XFree86/Linux-x86/185.13/>

x86\_64: <ftp://download.nvidia.com/XFree86/Linux-x86_64/185.13/>
