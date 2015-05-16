Title: Reconstructor：Ubuntu Live CD 个性化定制工具
Date: 2006-07-29 15:57
Author: toy
Category: Apps
Slug: reconstructor

[Reconstructor](http://reconstructor.aperantis.com)
目前正在测试，但开发者已经提供了下载文件，所以需要个性化定制
[Ubuntu](http://www.ubuntu.com) Live CD
的用户大可拿来一试。就个性化定制的内容来说，现在你可以通过 Reconstructor
来实现 boot screens（引导屏幕图像）、Gnome 设置（包括 GDM
主题、桌面壁纸、字体、主题）和软件的定制。当然，在创建 Live CD
之前，你同样可以使用 chroot 环境来作出其他的改变。

此程序使用 python 所写，无需安装，解压即可使用。但运行时需要
squashfs-tools 包（可通过 `sudo apt-get install squashfs-tools`
进行安装）。

相关下载：

[Reconstructor Beta
0.1.0.3](http://reconstructor.aperantis.com/index.php?option=com_remository&Itemid=33&func=download&id=2&chk=049e20bec5686771d56e731d265c2135)
