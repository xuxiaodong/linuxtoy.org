Title: [更新]Linux 桌面爆出入侵漏洞
Date: 2012-01-20 11:47
Author: gmsh
Category: News
Tags: Security
Slug: xorg-attack

Linux 桌面最近爆出安全漏洞，就是黑客 Xorg 1.11
版本下，在屏保密码锁界面，直接按下 Ctrl + Alt + * (*
是键盘数字区的 *)可以直接绕过密码， 进入桌面。

各位可以使用 X -version 命令查询自己的 X 版本，1.11
版本就有可能中招，在安全更新未到达前，可以使用这个[临时办法](http://www.reddit.com/r/linux/comments/onehx/every_linux_screen_locker_broken_by_a_keypress/)，同时提防身边能“物理接触”到你键盘的
Linux 黑客。

[来源1](http://www.phoronix.com/scan.php?page=news_item&px=MTA0NTU)

[来源2](http://www.webupd8.org/2012/01/xorg-111-vulnerability-allows-attackers.html)

[邮件列表](https://lists.ubuntu.com/archives/ubuntu-devel/2012-January/034652.html)

**Update**: 受影响的有 Fedora 16, Arch Linux, Fuduntu, Debian unstable
等等，不论你运行什么桌面环境, 只要是没有打补丁的 1.11 版
Xorg，统统有可能中招。

**fedora 16
已经[释出](https://admin.fedoraproject.org/updates/F16/FEDORA-2012-0712)更新档了**

[![](http://linuxtoy.org/img/2012/01/snapshot2.png)](http://linuxtoy.org/img/2012/01/snapshot2.png)
