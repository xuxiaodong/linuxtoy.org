Title: 打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (4)
Date: 2007-12-20 22:39
Author: toy
Category: Featured
Slug: the-perfect-linux-desktop-arch-linux-2007-08-2-4

我们已经连续写了本文的[第一部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-1.html)、[第二部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-2.html)和[第三部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-3.html)，相信通过这些步骤使
[Arch Linux](http://archlinux.org/)
愈加合用了。接下来，在第四部分中，我们将带来一些 Eye Candy 方面的东东。

### 安装 Compiz Fusion

Compiz Fusion 合并自 Compiz 和 Beryl，它不仅将 Linux 桌面带入了 3D
环境，而且包含许多既丰富又渲丽的效果。

**准备配置文件**

要在 Arch Linux 中安装 Compiz Fusion，首先确保 /etc/X11/xorg.conf
文件的正确配置。仍然以 NVIDIA 显卡为例：

1. Module 部分载入 GLX 模块：

`Load "glx"`

2. Device 部分添加下列选项：

`Option "AddARGBGLXVisuals" "True"`

以上是针对较新卡的配置，如果是使用旧卡的话，那么还应加上：  
` Option "RenderAccel" "true" Option "AllowGLXWithComposite" "True"`

3. 添加 Extensions 部分：  
` Section "Extensions"   Option "Composite" "Enable" EndSection`

使用其他显卡的朋友可以参考 [Arch Linux
维基](http://wiki.archlinux.org/index.php/AIGLX)上面的相关文章。

**安装 Compiz Fusion**

现在，让我们来安装 Compiz Fusion，执行下列命令：

`pacman -S compiz-fusion`

这将安装 Compiz Core、Compiz Fusion 插件、Compiz Fusion
设置管理器、Emerald 及主题、Fusion Icon 等。

另外，GNOME 用户可以安装窗口装饰：

`pacman -S compiz-fusion-gtk`

KDE 用户为：

`pacman -S compiz-fusion-kde`

**自动启动 Compiz Fusion**

要启动 Compiz Fusion，可以运行 Fusion
Icon，它是一个系统托盘程序，通过它可以很方便的切换：

`fusion-icon`

![Fusion Icon](http://i.linuxtoy.org/i/archlinux/fusion-icon.png)

从 Fusion Icon 中，我们可以将窗口管理器切换为 Compiz，窗口装饰切换为
Emerald。此外，该工具也可以调用 Compiz Fusion 设置管理器及 Emerald
主题管理器。具体的调整过程，你不妨亲自试试。

如果打算让 Compiz Fusion 自动启动，可以将 Fusion Icon 加入 GNOME
会话的启动程序组中。方法是，点击“系统 → 首选项 →
会话”，在启动程序标签中点击“添加”按钮，然后输入下列信息：

-   名称：填写 Compiz Fusion
-   命令：输入 fusion-icon
-   注释：填入 Compiz Fusion

[![Compiz
Fusion](http://i.linuxtoy.org/i/archlinux/compiz-fusion-thumb.png)](http://i.linuxtoy.org/i/archlinux/compiz-fusion.png)

### 安装 Avant Window Navigator (AWN)

Avant Window Navigator 是一个漂亮的 Dock
程序，提供程序启动、窗口管理等，并包含许多插件。我已经通过 AUR 编译好了
[AWN](http://i.linuxtoy.org/files/archlinux/avant-window-navigator-0.2.1-2-i686.pkg.tar.gz)，你可以下载后直接安装。

你可能需要先安装使用依赖：

`pacman -S gnome-python gnome-python-desktop gnome-python-extras`

再安装 AWN：

`pacman -U avant-window-navigator-0.2.1-2-i686.pkg.tar.gz`

AWN 可通过“应用程序 → 附件 → Avant Window
Navigator”启动。自动启动的设置可以参考 Compiz Fusion 的做法。

[![Avant Window
Navigator](http://i.linuxtoy.org/i/archlinux/awn-thumb.png)](http://i.linuxtoy.org/i/archlinux/awn.png)

(待续)
