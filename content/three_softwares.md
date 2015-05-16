Title: 介绍几个小软件：Boot-Up Manager、Baobab 和 GtkOrphan
Date: 2006-08-01 15:01
Author: toy
Category: Apps
Slug: three_softwares

这几个小软件皆由 [Fabio Marzocca](http://www.marzocca.net)
所开发，功能非常实用，现介绍给大家。

1.[Boot-Up Manager](http://www.marzocca.net/linux/bum.html)

该软件可以对服务、启动和关机脚本进行管理，图形化的操作使你能够非常轻易地启用或禁用服务及脚本。安装指令如下：

`sudo apt-get install bum`

2.[Baobab](http://www.marzocca.net/linux/baobab.html)

这个软件能够以图形化的形式表现磁盘所占用的空间，对于磁盘的管理来说相当具有帮助。可以如下指令安装：

`sudo apt-get install baobab`

3.[GtkOrphan](http://www.marzocca.net/linux/gtkorphan.html)

通过分析安装程序的状态，该软件可以找出那些仍旧存在于系统中的孤立的软件库。从某种意义上说，这相当于一个垃圾清理工具，因为你可以通过它来删除那些孤立的软件库。安装指令如下：

`sudo apt-get install gtkorphan`

执行下面的命令则可以运行它：

`gksu gtkorphan`
