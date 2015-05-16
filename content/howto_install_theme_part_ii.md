Title: 如何安装主题（2）
Date: 2006-10-27 17:06
Author: toy
Category: Tutorials
Slug: howto_install_theme_part_ii

在[《如何安装主题（1）》](http://linuxtoy.org/archives/howto_install_theme_part_i.html)中，我们介绍了有关
GDM 主题的安装、使用及删除过程。本篇我们将向大家继续介绍 Metacity 和 GTK
主题的安装步骤。

Metacity 为 GNOME
桌面环境所使用的默认窗口管理器，其主题主要负责窗口的边框部分。而 GTK
主题则负责控件部分。有的主题包是单独的，也有合二为一的主题包。不过，安装方法都是一致的。

1.  常规法：

    首先，启动 GNOME 主题管理程序，在终端中执行 `gnome-theme-manager`
    可以达到此目的。接着，在“主题首选项”中，点击“安装主题...”按钮，然后选择需要安装的主题包即可。

    [![GNOME Theme
    Manager](http://i.linuxtoy.org/i/2006/10/gnome_theme_manager_s.png)](http://i.linuxtoy.org/i/2006/10/gnome_theme_manager.png)

2.  拖动法：
    此法甚为简单，在 GNOME
    主题管理窗口打开的情况之下，直接将需要安装的主题包拖动过来，按照提示完成安装过程。
3.  释放法：
    有时候，可能会遇到主题作者打包的格式并不能直接安装。此时，就需要将主题包中的文件释放出来。对于个人用户而言，一般所安装的主题文件都保存在
    ~/.themes
    目录中。所以，你只需把先前释放出来的文件移动到该目录即可。

因为在 GNOME 中安装图标主题与安装 Metacity 和 GKT
主题十分类似，所以在此顺带提一下。不同的是方法三，你需要把释放的图标主题文件移动到
~/.icons 目录。
