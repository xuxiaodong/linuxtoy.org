Title: Skype 2.0 Beta 更新
Date: 2007-12-06 09:25
Author: toy
Category: Apps
Slug: skype-20-beta-update

在上月初，Skype 推出了包含视频通话功能的 [2.0 Beta
版](http://linuxtoy.org/archives/skype-20-beta-for-linux-released.html)。近日，Skype
方面对该版本进行了更新，其版本号显示为
2.0.0.27。这个版本一方面添加了一些新的特性和改进，使 Skype
更加好用；另一方面，也 hotfix 了很多反馈的问题。

![Skype](http://i.linuxtoy.org/i/2007/12/skype.png)

Skype 2.0.0.27 的更新记录如下：

- feature: Command-line login functionality provided by —pipelogin  
- feature: Show when someone is speaking during a call  
- feature: API: Add GET/SET WINDOWSTATE functionality  
- feature: Shift-Enter in contact list will activate the opposite
default action on the selected contact (call instead of chat and vice
versa)  
- improvement: UYVY conversion for Apple iSight cameras.  
- improvement: Changes to ease CPU usage on v4l(1) cameras  
- improvement: Support for more resolutions on v4l and v4l2 cameras  
- improvement: Avoid flickering in the call window video area  
- bugfix: Crash for v4l cameras when switching resolution.  
- bugfix: Crash when finishing call with some cameras.  
- bugfix: Crash/memory leak with uvc cameras on fglrx driver.  
- bugfix: Workaround for uvc split-frame video bug with new Logitech
cameras.  
- bugfix: Allow toggling of fullscreen while video is paused.  
- bugfix: Unable to resume video after resuming the call.  
- bugfix: Disable video while in a conference call.  
- bugfix: Crash on View Profile in Qt 4.3.1 and earlier.  
- bugfix: Fix contact/event skipping whilst scrolling through Contact
List and Events History with keyboard.  
- bugfix: Fix Call button for newly added SkypeOut contact. Remove Chat
button for newly added SkypeOut contact.  
- bugfix: Close chat window when you leave chat.  
- bugfix: Cancel search (if active) or close Search window if Escape is
pressed.  
- bugfix: Add connecting animation to status icon.  
- bugfix: Don’t call random names when quickfilter reveals a single
selection and we press enter.  
- bugfix: Rejecting incoming calls from the incoming call popup should
redirect to Voicemail if necessary.  
- bugfix: Incoming file transfer in Do Not Disturb should go to New
Events area without popup window.  
- bugfix: Add tooltip for (flag:xx) in chat.  
- bugfix: API: “OPEN FILETRANFER … IN path” command improvements.  
- bugfix: When offline, the number of online users should not be
shown.  
- bugfix: Shift-F3 should bring Find in chat dialog with search
direction preset to Up.

Skype 可用于
Ubuntu、Debian、Fedora、openSUSE、Mandriva、CentOS、Mepis、Xandros 等
Linux
发行版，你可以从[这里下载](http://www.skype.com/intl/en/download/skype/linux/beta/choose/)。
