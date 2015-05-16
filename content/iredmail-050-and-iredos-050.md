Title: iRedMail-0.5.0 & iRedOS-0.5.0 稳定版正式发布
Date: 2009-08-17 16:05
Author: toy
Category: News
Slug: iredmail-050-and-iredos-050

经过几个月的增强和修正，iRedMail-0.5.0 和 iRedOS-0.5.0
稳定版正式发布了。

- 下载 iRedMail：  
- 下载 iRedOS（CentOS-5.3-based）：

现在 iRedMail 支持以下发行版和对应的版本号：

- Red Hat Enterprise Linux 5.x  
- CentOS 5.x  
- Debian 5.x (Lenny)  
- Ubuntu 8.04 (Hardy)  
- Ubuntu 9.04 (Jaunty)

我们也为需要从 0.4.0 升级到 0.5.0 的用户准备好了升级指南：

-

开源版的管理后台也已经公开代码仓库，具体信息请大家参考论坛帖子：

-

目前这个版本的功能已经相当完善了，因此我们决定将它作为一个长期支持的版本，  
后期的工作主要是修正发现的
bug，升级相关的软件包，以及增加对其它发行版的支持，  
邮件方面的功能不会有太多大的改进和变化，大家尽管放心使用吧。

另外，iRedMail
开源项目希望得到大家的捐赠，以使这个项目能够继续存在下去，以及  
为大家提供及时的技术支持和其它服务。捐赠途径主要有：

- PayPal: michaelbibby@gmail.com （只接受人民币）  
- 淘宝：michaelbibby@gmail.com （只接受人民币）

需要直接银行转帐的朋友麻烦您以邮件联系我：michaelbibby@gmail.com。

以下是从 0.4.0 以来的更新记录：

*) 已知问题：  
- Ubuntu 9.04 系统上，使用 MySQL 方案时，Awstats 无法通过 https 访问。  
这似乎是 libapache2-mod-auth-mysql 的 bug 导致的，请大家耐心等待
Ubuntu  
发布升级包。

*) 新功能和功能增强：

-
支持为外发的邮件增加“免责声明”（disclaimer），而且可以针对单独的用户和单独的域进行配置。  
- 对用户的 maildir 路径做了 hash
处理，以减少文件系统索引方面的性能消耗：  
+ 旧的格式：domain.ltd/username/  
+ 新的格式：domain.ltd/u/us/use/username-2009.08.15.11.34.06/

- 更灵活的 maildir
路径控制，更易于修改用户邮箱的路径，更利于大量用户的情况和大规模部署。  
详情可以访问英文论坛的帖子：

- 新增了 python
脚本用于批量导入用户：tools/create\_mail\_user\_OpenLDAP.py

- OpenLDAP 方案相关的改进：  
+ 警告：'domainStatus' 属性已经废弃，请大家使用 'accountStatus'
属性来代替。  
具体修改方法在升级指南中有说明。  
+ 重新设计了邮件列表的实现方式。  
详情可以访问英文论坛的帖子：  
+ 支持 mail alias。  
+ 默认会创建 'all@domain.ltd'
邮件组，但不允许接收邮件。所有用户都是这个列表的成员。  
+ 启用了邮件地址簿控制。现在你可以通过设置
enabledService=displayedInGlobalAddressBook  
属性来控制邮件用户、列表、alias
的邮件地址是否出现在客户端的全局地址簿里。  
+ 支持针对单个用户和单个域的 sender bcc, recipient bcc 控制。  
* enabledService=senderbcc  
* enabledService=recipientbcc  
+ 支持针对单个用户的邮件转发控制：  
* enabledService=forward  
+ 支持针对单个用户的 managesieve
服务（用于提供给客户端自己定义邮件过滤规则）控制：  
* enabledService=managesieve  
+ 添加了其它一些有需要的 LDAP 属性，例如用于保存用户通过 POP3/IMAP
最后访问的时间、  
IP 地址和访问协议，等。

- MySQL 方案相关的改进：  
+ 在 vmail.mailbox 表中增加了多个字段：employeeid, lastlogindate,  
lastloginipv4, lastloginprotocol。

- Roundcube webmail 相关的改进：  
+ 升级到了 0.2.1-stable，相关的补丁和插件也都已经同步。  
+ 改进了全局 LDAP
地址簿。所有用户都只能搜索与自己同一个域内的用户，包括普通  
邮件用户、邮件列表和
alias。当然，你可以通过上面介绍的地址簿控制功能，控制  
这些地址是否显示在客户端的全局地址簿里。

- Postfix 相关的改进：  
+ 启用了针对单个用户的 transport map 支持。  
+ 增加了 relay\\\_domains 和 relay\\\_recipient\_maps 参数，提供对
backup  
mx 的支持。  
+ 移除了多余的 LDAP 查询。

- Dovecot 相关的改进：  
+ 默认启用了邮箱容量告警的功能。当用户邮箱使用量达到 85%, 90%, 95%
时，dovecot  
会自动发送一封邮件通知用户及时清理邮箱。

- Apache 相关的改进：  
+ 在文档的根目录增加了 robots.txt 文件以避免搜索引擎搜索某些目录。

- 软件包更新：  
+ Dovecot-1.1.18  
+ ClamAV-0.95.2  
+ Awstats-6.9  
+ SquirrelMail-1.4.19  
+ Mail-DKIM-0.36. 感谢 lidaobing@gmail 为 Debian 和 Ubuntu 8.04
提供二进制打包。  
+ phpLDAPadmin-1.1.0.7  
+ phpMyAdmin-2.11.9.5

{ Thanks Zhang Huangbin. }
