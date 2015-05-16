Title: 关于 Fedora 13 最近“没有更新”的修复
Date: 2010-07-31 18:39
Author: lovenemesis
Category: Tips
Tags: Fedora
Slug: fix-no-updates-error-for-fedora-13

如果您是 Fedora 13
的用户但是已经有很长时间没有得到安全更新的提示，很抱歉，是由于上一次
PackageKit-gnome 的更新出问题了……

**修复方法：**

在终端输入以下命令：

`su -c ’yum -y --skip-broken update‘`

如果您一直使用 yum
手动更新的话，那么对应的修复已经正确升级了，不受到此影响。

[英文原公告](http://forums.fedoraforum.org/showthread.php?t=249386)
