Title: 图说 Avant Window Navigator 新增功能
Date: 2007-08-28 15:09
Author: toy
Category: Apps, Desktop Stuff
Slug: avant-window-navigator-new-features

[Avant Window
Navigator](http://linuxtoy.org/archives/avant-window-navigator.html)（简称
Awn），它是一个完全可被定制的 Dock
应用程序。随着该程序的深入开发，一些比较令人兴奋的新功能在最近逐渐浮现了出来。本文将以图说的形式来向你逐一展现
Awn 的这些新增功能。

**安装 Awn**

我们以 Ubuntu 7.04 为例来说明 Awn 的安装过程，其他系统可以[参阅 Awn
网站的相关说明](http://awn.wetpaint.com/page/Download)。

1.  添加源：

    首先在终端执行
    `sudo gedit /etc/apt/sources.list`，然后添加下列内容：  

    ` ## Avant Window Navigator deb http://download.tuxfamily.org/syzygy42/ feisty avant-window-navigator deb-src http://download.tuxfamily.org/syzygy42/ feisty avant-window-navigator`

    在保存 sources.list 文件后，接着执行以下指令以便获取密钥：

    `wget http://download.tuxfamily.org/syzygy42/8434D43A.gpg -O- | sudo apt-key add -`

2.  更新源：
    只需执行 `sudo apt-get update` 即可。
3.  安装 Awn：

    你需要在终端输入下列命令：

    `sudo apt-get install avant-window-navigator-bzr libawn-bzr awn-core-applets-bzr`

**运行 Awn**

点击“应用程序 → 附件 → Avant Window Navigator”菜单命令，可以立即运行
Awn。如果你想让 Awn 随开机自动运行，那么可将其添加到会话中。

**Awn 新功能解说**

-   Awn 管理器：

    取代原来 Awn 首选项的是全新的 Awn
    管理器，该管理器将选项设置、插件管理、启动器配置、主题管理汇聚在一起实现集中管理。其中，主题管理为本次增加的新功能。

    [![Awn
    Manager](http://i.linuxtoy.org/i/awn/thumb_awn-manager1.png)](http://i.linuxtoy.org/i/awn/awn-manager1.png)  
    *在 Awn
    管理器中增加了新的三维外观设置选项，不必采用[原来的解决方案](http://linuxtoy.org/archives/add-reflection-and-3d-effect-for-awn.html)了。*

    [![Awn
    Manager](http://i.linuxtoy.org/i/awn/thumb_awn-manager2.png)](http://i.linuxtoy.org/i/awn/awn-manager2.png)  
    *Awn 插件管理，支持拖曳以便改变排列的次序。*

    [![Awn
    Manager](http://i.linuxtoy.org/i/awn/thumb_awn-manager3.png)](http://i.linuxtoy.org/i/awn/awn-manager3.png)  
    *应用程序启动器管理，可以添加或删除，但缺少编辑功能。*

    [![Awn
    Manager](http://i.linuxtoy.org/i/awn/thumb_awn-manager4.png)](http://i.linuxtoy.org/i/awn/awn-manager4.png)  
    *Awn 主题管理，支持添加、删除、应用、以及保存主题。*

-   新的插件：

    此次更新增加了 Awn 主菜单、Stack、时钟以及 Wobbly Zini
    等新的插件。其中，我个人比较喜欢前面两个插件，而 Wobbly Zini
    插件只是简单的动画展示，无太大的实用价值。

    [![Awn Main
    Menu](http://i.linuxtoy.org/i/awn/thumb_awn-main-menu.png)](http://i.linuxtoy.org/i/awn/awn-main-menu.png)  
    *Awn 主菜单插件，可从此处启动各种应用程序和游戏。*

    [![Awn
    Stack](http://i.linuxtoy.org/i/awn/thumb_awn-stack.png)](http://i.linuxtoy.org/i/awn/awn-stack.png)  
    *Awn Stack
    插件，我们[曾经介绍过](http://linuxtoy.org/archives/mac-stacks-for-awn.html)。*

    [![Awn
    Clock](http://i.linuxtoy.org/i/awn/awn-clock.png)](http://i.linuxtoy.org/i/awn/awn-clock.png)  
    *Awn 时钟插件。*


