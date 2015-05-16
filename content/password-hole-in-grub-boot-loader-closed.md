Title: GRUB 引导加载程序的漏洞被修复
Date: 2009-11-11 14:04
Author: toy
Category: News
Tags: GRUB
Slug: password-hole-in-grub-boot-loader-closed

{ 编译/渔樵而居 }

新版的 GNU  
GRUB 引导加载程序 1.97.1 修补了之前的 1.97  
版本的漏洞，这个漏洞使密码可以简单的绕过密码验证。密码保护措施是 GRUB  

中用来防止未经许可的修改引导参数。程序错误的特征导致只要输入密码的第一个字符就接受密码有效。

GRUB 1.97，也被叫做 GRUB
2，其新的配置文件格式支持简单的用户授权。然而密码需要被存储为可读的可见文本。很多
Linux 发行版本现在已经开始推送 GRUB 2，包括 Debian “sid”和最近发布的
Ubuntu 9.10。

参见：

* [GRUB 2: password checking
oddity](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=555195), Debian
project bug report.  
* [Laptop passwords vulnerable to
attack](http://www.h-online.com/news/item/Laptop-boot-passwords-vulnerable-to-attack-737053.html),
a report from The H.

{ via [The
H](http://www.h-online.com/open/news/item/Password-hole-in-GRUB-boot-loader-closed-855181.html)
}
