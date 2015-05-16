Title: memtop
Date: 2012-08-14 16:42
Author: lovenemesis
Category: Tools
Slug: memtop

memtop 是为长期运行而设计的终端 Python 脚本，方便了解内存使用情况。

与 htop 等工具不同，memtop
**只关心进程的私有的可写内存(及交换分区)使用**，也就代表在进程结束时会被释放的那一部分；它完全忽略私有不可写内存和共享内存。

于是它特别适用于查找 Linux 系统下最吃内存或者发生内存泄漏的进程。

此外它和可以通过[脚本](http://code.google.com/p/memtop/downloads/detail?name=memtop-graph.sh&can=2&q=)唤起
gnuplot 生成内存使用统计图：

[![](http://linuxtoy.org/img/2012/08/out.png "out")](http://linuxtoy.org/img/2012/08/out.png)

**注意：**若是需要了解系统当前的所有进程的内存占用情况，需以 `root`
身份运行该脚本。

[1.0.0
稳定版本（无需安装，直接运行）](http://code.google.com/p/memtop/downloads/detail?name=memtop-1.0.0.py)

[项目 Google Code 首页](http://code.google.com/p/memtop/)
