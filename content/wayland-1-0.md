Title: Wayland 1.0
Date: 2012-10-23 12:49
Author: lovenemesis
Category: Server
Tags: wayland
Slug: wayland-1-0

X11 Server 替代品 Wayland 发布 1.0 正式版本，宣布了 API/协议稳定。

Wayland 作为下一代的图形服务器，目的是替代有 25 年历史的 X11
Server。Wayland 关注于近年来 Linux
在桌面领域的改善，通过将**部分图像处理工作交由 Linux 内核提供的
GEM(Graphic Execution Manager)和 KMS(Kernel
Mode-Setting)**实现，大幅度缩减了图形服务器的体积和工作开销。

除此之外，Wayland 还提供了**运用 EGL 或 GLX 的混合器 Weston**
，充分利用客户端直接渲染的方式，可以有效的提高图形界面的相应速度，并且实现诸如异性窗口等原先难以达到的功能。

Wayland 的专注在带来更高性能的同时引入了一些弊端，比如尚未实现类似 X11
Server 一样的远程网络显示，过分依赖 Linux 内核导致难以移植到其他类 Unix
操作系统上，以及**对于 KMS 的依赖导致短期内不会有闭源驱动厂商**支持等。

Wayland 1.0 的发布 Linux
桌面最终用户来说意义不大，各大**今年末甚至明年初发布的发行版恐怕仍将默认使用
X11 Server 作为图形服务器**。对于各种桌面环境和 GUI
工具集开发者意义则代表着他们可以开始参照承诺未来版本向后兼容的 Wayland
1.0 的 API 进行迁移工作。

[官方发布公告及源代码包下载](http://lists.freedesktop.org/archives/wayland-devel/2012-October/005967.html)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTIxMzA)
