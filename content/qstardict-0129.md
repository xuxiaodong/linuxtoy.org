Title: 基于Qt4的字典：QStarDict 0.12.9
Date: 2008-06-22 21:38
Author: lovenemesis
Category: Apps
Tags: QT, stardict
Slug: qstardict-0129

QStarDict 是一款基于 Qt4 的 StarDict 的克隆，它完全兼容 StarDict
的字典，适合于使用 KDE4
朋友使用，节省了使用StarDict加载gtk+运行环境的系统资源，并且界面也更加协调。

目前 QStarDict 0.12.9 版本已经实现以下功能：

-   **完全兼容**已有的 Stardict 辞典，暂不支持树型辞典。
-   支持屏幕取词，通过 D-bus 支持在 Qt4 应用程序中的屏幕取词。
-   支持通过 festival TTS 发音，暂不支持真人语音库。
-   支持选择性的启用/禁用辞典，暂不支持辞典分组。
-   支持将查询结果打印或保存成文本文件。
-   支持网络辞典。
-   支持自定义显示字体和颜色。

截图：

![](http://i.linuxtoy.org/i/2008/06/qstardict-340x243.png)

下载地址[见这里](http://www.qt-apps.org/content/show.php/QStarDict?content=61606)。

**附： Fedora 8 X86\_64 下如何编译和安装**

1.  解压缩源代码包
2.  安装必要的依赖开发包 su -c 'yum install dbus-qt-devel.x86\_64
    qt4-devel.x86\_64'
3.  在源代码目录输入 qmake-qt4 生成安装配置文件， 默认安装目录在 /usr 下
4.  完成后输入 make 编译
5.  完成后输入 su -c 'make install' 安装

