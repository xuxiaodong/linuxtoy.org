Title: 安装 Aurora Gtk 主题引擎
Date: 2007-04-23 21:22
Author: toy
Category: Tutorials
Slug: install-aurora-gtk-engine

[Aurora](http://linuxtoy.org/archives/aurora-gtk-engine.html)
是一个在设计上颇有新意的主题引擎，之前本站曾有过简略的介绍。由于其作者并没有提供二进制的包可用，所以如果我们要在自己的系统中使用的话，就需要亲自动手编译啰。

在准备好 Aurora Gtk 主题引擎所用的依赖 Gtk 2.10
后，就可以开始进行编译工作了。其操作步骤如下：

1.  `tar jxvf Aurora-0.9.1.tar.bz2`：这会解出两个包：aurora-0.9.1.tar.gz
    和 themes.tar.bz2，前者为 Aurora Gtk
    主题引擎的源代码，后者为其所用的主题。
2.  `tar zxvf aurora-0.9.1.tar.gz`
3.  `cd aurora-0.9.1/`
4.  `./configure --prefix=/usr --enable-animation`：准备将 Aurora Gtk
    主题引擎安装到 /usr，并开启进度条的动画效果。
5.  `make`
6.  `sudo make install`

至此，Aurora Gtk
主题引擎的编译及安装已经完成。下面，我们将安装其所带的主题：

1.  `cd ..`
2.  `tar jxvf themes.tar.bz2 -C ~/.themes`

现在让我们来看看安装了 Aurora 主题之后的效果：

![Aurora Default](http://i.linuxtoy.org/i/2007/04/aurora-default.png)  
*Aurora 默认主题*

![Aurora Default](http://i.linuxtoy.org/i/2007/04/aurora-looks.png)  
*Aurora Looks 主题*

![Aurora Default](http://i.linuxtoy.org/i/2007/04/aurora-midnight.png)  
*Aurora Midnight 主题*

- [Download Aurora Gtk Engine
0.9.1](http://www.gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438)
