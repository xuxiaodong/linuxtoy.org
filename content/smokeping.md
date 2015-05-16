Title: Smokeping：网络延迟监视工具
Date: 2008-08-27 08:02
Author: hmy
Category: Apps
Tags: Smokeping
Slug: smokeping

[撰文/hmy]

Smokeping 主要是监视网络性能，包括常规的 ping，用 echoping 监视 www
服务器性能，监视 dns 查询性能，监视 ssh 性能等。底层也是 rrdtool
做支持，特点是画的图非常漂亮，网络丢包和延迟用颜色和阴影来表示。

[![Smokeping](http://i.linuxtoy.org/i/2008/08/smokeping-thumb.png)](http://i.linuxtoy.org/i/2008/08/smokeping.png)  
*（点击可放大）*

最新版本的 Smokeping 支持多个节点的检测结果从一个图上画出来。比如从 A、B
两个监视点检测 C 点的 ping 效果。可以把 A、B
的检测结果在一个图上表示出来，便于比较。

下面是官方提供的例子：

<http://oss.oetiker.ch/smokeping-demo/?target=multi>

另外一个小功能就是提供一个 ajax 的 traceroute 界面，挺实用。traceroute
的 demo：

<http://oss.oetiker.ch/smokeping-demo/tr.html#www.switch.ch>
