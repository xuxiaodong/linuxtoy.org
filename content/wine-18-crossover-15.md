Title: Wine 1.8 及 CrossOver 15
Date: 2015-12-21
Author: lovenemesis
Category: Emulator
Tags: wine, crossover
Slug: wine-18-crossover-15
Summary: 经过长达17个月的开发，开源的 Win32/64 API 实现 Wine 发布了 1.8 版本，基于其的商业解决方案 CrossOver 也随着发布了 15.0 版本。

Wine 1.8 带来的改善有：

* 对于 PulseAudio 的全新驱动，包括 5.1 环绕
* 更好的视频解码支持
* OLE 嵌入得到了支持
* 实现 DirectWrite 和 Direct2D 
* 将 Direct3D 11 支持到于当前 Direct3D 10 [一样的支持程度](https://www.codeweavers.com/about/blogs/caron/2015/12/10/directx-11-really-james-didnt-lie)（读作：可以运行非常简单的程序），并且现阶段不支持运行在 Mesa 上。
* 支持 64 位 Android
* 升级 Gecko 至 Firefox 40 版本，完善了 HSHTML 的功能
* 在 X11 下支持 X Drag & Drop 协议第五版本
* Wine 支持伪装为 Win8.1 或 Win10

[完整英文更新日志](https://www.winehq.org/announce/1.8)
[官方下载](https://www.winehq.org/download)

而基于其上的 CrossOver 15.0 则带来了：

* 基于 Wine 1.8-rc2 的更新内核
* 完全重写了图形界面，简化了安装和管理软件的流程

[官方发布公告](https://www.codeweavers.com/about/news/press/20151208)
