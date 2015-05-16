Title: VRMS: 你使用了多少非自由软件
Date: 2010-05-10 19:30
Author: toy
Category: Cli
Tags: VRMS
Slug: vrms

稍微熟悉 GNU 历史的朋友，相信对 Richard M. Stallman  
不会感到陌生。[VRMS](http://vrms.alioth.debian.org/) 即  
Virtual Richard M. Stallman
的简称，这是一个有趣的小程序，它可以检测出你的  
GNU/Linux
系统中到底安装了多少非自由软件，除了给出相应包的简略说明外，更有所占百分比作为度量。你可以通过  
VRMS 来了解自己使用了多少非自由软件。

[![vrms](http://i.linuxtoy.org/images/2010/05/thumb-vrms.png)](http://i.linuxtoy.org/images/2010/05/vrms.png)

VRMS 在基于 Debian 的系统上可以使用如下命令安装：

# aptitude install vrms

VRMS 的源代码可从  
[alioth.debian.org](http://alioth.debian.org/projects/vrms/) 获取。

在安装 VRMS 后接着执行 `vrms -e`
即可知晓你的系统中安装了哪些非自由软件。
