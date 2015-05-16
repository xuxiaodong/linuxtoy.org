Title: NVIDIA Driver 319.12 Beta
Date: 2013-04-10 09:48
Author: lovenemesis
Category: Drivers
Tags: NVIDIA
Slug: nvidia-driver-319-12-beta

NVIDIA 发布了闭源显卡二进制驱动 319.12 Beta 版本，带来了 RandR 1.4
支持及 SecureBoot 重签名支持。

作为首个 319.XX 系列的驱动，对于最终用户来说可能意义最大的就是 RandR 1.4
支持了。RandR 1.4 增加了新功能之一是允许把支持 Source Output
显卡中的渲染内容输出到支持 Sink Output 的显卡设备上，意味着在使用 NVIDIA
Optimus 技术的笔记本上，可以把在 NVIDIA 独立显卡上渲染的内容输出给 Intel
集显，在 Intel 集显所连接的显示器上显示。

注意该项支持的一些限制：

-   在 X.Org X server 1.13 以上才包含 RandR 1.4 支持。
-   需要内核的中包含最新的 GEM/PRIME 支持。
-   需要使用一个特定的 `xorg.conf` 文件。
-   不支持同步，所以会有渲染撕裂现象。
-   显示设备必须连接至集显所控制的端口上。

[详细 RandR 1.4
支持说明](http://us.download.nvidia.com/XFree86/Linux-x86/319.12/README/randr14.html)

此外这次驱动还引入其他变化：

-   增加对 NVIDIA GeForce GTX 650 Ti BOOST 显卡的支持。
-   安装程序可以对显卡内核模块进行重新签名，以满足 UEFI SecureBoot
    的要求（希望有条件的童鞋能提供更多内容）。
-   在控制中心中增加 VDPAU 页面，显示 PureVideo 可以硬件解码的编码类型。
-   一些内存溢出问题的修复。

[32
位下载](http://www.nvidia.com/object/linux-display-ia32-319.12-driver.html)

[64
位下载](http://www.nvidia.com/object/linux-display-amd64-319.12-driver.html)

[官方发布公告](https://devtalk.nvidia.com/default/topic/539249/unix-graphics-announcements-and-news/-linux-solaris-and-freebsd-driver-319-12-beta-/)
