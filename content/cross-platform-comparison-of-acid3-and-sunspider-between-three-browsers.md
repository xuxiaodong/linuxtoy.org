Title: 三款跨平台浏览器的 Acid3 及 Sunspider 测试
Date: 2009-08-01 21:33
Author: lovenemesis
Category: Reviews
Tags: chrome, Firefox, Opera
Slug: cross-platform-comparison-of-acid3-and-sunspider-between-three-browsers

相信各位都阅读过关于 Mozilla Firefox 3.5, Opera 10 Beta 和 Google Chrome
这三款跨平台浏览器的比较评测，不过很少读到在 Linux
平台下的评测吧？本文将分别在 Linux 和 Windows 平台下对于它们进行 Acid3
和 Sunspider 评测并比较。欢迎使用 Mac OS X 的朋友补充更多内容。

**测试平台介绍：**

*Linux 平台*

AMD Turion 64 X2 TL-58 1.9GHz 1M L2 Cache DDR2 800 4Gb

Fedora 11 2.6.29.6-213.fc11.i686.PAE

Nvidia GeForce 8400M G Nvidia 190.18

*Windows 平台*

AMD Althon 64 X2 3600+ 2.0GHz 512k L2 Cache DDR2 800 1Gb

Windows XP SP3

Nvidia GeForece 6100 Nvidia 190.38

**测试项目介绍**

*[Acid3](http://acid3.acidtests.org/)*

该项目主要考察对于网页标准的执行情况，尤其是 DOM 和
JavaScript，侧重于精准性。[Wikipedia](http://en.wikipedia.org/wiki/Acid3)

*[Sunspider](http://www2.webkit.org/perf/sunspider-0.9/sunspider.html)*

该项目主要考察浏览器执行核心 JavaScript 任务时速度，不包括
DOM，侧重于执行效率。
[Wikipedia](http://en.wikipedia.org/wiki/SunSpider_JavaScript_Benchmark#SunSpider)

**参加比较的三款浏览器信息：**

Mozilla Firefox 3.5.1 [Mozilla 官方版本](http://www.mozillaonline.com/)
（非发行版自带版本）

Opera 10 Beta 2 [官方 Qt4 版本](ftp://ftp.opera.com/pub/opera/)

Chromium （Google Chrome 的开源版本） [3.0.197.0 svn
22243](http://build.chromium.org/buildbot/snapshots/)

下面评测正式开始～

**首先是 Linux 平台下的 Acid3 测试（得分越高越好）**

*Mozilla Firefox*

93/100

*Opera 10*

100/100

*Chromium  
*  
100/100 右上角有一个奇怪的红叉

**下来是 Linux 平台下的 Sunspider 测试（耗时越少越好）**

*Mozilla Firefox*

Total: 3735.4ms +/- 5.3%

*Opera 10*

Total: 12549.8ms +/- 2.3%

*Chromium*

Total: 2090.6ms +/- 4.8%

**接下来是 Windows 平台下的 Acid3 测试（得分越高越好）**

*Mozilla Firefox*

93/100

*Opera 10*

100/100

*Chromium*

100/100 右上角有一个奇怪的红叉

**下来是 Windows 平台下的 Sunspider 测试（耗时越少越好）**

*Mozilla Firefox*

Total: 1602.2ms +/- 1.4%

*Opera 10*

Total: 6553.6ms +/- 0.6%

*Chromium*

Total: 759.0ms +/- 3.3%

**总结**

无论在哪个平台上，Acid 3 测试中表现程度 Opera > Chromium >
Firefox，同一浏览器在不同平台表现无差别。

而在 Sunspider 测试中， Chromium > Firefox > Opera，在 Windows
平台的用时比 Linux 平台下快了一倍！

Sunspider 测试中如此巨大的差异很什么原因呢？是 Athlon 64 X2 3600+
的速度比 Turion 64 X2 TL-58 快了一倍？还是在 Windows
平台的运行效率快了一倍？

**PS:**

为何没有在同一硬件平台上测试？

安装 Fedora 的本本是平日工作用的，自从入手后就没打算装过
Windows，没有预留分区。  
安装 Windows 的台式机的主板电源管理跟 2.6.24
以后内核相应模块有冲突，无法安装 Fedora 。

欢迎使用双系统的朋友提供进一步评测数据！
