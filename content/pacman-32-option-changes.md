Title: Pacman 3.2 的命令选项变化
Date: 2008-08-04 10:53
Author: toy
Category: Apps
Tags: Archlinux, Package Manager, Pacman
Slug: pacman-32-option-changes

昨天在读 [Archlinux
Newsletter](http://www.archlinux.org/static/newsletters/newsletter-2008-Aug-04.html)
时知道了
[Pacman](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-5.html)
3.2 已开始测试，Archlinux 官方表示不久后会进入 Core 仓库。Pacman 3.2
相比之前的旧版本，在命令选项方面有诸多改变，有些选项移除了，也增加了一些新选项。使用
Archlinux 的朋友需要注意了。

从 Pacman 3.2 的更新记录来看，下列命令选项已经移除：

-   -A/--add 选项
-   -e/--dependsonly 选项
-   从 repo-add 中移除 --force 选项

而新增及改进的命令选项包括：

-   已添加 --asexplicit 选项
-   新增移除选项 --unneeded
-   添加 -Rss 用来移除所有依赖
-   使用 -Ss 和 -Qs 操作可以处理多个组
-   允许 -q/--quiet 选项使用 -o/--own 及 -g/--groups 选项
-   添加 --quiet 选项到 repo-add/repo-remove

至于某些选项的具体作用，可能需要阅读 manpage 才能了解。

Pacman 3.2
除了在命令选项方面有所改变外，还包括其他一些改动，如配置选项区分大小写、添加了
CleanMethod 以用于各种缓存清理、针对 pacman.conf 添加了 SyncFirst
选项、支持按版本号来安装依赖 (pacman -S
"dep>=2.0")、添加了 --enable-git-version 和 --disable-internal-download
配置标志，等等。同时，libalpm-specific 和 makepkg-specific
也有一些变动。详细信息可以通过[这里](http://projects.archlinux.org/?p=pacman.git;a=blob;f=NEWS)了解。
