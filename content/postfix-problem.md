Title: Postfix 故障解决一例
Date: 2010-05-07 10:13
Author: toy
Category: Tips
Tags: Postfix, Ubuntu
Slug: postfix-problem

{ 撰文/[逸飞](http://www.billdeng.com) }

[清风博客](http://www.billdeng.com)的邮件系统升级至 Ubuntu 10.04  
后（全新安装，恢复配置），发现 Postfix  
出现故障，不能向外发送邮件了。

赶紧查看 Postfix 状态：

# service postfix status

    * postfix is not running

奇怪了，查看 log:

# tail /var/log/mail.log

    postfix/master[2391]: fatal: open lock file /var/lib/postfix/master.lock:
    cannot open file: Permission denied

权限不对？？？试一下：

# chown postfix.postfix /var/lib/postfix/master.lock  
# service postfix restart; service postfix status

    * postfix is running

OK. 服务总算跑起来了。过了一会，再查看一下邮件：

# postqueue -p

天哪，还有一大堆邮件没有发出去呀。再查：

# tail /var/log/mail.log

    May  6 14:05:37 * postfix/tlsmgr[15956]: fatal: open database
    /var/lib/postfix/smtpd_scache.db: Permission denied
    May  6 14:05:38 * postfix/master[3264]: warning: process
    /usr/lib/postfix/tlsmgr pid 15956 exit status 1
    May  6 14:05:38 * postfix/master[3264]: warning: /usr/lib/postfix/tlsmgr: bad
    command startup — throttling
    May  6 14:06:38 * postfix/tlsmgr[16384]: fatal: open database
    /var/lib/postfix/smtpd_scache.db: Permission denied
    May  6 14:06:39 * postfix/master[3264]: warning: process
    /usr/lib/postfix/tlsmgr pid 16384 exit status 1
    May  6 14:06:39 * postfix/master[3264]: warning: /usr/lib/postfix/tlsmgr: bad
    command startup — throttling

还是权限不对。再改：

# chown postfix.postfix /var/lib/postfix/smtp*  
# service postfix restart  
# postqueue -f

过了几分钟再查：

# psotqueue -p

    Mail queue is empty

哈哈，整个世界都清静了。

后记，为什么同样的配置在 Ubuntu 9.10 下可以，到 Ubuntu 10.04
就不行了，新系统做了什么改动？有研究过的同学分享一下。

{ Thanks 逸飞. }
