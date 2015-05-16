Title: EXT4文件系统测试
Date: 2008-12-05 13:38
Author: lovenemesis
Category: Featured
Tags: ext4
Slug: ext4-benchmarks

尽管 ext4 文件系统要到 Kernel 2.6.28
才被认为是完全稳定，但是相信有很多人随着 Fedora 10 的发布开始使用 ext4
文件系统了。到底 ext4 文件系统的性能怎么样呢？希望这篇来自于
[Phoronix](http://www.phoronix.com/scan.php?page=article&item=ext4_benchmarks&num=1)
的评测可以解答部分疑问。  

**注意：本文不是逐字逐句对原文的翻译！但是保留原文所有观点。转载并不代表认同。**

评测使用的硬件平台为英特尔双路四核 Xeon
E5320，泰安i5400XT，金士顿FB-DIMM 2GB，西数 WD1600YS-01SHB1 SATA 160 GB
硬盘，华硕 Geforce 9600GT 512MB。软件平台为 Fedora 10 X86\_64 Linux
2.6.27 内核，X server 1.5.3，GNOME 2.24.1，GCC 4.3.2和 IcedTea
1.3.1。显卡驱动使用的是nVidia官方 180.08版本。除了 4GB 的 SWAP
外全部为根分区。评测将在 EXT3、EXT4、XFS 和 ReiserFS 文件系统使用
[Phoronix Test Suit 1.6.0 Alpha
2](http://www.phoronix.com/scan.php?page=news_item&px=Njg5MQ)
测试以下项目：Nexuiz，World of Padman， Unreal Tournament 2004，7-Zip
压缩，并行 BZIP2 压缩，LZMA 压缩，LAME MP3 编码，FFmpeg 编码，GnuPG
文件加密，OpenSSL, 和 Bork
文件加密。每在一种文件系统下测试后都将重新安装系统，除了禁用 SELinux
外其余设置保持默认。另外，还会使用 Bonnie++，IOzone 和 Flexible IO
Tester 进行纯理论性能测试。

以下是测试结果条形图：

[![](http://i.linuxtoy.org/images/2008/12/1.png)](http://i.linuxtoy.org/images/2008/12/1.png)  

[![](http://i.linuxtoy.org/images/2008/12/2.png)](http://i.linuxtoy.org/images/2008/12/2.png)  

[![](http://i.linuxtoy.org/images/2008/12/3.png)](http://i.linuxtoy.org/images/2008/12/3.png)  

[![](http://i.linuxtoy.org/images/2008/12/4.png)](http://i.linuxtoy.org/images/2008/12/4.png)  

[![](http://i.linuxtoy.org/images/2008/12/5.png)](http://i.linuxtoy.org/images/2008/12/5.png)  

[![](http://i.linuxtoy.org/images/2008/12/6.png)](http://i.linuxtoy.org/images/2008/12/6.png)  

[![](http://i.linuxtoy.org/images/2008/12/7.png)](http://i.linuxtoy.org/images/2008/12/7.png)  

[![](http://i.linuxtoy.org/images/2008/12/8.png)](http://i.linuxtoy.org/images/2008/12/8.png)  

[![](http://i.linuxtoy.org/images/2008/12/9.png)](http://i.linuxtoy.org/images/2008/12/9.png)  

[![](http://i.linuxtoy.org/images/2008/12/10.png)](http://i.linuxtoy.org/images/2008/12/10.png)  

[![](http://i.linuxtoy.org/images/2008/12/11.png)](http://i.linuxtoy.org/images/2008/12/11.png)  

[![](http://i.linuxtoy.org/images/2008/12/12.png)](http://i.linuxtoy.org/images/2008/12/12.png)  

[![](http://i.linuxtoy.org/images/2008/12/13.png)](http://i.linuxtoy.org/images/2008/12/13.png)  

[![](http://i.linuxtoy.org/images/2008/12/14.png)](http://i.linuxtoy.org/images/2008/12/14.png)  

[![](http://i.linuxtoy.org/images/2008/12/15.png)](http://i.linuxtoy.org/images/2008/12/15.png)  

[![](http://i.linuxtoy.org/images/2008/12/16.png)](http://i.linuxtoy.org/images/2008/12/16.png)  

[![](http://i.linuxtoy.org/images/2008/12/17.png)](http://i.linuxtoy.org/images/2008/12/17.png)  

[![](http://i.linuxtoy.org/images/2008/12/18.png)](http://i.linuxtoy.org/images/2008/12/18.png)  

[![](http://i.linuxtoy.org/images/2008/12/19.png)](http://i.linuxtoy.org/images/2008/12/19.png)

**结论：**  
在 Bonnie++，IOzone, 和 Flexible IO Tester 三个纯理论性能测试软件中
EXT4 取得了八项测试中五项第一，XFS
取得了剩余三项的第一名。除非你的工作就是测试文件系统的理论性能，这个结果并不能说明太多。

在 Nexuiz，World of Padman，和 Unreal Tournament 2004
这三个游戏的测试中，四个文件系统的表现十分相近，这意味着迁移文件系统到
EXT4 或者 XFS 上并不能获得更高的游戏运行帧速。

文件压缩测试中，EXT4 和 XFS
一起分享了头把交椅，没有给其他文件系统一点空间。

而在多媒体编码测试中，四个文件系统各有胜负，这意味着高清爱好者们并不需要立刻切换到新的文件系统上，老的
EXT3 依然不错。这一点同样体现在加密测试中，EXT3 摘得 GnuPG
加密测试冠军，而 EXT4 则占据 Bork 加密测试的性能表现宝座。

尽管在实际效能测试中 EXT4
并没有带来如在纯理论测试中那么大的性能提升，但是迁移到 EXT4
文件系统并不是完全没有好处的。EXT４
文件系统相比它的前任提升了分区容量上限，增加了可允许的子目录数，并且增加了热碎片整理和日志校验码的功能。最重要的是，这些新功能的引进并没有对稳定性带来影响，它一如既往的安全高效。作为一个在
[Btrfs](http://en.wikipedia.org/wiki/Btrfs)
获得广泛应用之前的过渡品，EXT4 值得你考虑。

**再次注意：**[英文原文地址](http://www.phoronix.com/scan.php?page=article&item=ext4_benchmarks&num=1)
