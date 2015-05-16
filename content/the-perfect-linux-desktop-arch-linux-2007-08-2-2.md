Title: 打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (2)
Date: 2007-12-18 22:26
Author: toy
Category: Featured
Slug: the-perfect-linux-desktop-arch-linux-2007-08-2-2

在本文的[第一部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-1.html)中，我们从头至尾描述了
[Arch Linux](http://archlinux.org/)
基本系统的安装过程。此时，我们所得到的仅仅是一个命令行系统，离完美 Linux
桌面的目标还差一大截呢。现在让我们继续余下的工作。

### 更新系统

在我们进行后续的安装任务之前，先把 Arch Linux
更新到最新状态。你可以通过执行以下指令来完成 (需要 root
权限，如果是普通用户，可以先 su)：

`pacman -Syu`

### 安装 X.Org

X.Org 是 X Window System 的开源实现。如果我们要在 Arch Linux
中运行图形化的程序，那么 X.Org 的安装是必不可少的。安装 X.Org
可以执行命令：

`pacman -S xorg`

该指令将为你安装 X.Org 所必需的包，包括 X.Org
服务器、工具、字体、键盘驱动、鼠标驱动、显卡驱动等等。

值得注意的是，默认的 X.Org
安装可能并没有包含你的显卡驱动程序。因此，你需要单独为你的显卡安装驱动。你可以通过下列命令来进行搜索：

`pacman -Ss xf86-video`

比如，我在 VMware 中测试时，选择安装 xf86-video-vmware：

`pacman -S xf86-video-vmware`

**为 NVIDIA 显卡安装驱动**

作为 NVIDIA 和 ATI 显卡的用户，为了获得更好的性能和 3D
加速功能，可以安装它们的私有驱动。由于我本人是使用 NVIDIA
显卡，所以本文就以安装 NVIDIA 的显卡驱动为例来说明。ATI 显卡用户可以参照
[Arch Linux 维基的相关介绍](http://wiki.archlinux.org/index.php/ATI)。

如果你象我一样使用较新的 NVIDIA 显卡，那么可以执行以下指令来安装：

`pacman -S nvidia`

使用旧卡的朋友可以运行下列命令：

`pacman -S nvidia-96xx`

或者：

`pacman -S nvidia-71xx`

**生成 xorg.conf 配置文件**

在你使用 X.Org 前，需要为其创建 xorg.conf
配置文件。手动创建比较费事，我们选择相关工具自动生成，然后再根据自己需要来编辑调整。

我们选择使用 xorgconfig 工具来生成 xorg.conf
文件。要启动该工具，可以在命令提示符后执行：

`xorgconfig`

xorgconfig
是一个交互式的程序，它会向你问一些有关鼠标、键盘、显示器、显卡等方面的问题。根据你的实际情况回答即可。

另外，使用 NVIDIA 显卡的朋友，也可以使用 nvidia-xconfig。

**编辑 xorg.conf 配置文件**

直接由工具所生成的 xorg.conf
配置文件并不能满足实际情况的需要。因此，我们还有必要对该文件进行适当的编辑。

1. Module 部分

Module 这部分定义默认载入的模块。比如，要载入 GLX
模块，可以去掉下列内容前面的注释符 #：

`Load "glx"`

2. Files 部分

在这部分中，你应当开启默认的字体搜索路径。

3. InputDevice 部分

InputDevice 部分可以让你配置鼠标、键盘等。

4. Monitor 部分

对显示器进行配置，注意输入正确的水平和垂直刷新率。必要时可以查阅显示器说明手册。

5. Device 部分

此部分配置显卡。NVIDIA 显卡用户可以加上以下选项，从而去掉 NVIDIA
烦人的标志。

`Option "NoLogo" "true"`

6. Screen 部分

Screen 部分可以设置显示器的色深和屏幕分辨率。

### 安装桌面环境

**安装登录管理器**

因为接下来我们将要安装 GNOME 桌面环境，所以我们选择
GDM。你也可以选择其他的登录管理器，比如 SLiM。要安装 GDM，可以执行命令：

`pacman -S gdm`

在 GDM 安装完成后，我们打开 /etc/rc.conf 配置文件，将 gdm 添加到 DAEMONS
中：

`DAEMONS=(syslog-ng network netfs crond gdm)`

**安装 GNOME 桌面环境**

接着，我们执行下列指令来安装 GNOME 桌面环境：

`pacman -S gnome`

在安装 GNOME 时，你可以对其中所含的组件和程序进行有选择的安装。

**安装终端**

在登录到桌面环境之前，你应当安装一个合用的终端程序。我选择 GNOME
Terminal。因此，在命令行执行：

`pacman -S gnome-terminal`

当然，你可以选择安装其他的终端程序，如 rxvt-unicode。

**安装中文字体**

对我们这些中文用户来说，由于要处理汉字，所以总是需要安装中文字体和中文输入法。在
Arch Linux 中，你可以安装以下中文字体：

`pacman -S ttf-arphic-uming ttf-arphic-ukai`

同时，一些不错的英文字体也不妨安装上，比如：

`pacman -S ttf-bitstream-vera`

**安装中文输入法**

在 Arch Linux 中包含 SCIM 和 Fcitx 中文输入法。我们选择安装后者：

`pacman -S fcitx`

当 Fcitx 安装完成后，将下列内容添加到你用户主目录中的 .profile
中，以便让 Fcitx 自动启动：  

` export XMODIFIERS=@im=fcitx export GTK_IM_MODULE=xim export QT_IM_MODULE=xim fcitx &`

现在，重新启动系统。如果一切顺利的话，你将会看到如下登录画面：

[![Arch Linux
登录画面](http://i.linuxtoy.org/i/archlinux/archlinux92-thumb.png)](http://i.linuxtoy.org/i/archlinux/archlinux92.png)

在输入你的用户名和密码后，即可进入 GNOME 桌面环境。

[![Arch Linux
登录画面](http://i.linuxtoy.org/i/archlinux/archlinux93-thumb.png)](http://i.linuxtoy.org/i/archlinux/archlinux93.png)

(待续)

[声明：本系列文章尚需完善，谢绝转载]
