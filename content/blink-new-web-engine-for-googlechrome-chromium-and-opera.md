Title: Blink: Google Chrome/Chromium 及 Opera 的新 Web 渲染引擎
Date: 2013-04-04 10:28
Author: lovenemesis
Category: Web Browser
Tags: chrome, Opera, Webkit
Slug: blink-new-web-engine-for-googlechrome-chromium-and-opera

Google 宣布将在未来的 Google Chrome/Chromium 中使用基于 WebKit 的 fork
Web 渲染引擎：Blink。同时 Opera 表示也将跟进 Google Chrome/Chromium
的步伐。

Google Chrome/Chromium 从创始至今一直使用 WebKit(WebCore) 作为 HTML/CSS
渲染引擎。WebKit 早先由 Apple 由 KHTML 项目 fork 出来，用于 Safari
浏览器的 Web 引擎。由于宽松的协议、轻量级的设计和便捷的应用程序内嵌
API，WebKit 逐渐变得流行起来，除了 Google Chrome/Chromium 和
Safari，它在移动终端（ Symbian S60，Android，iOS）到 Toolkit 集成(GTK+,
Qt4) 都有不错的收获。

尽管上面一众经常被统称为 WebKit，实际上各自都使用了自己的 WebKit
分支或者编译时选项，使得最终的渲染结果也是存在一定的差异的。不过大体上
WebKit
社区内部还是比较和谐的，各个成员之间也为维持兼容性作出了努力，直到 2010
年随着 OS X Lion 一起面世的 WebKit2。由于 WebKit2 在 WebCore
层面上实现的进程隔离在一定程度上与 Google Chrome/Chromium
自己的沙箱设计存在冲突，故 Google Chrome/Chromium 一直停留在
WebKit，使用 Backport 的方式实现和主线 WebKit2 的兼容。显而易见这增加了
WebKit 和 Chromium 的复杂性，且在一定程度上影响了 Chromium
的架构移植工作。

基于以上原因，Google 决定从 WebKit fork 出自己的 Blink Web 引擎：

-   现阶段以精简内部结构为主，将删除大约 7000 个文件和 450 万行 WebKit2
    兼容代码。
-   未来将着重改善 DOM 架构，将使用 JavaScript 实现 DOM。
-   提升安全性，实现进程外 `iframes` 。

对于今年初宣布放弃自有渲染引擎跟随 Chromium 的 Opera
来说，其开发者也立刻发布博客公告 Opera 亦将切换至 Blink 引擎。

[详细 Blink 开发者 FAQ](http://www.chromium.org/blink/developer-faq)

[Chromium
官方公告](http://blog.chromium.org/2013/04/blink-rendering-engine-for-chromium.html)

[Opera 开发者公告](http://www.brucelawson.co.uk/2013/hello-blink/)
