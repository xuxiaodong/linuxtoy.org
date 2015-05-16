Title: Tapioca－语音通话及即时聊天软件
Date: 2006-08-24 16:18
Author: toy
Category: Apps
Slug: tapioca

[Tapioca](http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca)
是一个在 Linux 中可以有效替代 [Gtalk](http://www.google.com/talk/)
的语音通话和即时聊天软件，你可以直接使用 Gtalk 的帐号登录，并与 Gtalk
通话联络或文字交谈。虽然我们可以通过 Gaim 与 Gtalk
用户进行沟通，但方式毕竟有限，当前只能文字交流而无法语音通话。而 Tapioca
在功能上两者兼而有之，可以作为在 Gtalk 没有正式移植到 Linux
之前的有力尝试。在测试中，Tapioca
的通话质量尚可，通过文字交谈时，能够直接使用 SCIM
输入法，中文输入没有一点问题。但也存在程序不够稳定，界面功能过少等缺点。

[![Tapioca](http://i.linuxtoy.org/i/tapioca_s.png)](http://i.linuxtoy.org/i/tapioca.png)

Tapioca 最新版本为 0.3.9，在 Ubuntu Dapper
中可以通过以下方式安装（其他系统可参照[此页](http://tapioca-voip.sourceforge.net/wiki/index.php/Installation_Guide)提供的介绍）：

1.  将 `deb http://extindt01.indt.org/VoIP/apt dapper main` 添加到
    /etc/apt/sources.list 中。
2.  执行 `sudo apt-get update` 更新源。
3.  执行 `sudo apt-get install tapiocaui0.3` 安装 Tapioca。

安装完成后可以通过 tapiocaui
启动，或者自己建立一个快捷方式更方便。另外，Tapioca
网站上也提供了一个更多界面功能的
[Landell](http://tapioca-voip.sourceforge.net/wiki/index.php/Landell)，有兴趣的可以一试。
