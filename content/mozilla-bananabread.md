Title: Mozilla BananaBread
Date: 2012-08-29 00:33
Author: lovenemesis
Category: Games
Tags: html5, Mozilla
Slug: mozilla-bananabread

一年前有人 [JavaScript 版本
Doom](http://linuxtoy.org/archives/javascript-doom.html)
作为技术演示问世，现在 Mozilla 用 BananaBread
来展示这一年来技术上的进步。

和原先人工移植的 Doom 不同，BananaBread 使用
[Emscripten](http://linuxtoy.org/archives/emscripten.html) 将原先 C++
编写的游戏引擎 Cube2 移植到 JavaScript
上，仅做了少量更改即可让其在浏览器环境下运行。

[![](http://linuxtoy.org/img/2012/08/bananabread.png "bananabread")](http://linuxtoy.org/img/2012/08/bananabread.png)

从截图中可以看出其在特效和场景上有了长足的进步，支持全屏模式和鼠标指针捕获和
[Quake Live](http://linuxtoy.org/archives/quake-live-on-web.html)
已经不相上下。

和仅限于 Google Chrome/Chromium 的 Native Client 技术不同，使用
[Emscripten](http://linuxtoy.org/archives/emscripten.html) 得来的
BananaBread 具有良好的跨浏览器性能。Google Chrome/Chromium
用户记得需要打开默认关闭的 `Pointer Lock` 使得其可以捕捉鼠标指针。

开发人员表示下一步将尝试把 C# 和 Java 移植到 JavaScript
上使其可以在浏览器环境下运行。

[亲测场景2
屏幕录像(低分辨率模式)](http://youtu.be/EeD3xSawJnc)（[朝内视频镜像](http://v.youku.com/v_show/id_XNDQ0NDYyMTM2.html)）

[测试用机配置](http://www.smolts.org/client/show/pub_79c55d9b-ea8d-45f5-8159-fb546e8d06f6)
使用 Firefox 15 Beta 及 AMD Catalyst 12.8。

[Mozilla BananaBread
演示页面](https://developer.mozilla.org/en-US/demos/detail/bananabread)

消息来源：[Mozilla
Hacks](https://hacks.mozilla.org/2012/08/mozilla-and-games-pushing-the-limits-of-whats-possible/)
