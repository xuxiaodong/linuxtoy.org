Title: Transifex 1.0
Date: 2010-11-26 13:06
Author: lovenemesis
Category: Development
Tags: Transifex
Slug: transifex-10

开源的翻译平台 Transifex 升级至 1.0 版本，带来 **HTTP 代码跟踪**和**原生
Qt 本地化**支持。

*主要变化：*

-   **HTTP
    代码跟踪系统**替换了原先内部集成的版本控制系统，允许追踪放置在任意位置的代码。
-   所有**操作在字符串级别**实现，不再是原先的文件级别，允许翻译建议、批注和翻译词典等功能。
-   为维护者和翻译人员提供一款**更安全的终端控制程序**。
-   支持**对任意文件进行翻译**，不再局限于 po 文件，同时提供 **Qt
    本地化文件原生支持**。

*其他改善：*

-   翻译文件元信息自动更新。
-   翻译语言克隆。
-   非英语源代码支持。
-   提供 API。

由于升级，Transifex.net 网站将于 11月29日 10pm UTC 时间下线维护。

[英文原文](http://blog.transifex.net/2010/11/one-dot-zero/)

[Transifex 1.0
发布日志](http://help.transifex.net/technical/releases/1.0.html)

[迁移指南](http://help.transifex.net/user-guide/one-dot-zero.html#migrating-your-project)
