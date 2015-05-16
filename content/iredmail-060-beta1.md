Title: 开源邮件服务解决方案 iRedMail-0.6.0-beta1 发布，支持 FreeBSD
Date: 2009-12-22 17:40
Author: toy
Category: Apps
Tags: iRedMail
Slug: iredmail-060-beta1

{ 撰文/[Zhang Huangbin](mailto:michaelbibby@gmail.com) }

开源邮件服务解决方案 iRedMail 项目组发布了 0.6.0-beta1 新版本。

以下是自 0.5.1 稳定版发布之后的主要更改：

+ 支持 FreeBSD 7.x 和 8.0，包括 i386 & x86\\\_64/amd64
架构。这里是[安装文档](http://code.google.com/p/iredmail/wiki/Installation\_on\_FreeBSD)。  
+ MySQL 方案现在支持 domain alias。可以通过新版本的 PostfixAdmin-2.3
进行管理。  
+ 软件更新。  
- Dovecot -> 1.1.20  
- PostfixAdmin -> 2.3。支持 domain alias 管理。  
- phpMyAdmin -> 2.11.9.6  
- Roundcube webmail ->
0.3.1。用户定制邮件过滤规则和修改密码的插件都已经包含在内，且是
roundcube 官方提供的。  
- ClamAV -> 0.95.3

下载地址：  
技术支持论坛：

*注意：这是一个测试版，不建议在生产环境中使用。*

{ Thanks Zhang Huangbin. }
