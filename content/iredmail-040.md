Title: 开源邮件服务解决方案 iRedMail-0.4.0 稳定版发布
Date: 2009-03-11 13:07
Author: toy
Category: News
Tags: iRedMail
Slug: iredmail-040

[撰文/Zhang Huangbin (michaelbibby AT gmail.com)]

经过近 4 个月的完善，iRedMail-0.4.0 稳定版发布了。iRedOS 将会在 CentOS
5.3 发布之后推出，请大家耐心等待。

iRedMail 是针对 Red Hat(R) Enterprise Linux 和 CentOS
设计的邮件服务解决方案，是在操作系统安装好后使用的一套 shell
脚本，用于快速部署一套功能完善的邮件服务器解决方案。

- 基于 GPL v2 版权发布。  
- 目前支持的操作系统：Red Hat(R) Enterprise Linux, CentOS。  
- 支持的操作系统版本：5.0, 5.1, 5.2, 5.3

* 项目首页：  
[http://www.iredmail.org/](%20http://www.iredmail.org/)

* 下载地址：  

[http://code.google.com/p/iredmail/downloads/list](%20http://code.google.com/p/iredmail/downloads/list)

* 安装指南：  

[http://www.iredmail.org/wiki/index.php?title=IRedMail\_Installation\_Guide](%20http://www.iredmail.org/wiki/index.php?title=IRedMail_Installation_Guide)

* 如果您在安装和使用的过程中碰到问题，可以到论坛发贴讨论：  

[http://www.iredmail.org/bbs/index.php](%20http://www.iredmail.org/bbs/index.php)

* 如果您已经在使用
iRedMail/iRedOS，希望您能帮助我们，以支持项目的继续发展和长期存在：  

[http://www.iredmail.org/wiki/index.php?title=Help\_US](%20http://www.iredmail.org/wiki/index.php?title=Help_US)

后续的开发工作将集中在 bug
修正，细节的改进，以及管理后台的开发。非常欢迎您将自己的需求、改进建议发布在项目的论坛上：  

[http://www.iredmail.org/bbs/index.php](%20http://www.iredmail.org/bbs/index.php)

以下是自 0.3.2 版本以来的主要更新，更详细的更新信息请查看 ChangeLog
文件：  

[http://iredmail.googlecode.com/svn/trunk/iRedMail/ChangeLog](%20http://iredmail.googlecode.com/svn/trunk/iRedMail/ChangeLog)

* 所有核心组件都升级到最新稳定版：

- Postfix-2.5.6  
- Dovecot-1.1.11, dovecot-sieve-1.1.6  
- Amavisd-new-2.6.2  
- Roundcube-0.2-stable  
- awstats-6.9  
- phpLDAPadmin-1.1.0.6  
- rrdtool-1.2.30

* 本次发布移除了以下组件：

- ExtMail  
具体原因请参考论坛帖子：iRedMail 项目组为何决定去掉 ExtMail？  
<http://www.iredmail.org/bbs/viewthread.php?tid=590&extra=page%3D1>  
已部署了 ExtMail 的用户，我们会为您迁移到 Roundcube
提供全面的技术支持。

- Mailgraph  
原因：统计失效，形同鸡肋。但不排除后续版本对它做增强，并再次加入。

* 新功能和主要的改进：

- [安装程序] 在安装过程会提示您选择 webmail 程序的默认语言。  
- [增强] 极大地扩展了 LDAP schema。  
注意：如果您使用 0.3.2 版本部署基于 LDAP 的方案，此次升级需要修改 LDIF
结构。具体请参考稍后发布的升级指南。  
- [增强] 所有基于 web 的管理程序默认都只能通过 https
访问，增强安全性。例如
PostfixAdmin，phpMyAdmin，phpLDAPadmin，Awstats。  
- [增强] 在 Apache 中添加 容器用于禁止 webmail 程序目录的自动索引。感谢
muniao@gmail 的反馈和建议。  
- [增强] 增加了 HELO 检测规则，使反垃圾效果得到至少 10% 的提升。  
- [增强] 将 Postfix 队列重新投递时间改为 '300s'。  
- [增强] 将 Postfix maximal\_queue\_lifetime 和 bounce\_queue\_lifetime
参数设置为 '1d'。感谢 muniao@gmail 的反馈和建议。  
- [增强] Awstats 现在直接使用 LDAP/MySQL 里的管理员账号来做用户验证。  
- [增强] OpenLDAP 默认使用 SSHA 加密机制。  
- [新] 为 Roundcube 增加插件，用户现在可以自定义邮件过滤规则。  
- [新] 为 Roundcube 增加插件，用户现在可以自行修改密码。  
注：可以修改 MySQL 和 LDAP 的密码。感谢 jungleji@gmail 帮忙制作修改
LDAP 密码的插件。  
- [新] 增加几个脚本做为系统管理员的辅助工具：  
+ tools/create\_mail\_user\_OpenLDAP.sh：用于创建 LDAP 用户  
+ tools/create\_mail\_user\_MySQL.sh：用于创建 MySQL 用户  
+ tools/backup\_iRedMail.sh：用于备份整个邮件系统  
+ tools/get\_helo\_count.sh：统计 HELO 标识出现的次数
