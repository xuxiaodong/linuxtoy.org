Title: PyBackPack──文件备份工具
Date: 2007-05-28 19:21
Author: toy
Category: Apps
Slug: pybackpack

[PyBackPack](http://andrewprice.me.uk/projects/pybackpack/)
是一款文件备份工具，它具有用户界面友好、特别容易使用等特点。此工具为
GNOME
桌面环境而编写，能够存储预设的备份配置，支持将数据、文件备份到本地目录、CD/DVD、以及远程目录（通过
SSH）。当然，这个工具也包含将备份文件进行还原的功能。

[![PyBackPack](http://i.linuxtoy.org/i/2007/05/pybackpack_s.png)](http://i.linuxtoy.org/i/2007/05/pybackpack.png)  
*使用 PyBackPack 备份文件*

若需让 PyBackPack 在你的系统上顺利运行，则要满足下列依赖：

-   GTK+ 2.2.x
-   pygtk
-   pyglade
-   rdiff-backup
-   nautilus-cd-burner
-   gnomevfs

PyBackPack 目前所发布的最新版为 0.5.1，在下载后，可以使用
`python setup.py install` （注意需要 root 权限）进行安装。

- [Download PyBackPack
0.5.1](http://andrewprice.me.uk/projects/pybackpack/download/)
