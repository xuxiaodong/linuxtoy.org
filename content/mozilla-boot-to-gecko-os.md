Title: Mozilla Boot-To-Gecko OS
Date: 2011-11-09 11:55
Author: lovenemesis
Category: Embedded
Tags: html5, Mozilla
Slug: mozilla-boot-to-gecko-os

来自 Mozilla 基于 HTML5 和
[WebAPI](http://linuxtoy.org/archives/mozilla-webapi.html)的手机操作系统
Boot-To-Gecko(B2G) 预期将在 2012 年第二季度就绪。

从某种角度上看，B2G 系统是 Android 和 ChromeOS 的结合，跟
[Tizen](http://linuxtoy.org/archives/linux-meego-tizen.html)有些相似：

-   使用**源自 Android 的内核、驱动和部分底层库**，从而保证设备兼容性。
-   **移除 Android 的 Dalvik 虚拟机**架构，于是不再需要 Java，免于
    Oracle 的专利纠纷。
-   将**部分融合 Chrome 浏览器/ChromeOS 的
    [NativeClient](http://linuxtoy.org/archives/google-chrome-14-beta.html)
    技术**。
-   实现**名为 Gaia
    的用户界面**（见下图），包含浏览器、设置程序、媒体播放器和应用商店等，以及相机和电子书阅读。

[![](http://linuxtoy.org/img/2011/11/wireframes1.png "wireframes1")](http://linuxtoy.org/img/2011/11/wireframes1.png)

一些关于 B2G 的细节和说明：

-   将参考 [Fennc Virtual
    Keyboard](https://addons.mozilla.org/en-US/mobile/addon/virtual-keyboard-for-fennec/)
    实现**基于 HTML5 的输入法框架**。
-   与 [Webian Shell](http://linuxtoy.org/archives/webian-shell.html)
    有很多共通之处，但是前者着重于桌面体验，而 B2G 着重的手机移动体验。
-   目前处于早期阶段，所以尚未和 OEM
    接触，同时也**没有发布自有品牌的手机的计划**，短期内分发模式可以参考
    CyanogenMod 或者 MIUI。
-   **B2G 目标不是成为新的编程平台**，而是将成为 HTML5/CSS3/JavaScript
    在移动设备上的延伸和扩展，现有网页开发者无需学习其他技术如 Java。
-   根据路线图目前**开发者已经在使用搭载 B2G
    的开发机**了，而明年第二季度就将实现分发状态。

[B2G Wiki](https://wiki.mozilla.org/B2G/)

[B2G FAQ](https://wiki.mozilla.org/B2G/FAQ)

[B2G 路线图](https://wiki.mozilla.org/B2G/Roadmap)

*消息来源：*[Linux
Device](http://www.linuxfordevices.com/c/a/News/Mozilla-Boot-to-Gecko-roadmap-released-plus-Firefox-8/?kc=rss)
