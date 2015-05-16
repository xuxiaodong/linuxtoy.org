Title: Fedora 18 可能支持 UEFI Secure Boot
Date: 2012-06-06 00:48
Author: lovenemesis
Category: Featured
Tags: Fedora, uefi
Slug: fedora-18-might-supports-uefi-secure-boot

[Matthew Garrett
在博客](http://mjg59.dreamwidth.org/12368.html)上阐述了最近关于 Fedora
18 在 UEFI 支持方面的一些动向，表示 Fedora **有可能**会采取支付 $99
的方式获得 M$ 签名的第一阶段引导器，从而允许最终用户在不关闭 Secure
Boot 的情况下引导。

今年下半年发布的 Win8 将要求 UEFI 中启用 Secure Boot
模式，届时**所有带有的 Win8 认证徽标的硬件也将包含一组 M$
公钥，不局限于 OEM**。这将给包括 Fedora 在内的所有[Linux
发行版的安装带来不小的麻烦](http://linuxtoy.org/archives/uefi-secure-boot-impact-on-linux-white-paper.html)。怎么办呢？

一个直接的解决方法是和厂商合作在硬件中添加特定 Linux
发行版的公钥。这对于有 Red Hat 支持的 Fedora
来说并不是件难事，但是这样子做的话对其他没有长期硬件合作关系的发行版诸如
Arch、Gentoo、Mint
等是不公平的。同时由于难以让所有的硬件厂商都包含该公钥，又会无形的增加消费者选购
Linux 兼容硬件产品时的麻烦。

另一个方法是创建一个通用的 Linux
公钥。这意味着需要有一个可靠的组织掌管所有的 Linux
发行版密钥石，并且对签名请求进行必要的审核工作。这花费巨大，在短期内也是不现实的。

第三个方案，尽管不理想，但在目前看来是可行的。M$ 将在它的 [Sysdev
Portal](http://sysdev.microsoft.com/) 上提供付费的签名服务。在支付给
Verisign $99 并审核通过之后，将使用 M$
的密钥进行签名，不限次数，使得其可以在具备 M$ 公钥的设备上运行。Fedora
打算将利用此对一个**特制的初始阶段引导器进行签名**，从而使得**最终用户无需进入
UEFI 做任何更改即可顺利引导并安装 Fedora 18**。

这种便利，除了那 $99 以外，**还有其他代价的**。

会被用来签名的[初始阶段引导器](https://github.com/mjg59/shim)将设计的十分简单，仅仅用来链式引导真正的
GRBU2 引导器，从而避免每次引导器升级的都要找 M$
机器签名的麻烦。不过由于 UEFI Secure Boot 的要求，**GRUB2
的动态加载和部分内核参数编辑功能将被禁用**。

同样是由于 UEFI Secure Boot
的要求，所有可能会用到内核模块也需要签名。对于 Fedora
分发的内核树中模块自然是没有问题的，但是**对于像 AMD 和 NVIDIA
之类安装时动态编译内核模块的闭源显卡驱动来说则极为麻烦**。

需要自己编译内核的用户，则不得不使用 Fedora
提供的工具和文档，生成自己的公钥并将其添加到 UEFI
固件中，然后**对编译的内核和引导器重新签名**。若希望他人也能使用自定义的内核，则不得不像
Fedora 一样**花费 $99 使用 M$ 的签名服务**。

另一方面，M$ 对于在 ARM 平台上 UEFI Secure Boot
策略没有改变，意味着[预装 Win8 ARM 的设备将不能关闭 Secure Boot
模式](http://linuxtoy.org/archives/ms-forbids-disabling-uefi-secure-boot-on-arm.html)，也不能自己添加公钥。虽然理论上
Fedora 也可以像 X86 一样付费获得 ARM 版本的 M$
签名认证，但是这样一个丝毫不允许内核级别自定义的 Fedora ARM
意义甚微，故放弃。

**受不了这些限制和麻烦？**

没问题，**只要关闭 UEFI 的 Secure Boot
模式一切就和当下一样了**，但这将意味着**无法启动 Win8
系统，包括已经安装的**，双启动成为过去时。

无论有没有世界末日，M$ 都会在 2012 年底逼迫最终用户在 Win8 和全功能的
Linux 系统之间“做一个艰难的决定”。

值得注意的是，**Fedora 的这项方案目前处于讨论阶段**，尚不清楚 M$
方面对此会有什么样的反应。

**名为安全，实为垄断**

UEFI Secure Boot 带来这么多麻烦，那么它到底能起到什么作用呢？

它无法让您正在运行的系统更健壮，也无法抵御病毒对引导器的修改。**它唯一能做的就是当机器的引导器已经被病毒修改之后，给出提醒并拒绝启动，避免可能带来的进一步损失。**

没错，只有这些。没有办法恢复原先的引导器，没有办法动态加载任何杀毒或者数据挽救模块。或许届时您可以选择拨打
M$ 或厂商的客服获得解决方案，或者也可以选择购买必然会出现的某些经过 M$
认证的特制修复引导盘。介于 $99 的存在，这些恐怕都不会是免费的。

难道这是 M$ 想要的效果？

-   场景：当 UEFI
    提示引导器被修改，拒绝引导系统时，机器停滞在错误屏幕上，面对一切尝试修复的举动毫无反应……
-   用户：“我都不知道该用什么表情来面对了……”
-   M$：“微笑就可以了。”

文明用语!!!!

或许，是时候考虑加入 [Free Software 基金会发起的反对 Secure Boot
的签名活动](http://www.fsf.org/campaigns/secure-boot-vs-restricted-boot/)了。

**补充说明**

根据 M$ 的规定，Win8 仅能在 UEFI Secure Boot 开启时引导。**已经安装好的
Win8 系统在关闭 UEFI Secure Boot 之后也不能引导**。

Secure Boot 要求所有需要访问 PCI
地址的行为都要经过签名，而它的格式限制了一个程序或设备仅能被具有单一签名。这对于硬件厂商意味着什么？

-   若是**板卡和驱动所用签名并未包含在主板的 UEFI Secure Boot
    公钥库中，用户将无法使用该板卡**。
-   唯一能保证板卡和驱动被广泛使用的方法就是像 Fedora 一样使用 M$
    的付费签名服务，因为预期只有 M$ 的公钥会被包含在绝大多数主板中。

从目前公布的内容来看，**并不清楚 UEFI 中的 SB
是否是一个可以任意开关的选项**：

It shall be possible for a physically present user to use the Custom
Mode firmware setup option to modify the contents of the Secure Boot
signature databases and the PK.  
If the user ends up deleting the PK then, upon exiting the Custom Mode
firmware setup, the system will be operating in Setup Mode with Secure
Boot turned off.  
The firmware setup shall indicate if Secure Boot is turned on, and if
it is operated in Standard or Custom Mode. The firmware setup must
provide an option to return from Custom to Standard Mode which restores
the factory defaults.

“仅能通过删除 PK 的方式关闭 Secure
Boot”，“仅能通过恢复出厂设置的方式开启 Secure Boot”，这种操作也是符合
M$
规范的。过往的经验表明厂商倾向于给固件中最精简的功能，这很可能是他们会选择的方式。

“破解 ROM ”拯救世界？醒醒吧，亲……

-   是 M$ 限制了 Win8 不可以在 Secure Boot
    关闭情况下启动，不是主板厂商。
-   主板固件的开发难度可不一般，从
    [OpenBIOS](http://www.openfirmware.info/Welcome_to_OpenBIOS)
    的缓慢发展可见一斑。

*小贴士：*尽管常常混用，实际上固件和 ROM
可是两个完全不同的东西哦～固件负责的是最底层的硬件沟通，常见的 Android
自定义 ROM 中也仅仅是重用了从厂商官方 ROM 提取的固件而已。

*消息来源：*[Ars
Technica](http://arstechnica.com/information-technology/2012/06/fedora-could-seek-microsoft-code-signing-to-contend-with-secure-boot/)
