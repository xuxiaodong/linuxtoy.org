Title: 开源邮件服务解决方案 iRedMail-0.5.0-RC2 发布
Date: 2009-07-06 16:23
Author: toy
Category: News
Tags: iRedMail
Slug: iredmail-050-rc2-released

{撰文/Zhang Huangbin (michaelbibby AT gmail.com)}

开源邮件服务解决方案 iRedMail-0.5.0-RC2 发布了。

详细的修改记录：

* 改进对 Debian 5.x，Ubuntu 8.04, 9.04 的支持。  
* 支持为外发的邮件增加“免责声明”（disclaimer）内容。  
* 重新设计的内建邮件列表支持（仅 LDAP 方案可用）。  
* 在 Postfix 中增加了对 backup mx 的支持。  
* 增强了 Roundcube webmail 中的 LDAP
全局地址簿，用户只能搜索到和自己在同一个域内的邮件地址。  
* 修正了 Dovecot 对 mysql 后端的错误参数设置。  
* 更新软件包：clamav -> 0.95.2, awstats -> 6.9-2, dovecot ->
1.1.16.  
* 增加了更多的 LDAP 属性。  
* 修正在精简的 RHEL/CentOS 上安装时由于缺少 cron
软件包而导致的安装错误。  
* 在 Debian & Ubuntu 平台默认开启反垃圾和防病毒设置。感谢论坛的
Falador 反馈和测试。  
* 增加工作用于发送邮箱容量报警：tools/dovecot-quota-warning.sh.  
* 更新 Mail-DKIM 至 0.36 版本。感谢 lidaobing@gmail 为 Ubuntu 和
Debian 平台的打包。  
* 改进 tools/create\_mail\_user\_OpenLDAP.sh，创建的邮件帐号同时可作为
PureFTPd 帐号。  
* 改进的 Maildir
路径设计。加快内核在文件系统层面对文件的索引，在磁盘空间即将满了的情况下可以方便地增加存储和新增用户。  
* 所有 LDAP 用户都将默认被归到 all@domain.ltd 组。  
* 支持控制用户帐号是否显示在 LDAP 全局地址簿中。

下载地址：

相关讨论请前往官方论坛：
