Title: 偷看最终版 GNOME Shell 1
Date: 2009-10-04 15:13
Author: Yunkwan
Category: Desktop Stuff
Tags: GNOME, GNOME Shell
Slug: sneak-peek-at-gnome-shell-1

{ 撰文/[Yunkwan](http://kwanlife.yo2.cn/) }

早前的文章介绍过目前的 [GNOME  
Shell](http://linuxtoy.org/archives/gnome-shell-intro.html)。想知道最终
GNOME Shell 变成什么样子？  
往下看！

**先说一下 Top Menubar**

* GNOME Shell 有且只有一个 top menu bar。  
* Top menu bar 有 4  

个版块：“活动”(Activities)、“时间/日期”、“系统状态区域”、“用户状态菜单”。

[![Top  

Menubar](http://i.linuxtoy.org/images/2009/10/thumb-top-menubar.png)](http://i.linuxtoy.org/images/2009/10/top-menubar.png)

* “活动”估计和目前的 GNOME Shell 里面的变化不大。  
* “时间/日期”将会添加点击弹出下拉的东西 (未定)。  
* “系统状态区域”将把 Applets 踢走。  
* 并且“系统状态区域”不会被任何程序作通知使用。即什么邮件通知，IM  
程序等等的程序的 tray  

都不会出现。“系统状态区域”只显示系统状态相关信息，比如：声音、网络连接、电源……  
*
“系统状态区域”的状态图标只负责显示状态，不能像过去那样可以点击或进行操作。即是，这里的图标只许看不许动，也不能动。而且那些图标的样子也会设计成让你觉得是不可点击操作的。  
* “用户状态菜单”会包括 IM 状态，可能会加入联系人列表相关功能 (未定)。

**底部**

* 整个底部被用作 Message Tray “消息托盘”。  
*
“消息托盘”所弹处的通知将更加人性化，设计将会能做到通知的作用，却不会打扰你的工作~  
* “消息托盘”有 3 个模式：“通知模式”(Notification
Mode)、“概况模式”(summary mode)、“详细模式”。  
* “通知模式”

[![Notification  

Mode](http://i.linuxtoy.org/images/2009/10/thumb-notification-mode.png)](http://i.linuxtoy.org/images/2009/10/notification-mode.png)

当有新的消息时，通知会从屏幕底部向上划动出现。 (只有一行)  
如果消息没有被用户理会，通知将会淡淡消失，从而启动“概况模式”  
，未读信息数将显示在“概况模式”中。  
如果用户把指针移到通知处，通知停顿并保持可见。  
通知消失后，用户指针在“消息托盘”区域里面不会有任何影响。  

如果通知的消息有详细内容，用户点击通知就必须能打开进入消息的“详细模式”。

* “概况模式”

[![Summary  

Mode](http://i.linuxtoy.org/images/2009/10/thumb-summary-mode.png)](http://i.linuxtoy.org/images/2009/10/summary-mode.png)

“概况模式”中“消息托盘”会显示非空消息源的图标，点击图标就能打开看到"详细模式"。

* 在繁忙或无人的状态下会显示“概况模式”而不显示消息通知。  
* 如果消息源的程序在使用中 (在前台)  
或消息已被阅读的话，消息源的图标将不被显示在“消息托盘”。  
* “详细模式”

[![Detail  

Mode](http://i.linuxtoy.org/images/2009/10/thumb-detail-mode.png)](http://i.linuxtoy.org/images/2009/10/detail-mode.png)

“详细模式”将以合适的方式来显示消息。如果是即时消息，将显示消失并允许用户回复。(这将需要
IM 客户端的配合)

* 消息对话源可能结合来自该联系人的 IM、Email、SMS 和
Twitter，并应该提供完整的对话记录，即使上一个对话在另一个系统中进行。

还有不少东西是待定的。文档足足有 37 页，今天先选取这些最大变化的设计。

{
[Source](http://kwanlife.yo2.cn/articles/偷看最终版-gnome-shell-1.html).  
Thanks Yunkwan. }
