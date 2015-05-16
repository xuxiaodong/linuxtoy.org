Title: 为 Gtalk 配置 Gajim
Date: 2007-02-10 21:32
Author: toy
Category: Tutorials
Slug: configure-gajim-for-gtalk

之前我一直使用 [Gaim](http://gaim.sourceforge.net/) 作为
[Gtalk](http://www.google.com/talk/) 的默认客户端，最近通过尝试
[Gajim](http://linuxtoy.org/archives/gajim.html)，感觉甚和我意，于是有了替换的打算。Gaim
最大的特色在于支持多种即时通讯协议，不过个人对于这种 All in one
的做法并不太感冒。Gajim
就不同了，它专精于一个方面，提供完备而简约的即时通讯体验。而且，通过适当配置，在
Gajim 中利用 Gtalk 帐号也可与 MSN 好友交流。

为了能够在 Gajim 中使用 Gtalk 的帐号，可以通过以下方法来配置：

1.  打开 Gajim。
2.  点击 Edit -> Accounts 菜单命令，或者按 Ctrl + A。
3.  从 Accounts 窗口中点击 New 按钮。
4.  在 Gajim: Account Creation Wizard 的第一个屏幕窗口中选择 I already
    have an account I want to use，然后点击 Forward 继续。  
    [![Gajim
    Options](http://i.linuxtoy.org/i/2007/02/gajim-options_s.jpg)](http://i.linuxtoy.org/i/2007/02/gajim-options.jpg)
5.  在 Username 中输入 Gtalk 帐号的 @ 之前的内容，Server 中输入
    gmail.com，Password 中输入密码。如果需要保存密码，可以选中 Save
    password 选项。完成后点击 Forward。  
    [![Gajim
    Account](http://i.linuxtoy.org/i/2007/02/gajim-account_s.jpg)](http://i.linuxtoy.org/i/2007/02/gajim-account.jpg)
6.  去掉对 Connect when I press Finish 选项的选择，点击 Finish
    关闭窗口。  
    [![Gajim
    Finish](http://i.linuxtoy.org/i/2007/02/gajim-finish_s.jpg)](http://i.linuxtoy.org/i/2007/02/gajim-finish.jpg)
7.  回到 Accounts 窗口，选中刚才创建的 gmail.com，点击 Modify 按钮。
8.  切换到 Account Modification 窗口中的 Connection 标签，选中下面的 Use
    custom hostname/port，并在 Hostname 中输入 talk.google.com，Port
    中输入 5222，完成后点击 Save。  
    [![Gajim
    Modify](http://i.linuxtoy.org/i/2007/02/gajim-modify_s.jpg)](http://i.linuxtoy.org/i/2007/02/gajim-modify.jpg)

OK. 现在可以使用 Gajim 连接到 Google Talk 服务了。
