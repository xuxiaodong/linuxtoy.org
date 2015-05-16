Title: Ttyutils: Linux 终端截获工具
Date: 2008-06-26 08:22
Author: toy
Category: Tools
Tags: Ttyutils
Slug: ttyutils

Ttyutils 是一套 UNIX 终端工具，包括 ttyexec、ttylook、ttyadmin
和一些扩展程序。

ttyexec
建立伪终端去执行一个命令，捕获命令所有的输出，传递这些输出数据到内置的内存终端仿真器和真实的终端。通过
ttyexec 执行的命令和直接执行的命令，用户感觉不到有任何的区别。

通过内存终端仿真器，管理员可以在特定的条件下触发事件，例如，用户希望依赖程序
A 的状态来启动另外程序 B，但是不想或者不能修改程序
A，这种情况下，ttyexec 是有用的。

ttyadmin 是一个管理工具，它使用 ncurses(3X) 窗口界面，查看和控制存在的
ttyexec 实例。

ttylook 类似于 BSD watch(1)
程序，但是没有太多的限制，它能够轻易的连接到存在的 ttyexec
实例，查看那个终端的输出，或者，如果打开了可写模式的话，还可以输入数据到那个终端。

扩展程序包括 ttyfeed、ttysnap 等等，它们都支持 --help 命令行选项。

Ttyutils 遵循 GPL 版本 2 授权协议发布，这意味着您在获得 Ttyutils
的同时有权力获得完整的源代码。

Ttyutils 的主要目标平台是 GNU/Linux，开发和测试平台为 Fedora
7。它应该也可以在其它 GNU/Linux 发布系统上运行，理论上可以在符合 UNIX 98
规范的操作系统上运行。当目前为止，下列的操作系统可以运行 Ttyutils：

-   Fedora
-   AIX 5

下载地址: <http://groups.google.com/group/xiaohu417>

[撰文/xiaohu417]
