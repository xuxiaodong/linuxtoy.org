Title: Wayland 1.2
Date: 2013-07-14 00:06
Author: liangsuilong
Category: Apps, Distros, Embedded
Tags: Sailfish, wayland
Slug: wayland-1-2

Wayland 1.2 在今天发布了。

本次发布的亮点：

-   Wayland/Weston 色彩管理
-   Wayland 输入法框架
-   支持 Sub Surface 协议，允许从多个 Wayland Surface 创建程序窗口
-   适应 HiDPI 分辨率界面输出
-   Raspberry Pi 新渲染器以及后端
-   Wayland 客户端库改进线程安全
-   Wayland 服务器 API 认定为稳定
-   根据 udev 属性改进多头显示的配置
-   提供了一个用于说明 Wayland 合成器原理的客户端
-   XKB Common 库可以作为一个可选项用于 Wayland 没有完整键盘支持的场景
-   其他若干小修复

[官方发行公告](http://lists.freedesktop.org/archives/wayland-devel/2013-July/010278.html)

另外根据 Jolla
公司的官方[鸟嘀咕时间线](https://twitter.com/JollaHQ)上的表述，Sailfish
OS 将会使用 Wayland 作为显示服务器，但不会支持 XWayland，也就是不会有
X11 程序的支持。 以下是 Sailfish OS 的架构图。

[![sailfish-os-arch](http://lt-file.b0.upaiyun.com/files/2013/07/sailfish-os-arch-300x200.jpg)](http://lt-file.b0.upaiyun.com/files/2013/07/sailfish-os-arch.jpg)

**补充 By 黑日白月**

感兴趣的童鞋可以[下载 Wayland 1.2 的 RebeccaBlackOS
LiveCD](http://sourceforge.net/projects/rebeccablackos/files/latest/download?source=files)进行测试，其含有打开了
Wayland 支持的 GTK3+/Qt5/SDL/EFL 。注意根据反馈似乎 Nouveau 的 KMS
实现存在缺陷，请使用 Intel 或 AMD
显卡进行测试。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTQxMDQ)
