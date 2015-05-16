Title: 短消息：MariaDB 迁移
Date: 2013-03-26 10:18
Author: lovenemesis
Category: News
Tags: arch, Fedora, mariadb, MySQL, Slackware
Slug: briefing-mariadb-switch

又是一系列短消息，关于各大发行版向 MariaDB 的迁移进度。

由于 Oracle 对于 MySQL 的日趋封闭和缓慢的安全更新，继前段时间[刚刚发布的
openSUSE
12.3](http://linuxtoy.org/archives/opensuse-12-3-release.html)，各大发行版纷纷宣布将从
MySQL 迁至 MariaDB 。

**前卫的滚动发行版 Arch Linux 发出了迁移至 MariaDB 的通告**，并表示
MySQL 将在一个月之内从官方源移至 AUR
中。由于几个细微的兼容性问题，该迁移无法自动完成，需要使用者手动执行几条命令。[详细步骤及官方通告](https://www.archlinux.org/news/mariadb-replaces-mysql-in-repositories/)

**老牌发行版 Slackware Linux 的开发者也宣布将迁移至
MariaDB**，只是尚未给出具体时间表。待完成之后仓库中将不再包含
MySQL。Slackware
开发者表示他们相信[社区的投票的选择](http://www.linuxquestions.org/questions/slackware-14/replace-mysql-with-mariadb-in-slackware-4175447832/)以及
MariaDB
基金会的发展。[消息来源](http://www.h-online.com/open/news/item/Slackware-Linux-switches-to-MariaDB-1829261.html)

**Fedora Project 依然按部就班的计划在今年夏季的 Fedora 19 中换用
MariaDB**。现有 `mysql` 软件包将被全部重命名为 `MySQL`
（注意区分大小写），MariaDB 将成为依赖软件的默认选择。Fedora
并不打算支持同时安装 MySQL 和 MariaDB，必须两者择一。
[详细迁移原因及安排](https://fedoraproject.org/wiki/Features/ReplaceMySQLwithMariaDB)
