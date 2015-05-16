Title: 一个完备的个人邮件解决方案
Date: 2008-08-08 08:47
Author: toy
Category: Apps
Slug: personal-email-solution

[撰文/lmm]

有同学说搞wm是浪费时间，那我来发点有用的东西。一切关于linux和windows,cli和X的辩论请绕行。

本系统由以下软件组成：

-   getmail
-   crm114
-   maildrop
-   mutt
-   exim4
-   r2e
-   grepmail
-   pidgin(可选)

主要实现的目标：

-   从多个支持pop3协议的邮箱收信
-   订阅感兴趣的rss内容发到本地信箱
-   备份所有进出邮件
-   达到90%以上的垃圾邮件过滤
-   重要邮件的短信发送

顺便说一下，crm114是一个不错的邮件过滤系统，配置上稍微麻烦点，但是过滤效果惊人，官方主页说能有99%的过滤效果。有一个学习过程。就是你可以在mutt里面标记这个信是垃圾邮件或者是正常邮件来让crm114学习。也支持黑白名单。

grepmail可以搜索邮件，把你感兴趣的内容通过飞信发到你手机。

r2e是一个可以把rss内容发到邮箱的软件。

所有这些软件的定时执行都是用crontab来实现。

exim4是debian默认的MTA,非常不错。

mutt是一个不错的MUA,相信大家都很熟悉了。

这些软件的配合和邮件的流程参考结构图：

[![email-solution-thumb.png](http://i.linuxtoy.org/i/2008/08/email-solution-thumb.png)  
](http://i.linuxtoy.org/i/2008/08/email-solution.png)  
*点击可放大*

提供一个结构图，希望大家切磋。

ps:这是一个实际在运转的系统。
