Title: M$ 将在 ARM 设备上禁止关闭 UEFI 安全引导
Date: 2012-01-14 10:52
Author: lovenemesis
Category: Embedded
Tags: arm, ms, uefi
Slug: ms-forbids-disabling-uefi-secure-boot-on-arm

根据各方面情况的报道，M$ 将不允许在 ARM 设备上关闭 UEFI
安全引导，意味着预装 Win8 的 ARM 设备将无法引导其他任何系统。

不久前 Red Hat 联合 Linux 基金会对 X86 设备上 UEFI 对于 Linux
系统影响做了[初步评估](http://linuxtoy.org/archives/uefi-secure-boot-impact-on-linux-white-paper.html)，结果显示影响不如先前公众预期的那么大。但是在
ARM 领域的情况却丝毫不乐观。

在最近公布的 Win8
[硬件认证需求文档](http://msdn.microsoft.com/library/windows/hardware/hh748188)第
116 页中明确写到：**不允许任何在 ARM 系统上禁用安全引导的操作**。

这意味着**任何预装有 Win8 系统的 ARM 设备将只能引导 M$
签名的系统镜像，用户将完全无法自行安装包括 Linux
在内的其他任何操作系统。**

[SoftwareFreedom
博客上](http://www.softwarefreedom.org/blog/2012/jan/12/microsoft-confirms-UEFI-fears-locks-down-ARM/)列举了
M$ 决定施行该策略的三点可能原因：

-   在 ARM 领域 M$ 有着和 X86 PC 领域不同的硬件合作商，所以无需在意
    Intel 在 UEFI 论坛上提出的“允许用户关闭安全引导”的建议。
-   在 ARM 领域 M$ 并没有老版本的 Win 系统需要支持，于是将用户锁死在
    Win8 对于既有客户群体毫无影响。
-   在 ARM 领域 M$ 并没有取得足够的市场占有率引起反垄断制裁。

在过去的 2011 年里，已经有不少 Android ARM
手机厂商允许用户解锁手机及安装第三方系统，比如 [Sony
Ericsson](http://developer.sonyericsson.com/wp/2011/03/29/unlocking-the-boot-loader-in-the-new-xperia%e2%84%a2-smartphones/)
和 [HTC](http://www.facebook.com/HTC/posts/10150307320018084)。然而 M$
在 2012 年伊始的举动显然是为所有非 Win 系统在 ARM
领域的发展蒙上了一层阴影。

本站将持续追踪此事件的发展。

*资料来源：*[ReadWriteWeb](http://www.readwriteweb.com/enterprise/2012/01/microsoft-says-no-to-disabling.php)
