Title: Webilder：从 Flickr 下载图片
Date: 2006-10-12 21:34
Author: toy
Category: Apps
Slug: webilder

[Webilder](http://www.webilder.org)
兼具两方面的功能：一面充当下载器，可直接从
[Flickr](http://www.flickr.com)
上下载图片；另一面又扮演着壁纸更换器的角色，可手动或自动按时设置桌面壁纸。具体说起来，Webilder
还包含这些特长：

-   在下载方面，支持按 Tag 和用户名的方式从 Flickr
    下载图片。同时，也可以下载 Flickr
    上[最有趣](http://www.flickr.com/explore/interesting/)的图片。甚至包括自动下载。
-   对于那些已经下载的图片来说，Webilder
    具备简单的浏览和管理功能，可以在其中直接设置桌面壁纸，支持每隔几分钟便自动进行更换。

Webilder 于前天发布了
[0.5](http://www.webilder.org/static/downloads/Webilder-0.5.tar.gz)
版。Ubuntu 用户可以直接使用其所提供的源。

-   对于 Dapper：  

    ` deb http://debian.websterwood.com/ dapper main deb-src http://debian.websterwood.com/ dapper main`
-   对于 Edgy：  

    ` deb http://debian.websterwood.com/ edgy main deb-src http://debian.websterwood.com/ edgy main`

安装的话，则使用下列命令：  
` sudo apt-get update sudo apt-get install webilder`  
如果要支持 GNOME，那么安装 webilder-gnome；相应地，KDE 用
webilder-kde。

`sudo apt-get install webilder webilder-gnome`  
`sudo apt-get install webilder webilder-kde`

使用 webilder\_desktop 可以启动 Webilder。

[![Webilder](http://i.linuxtoy.org/i/webilder_s.png)](http://i.linuxtoy.org/i/webilder.png)

其他发行版的安装，或是手动安装，参阅[安装介绍](http://www.webilder.org/download.html#manual)。
