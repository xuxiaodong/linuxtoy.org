Title: Linux 包管理速查表
Date: 2008-09-22 18:48
Author: toy
Category: Tips
Tags: Cheat Sheet
Slug: linux-package-management-cheatsheet

使用 Linux 系统总是免不了要接触包管理工具。比如，Debian/Ubuntu 的 apt、openSUSE 的 zypp、Fedora 的 yum、Mandriva 的 urpmi、Slackware 的 slackpkg、Archlinux 的 pacman、Gentoo 的 emerge、Foresight 的 conary、Pardus 的 pisi，等等。DistroWatch 针对上述包管理器的主要用法进行了总结，对各位 Linux 用户来说具有很好的参考作用。这个总结还是有一点不足，有空给大家整理一个更全面的版本。

<!-- PELICAN_END_SUMMARY -->

任务 | 安装包 | 移除包 | 更新包列表 | 更新系统 | 列出源 | 添加源 | 移除源 | 搜索包 | 列出已安装的包
---- | ------ | ------ | ---------- | -------- | ------ | ------ | ------ | ------ | --------------

apt (Debian/Ubuntu) | apt-get install `<pkg>` | apt-get remove `<pkg>` | apt-get update | apt-get upgrade | cat /etc/apt/sources.list | (edit /etc/apt/sources.list) | (edit /etc/apt/sources.list) | apt-cache search `<pkg>` | dpkg -l

zypp (openSUSE) | zypper install `<pkg>` | zypper remove `<pkg>` | zypper refresh | zypper update | zypper repos | zypper addrepo `<path>` `<name>` | zypper removerepo `<name>` | zypper search `<pkg>` | rpm -qa

yum (Fedora/CentOS) | yum install `<pkg>` | yum erase `<pkg>` | yum check-update | yum update | yum repolist | (add `<repo>` to /etc/yum.repos.d/) | (remove `<repo>` from /etc/yum.repos.d/) | yum search `<pkg>` | rpm -qa
任务

urpmi (Mandriva) | urpmi `<pkg>` | urpme `<pkg>` | urpmi.update -a | urpmi --auto-select | urpmq --list-media | urpmi.addmedia `<name>` `<path>` | urpmi.removemedia `<media>` | urpmf `<pkg>` | rpm -qa

slackpkg (Slackware) | slackpkg install `<pkg>` | slackpkg remove `<pkg>` | slackpkg update | slackpkg upgrade-all | cat /etc/slackpkg/mirrors | (edit /etc/slackpkg/mirrors) | (edit /etc/slackpkg/mirrors) | -- | ls /var/log/packages/

pacman (Arch) | pacman -S `<pkg>` | pacman -R `<pkg>` | pacman -Sy | pacman -Su | cat /etc/pacman.conf | (edit /etc/pacman.conf) | (edit /etc/pacman.conf) | pacman -Qs `<pkg>` | pacman -Qii

conary (rPath/Foresight) | conary update `<pkg>` | conary erase `<pkg>` | conary updateall | -- | -- | -- | conary query `<pkg>` | conary query

pisi (Pardus) | pisi install `<pkg>` | pisi remove `<pkg>` | pisi update-repo | pisi upgrade | pisi list-repo | pisi add-repo `<name>` `<path>` | pisi remove-repo `<name>` | pisi search `<pkg>` | pisi list-installed

emerge (Gentoo) | emerge `<pkg>` | emerge -C `<pkg>` | emerge --sync (layman -S [for added repositories]) | emerge -NuDa world | layman -L | layman -a | layman -d | emerge --search | `cat /var/lib/portage | more`

**参考**

-   [Apt 使用参考](http://linuxtoy.org/archives/apt_reference.html)
-   [Dpkg 常用指令操作快速参考](http://linuxtoy.org/archives/dpkg_reference.html)
-   [Pacman ── Arch Linux 的包管理工具](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-5.html)

[via [DistroWatch](http://distrowatch.com/weekly.php?issue=20080922)]
