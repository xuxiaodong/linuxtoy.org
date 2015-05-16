Title: CheckInstall：快速创建 deb、rpm 包
Date: 2008-09-24 11:49
Author: hmy
Category: Apps
Tags: CheckInstall
Slug: checkinstall

[撰文/hmy]

CheckInstall 用于方便的创建 deb、rpm、slackware
二进制包。试用了一下，非常简单。值得推荐。

**用法：**

首先安装 CheckInstall，提供 rpm
和源代码方式，不赘述。然后编译你想安装的软件，但是不 make
install。比如你要安装 nginx：

1.  下载 nginx
2.  解压 nginx.tar.gz
3.  进入 nginx 目录执行 ./configure --prefix=/usr/local/nginx ; make
4.  运行 checkinstall
5.  回答几个问题就 ok 了，比如对包的描述、以及要创建哪种类型的包。

[CheckInstall](http://checkinstall.izto.org/)
