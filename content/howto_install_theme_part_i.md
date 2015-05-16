Title: 如何安装主题 (1)
Date: 2006-10-20 15:49
Author: toy
Category: Tutorials
Slug: howto_install_theme_part_i

读者无名在本站[留言](http://linuxtoy.org/archives/blubuntu_gdm_splash_wallpaper.html#comment-1046)道：“能不能有一篇详细介绍如果（何？）使用
GDM （主题的教程），从贵站知道很多这样漂亮的主题， 但下载了 package
后一直装不上。”有鉴于此，本站近期将针对新手组织一系列的初级教程，以帮助他们快速上手并投入使用当中。今天，我们就把如何安装主题的第一部分——GDM
篇介绍给大家。

[GDM](http://www.gnome.org/projects/gdm/) 即 GNOME Display Manager
的简称，它是一个图形化的登录管理程序。GNOME 桌面环境的默认登录管理器就是
GDM。GDM 是支持主题的，通过主题可以随时改变 GDM 的外观。

-   从哪里可以找到 GDM 主题

    推荐到这些网站去寻找：

    -   [GNOME art](http://art.gnome.org/themes/gdm_greeter/)：GDM
        官方的主题收集站点。
    -   [GNOME-Look](http://www.gnome-look.org/index.php?xcontentmode=150)：专门收集
        GNOME 外观资源的网站。
-   安装 GDM 主题
    1.  启动 GDM 设置程序：

        `sudo gdmsetup`

        [![gdm
        setup](http://i.linuxtoy.org/i/gdmsetup_s.png)](http://i.linuxtoy.org/i/gdmsetup.png)

    2.  点击 Local
        选项页中的“Add...”按钮，在打开的对话框中定位到所保存的 GDM
        主题目录，选择需要安装的 GDM 主题（一般为 *.tar.gz
        格式），然后点击“Install”按钮。
        [![gdm
        install](http://i.linuxtoy.org/i/gdm_install_s.png)](http://i.linuxtoy.org/i/gdm_install.png)
    3.  除了以上介绍的常规安装法之外，还有一个比较简便而快速的安装方法：那就是直接将需要安装的
        GDM 主题拖到设置窗口中即可。此法也支持批量安装 GDM 主题。（感谢
        [latteye](http://www.laroea.cn) 提示）

-   使用 GDM 主题

    只需点击已安装 GDM 主题旁边的单选按钮即可。

    [![gdm
    select](http://i.linuxtoy.org/i/gdm_select_s.png)](http://i.linuxtoy.org/i/gdm_select.png)

-   删除 GDM 主题
    先选中需要删除的 GDM 主题，然后点击右边的“Remove...”按钮。

