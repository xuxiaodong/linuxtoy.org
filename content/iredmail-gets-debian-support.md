Title: iRedMail 开源邮件方案已支持 Debian (Lenny, 5.0.1)
Date: 2009-05-05 10:59
Author: toy
Category: News
Tags: Debian, iRedMail
Slug: iredmail-gets-debian-support

{撰文/Zhang Huangbin (michaelbibby AT gmail.com)}

经过近一周的测试和修正，iRedMail 已经可以顺利地运行在 Debian (Lenny)
5.0.1 版本的 amd64 平台了。i386 平台还未测试，预计是应该不会有什么问题。

有兴趣的朋友可以根据这篇安装指南进行安装和部署，我们需要大家的测试和反馈：

Install iRedMail on Debian (Lenny):

目前已经良好工作的组件有：

* Postfix-2.5.x，支持 TLS。  
* Dovecot-1.1.x，支持 IMAPS，POP3S。  
* Amavisd-new-2.6.x，支持 DKIM 签名和校验。  
* OpenLDAP-2.4.x  
* MySQL-5.0.x  
* Roundcube webmail (0.2.1，用户可自行修改 SQL/LDAP
密码，可设置假期自动回复)

还需要调试的组件有：

* Apache-2.2.x，SSL 未能正常工作。

缺少的软件包：

* Pysieved-1.0。已由 LiDaobing 帮忙完成打包，等待进入官方 apt 仓库。

暂定的 iRedMail 发布周期是：

* 2009.05.15: iRedMail-0.5.0-beta1，完全支持 Debian (Lenny,
5.0.1)，包括 i386 和 amd64 平台。  
* 2009.05.25: iRedMail-0.5.0-beta2，尝试移植到 Ubuntu Server 8.04
TLS，包括 i386 和 amd64 平台。  
* 2009.06.15: iRedMail-0.5.0-stable，正式发布 0.5.0-stable 版本。

请大家帮忙测试，将发现的所有问题都反馈到论坛，以便我们完善
iRedMail。感谢大家的支持和帮助。

{ via [iRedMail
论坛](http://www.iredmail.org/bbs/viewthread.php?tid=760) }
