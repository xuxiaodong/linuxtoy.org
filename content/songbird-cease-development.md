Title: Songbird 停止开发
Date: 2013-06-18 11:07
Author: lovenemesis
Category: News
Tags: Songbird
Slug: songbird-cease-development

跨平台开源多媒体播放器 Songbird 的母公司 POTI Inc
宣布由于经济问题难以维系，Songbird 开发及其他所有服务将于 6 月 28
日全部停止。

[![](http://lt-file.b0.upaiyun.com/files/2013/06/sunsetthebird.png)](http://lt-file.b0.upaiyun.com/files/2013/06/sunsetthebird.png)

本站在 2006 年 Songbird
问世之初就[曾报道过](http://linuxtoy.org/archives/songbird.html)，其跨界融合浏览器和音乐播放器的特性在当时看来十分独特，从外观上来看跟平易近人的早期
iTunes 十分相近。

在这里稍微回顾下 Songbird 的特性：

-   使用 Mozilla 的 XUL 技术构建，实现跨平台的图形界面。
-   使用 GStreamer 框架实现跨平台多媒体回放，并且包含来自 Fluendo
    的解码包。
-   提供丰富的 Add-On 机制。
-   支持导入包括 iTunes Library 在内的媒体库。

Songbird 七年来的路程，期间参杂了不少**开源及整个 IT 的缩影**：

-   **产品定位**：
    1.  在 Songbird
        刚刚诞生的时候，数码音乐刚成为潮流，每个人的硬盘上几乎都有不少从各种渠道获得的
        MP3。于是能在同一个软件中一边浏览网页一边回放本地音乐的确很符合不少人的需求。
    2.  随着宽带的普及，现在在线流媒体播放成为主流，一个浏览器即可完成网页浏览 +
        在线音乐回放的需求，Songbird 的目标群体日渐缩小。
-   **同类竞争**：由 iTunes 开启的音乐管理软件潮流席卷开源界，除了
    Songbird 以外，还有 Rhythmbox、Banshee、Amarok、Jajuk
    等等，可谓一抓一大把。
-   **功能发展**：和 Banshee 一道被 iTunes
    带入歧途，先后增加视频回放、照片同步等功能，不单单针对移动音乐设备，还希望能成为移动影音设备甚至智能手机的同步中心。导致软件体积越来越大，启动时间越来越长，依赖关系愈加复杂。
-   **商业合作**：曾经和飞利浦合作，捆绑 Songbird 到旗下销售的消费级
    MP3/4 播放器下。可惜飞利浦在消费级 MP3 领域分额也只是个小角色……
-   **技术壁垒**：
    1.  Mozilla 为了提升 Firefox 的性能，XUL
        平台的升级速度加快，变动幅度也不小。但这同时也给基于 XUL
        的第三方应用开发增加了难度，Songbird
        所用版本相当古老，导致其在内存占用、界面响应和启动时间上相比其他本地应用逊色很多。
    2.  iTunes 在媒体库管理和同步协议方面变化频繁，Songbird
        的逆向工程难以继续。本来作为 iTunes 开源替代品存在的 Songbird
        到后来不得不依赖 iTunes 才能在 Win/OS X 平台实现同步。
-   **移动平台**：Songbird 在过去两年间先后推出了 Android 及 iOS
    版本，希望能吸引智能手机平台新用户并保留已有桌面版用户。但是其功能在面对系统内置播放器及市场上其他第三方的竞争中并没有太多优势。
-   **社交网络**：Songbird 后期推出音乐社交站点
    [Songbird.me](http://www.songbird.me/)，尝试增加用户黏性，但是其有限的功能很难长期留住用户。

对于 Songbird 简体中文贡献者之一，由于 Songbird 不再提供 64
位的预编译版本且对于本本的多媒体键支持欠佳，加之经过漫长的时间 Rhythmbox
也逐步成熟，大约从三年前便不再使用 Songbird
作为音乐库管理软件了。个人现在最常用 [GNOME Web
Apps](http://linuxtoy.org/archives/gnome-32-web-apps.html) 听
[8tracks](http://m.8tracks.com/)。

若是您依然留恋 Songbird 的话，可以尝试其社区化产品
[Nightingale](http://getnightingale.com/)。

[官方消息公告](http://blog.songbirdnest.com/you-gotta-know-when-to-fold-em/)

消息来源: [H
Open](http://www.h-online.com/open/news/item/Songbird-media-player-to-cease-development-1890617.html)
