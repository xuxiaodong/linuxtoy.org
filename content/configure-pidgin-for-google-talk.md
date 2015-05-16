Title: Pidgin 连接 Google Talk 的配置
Date: 2007-05-05 18:16
Author: toy
Category: Tips
Slug: configure-pidgin-for-google-talk

昨天，在编译好 Pidgin 2.0.0 之后，为了和使用 Google Talk
的朋友联络，在配置时发现与 Gaim 当初的稍有不同。现写下来供大家参考。

在 Pidgin 中添加新的帐号时，就会打开“Add Account”对话框。为了能够与
Google Talk 连接，其设置要点如下：

1.  在基本标签页：
    -   Protocol：选择 XMPP
    -   Screen name：填写 Gmail 帐号 @ 之前的内容
    -   Server：填写 gmail.com
    -   Resource：Pidgin
    -   Password：填写 Gmail 帐号的密码

    [![Pidgin](http://i.linuxtoy.org/i/2007/05/pidgin-add-account_s.png)](http://i.linuxtoy.org/i/2007/05/pidgin-add-account.png)
2.  切换到高级标签页：
    -   Connect port：默认是 5222
    -   Connect server：填入 talk.google.com

    [![Pidgin](http://i.linuxtoy.org/i/2007/05/pidgin-add-account-2_s.png)](http://i.linuxtoy.org/i/2007/05/pidgin-add-account-2.png)

