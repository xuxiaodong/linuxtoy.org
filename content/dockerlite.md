Title: dockerlite: 轻量级 Linux 虚拟化
Date: 2013-07-08 09:36
Author: lovenemesis
Category: Virtual Machine
Tags: Btrfs, docker
Slug: dockerlite

dockerlite 是使用脚本编写，利用了 LXC 和 BTRFS 的轻量级 Linux
虚拟化实现，这不是虚拟机哦～

和传统的虚拟机实现不同，dockerlite 利用
[LXC](https://en.wikipedia.org/wiki/LXC)（Linux
容器）实现运行时资源隔离，并利用 [Btrfs
文件系统](https://en.wikipedia.org/wiki/Btrfs)的快照功能完成状态保持和虚拟环境克隆。

所谓轻量级虚拟化，也指代操作系统级别的虚拟化，通过内核和用户态进程组的支持，实现的独立网络
IP、进程树等类似虚拟机的隔离运行环境，但是和宿主机运行同样的内核。

dockerlite 和另一款用 Go 语言实现的
[docker](https://github.com/dotcloud/docker)的区别有：

-   dockerlite 使用 Shell 脚本实现，而 docker 用 Go。
-   dockerlite 使用 BTRFS 文件系统，而 docker 使用 AUFS。
-   docker 以后台进程方式运行并通过命令行客户端实现操作交互，dockerlite
    则无法以后台进程运行。

更多说明及源代码下载请前往[官方 Github
主页](https://github.com/dotcloud/dockerlite)

[消息来源](http://weibo.com/2042892135/zENNC0CuO)
