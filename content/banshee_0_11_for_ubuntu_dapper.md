Title: Banshee 0.11 for Ubuntu 6.06 编译指南
Date: 2006-09-20 21:09
Author: toy
Category: Tutorials
Slug: banshee_0_11_for_ubuntu_dapper

目前，[Banshee](http://banshee-project.org) 的新版本 0.11
已然发布。可能有些同学早就想跃跃欲试了。以下就是 Banshee 0.11 在 Ubuntu
6.06 中的编译过程。

1.  准备编译依赖

        sudo apt-get build-dep banshee
        sudo apt-get install libavahi-cil

2.  下载 Banshee 0.11 及其插件

        wget http://banshee-project.org/files/banshee/banshee-0.11.0.tar.gz
        wget http://www.banshee-project.org/files/banshee-official-plugins/banshee-official-plugins-0.11.0.tar.gz

3.  解包

        tar -xvzf banshee-0.11.0.tar.gz
        tar -xvzf banshee-official-plugins-0.11.0.tar.gz

4.  配置、编译并安装 Banshee

        cd banshee-0.11.0
        ./configure --prefix=/usr --enable-avahi --disable-docs
        make
        sudo make install

5.  配置、编译并安装插件

        cd banshee-official-plugins-0.11.0
        ./configure --prefix=/usr
        make
        sudo make install

6.  运行 Banshee
    可通过在终端中输入 banshee，或从“Applications->Sound &
    Video”菜单中执行。

注意：如果启用了 QuinnStorm
源，在编译时可能会出错，解决办法见[这里](http://ubuntuforums.org/showthread.php?t=238449)。

（Via [Linux
Revolution](http://linuxrevolution.blogspot.com/2006/09/howto-banshee-011-ubuntu.html),
thanks!）
