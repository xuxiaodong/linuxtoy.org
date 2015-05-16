Title: 开源邮件服务解决方案──iRedMail
Date: 2008-11-27 11:12
Author: toy
Category: Apps
Tags: iRedMail
Slug: iredmail

[作者/Zhang Huangbin]

iRedMail，中文名为"艾瑞得邮件"，由 rhms 项目更名而来。是针对 Red Hat(R)
Enterprise Linux 和 CentOS
设计的邮件服务器解决方案，是在操作系统安装好后使用的一套 shell
脚本，用于快速部署一套功能完善的邮件服务器解决方案。

最新发布的 iRedMail 0.3.2-beta1 主要是基于 0.3.1 做了一些 bug
修正，完善已有组件的功能，并更新了少量软件包。

主要的改进有：

* Roundcube WebMail 现在已经搭配基于 LDAP
的方案，但用户自行修改密码和设置转发的功能暂时无法使用。设置假期自动回复的功能仍可正常使用。并且自动使用
OpenLDAP 做为全局地址簿。  
* 从基于 LDAP 的方案中移除 postgrey，统一使用 Policyd v1
提供灰名单（greylist）服务。  
注意：以上两个更改使得 MySQL 成为基于 LDAP
的方案中的一个必不可少的组件。  
* 在 Horde WebMail 里，用户可以自定义邮件过滤规则，如果使用 OpenLDAP
存储邮件账号，则会默认使用 OpenLDAP 作为全局地址簿。  
* 改进对已有 AMP (Apache, MySQL, PHP) 环境的支持。  
* 默认为 MySQL 启用 SSL 支持。  
* 默认使用 unix socket 方式连接 MySQL 数据库，性能更好一些。  
* 首次引入 php-eaccelerator -- PHP 加速器。  
* 首次引入 Awstats-6.8 作为 web 和 mail 日志分析工具。  
* 增加补丁用于修正 PostfixAdmin
登录页面的安全隐患。参考链接：https://sourceforge.net/mailarchive/forum.php?thread\_name=49057E07.30...  
* 在 logrotate 中默认使用 bzip2
对日志文件进行压缩，以得到更大的压缩比，为您节省一些磁盘空间。  
* 修正 ExtMail 默认附件大小。感谢 tongds@gmail 的反馈。  
* 在 Dovecot 中集成对磁盘容量告警、删除过期邮件的支持。但默认禁用。  
注：用于邮箱容量告警的脚本需要自己编写，也可以从 iredmailsupport@
邮件列表的文件下载区获得模板。  
* 增强 mailgraph，现在可以正确统计 greylist 信息了。  
* 软件包更新：  
- ClamAV => 0.94.1。感谢 chenwei1973@gmail 的提醒。  
- php-rrdtool, rrdtool => 1.2.28  
- phpMyAdmin => 2.11.9.3  
* 移除了几个工具脚本：  
- tools/backup\_mysql\_db.sh：MySQL 数据库备份脚本  
- tools/convert\_winmail\_mailbox.sh：迁移 WinMail 用户邮箱的脚本  
- tools/create\_mail\_user\_ldap.sh：批量创建 LDAP 用户的脚本  
- tools/create\_mail\_user\_mysql.sh：批量创建 MySQL 用户的脚本  
- tools/get\_helo\_count.sh：统计 HELO 标识的脚本  
- tools/migrate\_extmail\_mailbox.sh：迁移 ExtMail 用户的脚本  
- tools/sysreport.sh：获取系统报告的脚本

项目主页：<http://iredmail.googlecode.com>  
下载地址：<http://code.google.com/p/iredmail/downloads/list>
