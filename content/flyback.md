Title: FlyBack: 另一个 for Linux 的 Time Machine
Date: 2007-11-14 08:00
Author: toy
Category: Apps
Slug: flyback

类似 Apple 最新操作系统中所具有的 Time Machine
功能，我们先前已经介绍过一个
[TimeVault](http://linuxtoy.org/archives/timevault.html)，那么这是另外一个
[FlyBack](http://code.google.com/p/flyback/)，同样 for Linux。FlyBack
基于 rsync，提供简单的 GUI，能够执行 snapshot 式的备份。

[![FlyBack](http://i.linuxtoy.org/i/2007/11/flyback-thumb.png)](http://i.linuxtoy.org/i/2007/11/flyback.png)

FlyBack 目前版本为
0.3.3，可从[这里下载](http://code.google.com/p/flyback/downloads/list)。要运行
FlyBack，你需要先安装相关依赖：

Debian 用户可在终端运行：

`sudo apt-get install python python-glade2 python-gnome2 rsync`

Ubuntu 用户需运行：

`sudo apt-get install python python-glade2 python-gnome2 python-gconf rsync`

Redhat/Fedora 用户可运行：

`yum install pygtk2 gnome-python2-gconf pygtk2-libglade`

然后在解包后执行以下命令：

`python flyback.py`
