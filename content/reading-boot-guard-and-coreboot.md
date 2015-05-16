Title: 阅读：Boot Guard 与 Coreboot
Date: 2015-02-17 13:03
Author: lovenemesis
Category: We reading
Tags: bootguard, coreboot
Slug: reading-boot-guard-and-coreboot

[Coreboot](http://www.coreboot.org/) 作为得到 FSF 青睐的开源 BIOS
方案，已经随着 Chromebook
的发布成长了不少。不过若是您想要在新近购买、搭载 Intel Broadwell
处理器上的~~壕~~笔记本使用 Coreboot　的话，死了这条心吧……

由于各方面的限制，在市场上找到一块兼容主流 CPU 且[被 Coreboot
支持的桌面级主板](http://www.coreboot.org/Supported\_Motherboards)相当困难，[支持的笔记本](http://www.coreboot.org/Laptop)则更少了。而这个问题很可能会随着
Broadwell 处理器的铺开变得更加严峻。

近日[PCWorld](http://www.pcworld.com/article/2883903/how-intel-and-pc-makers-prevent-you-from-modifying-your-pcs-firmware.html)发布了一篇文章，简单介绍了
Intel　在 Broadwell　处理器上引入的名为[ Boot
Guard](http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/4th-gen-core-family-mobile-brief.pdf)　的技术。

简单来说，该技术允许 OEM 厂商将使用非对称密钥签名的**公钥部分烧入
CPU**，这样意味着**未经厂商签名的 BIOS 固件**将会被 CPU 拒绝执行。

根据 Intel
方面的表示，这些技术主要是为了避免黑客通过修改固件的方式，绕过 UEFI
固件中 Secure Boot 的安全保护。不过从技术上来讲，Boot Guard
提供了两种模式：

* Verified Boot 模式下会验证固件签名，且将完全拒绝未通过验证固件的运行  
* Measured Boot 模式下将启动过程的信息记录到 TPM（可信任平台模组）
中，交由操作系统去做后续进一步处理。

和 Secure Boot 模式状态可以由用户翻遍 UEFI 后再禁掉不同，Boot Guard
的模式是由 OEM 在出厂前决定的。而**几乎所有的笔记本厂商在搭载
Broadwell 笔记本出厂前都将 Boot Guard
设为了第一种模式**，在带来安全性的一定提升，与 Coreboot
等第三方固件永别了。

当年对 Secure Boot 开炮且实现 Linux 支持的 Matthew Garrett
在[自己的博客上再次开轰](http://mjg59.dreamwidth.org/33981.html)，认为
Intel 引入的 Boot Guard
技术在某种程度上可以说是逼迫厂商在安全与自由之间做抉择，结果是消费者的选择自由以“大多数的安全”名义被剥对了。他认为，对于整个行业来讲，引入一项新技术时应同时考虑安全与自由，而非对立起来。

如同[某个在 Phoronix
读者评论](http://www.phoronix.com/forums/showthread.php?113937-Thoughts-On-Intel-Boot-Guard-Impairing-Coreboot&p=471525#post471525)中所说的，安全关乎的是谁掌握着钥匙。**如果您被安全的门紧紧保护起来了，但是却没有钥匙，那恐怕只能是监狱。**

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Intel-Boot-Guard-MJG)
