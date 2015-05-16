Title: 基于 Plasma 插件的新输入法面板
Date: 2009-03-22 16:04
Author: JimHu
Category: News
Tags: Input Method, KDE, Plasma
Slug: kimpanel

Linux 下的输入法无非就是 Scim/Fcitx/iBus 这么几款。除去还没有移植到 QT4
的 Skim 以外，均采用的是 GTK 或者 XIM。（iBus 似乎有 QT
界面，但是我还没有成功的在 KDE 中调出过 iBus……）因此，KDE
的用户可能一直有着找不到合适输入法的苦恼。但是，正在开发中的 KimPanel
可能可以改变这个现状。  

Wkai 正在开发的 KimPanel 是一个可以用多个输入法作为后端的 Plamsmoid
插件。通过 KimPanel 提供一个统一的UI接口给不同输入法，Plasmoid
的形式能够使它能够高度整合到 KDE 中去，比如根据当前 Plasma
主题自动换肤、能够放到面板容器中，就像 Windows 下的语言栏面板。

[gallery]

由于出于早期开发阶段，没有任何可用的测试版供下载。该插件可能在 KDE 4.3
中作为默认的 Plasmoid 插件供使用。  
想做小白鼠的朋友可以进行 Alpha Milestone 的测试。  
svn co
svn://anonsvn.kde.org/home/kde/trunk/playground/base/plasma/applet/kimpanel  
然后读README文件安装配置。

详细参阅：

<http://forum.ubuntu.org.cn/viewtopic.php?f=38&t=188228>

<http://www.linuxsir.org/bbs/thread345494.html>

<http://forum.kdecn.org/thread-21.html>
