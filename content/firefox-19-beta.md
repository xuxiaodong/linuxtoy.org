Title: Firefox 19 Beta
Date: 2013-01-11 10:21
Author: lovenemesis
Category: Android
Tags: Firefox, Mozilla
Slug: firefox-19-beta

Mozilla 发布跨平台开源浏览器 Firefox 19 Beta 版本，整合了完全基于 HTML5
技术的 PDF 阅读器，移动版本则实现了中文本地化。

**桌面版本**新功能有：

-   整合基于 HTML5 的
    [pdf.js](http://linuxtoy.org/archives/pdfjs-02218.html) 阅读器。
-   允许重置 Awesome Bar 搜索引擎为默认值。
-   使用 `canvas.toBlob()` 可以[将 Canvas
    元素内容输出为图片](https://hacks.mozilla.org/2012/10/firefox-development-highlights-viewport-percentage-canvas-toblob-and-webrtc/)。
-   [改善启动速度](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=715402%2C756313)
-   调试器支持在遇到异常时暂停，且可以跳过非可递归属性。
-   远程网络终端允许连接至 Firefox for Android 及 Firefox OS，将
    `devtools.debugger.remote-enabled` 设为 `true`。
-   为浏览器和插件开发者提供了试验性浏览器调试器，将
    `devtools.chrome.enabled` 设为 `true` 即可看到。
-   在网络终端中点击 CSS 链接将打开样式编辑器。
-   支持 CSS [@page](https://developer.mozilla.org/en-US/docs/CSS/@page)
    属性。
-   实现 CSS `viewport-percentage`
    [长度单位](https://developer.mozilla.org/en-US/docs/CSS/length#Viewport-percentage_lengths)属性。
-   CSS text-transform 现在[支持
    full-width](https://developer.mozilla.org/en-US/docs/CSS/text-transform)。
-   修复使用 `-private` 标示启动 Firefox 未提示在隐私模式的问题。

除此之外，**Android 版本**还包含有如下改善：

-   实现了主题支持。
-   增加了**正体中文和简体中文的支持**。
-   降低 CPU 主频最低要求至 600MHz。
-   修复了使用退格键可能删除光标前后两个字母的问题。

[完整英文发行日志](https://www.mozilla.org/en-US/firefox/19.0beta/releasenotes/)

[全平台官方下载](https://www.mozilla.org/en-US/firefox/beta/)

PS: 若是您也在 Win 或者 OS X 平台使用 Firefox 19 Beta，Mozilla
推荐尝试使用 [Flash Player 11.6 Beta 2
版本](http://labs.adobe.com/downloads/flashplayer.html)。
