Title: Adobe 宣布将停止更新 Linux 平台 Flash Player
Date: 2012-02-23 09:29
Author: lovenemesis
Category: News
Tags: chrome, Flash
Slug: adobe-announce-to-abondon-naapi-flash-player-on-linux

Adobe 宣布在 Flash Player 11.2 之后将不再为桌面 Linux 平台提供使用 NPAPI
接口的新版本 Flash Player，仅提供安全更新。

Adobe 表示在 Flash Player 11.2 之后将和 Google 合作，在 Linux 平台上仅为
Google Chrome 提供使用[代号 “Pepper”
PPAPI](http://linuxtoy.org/archives/google-chrome-14-beta.html)
接口的新一代 Flash Player。

[Adobe
消息公告](http://blogs.adobe.com/flashplayer/2012/02/adobe-and-google-partnering-for-flash-player-on-linux.html)

**消息要点：**

-   从今年晚些时候开始，新的 **PPAPI 的 Flash Player 将仅随 Google
    Chrome 在全部平台分发**，Adobe 不再为 Linux 平台提供单独的下载。
-   Chromium 用户依然需要从 Google Chrome 中“剥离”出 PPAPI 的 Flash
    Player 使用，或者并行安装。
-   现有的 NPAPI 的 Flash Player 将止步 11.2
    版本，不会升级至新的功能版本，不过在接下来的**五年里可以获得安全更新**。
-   **Adobe 将依然为 Win 和 OS X 平台上的非 Google Chrome
    用户提供可以单独下载的 NPAPI 接口新版本 Flash Player**。
-   Adobe 计划提供一个 Linux 平台上包含除错功能的 Flash Player
    版本和技术白皮书，具体分发形式待定。或许可以使 Lightspark 或者 Gnash
    开源项目收益。

结合过往 Flash Player 在 Linux 平台的表现：

-   如果你是 Google Chrome 粉丝，恭喜你可以期待 PPAPI 或许可以给 Flash
    Player for Linux
    带来新生了，不过至少[目前没看出来](http://support.google.com/chrome/bin/answer.py?hl=en&answer=108086)。
-   如果你是 Chromium 粉丝，那么或许该转用 Google Chrome，或者学习如何从
    Chrome 中剥离 PPAPI 版本 Flash Player 使用。
-   如果你是 Firefox 或者 Opera 粉丝，目前还没有它们何时会实现 PPAPI
    的消息，可以理解因为 PPAPI 尚未稳定。不过至少它们都对 NPAPI
    的架构表示不满了。
-   如果**你只是个正常的桌面 Linux 用户，什么都不用做。**原因？
    1.  近几年来在 Linux 平台 Flash Player “新功能”仅有 64
        位支持值得一提，对 Flash Player 11.2
        后会有什么新功能呢？呃……现实些吧。
    2.  NPAPI 接口的 Flash Player 11.2 还将获得长达 5
        年的安全更新，依然可以安全的看网络视频和在线游戏（同时忍受居高不下的
        CPU 占有率）
    3.  HTML5、WebGL 等带来的变革将在接下来的几年了逐渐成形，Flash
        Player 不再像以前那样重要了。甚至 Google 自家的 Maps 已经开始用
        WebGL 了。

[PPAPI Dummy 代码首页](http://code.google.com/p/ppapi/)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTA2MDc)
