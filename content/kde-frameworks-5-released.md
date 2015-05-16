Title: KDE Frameworks 5 发布
Date: 2014-07-08 08:41
Author: lovenemesis
Category: Desktop Environment
Tags: KDE
Slug: kde-frameworks-5-released

KDE Frameworks 5 的首个版本发布，带来了 50
多个组件提供从硬件管理到拼写检查等各种功能。

新的 Framework 从原先的 Platform 发展而来，在功能规划上更为细致。所有
Framework 组件依据**编译时依赖关系**分为三个**级别(Tiers)**：

-   级别 1 仅需要 Qt 及其关联库。
-   级别 2 仅依赖级别 1。
-   级别 3 除了会依赖级别 1 和 2可能依赖其他同级别的库。

依据**运行时依赖关系**分为三个**类别(Categories)**：

-   功能(Functional)组件没有任何依赖关系。
-   整合(Integration)组件需要依赖平台相关的一些依赖才能实现功能。
-   解决方案(Solutions)组件则会有必须满足的额外依赖关系。

[更多关于 KDE Framework 5
的内容可以参考此文](http://dot.kde.org/2013/09/25/frameworks-5)。

值得一提的组件有：

-   KArchive ：提供了适用于多种压缩格式支持的库，方便整合进 Qt
    程序实现压缩文档支持。
-   ThreadWeaver：提供基于任务和队列接口的线程管理库。
-   KConfig：提供了配置文件的存储和访问机制，兼容 INI 及 XDG。
-   Solid：提供硬件侦测及事件通知功能。
-   KI18n：提供 Gettext 国际化支持。

对于普通桌面用户来言，这只是 KDE5 的第一步，最重要的 KDE Plasma 5
还要等到七月中旬的某个时候。

[官方发布公告](http://kde.org/announcements/kde-frameworks-5.0.php)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTczNzE)
