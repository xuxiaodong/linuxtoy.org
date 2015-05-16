Title: GDB 7.5
Date: 2012-08-21 09:54
Author: lovenemesis
Category: Development
Tags: GDB
Slug: gdb-7-5

常用的除错诊断工具 GDB 发布 7.5，带来了 Go 语言支持。

新版本的功能有：

-   对 Google Go 语言支持。
-   支持 [x32 ABI](http://linuxtoy.org/archives/linux-kernel-3-4.html)
    和 microMIPS。
-   配合 SystemTap 实现 SDT(定位静态追溯)。
-   改善了 GDBserver 支持，支持通过 stdio 的连接。
-   在 ARM 平台上支持逆向除错诊断。
-   移除 `gdbtui` 二进制文件，转而使用 `gdb -tui`。

[发布公告](http://www.gnu.org/software/gdb/download/ANNOUNCEMENT)

[源代码包下载](http://www.gnu.org/software/gdb/download/)
