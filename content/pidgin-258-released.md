Title: Pidgin 2.5.8 发布
Date: 2009-06-29 11:08
Author: toy
Category: Apps
Tags: IM, Pidgin
Slug: pidgin-258-released

继
[2.5.7](http://linuxtoy.org/archives/pidgin-releases-257-bug-fixed-version.html)
之后，Pidgin 开发团队在今天发布了又一个 Bug 修订版本
2.5.8。该版本主要包含对 ICQ、MSN、MySpace、Yahoo、以及 XMPP
等协议的修正。

以下为 Pidgin 2.5.8 Changlelog，供参考：

ICQ

* Fix misparsing a web message as an SMS message. (Yuriy Kaminskiy)

MSN

* Increase NS command history size to prevent crashes on buddy lists
that have a lot of buddies on other networks like Yahoo!

MySpace

* Accounts with empty buddy lists are now properly marked as
connected.  
* Fix receiving messages from users of MySpace IM's web client.

Yahoo

* Fixed phantom online buddies. They should now properly disappear when
signing out.  
* Fixed the crashes some users were seeing with cn.scs.msg.yahoo.com
in 2.5.7.  
* Fixed compiling on systems with glib 2.4.x or older.  
* Fixed an issue with file transfers. This may not resolve all issues,
but it should resolve at least some of the most common ones.  
* The pager server will automatically update to scsa.msg.yahoo.com if
the user empties the field or if it is scs.msg.yahoo.com. This should
ease the pain of transition to the new login method.

XMPP

* Fix an incompatibility betweeen Prosody and libpurple clients.

[下载 Pidgin 2.5.8](http://pidgin.im/download/)。
