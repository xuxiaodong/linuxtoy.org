Title: 使用 GConf Cleaner 清理 GConf
Date: 2007-06-11 08:30
Author: toy
Category: Apps
Slug: gconf-cleaner

[GConf](http://www.gnome.org/projects/gconf/) 是一个用于存储 GNOME
应用程序选项设置的系统。如果该系统充斥着大量无用键值，那么将使 GConf
臃肿不堪。这对应用程序的启动速度和性能都是有影响的。为了解决这个问题，你可以使用
[GConf Cleaner](http://code.google.com/p/gconf-cleaner/)
来对其进行清理。

在 GConf Cleaner 的项目主页上，你现在可以下载到 0.0.2
版。然后，你需要通过以下步骤来安装它：

1.  `tar zxvf gconf-cleaner-0.0.2.tar.gz` #解压
2.  `cd gconf-cleaner-0.0.2/` #进入解压后的目录
3.  `./configure` #执行配置过程
4.  `make` #编译
5.  `sudo make install` #安装

从终端执行 `gconf-cleaner` 启动 GConf Cleaner
程序。这个程序具有执行向导，只需按步骤操作即可。

[![GConf
Cleaner](http://i.linuxtoy.org/i/2007/06/gconf-cleaner01_s.png)](http://i.linuxtoy.org/i/2007/06/gconf-cleaner01.png)  
向导初始画面，点击 Forward 会进入分析过程。

[![GConf
Cleaner](http://i.linuxtoy.org/i/2007/06/gconf-cleaner02_s.png)](http://i.linuxtoy.org/i/2007/06/gconf-cleaner02.png)  
分析结果，提供具体数据，并可保存。再次点击 Forward 则开始清理过程。

[![GConf
Cleaner](http://i.linuxtoy.org/i/2007/06/gconf-cleaner03_s.png)](http://i.linuxtoy.org/i/2007/06/gconf-cleaner03.png)  
清理完成。

- [Download GConf Cleaner
0.0.2](http://code.google.com/p/gconf-cleaner/downloads/list)

[[via](http://www.linuxinsight.com/how-to-cleanup-your-gnome-registry.html)]
