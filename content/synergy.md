Title: 使用 Synergy 来进行协同工作
Date: 2008-04-30 20:05
Author: toy
Category: Apps
Tags: Cool apps, Synergy
Slug: synergy

这两天发现 [Synergy](http://synergy2.sf.net/) 这个软件挺不错的。Synergy
有 Windows、Linux、Mac OS
下面的版本，主要用来让多台机器之间共享一套鼠标和键盘。例如：Windows
可以共享 Linux 下面的鼠标和键盘。

Synergy 的主要工作原理是，Linux 下面开启 synergy 这个服务，Windows
下面使用客户端链接服务器就 OK 了。反过来在 Windows
下面也可以开启服务，Linux 来连接 Windows 下面的服务器。

Synergy 配置起来也很简单，例如我的 Linux 下面的配置文件
/etc/synergy.conf 的内容是：


    section: screens
            linux:
            windows:
    end

    section: links
            linux:
                right   = windows
            windows:
                left    = linux
    end

screens 那段的意思就是设置了两个屏幕，一个是 Linux 的，一个是 Windows
的。links 那段的意思就是，当鼠标从 Linux 屏幕右边 (right)
移出去之后，就到了 Windows 的那个屏幕中了。当鼠标从 Windows 的屏幕左边
(left) 移出去之后，就到了 Linux 了。

当然还可以配置更多台机器，比如当鼠标从 Linux 屏幕上面 (top)
移出去之后，就可以设置到了 Windows1 的屏幕中了，等等。

使用 Synergy 之后，还可以共享系统的剪贴板 (Linux 和
Windows)。不过用起来感觉不太习惯。

[撰文/leeight]
