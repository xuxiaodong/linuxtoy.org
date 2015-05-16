Title: 估计你知道的命令
Date: 2010-08-24 06:52
Author: lovenemesis
Category: Cli
Slug: the-command-you-might-know

如果你刚刚接触 Linux 的话，或许你知道这些命令。如果你不知道的话……

**NetworkManager 命令行版: nmcli**

*举例：*

查看当前区域内的无线网络: `nmcli dev wifi`

启动网络名为 Fedora 的链接：`nmcli con up id Fedora`

**PackageKit 命令行版: pkcon**

*举例：*

查询软件包描述信息中包含 quake
关键词的软件包：`pkcon search group quake`

显示软件仓库操作记录：`pkcon get-transactions`

查询远程软件包 warzone2100 中所包含的文件：`pkcon get-files warzone2100`

**[systemd
进程管理](http://0pointer.de/blog/projects/systemd-for-admins-1)：systemctl**

*举例：*

显示系统所有服务的运行状态：`systemctl`

显示 ntpd 服务的详细信息：`systemctl status ntpd.service`

欢迎各位朋友补充这些**新生代命令行工具**的简要信息～
