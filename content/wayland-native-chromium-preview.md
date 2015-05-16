Title: Wayland 原生版 Chromium
Date: 2013-11-12 10:29
Author: lovenemesis
Category: Web Browser
Tags: Chromium, wayland
Slug: wayland-native-chromium-preview

Intel 开源实验室的工程师们（而不是 Google ）一直在名为 [Ozone-Wayland
的项目](https://01.org/ozone-wayland)下尝试实现 Chromium 的 Wayland
原生支持，现在它们释出了首个预览版本。

该预览版本完全不依赖 XWayland 仅以 Wayland 协议运行：

-   仅提供针对64位 Ubuntu 12.04 和 Fedora 19
    的预编译版本，不支持其他发行版。
-   需要 Mesa 9.2 及 Wayland 1.3 。
-   建议以 `--no-sandbox --profile-directory` 参数运行。
-   仅支持单一窗口，菜单折叠和右键菜单不可用。
-   不支持大写字母输入。

[Tar
包下载地址](https://01.org/ozone-wayland/downloads/2013/chromium-browser-wayland-preview-developers-only)

[官方公告](https://01.org/ozone-wayland/blogs/tiagovignatti/2013/chromium-browser-wayland-preview-release)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTUxMTA)
