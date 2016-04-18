Title: Redox：使用 Rust 编写的类 Unix 系统
Date: 2016-04-18 13:06:32
Authors: toy
Category: Distros
Tags: unix, os, redox, rust
Slug: redox

Redox 是采用 Rust 编程语言而开发的一套类 Unix 操作系统，其主要特点是微内核（Microkernel）设计、具有图形化的用户界面 Orbital、以及驱动程序在用户空间执行等。

<!-- PELICAN_END_SUMMARY -->

[![redox]({filename}/images/redox.thumb.png)]({filename}/images/redox.png)

*截图来自 Redox 官网*

Redox 包含常见的 Unix 命令，为 C 程序提供了 Newlib 库，提供 ZFS 文件系统支持（目前仍在开发中）。除此之外，Redox 还有 shell 程序 Ion、包管理器 Magnet、以及类似 vi 的文本编辑器 Sodium 等应用。

如果你对 Redox 感兴趣，那么不妨参考官方的文档来[编译安装 Redox][c]。

&rarr; [Redox](http://www.redox-os.org/)

[c]: https://doc.redox-os.org/book/getting_started/preparing_the_build.html
