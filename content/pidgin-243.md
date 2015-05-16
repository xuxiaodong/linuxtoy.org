Title: Pidgin 已更新到 2.4.3
Date: 2008-07-03 15:06
Author: toy
Category: Apps
Tags: IM, Pidgin
Slug: pidgin-243

著名的跨平台多协议即时通讯软件 [Pidgin](http://linuxtoy.org/tag/pidgin)
已经更新到了 2.4.3 版。新版本对 [Pidgin](http://linuxtoy.org/tag/pidgin)
和 libpurple 库中的 bug 进行了修订，主要解决了内存泄漏、有关 Yahoo!
协议、jabber id 无效造成程序崩溃等问题。

![Pidgin](http://i.linuxtoy.org/i/logo/pidgin.png)

以下为 [Pidgin 2.4.3
更改记录](http://www.pidgin.im/ChangeLog)，供大家参考：

> libpurple:  
>  * Yahoo! Japan now uses UTF-8, matching the behavior of official
> clients and restoring compatibility with the web messenger (Yusuke
> Odate)  
>  * Setting your buddy icon once again works for Yahoo! accounts.  
>  * Fixes in the Yahoo! protocol to prevent a double free, crashes on
> aliases, and alias functionality  
>  * Fix crashes in the bonjour protocol  
>  * Always use UTF-8 for Yahoo! (#5973)  
>  * Fix a crash when the given jabber id is invalid.  
>  * Make the IRC "unknown message" debugging messages UTF-8 safe.  
>  * Fix connecting to ICQ  
>  * Fix a memleak when handling jabber xforms.
>
> Pidgin:  
>  * Include the send button plugin in the win32 build  
>  * Various memory leak fixes

[Pidgin 2.4.3 的源码包及 RPM
包](http://www.pidgin.im/download/)可从其官方网站下载。
