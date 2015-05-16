Title: 窗口管理器 Openbox 入门指南 (1)
Date: 2008-07-30 10:01
Author: toy
Category: Featured
Tags: Guide, Openbox, WM
Slug: openbox-getting-started-guide

也许你听说过 Blackbox 和
[Fluxbox](http://linuxtoy.org/search/fluxbox)，那么，Openbox
又是什么？Openbox 跟它们很相似。不过，我们还是来看看 Openbox
官方给出的说明吧。Openbox 官方称，Openbox
是一个可高度定制且包含广泛标准支持的下一代窗口管理器。近来，我玩 Openbox
是越来越上心，自以为有些小得，遂立此文，以助新手快速入门。

**目录表**

-   [我喜欢 Openbox
    的原因](http://linuxtoy.org/archives/openbox-getting-started-guide.html#reasons)
-   [如何安装
    Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide.html#installation)
-   [运行
    Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide.html#running)
-   [配置
    Openbox](http://linuxtoy.org/archives/openbox-getting-started-guide-2.html#configuration)
-   [设定键盘和鼠标绑定](http://linuxtoy.org/archives/openbox-getting-started-guide-3.html#bindings)
-   [控制应用程序](http://linuxtoy.org/archives/openbox-getting-started-guide-4.html#applications)
-   [使用自动启动脚本](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#autostart)
-   [提示与技巧](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#tips)
-   [参考资源](http://linuxtoy.org/archives/openbox-getting-started-guide-5.html#ref)

### 我喜欢 Openbox 的原因 {#reasons}

从了解到学习，再到天天使用 Openbox，我主要基于以下理由：

1.  速度非常快，资源占用极少。
2.  可高度定制化，能够对应用程序加以灵活控制。
3.  能够绑定键盘和鼠标。比如，你可以为程序设定启动快捷键，也可以为最小/大化窗口设置热键。对于鼠标，同样如此。
4.  具有自动启动脚本，能够随机自动启动各种程序。
5.  主题资源丰富，与 *box 类视觉样式兼容。Openbox
    的外观是简约而不简单。
6.  支持会话，可深入 GNOME、KDE、Xfce 等桌面环境使用。换句话说，Openbox
    可替代这些桌面环境中默认的窗口管理器，而其他桌面组件仍旧保持原样。

### 如何安装 Openbox {#installation}

要安装 Openbox 有两种方法：其一是直接从所用的 Linux
发行版中安装；二是下载其源代码，自行编译安装。前者的优势是省事，不过有时候安装的
Openbox 并非是最新版。而后者虽然稍显麻烦，但可以实现更加灵活的掌控。

**从发行版安装**

Openbox 已被包含到大多数流行的 Linux
发行版中。因此，使用该发行版的包管理工具来安装 Openbox
是一件十分容易的事情。

Archlinux 用户执行以下命令可以安装 Openbox：

`pacman -S openbox`

而 Debian/Ubuntu 用户可以执行下面的命令：

`sudo apt-get install openbox`

Fedora 用户也可以使用 yum 来安装 Openbox：

`yum install openbox`

**从源代码编译安装**

然而，有时候从发行版安装的 Openbox 并非是最新版本，或者在你所用的 Linux
发行版中不能找到 Openbox，这时候可以考虑从源代码编译安装它。

**编译依赖**

要从源代码编译安装 Openbox，首先要准备以下依赖包：

-   C 编译器（比如 GCC）
-   Libc
-   Xlib
-   Glib-2
-   LibXML-2
-   Pango
-   Startup-notification（可选，推荐安装）
-   XCursor（可选，推荐安装）
-   Pkg-config

不要被这些依赖包所吓倒，其实多数 Linux
发行版已经默认安装了。你所要做的就是一一检查和核对而已。

**编译及安装**

一旦准备好编译 Openbox
所需的依赖包，在下载并解包源代码文件后，便可按如下指令来编译并安装
Openbox：


    ./configure --prefix=/usr --sysconfdir=/etc #配置，更多选项可通过 ./configure --help 获取
    make #编译
    sudo make install #安装

哈，很熟悉的编译安装三步曲。

### 运行 Openbox {#running}

如果你使用了 GDM/KDM
之类的图形登录管理器，那么在系统登录时从会话类型菜单中选择 Openbox
相关条目即可启动 Openbox。

![sessions.png](http://i.linuxtoy.org/i/2008/07/sessions.png)

另一种启动 Openbox 的方式是命令行。只需向主目录中的 ~/.xinitrc
文件加入如下内容即可：

`exec openbox`

另外，包含会话支持功能的 Openbox 可以使用下面的内容代替：

`exec openbox-session`

Openbox 看起来像下面的样子：

[![openbox-desktop-thumb.png](http://i.linuxtoy.org/i/2008/07/openbox-desktop-thumb.png)](http://i.linuxtoy.org/i/2008/07/openbox-desktop.png)

[待续]
