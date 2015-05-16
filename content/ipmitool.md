Title: IPMItool: IPMI 管理工具
Date: 2009-01-03 10:13
Author: hmy
Category: Apps
Tags: ipmitool
Slug: ipmitool

IPMI（智能管理协议）是一个被大多数服务器厂商支持的协议，配合主板上的一个独立的部件（BMC），可以实现很多有用的功能。比如远程电源状态控制和端口重定向。利用这个特性，你可以远程控制机房的服务器电源状态（比如你机器之前的状态是关机，但是只要电源还插着，就可以远程打开电源）和安装操作系统，配置
BIOS 等等。

由于短篇幅说不完，详细的介绍可以自己去找，这里我简单说一下如何管理 Dell
x99xx 系列机器（不需要 Dell 机器安装 DRAC 卡）。

首先配置 Dell 服务器的 BMC，开机的时候，根据提示按
Ctrl+e，进入管理界面，设置好 IP、Sol 等。比如设置 IP 为 10.0.0.2。

然后在另一个同网段的电脑（IP 10.0.0.3）上安装好
IPMItool，利用如下的命令来执行管理，比如：

`ipmitool -I lanplus -U root -P calvin -H 10.0.0.2  power off`

直接关机

`ipmitool -I lanplus -U root -P calvin -H 10.0.0.2 power on`

开机

`ipmitool -I lanplus -U root -P calvin -H 10.0.0.2 sol activate`

打开端口转发，然后可以从这里可以看到被管理机器的 BIOS 启动画面。

更多的功能以及详细的配置需要自己参考文档，这里只是抛砖引玉，我也比较懒，不会写很详细的操作手册。

ps: 本文适合管理机房服务器人员，不适合 PC 用户。

[IPMItool](http://ipmitool.sourceforge.net/)
