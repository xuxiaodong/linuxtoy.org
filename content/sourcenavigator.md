Title:  源代码阅读利器：Source Navigator
Date: 2008-11-20 11:22
Author: MDZ
Category: Apps
Tags: redhat, sourcenavigator, 源代码阅读
Slug: sourcenavigator

想阅读 linux
的源代码，却又苦于在扎堆的文件中寻找目标头文件？如果没有好的工具，那么阅读代码将成为一件苦差事。幸而世界上存在帮助你分析源代码的软件。[Source
Navigator](http://sourcenav.sourceforge.net/) 是 Red Hat 开发的一个
IDE，但我们一般不用它来开发，而是用来阅读源代码 ──
因为它能很好地解决文件定位和跳转问题（比如哪个函数在哪个头文件中出现，它将自动帮你做好链接）。

[![Source
Navigator](http://i.linuxtoy.org/images/2008/11/sourcenavigator-300x197.png)](http://i.linuxtoy.org/images/2008/11/sourcenavigator.png)

Source Navigator 可从其官方网站上获取，也可直接从软件源中安装。在 Ubuntu
中，我们通过  
`sudo apt-get install sourcenav`  
安装，然后通过 snavigator 来运行。（好变态，看到没有，一个是
sourcenav，另一个是 snavigator）

运行第一步是要建立源代码的 project
以及扫描源代码文件，自动建立文件之间的索引。对 2.6 版本以上的 linux
来说，这项工作通常要花好几分钟。然后我们就可以畅游在 Source Code 中了。

Source Navigator 资源：  
官方网站：<http://sourcenav.sourceforge.net/>  

下载地址：<http://sourceforge.net/project/showfiles.php?group_id=51180>  
文档：<http://sourcenav.sourceforge.net/online-docs/index.html>

在 Windows 下，与 Source Navigator 类似的软件为 Source
Insight，要钱的，BS！
