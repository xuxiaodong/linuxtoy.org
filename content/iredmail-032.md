Title: iRedMail 0.3.2 稳定版发布
Date: 2008-12-12 19:55
Author: toy
Category: News
Tags: iRedMail
Slug: iredmail-032

[iRedMail](http://linuxtoy.org/archives/iredmail.html) 0.3.2
稳定版发布了。0.3.2 主要是基于 0.3.1 做了一些 bug
修正，完善已有组件的功能，并更新了少量软件包。升级文档将会稍后放出，请已部署了
iRedMail 之前版本的用户耐心等待。

相对于 0.3.1 版本，本次发布的 0.3.2 版本主要的改进有：

-   增加了补丁用于让 ExtMail 可以自动创建用户的 maildir
    目录。现在可以考虑使用 MySQL+ExtMail+PostfixAdmin
    的组合，用以替代您之前的 MySQL+ExtMail+ExtMan 的组合。
-   修正了 MySQL/LDAP 的 root 用户密码无法使用特殊字符的问题。

0.3.2 beta1 测试版本发布时相对于 0.3.1
所做的改进和修正，可[参考这里](http://linuxtoy.org/archives/iredmail.html)。

[下载 iRedMail
0.3.2](http://code.google.com/p/iredmail/downloads/list)。

另外，裁减 CentOS 系统并整合 iRedMail 的 iRedOS 0.1.2 的 ISO
镜像也已就绪，可以从[这里下载](http://www.iredmail.org/iRedOS/)。
