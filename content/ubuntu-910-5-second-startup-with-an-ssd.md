Title: Ubuntu 9.10 在 SSD 上完成启动仅用 5 秒
Date: 2009-09-23 15:57
Author: toy
Category: News
Tags: Ubuntu
Slug: ubuntu-910-5-second-startup-with-an-ssd

自 Ubuntu 9.04 开始，Canonical 一直致力于改进 Ubuntu 的启动速度。据 Ars  
Technica 报道，Ubuntu 9.10 的最新  

[Alpha](http://linuxtoy.org/archives/ubuntu-karmic-alpha-6-released.html)
版本在  
SSD（solid state disk，固态硬盘）上完成系统启动过程仅用了 5
秒，其中，Xorg  
用了两秒。该结果通过
[Bootchart](http://linuxtoy.org/archives/bootchart.html)  
工具测试得到，见下图。

[![Bootchart](http://i.linuxtoy.org/images/2009/09/watson-karmic-20090909-3-thumb.png)](http://i.linuxtoy.org/images/2009/09/watson-karmic-20090909-3.png)

*点击可放大*

探究其中的原因，主要有二：

* 一是通过使用 [Sreadahead](http://code.google.com/p/sreadahead/)  
系统服务来预存引导过程所需的数据，从而加快系统启动速度。  
* 二是 Ubuntu 所用的基于事件的引导守护程序 Upstart
具有并行处理引导进程的能力。

{ via [Ars  

Technica](http://arstechnica.com/open-source/reviews/2009/09/ubuntu-910-alpha-6-released-boot-optimizations-arrive.ars)  
}
