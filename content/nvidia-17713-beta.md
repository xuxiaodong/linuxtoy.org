Title: Nvidia 177.13 Beta 驱动发布
Date: 2008-06-20 12:59
Author: lovenemesis
Category: Drivers
Tags: NVIDIA
Slug: nvidia-17713-beta

继 Nvidia 于6月17日发布 Geforce 显卡驱动 For Linux 修正版 173.14.09
后，近日又发布了 177.13 Beta版本。该版本中增加了对最新发布的Geforce
GTX200 系列的支持。该版本在相比于早先发布的**稳定版173.14.05**，**修正版
173.14.09** 有如下变化：

-   修正在X.org Server 1.5下别名字体渲染错误的问题。
-   修正了在 Quadro FX 1700 显卡双头输出错误的问题。
-   修正了在部分 GeForce FX/6/7 系列显卡上阻止 X 驱动载入的回归错误。
-   修正了 nvidia-settings 中的一个场所交互分析错误。
-   为 Linux 2.6.26 内核提供了有限支持。

**Beta 版 177.13** 在以上基础上增加了对以下GPU的支持：

-   GeForce GTX 260
-   GeForce GTX 280

177.13 Beta
32位版本下载地址[见这里](http://www.nvidia.com/object/linux_display_ia32_177.13.html)，64位版本[见这里](http://www.nvidia.com/object/linux_display_amd64_177.13.html)。

转载自 Phoronix
，英文原文[见这里](http://www.phoronix.com/scan.php?page=news_item&px=NjUzMA)。

**PS:** 留给“不慎”进入此 Nvidia 驱动发布说明的 ATi 用户的好消息：

1.  AMD 已经决定从 HD 4000 系列开始在产品包装盒上标明对 Linux
    系统的支持。
2.  在 AMD 最近一次贡献给开源驱动开发者的文档中包含了关于 HD
    4000系列的内容，初步结果 AMD HD 4850 已经可以在开源的 xf86-video-ati
    驱动下使用，目前正在进一步测试。
3.  （6月22日更新）最新发布的 Linux 2.6.26-rc7 中增加了对 R500 DRM
    的支持，并且更新了所有 Radeon GPU 的微代码。

