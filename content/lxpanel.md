Title: LXPanel：轻巧快速的桌面面板
Date: 2006-11-02 21:29
Author: toy
Category: Apps
Slug: lxpanel

[LXPanel](http://sourceforge.net/projects/lxpanel)
是一个轻巧快速的桌面面板程序，尤其适合用在 Fluxbox、Openbox、Blackbox
等不含整合桌面环境的窗口管理器中。LXPanel 从 fbpanel
改造而来，包含能够从系统上安装的 *.desktop
文件自动产生应用程序菜单、程序启动图标、工作区、系统托盘、时钟、中文支持等特色。

[![LXPanel](http://i.linuxtoy.org/i/2006/11/lxpanel_s.png)](http://i.linuxtoy.org/i/2006/11/lxpanel.png)  
LXPanel 效果图

我在 Ubuntu Edgy Eft + Fluxbox 中尝试了
LXPanel。其编译过程颇费周折：其一是需要准备好编译环境，如可能要安装
libgtk2.0-dev、libstartup-notification0-dev、libxpm-dev
等包；其二是程序在配置时找不到
config.rpath、intltool-extract.in、intltool-merge.in、intltool-update.in
等文件，可能要从系统中找到这些文件并将其复制到 LXPanel
解包后的目录。需要尝试的朋友可去抓取 [LXPanel 0.2.0
的源码包](http://sourceforge.net/project/showfiles.php?group_id=178827)。
