Title: xdmx：分布式多头 X 服务器
Date: 2008-08-17 18:01
Author: hmy
Category: Apps
Slug: xdmx

[撰文/hmy]

xdmx，简单说来就是把多个 X server 整合成一个 X server 来用。比如你有 2
台独立的 Linux 电脑运行了 X server。你可以把两个显示并放在一起。然后通过
Xdmx 整合成一个大显示器来用，比较适合用来看电影。

xdmx 还支持动态的增加删除 X server。比如你原本是 3 个 X server
组成一个大的 X server。现在因为其中一个 X server
暂时要用来做别的事情，你可以用一个命令删除这个 X
server。然后继续使用，连运行在 X server 之上的 wm 或者 desktop
都不用重启。

xdmx 项目主页：<http://dmx.sourceforge.net>
