Title: Pidgin 2.2.0 版发布
Date: 2007-09-14 20:33
Author: toy
Category: Apps
Slug: pidgin-220-released

支持多种协议的即时通讯软件 [Pidgin](http://pidgin.im/) 已经发布了 2.2.0
版。该版本引入了 Google 代码之夏的一些成果，添加了 MySpaceIM
新协议的支持，为 XMPP
协议增添了新的特性，加入了新的证书管理功能。另外，还修正了一些 bug。

![Pidgin](http://i.linuxtoy.org/i/logo/pidgin.png)

下面是引用自官方的 Pidgin 2.2.0 详细更新记录，供大家参考：

**Libpurple:**  
- New protocol plugin: MySpaceIM (Jeff Connelly, Google Summer of
Code)  
- XMPP enhancements. See
http://www.adiumx.com/blog/2007/07/soc-xmpp-update.php (Andreas
Monitzer, Google Summer of Code for Adium)  
- Certificate management. Libpurple will validate certificates on
SSL-encrypted protocols (William Ehlhardt, Google Summer of Code)  
- Some adjustments were made to fix sending messages when using the MSN
HTTP method. (Laszlo Pandy)  
- Yahoo! Chat is fixed.  
- Some AIM file transfer issues between Pidgin and other clients have
been fixed. (Kyryll A Mirnenko)  
- Properly restore idle status and time for AIM and ICQ accounts when
they reconnect after being disconnected.

**Pidgin:**  
- Insert Horizontal Rules and Strikethrough text from toolbar.  
- Option to show protocol icons in the buddy list, from the Buddies >
Show menu. (Justin Heiner)  
- Ability to build with native, non-X11 GTK+ on OSX. (Anders
Hasselqvist)  
- Remember the 'Enable Sounds' setting for a conversation.  
- Right-clicking the empty space in the formatting toolbar allows you
to toggle back to the old "ungrouped" version.  
- Protocols supporting account registration via Pidgin now show a
descriptive checkbox instead of a vague "Register" button.  
- Fixed a bug where a tab would be shown on single conversations when
tabs were disabled.

**Finch:**  
- Per-conversation mute and logging options (accessible from the menu).

- [Download Pidgin
2.2.0](http://sourceforge.net/project/showfiles.php?group_id=235&package_id=230234&release_id=539413)
