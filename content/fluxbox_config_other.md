Title: Fluxbox 配置补遗
Date: 2006-08-30 22:34
Author: toy
Category: Tutorials
Slug: fluxbox_config_other

-   如何使用 keys 文件

    我们可以利用 keys
    文件来给应用程序绑定快捷键，这样就能够直接通过所绑定的快捷键来启动该应用程序。此文件一般位于
    ~/.fluxbox/keys，可以使用任何文本编辑器修改。

    keys 文件的使用语法是：

    <mod> [<mod> <mod>] key [key key] :command <commanoptions>

    其中，<mod> 是指 modifier，包括 Mod1（即 Alt）、Mod4（即
    Windowskey）、Control（即 ctrl）、Shift（即 shift）等。通过
    xmodmap -pm 可以看到更多的 modifier。modifier
    可以不用、也可以使用一个、或使用两个、甚至三个。key 和 command
    很好理解，前者为所用的按键，后者为执行的命令。

    现在让我们来举个例子，假如我想通过按 Ctrl+F 组合键来启动
    Firefox，那么可以这样写：`Control f :exec firefox`。例子中的 exec
    也可以写成 ExecCommand。

    通过执行 fluxbox menu -> Reload config
    右键菜单命令，上述更改将立即生效。


