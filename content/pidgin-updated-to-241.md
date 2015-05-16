Title: Pidgin 更新到 2.4.1 版
Date: 2008-04-01 09:46
Author: toy
Category: Apps
Tags: IM, Pidgin
Slug: pidgin-updated-to-241

即时通讯软件 [Pidgin](http://pidgin.im) 已经更新到了 2.4.1
版。新版本除了对 Pidgin、Finch 及 libpurple 库中所存在的 bug
进行修正之外，也包括其他一些改进，比如：针对 Gadu-Gadu 添加了设置 buddy
图标的支持、改善了 ICQ 中 UTF-8 群名的处理、增大了 XMPP 的 ping
超时时间，等等。推荐使用 Pidgin 的朋友更新。

![Pidgin](http://i.linuxtoy.org/i/logo/pidgin.png)

以下摘自 [Pidgin 2.4.1
的详细更改记录](http://developer.pidgin.im/wiki/ChangeLog)，谨供参考：

> * libpurple  
>  o Treat AIM Unicode messages as UTF-16 rather than UCS-2; this should
> have no functional effect, other than continued support on systems
> which have dropped UCS-2 conversions.  
>  o Add support for setting buddy icons on Gadu-Gadu (Tomasz
> Salacinski)  
>  o Fix a crash when clearing the buddy icon for an account on XMPP  
>  o Fix a crash during login for some ICQ accounts  
>  o Prefer more available resources on XMPP when priorities are equal  
>  o Fix incorrectly marking some Yahoo! contacts as blocked  
>  o Improved handling of UTF-8 group names on ICQ (beret)  
>  o Fix a crash when starting if you have a Zephyr account  
>  o Increase XMPP ping timeout to 120 seconds, to prevent poor network
> connections from timing out unnecessarily.  
>  o Don't crash on XMPP forms with empty default values.  
>  o Fix issues with CHAP authentication for SOCKS5 proxies.
>
> * Pidgin  
>  o Remove a workaround for older versions gstreamer that was causing
> crashes on some non-Linux systems such as HPUX  
>  o Fix some cases of the conversation input entry area being 1 pixel
> high  
>  o Fix for displaying channel & buddy names in conversation window
> when they have '&' in them  
>  o Some memory leak fixes, especially in the Text Replacement plugin  
>  o Rectangular but non-square buddy icons have rounded corners in the
> buddy list
>
> * Finch  
>  o Fix compiling with Glib older than 2.6  
>  o Ensure existing conversations selected from the 'Send IM' dialog
> are given focus  
>  o Move the tooltip on the left of the buddylist if there's not enough
> room on the right to show it.

Pidgin 能够在 Linux/Unix 及 Windows 平台上运行，其 [2.4.1
版可从这里下载](http://pidgin.im/download/)。
