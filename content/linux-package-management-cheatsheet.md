Title: Linux 包管理速查表
Date: 2008-09-22 18:48
Author: toy
Category: Tips
Tags: Cheat Sheet
Slug: linux-package-management-cheatsheet

使用 Linux 系统总是免不了要接触包管理工具。比如，Debian/Ubuntu 的
apt、openSUSE 的 zypp、Fedora 的 yum、Mandriva 的 urpmi、Slackware 的
slackpkg、Archlinux 的 pacman、Gentoo 的 emerge、Foresight 的
conary、Pardus 的 pisi，等等。DistroWatch
针对上述包管理器的主要用法进行了总结，对各位 Linux
用户来说具有很好的参考作用。这个总结还是有一点不足，有空给大家整理一个更全面的版本。

任务

apt  
Debian, Ubuntu

zypp  
openSUSE

yum  
Fedora, CentOS

安装包

apt-get install <pkg>

zypper install <pkg>

yum install <pkg>

移除包

apt-get remove <pkg>

zypper remove <pkg>

yum erase <pkg>

更新包列表

apt-get update

zypper refresh

yum check-update

更新系统

apt-get upgrade

zypper update

yum update

列出源

cat /etc/apt/sources.list

zypper repos

yum repolist

添加源

(edit /etc/apt/sources.list)

zypper addrepo <path> <name>

(add <repo> to /etc/yum.repos.d/)

移除源

(edit /etc/apt/sources.list)

zypper removerepo <name>

(remove <repo> from /etc/yum.repos.d/)

搜索包

apt-cache search <pkg>

zypper search <pkg>

yum search <pkg>

列出已安装的包

dpkg -l

rpm -qa

rpm -qa

任务

urpmi  
Mandriva

slackpkg  
Slackware

pacman  
Arch

安装包

urpmi <pkg>

slackpkg install <pkg>

pacman -S <pkg>

移除包

urpme <pkg>

slackpkg remove <pkg>

pacman -R <pkg>

更新包列表

urpmi.update -a

slackpkg update

pacman -Sy

更新系统

urpmi --auto-select

slackpkg upgrade-all

pacman -Su

列出源

urpmq --list-media

cat /etc/slackpkg/mirrors

cat /etc/pacman.conf

添加源

urpmi.addmedia <name> <path>

(edit /etc/slackpkg/mirrors)

(edit /etc/pacman.conf)

移除源

urpmi.removemedia <media>

(edit /etc/slackpkg/mirrors)

(edit /etc/pacman.conf)

搜索包

urpmf <pkg>

--

pacman -Qs <pkg>

列出已安装的包

rpm -qa

ls /var/log/packages/

pacman -Qii

任务

conary  
rPath, Foresight

pisi  
Pardus

emerge  
Gentoo

安装包

conary update <pkg>

pisi install <pkg>

emerge <pkg>

移除包

conary erase <pkg>

pisi remove <pkg>

emerge -C <pkg>

更新包列表

 

pisi update-repo

emerge --sync | layman -S [for added repositories]

更新系统

conary updateall

pisi upgrade

emerge -NuDa world

列出源

 

pisi list-repo

layman -L

添加源

 

pisi add-repo <name> <path>

layman -a

移除源

 

pisi remove-repo <name>

layman -d

搜索包

conary query <pkg>

pisi search <pkg>

emerge --search

列出已安装的包

conary query

pisi list-installed

cat /var/lib/portage | more

**参考**

-   [Apt 使用参考](http://linuxtoy.org/archives/apt_reference.html)
-   [Dpkg
    常用指令操作快速参考](http://linuxtoy.org/archives/dpkg_reference.html)
-   [Pacman ── Arch Linux
    的包管理工具](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-5.html)

[via [DistroWatch](http://distrowatch.com/weekly.php?issue=20080922)]
