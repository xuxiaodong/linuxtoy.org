Title: 安装 Murrine GTK2 Cairo Engine
Date: 2006-12-15 22:21
Author: toy
Category: Tutorials
Slug: install_murrine_gtk2_cairo_engine

Murrine GTK2 Cairo Engine 是一个相当漂亮的 GTK2 主题引擎，该引擎本身基于
Cairo，与 Clearlooks-Cairo 和 Ubuntulooks 相比，速度上大约要快 30%
左右。而且，现在 GNOME-LOOK 上针对 Murrine GTK2 Cairo Engine
所制作的样式也是非常的多，选择的空间很大。

下面，介绍 Murrine GTK2 Cairo Engine 在 Ubuntu 中的安装过程。

1.  `wget http://malteo.homelinux.net/B54820BC.gpg -O- | sudo apt-key add -`
2.  在 /etc/apt/sources.list 中，加入  

    ` deb http://malteo.homelinux.net edgy-malteo all deb-src http://malteo.homelinux.net edgy-malteo all`
3.  `sudo apt-get update`  
    `sudo apt-get install gtk2-engines-murrine`

OK. 到 [gnome-look](http://gnome-look.org/) 上去抓取喜欢的 Murrine
样式吧。
