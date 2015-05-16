Title: 更改 GNOME 下 Qt 程序的外观
Date: 2007-02-22 19:09
Author: toy
Category: Tutorials
Slug: change-qt-applications-look-and-feel-under-gnome

在默认情况下，由于 GNOME 环境中所安装的 Qt 应用程序使用 Motif
样式，其外观甚为不好看。不过，我们可以通过安装 Qt Configuration 程序和
Polymer Qt Style 来加以改善。

首先，我们在终端中执行
`sudo apt-get install qt3-qtconfig polymer`。该指令会同时安装 Qt
配置程序和 Polymer Qt 样式。需要注意的是，对于
Polymer，如果你不是使用最新的 Feisty，恐怕需要手动安装。具体可以通过
[Polymer 主页](http://static.int.pl/~mig21/dev/polymer/)查询。

然后，执行 qtconfig 就可以启动 Qt 配置程序了。在 Appearance 页面的 GUI
Style 部分，选择 Polymer。同时，你也可以切换到 Fonts 标签对 Qt
程序外观所用的字体进行配置。

[![Qt
Configuration](http://i.linuxtoy.org/i/2007/02/qt-configuration_s.jpg)](http://i.linuxtoy.org/i/2007/02/qt-configuration.jpg)

另外，你还可以执行 polymer-config 来对 Polymer 样式进行配置。

![Polymer](http://i.linuxtoy.org/i/2007/02/polymer.jpg)

经过以上几步简单的配置后，在 GNOME 中 Qt 应用程序的外观基本上就与 Gtk
程序保持一致了。更改前后的效果如下图所示。

[![Qt
Application](http://i.linuxtoy.org/i/2007/02/qt-app-look_s.jpg)](http://i.linuxtoy.org/i/2007/02/qt-app-look.jpg)
