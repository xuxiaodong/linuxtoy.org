Title: OpenNTPD 的误差……
Date: 2010-01-02 12:34
Author: toy
Category: Tips
Tags: OpenNTPD
Slug: openntpd-tip

{ 撰文/[shadow](http://ashadow.blogbus.com) }

我一直认为 OpenNTPD
能使我电脑的时间保持准确，但我直到昨天才发现电脑的时间跟实际的有两分钟左右的误差，不太准确……

我刚才查出了原因——只有当 OpenNTPD 发现系统时间与 NTP
服务器所提供的时间相差超过 180 秒时才会校正时间。

奇怪的是，该软件并没有提供修改这 180 秒的误差范围的方法……

显然，这 180 秒的范围实在太大了，远不能满足我的要求（误差 1 秒内）。

于是，我想到了个不是办法的办法，就是先把系统时间弄得很离谱，然后再让
OpenNTPD 来同步时间……

具体命令如下（Arch 下）：

(sudo) date -s 00:00:00 （先随便设个时间）  
(sudo) ntpd -s （同步）  
(sudo) hwclock -w （把系统时间写进硬件）

……不知大家能否提供更好的解决方案？

{ [Source](http://ashadow.blogbus.com/logs/55818007.html). Thanks
shadow. }
