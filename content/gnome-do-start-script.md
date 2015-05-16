Title: GNOME Do 的启动脚本
Date: 2008-01-20 09:06
Author: toy
Category: Apps
Slug: gnome-do-start-script

[GNOME Do](http://linuxtoy.org/archives/gnome-do.html) 是非常酷的一个
Linux
下的应用程序。最近更新了版本，插件的功能有所增强，现在已经是我不可或缺的日常应用了。我可以随便敲几个键就呼出想用的应用程序，可以随便敲入几个键就播放我想听的专辑，可以随便敲入几个键就搜索出我想回顾的笔记，可以随便敲入几个键就和某个朋友聊天或者发送电子邮件，可以随便……very
awesome……基本不用动鼠标了……如果你对 Mac 下面的 Quicksilver
有所了解的话，就不难理解 GNOME Do 是干嘛的了，我只希望 GNOME Do
的作者多多努力，早日赶超 Quicksilver，哈。

如果你也在使用 Linux，如果你也对键盘有特殊偏爱，那么我强烈向你推荐 GNOME
Do，官方主页在这里：<http://do.davebsd.com/> 去折腾吧……

现在的 GNOME Do 版本在启动的时候如果同时启动 Compiz 就有可能会出现
Conflict，导致背景变透明，这样在某些白色背景的应用程序上面可能就看不清楚字母了，没关系，写了一个
script 来解决这个问题，和解决 avant window navigator
类似问题的方法一样。

1. `sudo vim /usr/local/bin/startdo`  
2. 输入下面的代码

`#!/bin/bash # vim:sts=4:ai:et:`

    while ! {
        ps x | grep compiz | grep -v grep >/dev/null 2>&1
    }
    do
        sleep 3
    done

`exec gnome-do -quiet >/dev/null 2>&1 & echo "Gnome-Do started"`

3. :wq! 存盘退出 vim  
4. `sudo chmod +x /usr/local/bin/startdo`  
5. 在你开机启动 gnome－do 的地方换成 startdo

enjoy it, 哈。

[撰文 /
[Jay](http://thatssky.spaces.live.com/blog/cns!251B8640E925FC00!627.entry)]
