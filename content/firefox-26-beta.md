Title: Firefox 26 Beta
Date: 2013-11-01 10:40
Author: lovenemesis
Category: Android
Tags: Firefox
Slug: firefox-26-beta

Mozilla 释出 Firefox 26 的第一个 Beta 版本，默认启用了 Linux 平台 H264
GStreamer 解码支持。

本次**桌面版本**的变更有：

-   除了最新版本的 Flash
    Player，其他插件一律默认为[点击播放](https://blog.mozilla.org/futurereleases/2013/09/24/plugin-activation-in-firefox/)。
-   密码管理器现在支持通过脚本生成的密码区域。
-   在 Win
    平台上普通用户亦可通过维护服务完成升级，哪怕没有安装目录写权限。
-   在安装合适 GStreamer 解码器的情况下启用 Linux 平台 H264 解码支持。
-   将 MP3 音频解码支持扩展至 XP 系统。
-   CSP 实现现在支持多重规则。
-   Social API 增加 [SocialMarks
    功能](https://developer.mozilla.org/en-US/docs/Social_API)，支持多个社会化书签提供商。
-   当网站使用 appcache 时不再弹出提示。
-   支持 CSS 图片方向信息。
-   新的应用管理器允许在 FirefoxOS 手机和 FirefoxOS 模拟器上部署和除错
    Web 应用程序。
-   IndexedDB
    允许以优化方式当作临时存储使用，不会弹出任何提示，数据也会以 LRU
    方式移除。
-   当显示一个单独图片时，会[依据 JPEG EXIF
    的方向信息旋转图片](https://bugzilla.mozilla.org/show_bug.cgi?id=298619)。
-   [改善页面载入速度](https://bugzilla.mozilla.org/show_bug.cgi?id=847223)，不再解码当前不可见的图片内容。
-   在 OS X 平台上实现 AudioToolbox MP3 后端。

[桌面版本下载](https://www.mozilla.org/firefox/beta/)

Android 版本的变化有：

-   改善启动主页面，增加常见站点缩略图。
-   密码管理器现在支持通过脚本生成的密码区域。
-   改善在 NVIDIA 设备上的性能。
-   CSP 实现现在支持多重规则。
-   当网站使用 appcache 时不再弹出提示。
-   支持 CSS 图片方向信息。
-   IndexedDB
    允许以优化方式当作临时存储使用，不会弹出任何提示，数据也会以 LRU
    方式移除。
-   当显示一个单独图片时，会[依据 JPEG EXIF
    的方向信息旋转图片](https://bugzilla.mozilla.org/show_bug.cgi?id=298619)。
-   [改善页面载入速度](https://bugzilla.mozilla.org/show_bug.cgi?id=847223)，不再解码当前不可见的图片内容。
-   修复在部分情况下[地址栏隐藏后不再更新页面内容的问题](https://bugzilla.mozilla.org/show_bug.cgi?id=928977)。
-   修复 position:fixed
    的[无效渲染问题](https://bugzilla.mozilla.org/show_bug.cgi?id=923969)。

[移动版本下载](https://www.mozilla.org/mobile/beta/)

[英文发布公告](https://www.mozilla.org/en-US/firefox/26.0beta/releasenotes/)
