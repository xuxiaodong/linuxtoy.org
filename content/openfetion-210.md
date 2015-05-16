Title: OpenFetion 2.1.0
Date: 2010-12-27 03:42
Author: lovenemesis
Category: Instant Messenger
Tags: openfetion
Slug: openfetion-210

GTK2 开源飞信客户端 OpenFetion 2.1.0 发布，增加**命令行支持**。

本次分布中 OpenFetion 拆分成三部分：协议库 libofetion，GTK+ 客户端
openfetion 及命令行版本 cliofetion。

[协议库独立下载](http://code.google.com/p/ofetion/downloads/detail?name=libofetion-2.1.0.tar.gz)

[GTK+
客户端独立下载(**推荐大多数用户使用**)](http://code.google.com/p/ofetion/downloads/detail?name=openfetion-standalone-2.1.0.tar.gz)

[命令行版本独立下载](http://code.google.com/p/ofetion/downloads/detail?name=cliofetion-standalone-2.1.0.tar.gz)

[完整版本下载](http://code.google.com/p/ofetion/downloads/detail?name=openfetion-all-2.1.0.tar.gz)

这次 openfetion 编译工具链迁移到 cmake 上了，这里简单说下 **Fedora
上的编译方法**：

安装编译前提条件：

`pkcon install cmake gcc-c++ gstreamer-devel gtk2-devel libxml2-devel
openssl-devel intltool sqlite-devel NetworkManager-devel
libXScrnSaver-devel libnotify-devel`

遵循 cmake 的习惯，创建编译目录并进入：

`mkdir build ; cd build`

使用 cmake 生成编译文件：

`cmake .. -DDISABLE\_NLS="1" -DCMAKE\_INSTALL\_PREFIX=/usr`

编译：

`make`

安装：

`su -c 'make install'`

**卸载方法请参考压缩包内自述文件！**
