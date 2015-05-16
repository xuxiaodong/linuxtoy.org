Title: WineHQ 数据库泄漏
Date: 2011-10-12 10:53
Author: lovenemesis
Category: News
Tags: Wine
Slug: winehq-database-comprised

运行于 *Nix 之上的开源跨平台 Win32 API 兼容层 WineHQ 的 AppDB 和
Bugzilla 数据库被黑客攻击。

CodeWeavers CEO Jeremy 在信中提到黑客利用某种方式获取了 WineHQ 的 AppDB
和 Bugzilla 的访问，并且下载了完整数据库文件。

-   其他位于 WineHQ 的数据库没有收到攻击的痕迹。
-   尽管用户密码已经加密，但是依据密码强度，黑客依然有可能获得密码信息。[参考文献](http://asiknews.wordpress.com/2011/03/02/best-practice-password-management-for-internet-web-sites/)
-   目前不清楚是由于某个有外部访问权限的账户失窃，还是由于某个未知的
    phpMyAdmin 的安全漏洞。

这已经是近期来继 Kernel.org 和 Linux.com
之后针对开源项目的又一次黑客行为，再度**提醒提高 Linux
系统安全性的认识，尤其是在涉及外部人员领域**。

[原始信件](http://www.winehq.org/pipermail/wine-users/2011-October/097753.html)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=OTk5NQ)
