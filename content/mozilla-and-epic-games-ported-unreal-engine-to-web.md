Title: Mozilla 和 Epic Games 将虚幻3引擎移植至 Web (Demo 释出)
Date: 2013-04-01 14:30
Author: lovenemesis
Category: Videos
Tags: Firefox, html5, Mozilla, webgl
Slug: mozilla-and-epic-games-ported-unreal-engine-to-web

Mozilla 显然不满足 [Cube2
引擎带来的视觉效果](http://linuxtoy.org/archives/mozilla-bananabread.html)，这次与
Epic Games 合作将著名的 Unreal 3（虚幻3）引擎移植到了开放 Web
平台，未来的 HTML5/WebGL 游戏将异常多彩。

Mozilla 此次和 Epic Games 的团队合作，在
[Emscripten](http://linuxtoy.org/archives/emscripten.html)
技术的帮助下[仅用了四天就将约一百万行 Unreal 3 引擎移植到 HTML5/WebGL
平台](http://www.h-online.com/open/news/item/Unreal-gaming-from-within-the-browser-1832677.html)，速度可谓惊人。

为了满足 Unreal 3 引擎对于性能的要求，Mozilla 也引入了[高性能的
JavaScript 子集 Asm.js 的新技术和对应的 OdinMonkey
优化器](http://www.h-online.com/open/news/item/OdinMonkey-and-Asm-js-arrive-in-Firefox-Nightly-1828202.html)：

-   Asm.js 是 JavaScript 的子集，可以任何 JavaScript
    解析器下运行，但仅在相应优化器（比如
    OdinMonkey）存在的情况下才能体现性能优势。
-   Asm.js 主要设计初衷是成为 Emscripten 所用 LLVM
    的输出目标语言，可以手写，不过主要还是由 C/C++ 源代码转换而来。
-   OdinMonkey 优化器构建在长时 JavaScript 引擎 IonMonkey
    框架之上，对于非 Asm.js 的 JavaScript
    长时应用亦有改善。目前已完成桌面版本的 OdinMonkey，ARM
    移动版本即将完成，将于 Firefox 22 与公众见面。

[视频演示](http://www.youtube.com/watch?v=XsyogXtyU9o&feature=player_embedded)（[朝内镜像](http://v.youku.com/v_show/id_XNTMzNzYyNjY0.html)）

[官方发布公告](https://blog.mozilla.org/blog/2013/03/27/mozilla-is-unlocking-the-power-of-the-web-as-a-platform-for-gaming/)

**2013 年 5 月 7 日更新：** [该 Demo
已经放出供公众测试体验](http://www.unrealengine.com/html5/)，推荐使用
Firefox 23+ 版本，截至更新的稳定版本 Firefox 20
亦可。[发布公告](http://www.unrealengine.com/en/news/epic_games_releases_epic_citadel_on_the_web/)
