Title: GtkHash — 计算校验和
Date: 2008-01-08 09:00
Author: toy
Category: Apps
Slug: gtkhash

[GtkHash](http://gtkhash.sourceforge.net/) 具有 GTK+
界面，是用来计算校验和的小工具。当前，GtkHash 支持计算
MD5、SHA1、SHA256、SHA512、RIPEMD、HAVAL、TIGER、WHIRLPOOL 等 hash 值。

[![GtkHash
截图](http://i.linuxtoy.org/i/2008/01/gtkhash-thumb.png)](http://i.linuxtoy.org/i/2008/01/gtkhash.png)  
GtkHash 截图 (点击可放大)

**编译安装 GtkHash**

GtkHash 要求 GTK+ 2、mhash 及 libglade 2，在编译之前需安装好。接着，获取
GtkHash 目前版本 0.2.0
的[源代码](http://sourceforge.net/project/showfiles.php?group_id=199892&release_id=532163)。

要编译并安装 GtkHash，可以执行下列指令：  

` tar zxvf gtkhash-0.2.0.tar.gz cd gtkhash-0.2.0 ./configure make make install`

注意，最后一步需要 root 权限。

现在，在终端中执行 gtkhash 即可启动 GtkHash。
