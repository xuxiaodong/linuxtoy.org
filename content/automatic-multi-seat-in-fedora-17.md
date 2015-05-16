Title: Fedora 17 中的自动化多座位支持
Date: 2012-05-17 10:28
Author: lovenemesis
Category: Desktop Stuff
Tags: Fedora
Slug: automatic-multi-seat-in-fedora-17

Fedora 17
从系统底层到应用层全方位为多座位支持进行了改进，已经实现了完全自动化的即插即用多座位体验。

所谓“多座位”，是指一台电脑可以允许多个独立的用户在同一时间使用。

过去的文本操作时代，实现多座位支持对于类 Unix 家族的 Linux
系统来说是水到渠成的事情。但是步入图形化时代之后，这个工作却越发复杂了，牵扯
x.org 配置文件、登录管理器、桌面环境等等。

Fedora 17 开发过程中开发者与 [Plugable
公司](http://plugable.com/)合作，改善了 USB DisplayLink
显卡驱动，在该公司的
[DC-125](http://amzn.com/B004PXPPNA)/[165](http://amzn.com/B002PONXAI)
产品中实现多座位支持的即插即用。

步骤很简单：

1.  使用通用的 USB 2.0 线接线将 DC-125/165 与安装有 Fedora 17 GNOME 3
    的主机相连。
2.  将 DC-125/165 与另外一台显示器、键盘和鼠标相连。
3.  无需任何配置，其他家庭成员就可以在新显示器上通过 GNOME 3
    登录对话框开始使用。

一些具体的实现细节：

-   新接入的终端的图形渲染工作通过 USB DisplayLink 中的 GPU 完成。
-   提供完整的 GNOME Shell 图形加速体验。
-   负责挂载外部设备的 udisks 也得到改善，每个用户仅能看到自己挂载的 USB
    大容量存储设备。
-   Plugable 开源了 USB DisplayLink GPU 全部内容并已合并入上游。
-   该功能的实现依赖于 systemd，故不会在使用 Upstart 的 Ubuntu 中出现。
-   该功能亦可在其他使用 USB DisplayLink GPU
    的多座位支持设备上实现，只需做少量修改。
-   该功能向后兼容新生代 X 服务器 Wayland。
-   后续将增加一个图形化的配置工具提供多座位支持的微调。
-   目前仅在 GNOME 3 环境下实现，KDE 4 的支持正在和上游商讨中。

[博客介绍](http://0pointer.de/blog/projects/multi-seat.html)

[此项功能在 Fedora 17
中的描述](http://fedoraproject.org/wiki/Features/ckremoval)
