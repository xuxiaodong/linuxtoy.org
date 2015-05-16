Title: Wine 1.6.0
Date: 2013-07-19 08:26
Author: lovenemesis
Category: Emulator
Tags: Wine
Slug: wine-1-6-0

开源的 Win32/64 API 实现 Wine 发布了 1.6 正式版，代表着长达 16
个月紧张开发的成果。

本次发布包含多达 10000 个变更，其主要改善有：

-   在 OS X 平台上不再依赖 X11，使用原生驱动实现。
-   通过 DIB 引擎使用客户端渲染窗口（除了 OpenGL
    调用），且支持透明及缩放。
-   移除所有 X11 所有调用锁，不再支持服务器端字体，新增 XRandR 1.2 及
    1.3 支持。
-   允许自由安装通过 Mono 实现的 .Net 应用支持。
-   Gecko HTML 引擎升级至 21 版本，优先调用 Wine 内置 JavaScript 引擎。
-   改善 DX9/DX10 实现，且为 OpenGL 调试输出提供更多信息。
-   在 Linux 平台支持 UDisk2 服务支持，允许构建 ARM64 版本，初步实现
    Android 平台构建。

[完整英文发布公告](http://www.winehq.org/announce/1.6)

[二进制及源代码包下载](http://www.winehq.org/download)
