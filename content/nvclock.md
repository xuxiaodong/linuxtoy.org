Title: NVClock：优化 Nvidia 显卡
Date: 2008-10-26 09:51
Author: toy
Category: Apps
Tags: NVClock, NVIDIA
Slug: nvclock

最近忽然发现我的 Nvidia
显卡转得有点快，响声很大，于是想降降噪。经过一番搜索，找到了 NVClock
这个小工具。利用
NVClock，既可以控制显卡风扇的转速，也可以调整显卡的时钟频率，换句话说，就是超频。

NVClock 在一般的 Linux
发行版软件仓库中可能都有收录，要安装它，只需使用包管理器搜索并安装即可。不过，这种安装方式有可能不是最新版。如果显卡较新的话，推荐使用
NVClock 的最新版本，这样支持的显卡型号更多。目前，NVClock 的最新版本是
0.8 (beta 3)。在获取源码并解包后，可执行以下命令安装：

./autogen.sh  
./configure  
make  
make install

在第二步配置时，有一些编译选项可以使用。具体可以通过
`./configure --help` 查询。

当 NVClock 安装完成后，就可以在终端中输入 nvclock
命令来执行了。比如，我想调整风扇转速，可执行：

`nvclock -F nn`

这里的 nn 介于 10 到 100 之间。

关于 nvclock 的更多选项，可执行 `nvclock -h` 了解。

NVClock 也包括图形化的界面可以使用：

[NVClock](http://i.linuxtoy.org/i/2008/10/nvclock-gtk.png)

NVClock 网站位于：
