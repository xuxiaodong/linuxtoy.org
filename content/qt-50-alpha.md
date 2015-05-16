Title: Qt 5.0 Alpha
Date: 2012-04-05 08:37
Author: lovenemesis
Category: Development
Tags: Qt
Slug: qt-50-alpha

跨平台 GUI 开发框架 Qt 发布 5.0 Alpha 版本。

Qt 5.0 引入了如下变化：

**所有平台迁移至 Qt 平台抽象层(QPA)**

QPA 原先在 Qt 4.8 时引入作为 Qt Embedded
的替代品，现在将应用在全部平台上。这将方便将各个平台相关的代码抽象化，方便
Qt 面向不同平台的移植，比如 QNX 和 Android 。

**重新构建的图形层**

-   相比 Qt4 获得了效率上的提升。
-   Qt Quick 将使用基于 OpenGL 的 Scenegraph，依赖于 OpenGL ES 2.0。
-   引入 QOpenGL 类，替代 QGL 类。
-   从 QPainter 中移除平台相关的 X11 和 CoreGraphics 后端。

**内部模块化设计**

尽管使用 Qt 5 的应用程序开发者看不到，但是 Qt 5.0
内部重新进行了模块化设计。

目前整理出一个称为 Qt Essential 的类集合，包含基本功能(Qt 3D, Qt Core,
Qt GUI, Qt JS Backend, Qt Location, Qt Multimedia, Qt Network, Qt Qml,
Qt Quick, Qt SQL, Qt Test 和 Qt
WebKit)。更多的功能或者平台设备相关部分将通过模块方式按需提供。

此举允许了不同模块之间的独立进步，方便了第三方开发者对 Qt 的贡献。

**将 QWidget 分离出成为独立的库**

QWidget
被分离出成为单独的一个库，一方面保证依然想要使用该类的用户提供兼容性，另一方面也是在鼓励用户转向使用
QML 和 Qt Quick 方式的图形软件开发。

**其他改进**

-   Qt Core 改善了 JSON 解析器并提供了新的 Perl 正则引擎。
-   改善了对 C++11 支持。
-   新的 Qt Quick 使用 Google V8 引擎。
-   引入支持 3D 显示的 Qt 3D 模块和提供位置相关服务的 Qt Location 模块。
-   Qt WebKit 将使用来自 WebKit 上游的最新版本，提供更好的 HTML5
    兼容性。注意目前暂时禁用其在 Win 平台上的编译，将会在 Beta
    重新启用。

[Qt 4.X 至 Qt 5.X
迁移指南](http://wiki.qt-project.org/Transition_from_Qt_4.x_to_Qt5)

[源代码包下载](http://releases.qt-project.org/qt5.0/alpha/)

[官方发布博客](http://labs.qt.nokia.com/2012/04/03/qt-5-alpha/)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTA4MjM)
