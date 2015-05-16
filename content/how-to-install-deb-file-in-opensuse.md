Title: 浅谈各种软件包转换及在openSUSE下如何安装deb包
Date: 2009-08-31 19:55
Author: gmsh
Category: Apps
Tags: alien, openSUSE
Slug: how-to-install-deb-file-in-opensuse

openSUSE 默认的包管理系统用的是 RPM 系统。而能得到的很多软件安装包却是
Debian 系的 DEB 格式的，比如目前的 Chromium 官方只提供 DEB 包。

[John Smith](http://blog.gmsh.pp.ru/about)就介绍一种在 openSUSE 下安装
deb 安装包的方法。

[![](http://i.linuxtoy.org/images/2009/08/deb.jpeg)](http://i.linuxtoy.org/images/2009/08/deb.jpeg)[![](http://i.linuxtoy.org/images/2009/08/rpm.jpeg)](http://i.linuxtoy.org/images/2009/08/rpm.jpeg)

*转自
[http://blog.gmsh.pp.ru/2009/08/how-to-install-deb-file-in-opensuse/
(Gmsh's
Blog)](http://blog.gmsh.pp.ru/2009/08/how-to-install-deb-file-in-opensuse/)*

其实，各个系列的安装包，细数起来功能不过一下几种：压缩存储数据，检查软件依赖性，控制文件复制到指定目录，在指定的位置产生配置文件，向某些系统注册等功能罢了。最多也就是加上个交互的功能。同时，包管理系统能保证同一时间内只有一个配置进程锁定修改系统，以保证稳定性。简单的说，就是数据和控制两部分。既然各个系列的包管理器原理上差不多，那么名目繁多的各种格式安装包，就能说是大同小异，殊途同归了。何况现在的
Linux
系统的各个发行版还没有分化到完全不兼任的地步，那么，借助软件和手工配置达到通用软件包的内容的目的是完全可能，毕竟基本上都是同源、类似架构的。

有这么一款软件叫 alien 的软件可以达到这一目的。它可以实现
DEB、RPM、SLP、TGZ、PKG
等几种安装包的转换生成。这里仅介绍在openSUSE下安装deb安装包的情况，更详细的内容请参考
alien 手册。

你拿到一个软件包，名为 packagename.deb 那么在装有 alien
的情况下，可以如此解决：

`su -c "alien -rc packagename.deb && rpm -i packgename.rpm" `

su 是保证产生的 RPM 包的所有权正确；-r 是标明转换为 RPM 格式；-c
是保证脚本也会被安装。

需要提醒的是如果这样生成的包不能安装，那就要手动改变了，无非是补全依赖性，作几个拷贝、链接罢了。那些真正由于架构相异而不兼容的问题是只能通过重新编译解决的，不能偷懒的。
