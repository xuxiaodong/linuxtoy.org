Title: Grsync：rsync 的图形化界面
Date: 2007-07-26 15:30
Author: toy
Category: Apps
Slug: grsync

rsync 是一个命令行界面的目录同步备份工具。Grsync
为其提供图形化的用户界面，方便用户使用。当前，Grsync
的主要功能包括：具有常用的 rsync 选项，可以保存多个配置，在 rsync
执行前后能够运行自定义的命令，可用于 Shell 脚本和
crontab，支持导入/导出配置等。

[![Grsync](http://i.linuxtoy.org/i/2007/07/grsync_s.jpg)](http://i.linuxtoy.org/i/2007/07/grsync.jpg)

**安装 Grsync**

你能[从 Grsync 的主页获取 0.6
版本的源代码](http://www.opbyte.it/grsync/)，然后使用如下命令编译安装：

` ./configure make sudo make install`

**其他替代品**

除了 Grsync 之外，还有一些其他的 rsync 前端程序，你可以参考：

-   [QSync](http://transamrit.net/projects/qsync/)：使用 Qt 所写的 rsync
    GUI。
-   [Zynk](http://hanez.org/zynk.html)：适用于 GNOME 桌面的 rsync GUI。

