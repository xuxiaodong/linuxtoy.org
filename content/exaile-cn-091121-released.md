Title: Exaile-cn 091121 发布
Date: 2009-11-22 15:01
Author: toy
Category: Apps
Tags: Exaile
Slug: exaile-cn-091121-released

[Exaile-cn](http://linuxtoy.org/archives/exaile-cn.html) 091121  
版本现已发布。该版本提供了对 Exaile 0.3  
的支持。Exaile-cn  

目前的功能包括解决乱码问题、同步显示歌词、获取豆瓣封面等。其功能基本完善，欢迎  
Exaile 用户试用。

[![Exaile-cn](http://i.linuxtoy.org/images/2009/11/exaile-cn-thumb.png)](http://i.linuxtoy.org/images/2009/11/exaile-cn.png)

**使用说明**

1. 解决乱码问题方法：将 \\\_id3.py 覆盖到 /usr/lib/exaile/xl/metadata
目录下（需要 root）  
2. 豆瓣封面插件安装方法：将 doubancovers 复制到
/usr/share/exaile/plugins/ 下，然后启动 Exaile，选中插件选项即可  
3. 歌词同步显示插件安装方法：先把 engine\_unified.py 和
engine\_normal.py 覆盖到 /usr/lib/Exaile/xl/player 下，再将 LyricDisp
复制到 /usr/share/exaile/plugins/ 下，然后启动 Exaile，选中插件选项即可

* [项目主页](http://code.google.com/p/exaile-cn/)  
*
[程序下载](http://exaile-cn.googlecode.com/files/Exaile-cn091121.tar.gz)

{ Thanks billma. }
