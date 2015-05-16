Title: 短消息：Linux 游戏开发相关(3 月 13 日更新)
Date: 2014-03-12 13:29
Author: lovenemesis
Category: Development
Tags: crytek, Mozilla, sdl, unreal, valve
Slug: briefing-linux-gaming-development-related

短消息两条，关于 Linux 平台游戏开发的四则最新消息。

**Valve 以 MIT 协议开源了用于 Source 引擎 Linux 平台移植的中间层
`TOGL`**，该中间层提供了将 API 调用从 Direct3D 翻译到 OpenGL
的功能。通过它上层引擎几乎无需担心底层 API 到底是 Direct3D 还是
OpenGL。本次开源的部分是直接从 DotA2 中复制过来的，仅有限支持
DX9c，实际应用可能比较有限。不过按照[先前公布的资料](https://developer.nvidia.com/sites/default/files/akamai/gamedev/docs/Porting%20Source%20to%20Linux.pdf)，TOGL
应该还支持 DX10/DX11 的，在此期待未来 Valve 会有更大的举动。[Github
源代码](https://github.com/ValveSoftware/ToGL)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTYyNjM)

**以 Crysis 和 Far Cry 系列作品闻名的 Crytek 宣布将在 GDC 2014
上展示原生 Linux 支持的 CryEngine 3 引擎**
，这或许意味着未来不少大作也会借着引擎支持的便利性提供 Linux
版本，比如说自家旗下的
[Warface](https://www.warface.com/)？暂时还没有确切的证明表明这和 Valve
的 Steam Machines
推出有直接关系。[发布公告](http://www.crytek.com/news/conference-attendees-can-also-see-a-brand-new-mobile-game-extra-engine-updates-and-much-more-at-crytek-s-booth)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTYyNjQ)

**被游戏业界广泛使用的跨平台库 SDL 发布 2.0.2 版本，带来试验性 Wayland
和 Mir
支持**，该支持默认是禁用的，需要编译时打开。此外修复了全屏模式的一些问题，在
Android 平台上支持手柄，增加 PS4 和 OUYA
控制器映射等。[详细发布日志](http://lists.libsdl.org/pipermail/sdl-libsdl.org/2014-March/093652.html)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTYyNjU)

**Epic 将在 GDC 2014 上展示运行在 Firefox 浏览器中的的 Unreal 4
引擎效果**，达到与原生几乎一致的性能。利用 Mozilla 的 Asm.js
技术，Unreal 4 可以在无需任何浏览器插件的情况下以 WebGL 方式在最新版
Firefox 中流畅运行。即使不能亲临展台体验 Web
即游戏平台，亦可从[此演示视频](https://www.youtube.com/watch?v=c2uNDlP4RiE)中看个大概（[朝内镜像](http://v.youku.com/v_show/id_XNjg0NTM4NDA4.html)）[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTYyODM)
