Title: WebKitGTK+ 2.0
Date: 2013-04-15 10:38
Author: lovenemesis
Category: Development
Tags: webkit2
Slug: webkitgtk-2-0

WebKit 的 GNOME ~~绑定~~ 平台移植 WebKitGTK+ 2.0 正式发布，将默认使用
WebKit2 的 API。

本次新功能有：

-   同时提供 WebKit1 和 WebKit2，但将默认使用多进程的 WebKit2，WebKit1
    将进入维护模式。
-   WebKitWebView 本身即为可滚动控件。
-   嵌入式的 HTTP 授权对话框，且可以通过
    [libsecret](https://live.gnome.org/Libsecret) 与系统密钥环管理联结。
-   使用独立进程运行 GTK+ 2 的插件，比如 Adobe Flash Player。
-   Web Inspector 可以在自动在停靠和非停靠状态下运行，且支持远程调试。
-   默认启用内容硬件加速混成，可选[由 Clutter
    提供](http://blogs.gnome.org/joone/2013/03/22/accelerated-compositing-with-clutter/)。

在[下一个版本 2.2
中](http://trac.webkit.org/wiki/WebKitGTK/WebKit2Roadmap)项目组计划实现沙箱、Win32
支持和 Wayland 支持等更多功能。

[详细发布公告及截图](http://blogs.igalia.com/carlosgc/2013/04/11/webkitgtk-2-0-0/)

目前随 GNOME 3.8 发布的 [Epiphany 已经完成了向 WebKitGTK+ 2.0
的迁移工作](https://live.gnome.org/Epiphany/Roadmap/3.8)。另一款轻量级
GTK+ 浏览器 Midori 在[最新发布的 0.5.0 版本中也开始了向 WebKit2
的迁移](http://twotoasts.de/index.php/2013/04/high-five/)。

[WebKitGTK+ 项目首页](http://webkitgtk.org/)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTM0OTI)
