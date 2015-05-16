Title: Pidgin 登陆 MSN 失败解决方案
Date: 2008-12-28 18:53
Author: JimHu
Category: Apps
Tags: MSN, Pidgin
Slug: pidgin-msn-failure

Pidgin 最近已经更新到 2.5.3 了，对于 QQ
协议的支持已经日趋完善，连校验码都能显示了。但是，问题还是不断。  
这次更新完毕后，MSN 协议似乎在我这里是不能登陆了。同样的情况下，使用
Windows Live Messenger 8.5 可以登陆，但是用 Pidgin for Windows
就是不能登陆。并且在 Ubuntu-CN
的论坛上，也有人报告了同样的情况。因此撰写此文以期帮助那些不能登陆的朋友。  
  
估计这个问题是由于 MSN
的协议插件导致的，所以我们只需要下载一个替代品就好了。  
MSN-Pecan 就是一个 Pidgin 用的 MSN 协议替代品。作者对于 Pidgin 中原来的
MSN 协议滞后非常不满，所以决定自行开发。使用这个插件就可以正常登陆 MSN
了。

我们需要下载这个用于替代的插件。可以从下面地址下载：  
<http://code.google.com/p/msn-pecan/downloads/list>

Windows 用户下载 exe 文件，Ubuntu 或者 Debian 用户下载 deb
文件。然后按照提示完成安装。

安装完毕后，我们需要重新开启一下 Pidgin。然后，我们需要禁用 MSN。  
找到“帐户”->“帐户管理( Manage Account )”。在新打开的窗口中，把 MSN
协议前面的钩取消掉，然后按下面的“ Modify... ”。

在新弹出的对话框中，将“登陆选项”修改为“ WLM ”。“保存”即可。  

[![](http://i.linuxtoy.org/images/2008/12/pidgin.png)](http://i.linuxtoy.org/images/2008/12/pidgin.png)

完成后，钩上 WLM 协议前面的对钩，然后应该就可以登陆 MSN 了。

最后，说句题外话。在 Windows 下，Pidgin
似乎又遇到了退出卡死的错误，真的是功能虽多，但却简陋，问题也不少。如果各位希望能够帮助
Pidgin 提高，不如前往他们的网站完成一个英文的问卷调查，帮助 Pidgin。  
问卷地址如下：<http://www.pidgin.im/survey/index.php?sid=84494>
