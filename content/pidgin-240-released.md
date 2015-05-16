Title: Pidgin 2.4.0 发布
Date: 2008-03-01 13:33
Author: toy
Category: Apps
Slug: pidgin-240-released

[Pidgin](http://linuxtoy.org/search/pidgin) 在今天发布了 2.4.0
版。新版本对 libpurple 库、Pidgin 及 Finch 都有所改进。比如，libpurple
添加了对 AIM 的离线消息支持、现在支持 Yahoo! Messenger 7.0+
以上版本的文件传输方法、Pidgin
聊天窗口的文字输入区域能够自动调整大小等。另外，Pidgin 2.4.0 也对一些
bug 进行了修正。

![Pidgin](http://i.linuxtoy.org/i/logo/pidgin.png)

Pidgin 2.4.0 的详细更改日志如下：

> * libpurple  
>  o Added support for offline messages for AIM accounts (thanks to
> Matthew Goldstein)  
>  o Fixed various problems with loss of status messages when going or
> returning from idle on MySpaceIM.  
>  o Eliminated unmaintained Howl backend implementation for the Bonjour
> protocol. Avahi (or Apple's Bonjour runtime on win32) is now required
> to use Bonjour.  
>  o Partial support for viewing ICQ status notes (Collin from ComBOTS
> GmbH).  
>  o Support for /notice on IRC.  
>  o Support for Yahoo! Messenger 7.0+ file transfer method
> (Thanumalayan S.)  
>  o Support for retrieving full names and addresses from the address
> book on Yahoo! Japan (Yusuke Odate)  
>  o The AIM/ICQ server-side preference for "allow others to see me as
> idle" is no longer unconditionally set to "yes" even when your
> libpurple preference is "no."  
>  o Fix SSL certificate checks for renewed certificates  
>  o Fix the ability to set vCard buddy icons on Google Talk/XMPP  
>  o D-Bus fixes on 64bit  
>  o Fixed retrieval of buddy icons and setting of server-side aliases
> on Yahoo! and Yahoo! Japan when using an HTTP proxy server (Gideon N.
> Guillen)  
>  o Fixed an MSN bug that would leave you appearing offline when
> transferred to different server
>
> * Pidgin  
>  o Input text area in conversation windows auto-resizes to fit more
> lines (up to a maximum of 4 lines)  
>  o Added the ability to theme conversation name colors (red and blue)
> through your GTK+ theme, and exposed those theme settings to the
> Pidgin GTK+ Theme Control plugin (Dustin Howett)  
>  o Fixed having multiple alias edit areas in the infopane (Elliott
> Sales de Andrade)  
>  o Save the conversation "Enable Logging" option per-contact (Moos
> Heintzen)  
>  o Typing notifications are now shown in the conversation area
>
> * Finch  
>  o Color is used in the buddylist to indicate status, and the
> conversation window to indicate various message attributes. Look at
> the sample gntrc file in the man page for details.  
>  o The default keybinding for dump-screen is now M-D and uses a file
> request dialog. M-d will properly delete-forward-word, and M-f has
> been fixed to imitate readline's behavior.  
>  o New bindings alt+tab and alt+shift+tab to help navigating between
> the higlighted windows (details on the man page).  
>  o Recently signed on (or off) buddies blink in the buddy list.  
>  o New action 'Room List' in the action list can be used to get the
> list of available chat rooms for an online account.  
>  o The 'Grouping' plugin can be used for alternate grouping in the
> buddylist. The current options are 'Group Online/Offline' and 'No
> Group'.  
>  o Added a log viewer  
>  o Added the ability to block/unblock buddies - see the buddy context
> menu and the menu for the buddy list.  
>  o Fixed a bug preventing finch working on x86\_64

你可以从这里[下载 Pidgin 2.4.0 的源代码及 RPM
包](http://pidgin.im/download/)。
