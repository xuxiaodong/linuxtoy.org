Title: 登陆管理器 wdm 的使用
Date: 2009-10-02 21:14
Author: toy
Category: Tutorials
Tags: wdm
Slug: wdm-usage

{ 撰文/lig-linux }

[wdm](http://voins.program.ru/wdm/) 是和 GDM、SLiM、KDM
差不多的登陆管理器，下面介绍一下他的使用方法。

**安装**

sudo apt-get install wdm

如果你同时装有 GDM，一般会出现选择框，来选择是使用 GDM 还是 wdm。

**使用**

运行 `update-alternatives --display x-window-manager`

出现如下情况的话，

    x-window-manager - 自动模式
    链接目前指向 /usr/bin/fvwm
    /usr/bin/fvwm - 优先级 50
    /usr/bin/openbox - 优先级 30
    /usr/bin/aewm - 优先级 40
    目前“最佳”的版本为 /usr/bin/fvwm

那么 wdm 登陆时候会有这三个 WM 来选择。

运行 `update-alternatives --display x-session-manager`

如果出现

    x-session-manager - 自动模式
    链接目前指向 /usr/bin/lxsession
    /usr/bin/lxsession - 优先级 50

那么 wdm 登陆时候会有 lxsession 来选择。

如果 update-alternatives 没有这两项就会出现错误提示。

选择后的 WM 会保存在 ~/.wm\\\_style 中，下次选择 NOCHANGE 就会运行此
WM。

如果某 WM 安装的时候没有运行 `update-alternatives`，可以手动添加

sudo update-alternatives --install /usr/bin/x-window-manager
x-window-manager /usr/bin/thiswm 40

数字 40 代表优先级。

**中文与输入法**

添加文件 /etc/X11/Xsession.d/95xinput 如下

    #export LANG="en_US.UTF-8"
    export LC_CTYPE="zh_CN.utf8"
    export LANG="zh_CN.UTF-8"

    #Chinese Input Engine

    export XMODIFIERS=@im=SCIM
    export XIM=scim
    export XIM_PROGRAM=scim
    export GTK_IM_MODULE=scim-bridge
    export QT_IM_MODULE="scim"
    scim -d

    xrdb -merge ~/.Xresources
    xmodmap ~/.xmodmaprc
    xset b off

就可以了。

最后，给 wdm 的开发者的一个建议是，改个长点的名字，因为 WDM 是英文
Windows  
Driver Model (WDM) 的缩写，所以搜索不到 wdm 的相关网页。

{ Thanks lig-linux. }
