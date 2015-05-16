Title: 跨平台飞信软件 libFetion 发布 1.0 版本
Date: 2009-07-04 00:19
Author: lovenemesis
Category: Instant Messenger
Tags: LibFetion
Slug: linux-libfetion-10-final-released

跨平台的飞信通讯软件 libFetion 近日发布了 1.0
正式版，做为具有里程碑意义的首个正式版本，包含了诸多改善。

*以下内容摘自 libfetion 发布日志*

v1.0.0 (09.06.08-09.07.01)  
1:解决英文菜单问题.  
2:增加群消息可以选择不自动弹出功能.  
3: 解决取消登录导致程序崩溃bug.  
4: 完善手机用户登录状态显示.  
5: 解决聊天记录窗口打开多次问题.  
6: 解决表情代码与官方有些差异问题.  
7: 解决边缘隐藏的问题.  
8: 解决a2启动主界面隐藏功能不正常.  
9: 解决a2好友列表出现负数BUG.  
10: a2热键失效问题(windows).

v1.0.0 alpha2 (09.05.24-09.06.07)  
1: 完成新皮肤的管理功能.  
2: 增加记住新皮肤的窗口大小,位置功能.  
3: 完善新皮肤设置字体功能.  
4: 解决1.0a部分用户登录崩溃问题.  
5: 解决windows输入法不兼容这个历史遗留老问题.  
6: 解决1.0a区分用户登录设备功能失效问题.

v1.0.0 alpha1 (09.04.21-09.05.23)  
1: 增加定时短信发送功能.  
2: 增强界面,如边界隐藏,皮肤.  
3: 解决V0.9.3 不能给自己发短信BUG.  
4: 区分用户登录设备,如手机登录还是电脑登录.(需要图标支持)  
界面改善  
1: 支持使用CSS来定制界面元素.  
2: 窗口边框,背景可定制,不再使用缺省系统样式.  
3: 增加其它图片格式支持. (png,jpeg)  
4: 改善好友列表显示效果.  
5: 主窗口将布局改善,并支持Layout.  
6: 主窗口增加边缘隐藏功能并除去任务栏图标(仅windows).

*引用结束*

[Linux 平台下载](http://www.libfetion.cn/Linux_demoapp_download.html)

Fedora 11 用户下载见 [FZUG Gcell
专贴](http://bbs.fedora-zh.org/showthread.php?t=700)

或者在下的 Dropbox
分流点：[linux-fetion-1.0-2.fc11.i586](http://files.getdropbox.com/u/464139/linux-fetion-1.0-2.fc11.i586.rpm)

建议已经安装了老版本的朋友先在终端使用

`su -c 'yum remove linux-fetion' `

删除老版本，即可双击新版本 RPM 包安装了。
