Title: tasque: linux上的RTM客户端
Date: 2008-09-14 09:49
Author: lwl
Category: Apps
Tags: GTD
Slug: tasque_for_rt

RTM, [remember the
milk](https://www.rememberthemilk.com)是现在比较流行的在线待做事宜网站之一，如果你正好在使用RTM，
而又不喜欢老是用浏览器登录的话，tasque就是一个不错的选择。当然，tasque也可以用来使用本地的文件，或者Evolution
Data Server。

[tasque](http://live.gnome.org/Tasque)，读做task，两位作者在他们的某周时间内使用C#进行了快速开发，作为todo
list管理的前端, 效果还是不错的。更多后端服务正在添加之中。

如果使用RTM作为后端服务器的话，它会让你登录到RTM，在其中允许tasque进行访问。然后就可以在本地管理待做事宜了.
因为相当于一个网络终端，同步可能需要一些时间。

截图：  

[![tasque](http://i.linuxtoy.org/i/2008/09/2329404961_6d40366a90_o.png)](http://i.linuxtoy.org/i/2008/09/2329404961_6d40366a90_o.png)

如何在Ubuntu 8.04中安装？  
将

> deb http://ppa.launchpad.net/tasque-packagers/ubuntu hardy main

加入source.list即可。  
源代码安装见[此](http://live.gnome.org/Tasque/Building)。

详情请看[tasque＠live.gnome.org](http://live.gnome.org/Tasque)。
