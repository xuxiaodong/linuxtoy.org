Title: Firefox GTK3 测试版
Date: 2014-01-14 15:09
Author: lovenemesis
Category: Web Browser
Tags: Firefox, GTK
Slug: firefox-gtk3-test-build

Mozilla 将 Firefox 迁移至 GTK3 并移除 X11 特定代码的工作似乎终于会在
2014 年结束了，现在已经有 Firefox GTK3 测试版。  

相比现在 Linux 平台上基于 GTK2 的 Firefox 版本，基于 GTK3
的版本新特性有：

-   在窗口标题栏实现 Firefox 主题效果。
-   实现完全不依赖 X11 的 Wayland 原生支持。
-   移除原先对 X11 的直接访问而转而使用 Cairo，从而实现多点触控。
-   支持[新版 UI
    风格](https://linuxtoy.org/archives/firefox-nightly-introduces-new-ux-australis.html)

无责任猜测 Firefox GTK3 版将会在今年八月份发布的 Fedora 21
生命周期内发布。当下面临的主要问题之一是硬依赖 GTK2 的 Adobe Flash
Player，开发者计划将进一步从主程序独立出 plugin-container，曲线实现
Flash 支持。

[适用于 Fedora 的 Firefox GTK3 测试版 Copr
仓库](http://copr.fedoraproject.org/coprs/stransky/FirefoxGtk3/)

[Mozilla Wiki](https://wiki.mozilla.org/Platform/GFX/GTK3)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTU2OTk)
