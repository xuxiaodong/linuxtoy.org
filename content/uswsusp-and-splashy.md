Title: µswsusp & Splashy: 给 Linux 内核减负
Date: 2009-09-23 10:50
Author: toy
Category: Apps
Tags: Splashy, uswsusp
Slug: uswsusp-and-splashy

{ 撰文/run\_lisp }

9 月 21 日，托瓦尔兹说：“目前 Linux
内核体积很大，这确实是个问题。”µswsusp 和  
Splashy 是 Linux 内核减负的典型代表，两者利用 initramfs
机制，把以前内核实现的功能放入 user  

space，相信在不久的将来，会有更多内核里的功能跑到内核外面，使内核能够更为简洁。

下面介绍 µswsusp 的使用：

sudo dpkg-reconfigure uswsusp

然后按照提示配置，s2disk 挂起到硬盘，s2ram
挂起到内存，当内存不够大可能就不能运行。

Splashy 的使用见 。

**参考链接**

* [µswsusp](http://suspend.sourceforge.net)  
* [Splashy](http://splashy.alioth.debian.org)
