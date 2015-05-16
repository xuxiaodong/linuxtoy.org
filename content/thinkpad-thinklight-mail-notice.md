Title: 使用 ThinkPad 键盘灯做邮件提醒
Date: 2009-07-15 15:23
Author: toy
Category: Tips
Slug: thinkpad-thinklight-mail-notice

{撰文/[lvscar](http://blog.lvscar.info/)}

ThinkPad
屏幕顶部的键盘灯（ThinkLight）很可爱，虽然起不了什么照明效果，但黑暗环境下挂在视线正中的一束幽幽冷光貌似真能给思考增添灵感。这灯和小红点一道构成了
THINK 味的重要调料。

[Pidgin](http://www.pidgin.im/) 有一个有趣的插件
[blanklight](http://www.joachim-breitner.de/blog/archives/239-gaim-thinklight-pidgin-blinklight.html)，能在新
IM 消息到来时闪烁 ThinkPad
键盘灯以做提醒。我很喜欢这个插件，虽然其只能用于 IM
消息提醒，且只能闪烁固定的 3 次。

对于大多数用户来说，新邮件提醒应该比 IM 消息提醒更为重要。受 blanklight
的启发，我决定用 ThinkLight 来进行邮件提醒。

我的桌面环境是 [Xfce
4](http://www.xfce.org/)，她的面板自带一个非常出色的邮件提醒插件 [Xfce4
Mailwatcher](http://spuriousinterrupt.org/projects/mailwatch)
能同时监视多个邮件帐号，支持几乎所有邮件服务（IMAP、POP3、GMAIL、LocalMail...），并且能在监测到新邮件时执行指定程序。

我写了一个控制 ThinkLight 的小脚本，以 `--start`
作为参数运行时能让键盘灯一直闪烁，如果以 `--stop`
参数运行则检查小灯是否已经在闪烁，如果是则让其闪烁停止。让 Xfce4
Mailwatcher 在收到新邮件和点击图标时执行这脚本的两种运行方式。一套完美的
ThinkLight 邮件提醒系统就完成了 ;-)

用 Linux 的 ThinkPad 用户可以玩玩这个脚本
[lightup](http://lvscar.info/code-snippet/python/lightup)，很简单的配置过程已经写在里面，请用文本编辑器查看。

ps1:

[ThinkWiki](http://www.thinkwiki.org/wiki/ThinkLight) 中列出了其他一些和
ThinkLight 有关的程序。

ps2:

GNOME 或 KDE 中有类似 Xfce4 Mailwatcher 的面板插件吗？
