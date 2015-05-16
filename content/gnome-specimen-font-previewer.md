Title: 使用 GNOME Specimen 查看字体
Date: 2007-06-05 19:06
Author: toy
Category: Apps
Slug: gnome-specimen-font-previewer

如果你想知道系统中所安装的字体究竟什么样，那么使用 [GNOME
Specimen](http://uwstopia.nl/blog/2007/06/gnome-specimen-0-2-is-out)
吧。GNOME Specimen
可以让你查看系统中已安装的所有字体，并对各种字体进行比较，以帮助你进行选择。

[![GNOME
Specimen](http://i.linuxtoy.org/i/2007/06/gnome-specimen_s.png)](http://i.linuxtoy.org/i/2007/06/gnome-specimen.png)  
*使用 GNOME Specimen 查看系统中已安装的字体*

GNOME Specimen 当前最新版本是 0.2，具有 DEB
包和源码包可用。如果你的系统是 Debian/Ubuntu，那么在下载 DEB
包后，可以执行如下指令安装：  
`sudo dpkg -i gnome-specimen_0.2-0_all.deb`

如果你的系统是其他 Linux
发行版的话，可以在下载源码包之后，通过下列步骤安装：

1.  `tar zxvf gnome-specimen-0.2.tar.gz`
2.  `cd gnome-specimen-0.2/`
3.  `./configure`
4.  `make`
5.  `sudo make install`

注意在编译之前检查你的系统是否满足如下依赖：

-   PyGTK
-   Gnome Python bindings
-   Glade Python bindings
-   Gconf Python bindings

在安装完成后，从终端执行 `gnome-specimen` 即可启动 GNOME Specimen。

- [Download GNOME Specimen 0.2
(source)](http://uwstopia.nl/files/2007/06/gnome-specimen-0.2.tar.gz)  
- [Download GNOME Specimen 0.2
(deb)](http://uwstopia.nl/files/2007/06/gnome-specimen_0.2-0_all.deb)
