Title: Bash 及 Linux 命令行工具将现身 Win10 ？
Author: lovenemesis
Date: 2016-03-31
Category: News
Slug: bash-and-linux-command-tools-heading-to-win10
Tags: bash, win10
Summary: M$ 在最近的 Build2016 活动上宣布将为 Win10 带来 Bash 及一些 Linux 命令行工具。那么究竟如何呢？

根据 [Ars Technica](http://arstechnica.com/information-technology/2016/03/ubuntus-bash-and-linux-command-line-coming-to-windows-10/) 的报道，这次 M$ 与 Canonical 合作，将在 今年 Win10 周年庆补丁更新中包含 Bash 及部分 Linux 命令行工具移植到。

结合报道以及当下的信息，在下推测其实质为：

* 闭源实现了一部分 Linux 内核 API，以 `lxcore.sys`,`lxss.sys`，如同 WINE 之于 Win32 API
* 根据[现场演示截图](http://arstechnica.com/information-technology/2016/03/ubuntus-bash-and-linux-command-line-coming-to-windows-10/?comments=1&post=30919415#comment-30919415)来看文件系统结构基于砍掉的 Project Astoria 的，具备 Android 特征的 `acct` 及 `data` 目录。有趣的是 64bit 兼容库采用的是 `lib64` 的方式，并非 Debian 的传统风格
* 至于 Bash 和命令行工具，现在并没有看到超出 `coreutils` 范畴的应用，至于是否能用 `gcc` 及 `binutils`，不得而知。

这次是否会如同 NT 时代的 POSIX 兼容层一样成为鸡肋？今两年 M$ 对于非自家操作系统的态度变化颇大，究竟是画饼还是真爱，让我们拭目以待吧！

PS 心急的童鞋可以通过 [GNUWin 项目](http://gnuwin32.sourceforge.net/)体验下。
