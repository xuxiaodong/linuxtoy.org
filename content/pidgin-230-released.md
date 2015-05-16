Title: Pidgin 2.3.0 发布
Date: 2007-11-27 10:07
Author: toy
Category: Apps
Slug: pidgin-230-released

支持多种协议的即时通讯软件 [Pidgin](http://www.pidgin.im/) 已经发布了
2.3.0 版。Pidgin 2.3.0 是一个 bug 修订版本，主要针对 2.2.1、2.2.2 及
2.2.3 中的各种 bug 进行了修复。除此之外，该版本也包括少许改进和增强。

![Pidgin](http://i.linuxtoy.org/i/logo/pidgin.png)

Pidgin 2.3.0 的详细更改情况如下：

**libpurple**

- Real usernames are now shown in the system log.  
- We now honor a PURPLE\_DISABLE\_DEPRECATED define to allow plugins to
catch deprecated functions earlier rather than later.  
- Thanks to a patch from Intel, the Bonjour prpl now supports file
transfers using XEP-0096 and XEP-0065. This should enable file transfers
between libpurple clients and Gajim clients, but will not work with
iChat or Adium as they use a different file transfer implementation.  
- XMPP password changes that return errors no longer cause the saved
password to be changed.  
- XMPP file transfer support has been enhanced to support sending files
through a proxy when the server supports discovering a a bytestream
proxy. This should make file transfers much more reliable. The next
release will add support for manually specifying a proxy when the server
doesn't advertise one.

**Pidgin**

- If a plugin says it can't be unloaded, we now display an error and
remove the plugin from the list of saved plugins so it won't load at the
next startup. Previously, we were ignoring this case, which could lead
to crashes.  
- Connection errors are now reported in mini-dialogs inside the buddy
list, rather than as buttons in the buddy list and with dialog boxes. If
several accounts are disabled when you sign on elsewhere, you can now
re-enable them all with a single click.  
- Added tooltips to the Room List window to show full topics  
- Added buttons in preferences to access GNOME network and browser
preferences configuration dialogs when running under GNOME  
- If you alias a buddy to an alias that is already present within a
particular group, we now offer to merge the buddies into the same
contact.  
- A music emblem is now displayed in the buddy list for a buddy if we
know she is listening to some soothing music.  
- Added a 'Move to' menu in buddy list context menu for moving buddies
to other groups as an alternative to dragging.  
- Group headings are now marked via an underline instead of a different
color background.  
- It is now possible to mark a chat on your buddy list as "Persistent"
so you do not leave the chat when the window or tab is closed.  
- The auto-join option for chats is now listed in the "Add Chat" dialog
along with the new persistence option.  
- Closing an IM no longer immediately closes your conversation. It will
now remain active for a short time so that if the conversation resumes,
the history will be retained. A preference has been added to toggle this
behavior.  
- The "Smiley" menu has been moved to the top-level of the toolbar.  
- Pidgin's display is now saved with the command line for session
restoration. (David Mohr)  
- ICQ Birthday notifications are shown as buddy list emblems.  
- Plugin actions are now available from the docklet context menu in
addition to the Tool menu of the buddy list.  
- The manual page has been heavily rewritten to bring it in line with
current functionality.

**Finch**

- If a plugin says it can't be unloaded, we now display an error and
remove the plugin from the list of saved plugins so it won't load at the
next startup. Previously, we were ignoring this case, which could lead
to crashes.  
- It's possible to bind key-strokes to specific menuitems in the
windows. Read the 'Menus' section in the man-page for details.  
- 'transpose-chars' operation for the entry boxes. The default
key-binding is ctrl+t.  
- 'yank' operation for the entry boxes. The default binding is ctrl+y

**Windows-specific changes**

- Updated SILC to use SILC Toolkit 1.1.5.

- [下载 Pidgin
2.3.0](http://sourceforge.net/project/showfiles.php?group_id=235&package_id=230234&release_id=556443)

[Thanks leeight!]
