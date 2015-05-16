Title: 软响铃 ── 把 beep 换成音乐
Date: 2007-07-01 21:23
Author: toy
Category: Apps
Slug: softbeep

很多人千方百计想关掉控制台（或 X
终端模拟器）的嘀嘀声。我觉得有提示音不一定是坏事，但是那个嘀嘀声听起来的确有点烦人。而且在我的
irssi 中那个 beep
提示音实在是太小声了（而且也不好听）。经过一番寻找，找到了这个
[softbeep](http://0pointer.de/lennart/projects/softbeep/)。softbeep
可以拦截多个发出 beep 的动作，并将其转化成运行任意命令，包括播放音乐。

softbeep 可以拦截这些事件：

1.  写入 tty 控制台的 bell 字符，就是平时所说的’\\a’
2.  基于 gtk/gnome 的程序对 gdk\_bell() 的调用
3.  基于 Xlib 的程序对 XBell() 的调用
4.  基于 curses 的程序对 beep() 的调用

安装不多述。启用 softbeep 很简单，设置在环境变量 $LD\_PRELOAD 中加
/usr/lib/softbeep/libsoftbeep.so，或者用软件包提供的包装程序：

`softbeep foo`

softbeep 完全是通过环境变量控制的：

`SB_REMOVE_BEL 设为 yes 的话会丢掉 TTY 控制台的‘a’字符。 SB_RUN 事件发生时运行的程序。`

如果使用 softbeep foo 的形式启用 softbeep，那么 SB\_RUN 默认为
sb-beep，可以自定义 SB\_RUN 的值，但记着要用 shell
脚本包起来。我为方便直接改了一下 /usr/bin/sb-beep：

    #!/bin/sh

    FILE=/usr/share/sounds/pidgin/alert.wav

    # if [ “$1″ == “irssi” ] || [ “$1″ == “xchat” ] ; then
    #       FILE=/usr/share/sounds/email.wav
    # fi

    # use the player specified in $SB_PLAYER if defined

    if [ -z “$SB_PLAYER” ]; then
           exec esdplay $FILE
    else
           exec $SB_PLAYER $FILE
    fi

从此烦人的嘀嘀声就变成音乐了~…

[撰文/[AutumnCat](http://bigsnakecat.blogspot.com/2007/06/beep.html)]
