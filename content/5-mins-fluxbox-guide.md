Title: 5 分钟 Fluxbox 指南
Date: 2011-07-04 00:00
Author: lovenemesis
Category: Featured
Tags: Fluxbox
Slug: 5-mins-fluxbox-guide

受够了繁复的 DE，想尝试下纯粹的 WM？那么可以从
[Fluxbox](http://linuxtoy.org/archives/fluxbox-110.html) 开始，只需 5
分钟哦~

本文目的在于帮助您在 5 到 10 分钟内，通过一种简单的方式在配置好 Fluxbox
桌面环境。注意这里**假设您已经安装了某个桌面环境**比如
GNOME，而不是从最小系统开始。

**安装所需软件**

-   fluxbox：不解释。
-   feh：设置壁纸。
-   xcompmgr：透明及其他一些特效。
-   lxappearance：管理 GTK、图标和鼠标主题。
-   nitrogen：图形化壁纸管理工具。
-   dmenu：图形化命令运行和命令补全。
-   xscreensaver：不解释。

Fedora 下安装：  

`pkcon install fluxbox feh xcompmgr lxappearance nitrogen xscreensaver dmenu`

Debian/Ubuntu 下安装：  

`apt-get install fluxbox feh xcompmgr lxappearance nitrogen xscreensaver dmenu`

**创建菜单**

Fedora 默认生成的菜单比较简陋，不过可以通过调用一个 Python 脚本生成：

`fluxbox-xdg-menu --with-icons --theme /usr/share/icons/Faenza-Dark --with-backgrounds --bg-path=~/Pictures`

这里指定使用 Faenza-Dark 图标主题，主目录下的 Pictures
为背景图片搜索路径。

Debian/Ubuntu 应该已经默认生成了菜单，若是觉得过于拥挤的话，可以去[下载
fluxbox-xdg-menu](http://code.google.com/p/fluxbox-xdg-menu/) 来更改。

**自定义菜单**

如果还想进一步自定义菜单的话，这里是一些有用的小提示。

*自定义标题*

更改 `~/.fluxbox/menu` 文件中 `[begin]` 一行括号中的内容。

*添加收藏置顶程序*

还是在 `~/.fluxbox/menu` 文件中，添加 `[include] (~/.fluxbox/fbfav)`
一行，指定收藏的配置文件。

然后打开刚才指定的配置文件`~/.fluxbox/fbfav`，按照如下语法添加应用程序：

    [exec] (Menu_name) {program} 

例如：`[exec] (Firefox) {/usr/bin/firefox} `

**设置壁纸**

同样先添加`[include] (~/.fluxbox/fbbg)`，指定壁纸配置文件。

然后编辑刚才指定的配置文件`~/.fluxbox/fbbg`，将其中 **username**
替换为您实际用户名：

    [submenu] (Backgrounds)
    [exec] (username) {/usr/bin/nitrogen ~/Pictures}

    [exec] (system) {/usr/bin/nitrogen /usr/share/backgrounds}
    [end]

**屏幕保护**

编辑 `~/.fluxbox/menu` 文件并添加如下内容：

    [submenu] (Screen saver)
    [exec] (Enable screensaver) {/usr/bin/xscreensaver}
    [exec] (Disable screensaver) {/usr/bin/xscreensaver-command -exit}
    [exec] (Lock screen) {/usr/bin/xscreensaver-command -lock}
    [exec] (Configure screensaver) {/usr/bin/xscreensaver-command -prefs}
    [end]

**用户切换**

依然在 `~/.fluxbox/menu` 文件添加

`[exec] (Switch User) {/usr/bin/gdmflexiserver -a}`

**文件管理器**

可以配置使用 Nautilus ，当然也可以使用 pcmanfm：

`[exec] (Nautilus) {/usr/bin/nautilus --no-desktop}`

**视觉效果**

如果希望使用 xcompmanager 带来的视觉效果，那么可能需要添加如下字段到
`/etc/X11/xorg.conf ` 中：

    Section "Extensions"
    Option "Composite" "Enable"
    Option "RENDER" "Enable"
    Option "RenderAccel" "true"
    Option "AllowGLXWithComposite" "true"
    EndSection

**自启动**

Fluxbox 读取 `~/.fluxbox/startup` 获得自启动的文件信息，只需要在
`exec fluxbox` 行之前添加的内容，都会在启动时运行，例如：

    /usr/bin/nitrogen --restore &
    /usr/bin/xscreensaver &
    /usr/bin/start-pulseaudio-x11 &
    /usr/bin/xcompmgr -f -c -n -C -F &

    # Network manager
    nm-applet >/dev/null 2>/dev/null &

    #Wicd
    wicd-client -n

**注销**

在某些极少数情况下，Fluxbox 的注销菜单只会停止 Fluxbox
本身而不会终结应用程序，这是一个临时解决方法：

`[exec] (Log Out) {killall fluxbox && killall fluxbox}`

**Fluxbox 快捷键**

Fluxbox 读取`~/.fluxbox/keys` 获得快捷键信息，按照如下语法配置：

`key stroke :Command`

例如：`Mod4 f :Exec /usr/bin/firefox`

其中 `Mod4` 代表徽标键。

记得在配置完后**需要重新启动 Fluxbox** 才能生效！

**Dmenu**

参看[本站先前报道](http://linuxtoy.org/archives/dmenu.html)。

[英文原文](http://blog.bodhizazen.net/linux/a-5-minute-guide-to-fluxbox/)
