Title: Netenv: 开机时选择你的网络环境
Date: 2009-04-24 17:12
Author: hmy
Category: Apps
Tags: Netenv
Slug: netenv

Netenv
适合于网络环境经常变动的情况，比如带着笔记本在家和公司切换，网络环境又还不一样。这个工具思路很简单，启动的时候，弹出一个对话框，让你选择一个环境，然后网络就按特定的参数设置。

![Netenv](http://i.linuxtoy.org/images/2009/04/netenv.png)

在 Debian/Ubuntu 上，就是简单的把 /etc/network/inetfaces
文件做符号链接到不同的配置文件上（不同的环境不同的配置文件）。

因为选择不同的环境，可以执行不同的脚本，这样可以在脚本里面做一个时间判定，比如在工作时间把网络配置成公司网络环境，在非工作时间，配置成在家的环境。当然这个方法不适合经常加班的同学
:D

[Netenv](http://netenv.sourceforge.net/)
