Title: Seagate Momentus XT 750 GB 混合硬盘
Date: 2012-06-06 23:26
Author: lovenemesis
Category: Gadget
Slug: seagate-momentus-xt-750-gb-hybrid-drive

羡慕超级本固态硬盘的快速启动，但又有大容量存储需求，那么希捷的这款混合式硬盘或许就是您
Linux 本本的好伙伴。

这块混合式硬盘有如下特点：

-   7200 转，32MB 缓存，SATA III 接口。
-   750G 机械硬盘 + 8GB 高速闪存。
-   内置**完全不依赖操作系统或上层驱动的优化引擎**，自动将最常用内容复制到闪存中加速读取和写入。
-   位于 8GB
    高速闪存中的内容依然在机械硬盘中有副本，不必担心闪存中的内容由于老化而丢失。
-   标准 2.5 寸硬盘体积，无论新旧机器兼容性良好。

[Seagate
官方介绍](http://www.seagate.com/internal-hard-drives/laptop-hard-drives/momentus-xt-hybrid/)

在经过本人在 Fedora 的本本上亲自测试后，证实它与 Linux
系统兼容良好，性能提升显著。

未进行任何特别优化，SELinux 开启，Fedora 16 i686 PAE 在希捷 Momentus
5400.6 500G 的**启动用时约 29s**：

[![](http://linuxtoy.org/img/2012/06/boot.png "boot")](http://linuxtoy.org/img/2012/06/boot.png)

未进行任何特别优化，SELinux 开启，Fedora 17 x86\_64 在换用 Momtntus XT
750G 的**启动用时约 12s**：

[![](http://linuxtoy.org/img/2012/06/boot-hybrid.png "boot-hybrid")](http://linuxtoy.org/img/2012/06/boot-hybrid.png)

如果对于固态硬盘的寿命不慎放心，或者有大容量数据保存需求，那么这个混合式硬盘的确是个值得您考虑的升级产品。

[亚马逊 500GB
版本](http://www.amazon.cn/Seagate-%E5%B8%8C%E6%8D%B7-2-5-500GB-7200%E8%BD%AC-32MB-SATA-3Gb-s-%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%A1%AC%E7%9B%98-ST95005620AS/dp/B003ZUX50Y/ref=sr_1_1?ie=UTF8&qid=1338995557&sr=8-1)（记得[升级固件](http://knowledge.seagate.com/articles/en_US/FAQ/215451en)获得写入加速支持）

[Amazon 750G 版本](http://amzn.com/B00691WMJG)

**PS：**最近 [Ars Technica
上关于固态硬盘的深入解析文章](http://arstechnica.com/information-technology/2012/06/inside-the-ssd-revolution-how-solid-state-disks-really-work/)，值得推荐～
