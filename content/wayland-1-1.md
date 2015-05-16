Title: Wayland 1.1
Date: 2013-04-17 12:06
Author: lovenemesis
Category: Desktop Stuff
Tags: wayland
Slug: wayland-1-1

Wayland 显示服务协议及参考混成器 Weston 发布 1.1 版本，带来了 Raspberry
Pi 和远程桌面支持。

本次发布是即去年年底 [1.0
版本发布](http://linuxtoy.org/archives/wayland-1-0.html)后的首个正式发布，带来的功能亮点有：

-   为 Weston 增加可用于 Raspberry Pi 的渲染后端。
-   增加 Pixman 渲染后端，允许使用基于软件方式混成。
-   增加支持 Remote Desktop Protocol 的渲染后端，实现远程桌面。
-   增加支持 FBDEV 设备的后端，开启了未来向 FreeBSD 移植的可能。
-   新增模块 SDK，便于开发主线外的模块。
-   其 KMS 后端增加对 EGL buffer-age
    扩展的支持，预期将带来更好的混成性能。
-   支持触摸屏校准，且提供配置工具。
-   进行了多处优化，并完善了文档。

[邮件列表发布公告](http://lists.freedesktop.org/archives/wayland-devel/2013-April/008631.html)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTM1Mjk)
