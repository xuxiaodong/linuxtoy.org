Title: Qt 5.0 Beta
Date: 2012-08-31 11:14
Author: lovenemesis
Category: Development
Tags: qt5
Slug: qt-5-0-beta

经历了几番波折，开源跨平台 GUI 库 Qt 终于发布 5.0 Beta 版本。

-   支持使用 GPU 进行图形加速，甚至在 [Raspberry
    Pi](http://qt-project.org/wiki/Qt-RaspberryPi) 上。
-   引入使用 QML 和 JavaScript 编写的高级 UI，参见 [Qt Media
    Hub](http://qt-project.org/wiki/QtMediaHub)。
-   使用 Qt 平台抽象层实现更好的多平台支持，包括对于 Android, iOS， QNX
    和 Blackberry 10 的支持。

目前 Qt Quick 5.0 Beta 在 Win 平台上需要一个具备良好 OpenGL
支持的显卡才可运行，待正式发布时将转用 ANGLE 层移除此限制。

此外在 Qt 5.0 的开发过程中融入了很多源自 KDE
库的内容，这将有利于进一步缩小 [Qt 程序和 KDE
程序之间的差异](http://files.kde.org/akademy/2012/slides/KDE_Frameworks_5_for_Application_Developers_-_David_Faure.pdf)。

另一方面，这一天也是 [Nokia 正式关闭负责 Qt
开发的布里斯班办公室的日子](http://linuxtoy.org/archives/breaking-nokia-starts-saying-bye-to-qt.html)。

更多内容可以查看[本站早先报道](http://linuxtoy.org/archives/qt-50-alpha.html)。

[官方发布公告](http://labs.qt.nokia.com/2012/08/30/qt-5-beta-is-here/)

[官方下载](http://releases.qt-project.org/qt5.0/beta1/)

[已知问题列表](http://qt-project.org/wiki/Qt500beta1KnownIssues)
