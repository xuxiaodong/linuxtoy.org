Title: Pidgin 更新：2.5.2
Date: 2008-10-20 19:43
Author: toy
Category: Apps
Tags: IM, Pidgin
Slug: pidgin-252

支持多种协议的流行即时通讯客户端 [Pidgin](http://pidgin.im/)
已于近日放出了一个维护版本 2.5.2。该版本主要对 MSN、XMPP、Yahoo
等协议，以及 Pidgin 本身和 libpurple
库中的缺陷进行了修正。另外也包括一些细微的改进，如 XMPP
支持发送和接收自定义表情、在首选项中添加了静音选项等。

以下是 Pidgin 2.5.2 的更新记录，供大家参考：

> libpurple:  
>  * Fixed a crash on removing a custom buddy icon on a buddy.  
>  * Fixed a crash caused by certain self-signed SSL certificates.  
>  * Enable a number of strong ciphers which were previously disabled
> when using NSS. (Thanks to Marcus Trautwig.)
>
> Pidgin:  
>  * The status selector now saves your message when changing status.  
>  * Fix a case where a conversation window could close unexpectedly.  
>  * A mute sounds option has been added to the preferences window to
> help with discoverability. CTRL+S is no longer bound to mute.  
>  * Added ability to change the color of visited links (using the
> theme control plugin, or setting the color in ~/.gtkrc-2.0)  
>  * Fix a crash occuring when a custom smiley is deleted and re-added
> and used in an open conversation after being re-added.
>
> Finch:  
>  * A new 'Nested Grouping' option in the 'Grouping' plugin. Group
> hierarchies are defined by the '/' character in the group names.  
>  * A bug was fixed where some key-bindings wouldn't work with some
> TERMs (e.g. xterm-color, screen-linux etc.)
>
> MSN:  
>  * Operations (such as moving to a new group) on contacts that were
> added in the same session should now complete correctly, and not cause
> synchronization errors at next login.  
>  * Minor fixes to login process during a server transfer.  
>  * Restored the "Has You" feature to the MSN protocol tooltips.  
>  * ADL 205/214/etc errors should no longer prevent login.
>
> XMPP:  
>  * Sending and receiving custom smileys using the specification in
> XEP-0231 (bits of binary) and XHTML-IM
>
> Yahoo:  
>  * Only send a Ping once every hour. This prevents the account from
> being disconnected from the server periodically.

[Pidgin 2.5.2
的源代码](http://downloads.sourceforge.net/pidgin/pidgin-2.5.2.tar.bz2)可从这里下载。
