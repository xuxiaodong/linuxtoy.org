Title: Fedora 16 安装前指南
Date: 2011-11-08 00:00
Author: lovenemesis
Category: Tutorials
Tags: Fedora, pre-installation
Slug: fedora-16-pre-installed-notes

和以往的 Fedora 版本一样，即将发布代号为 Verne 的 Fedora 16
也带来了大量变化，本文将摘取其中一些做简单介绍，方便您尽快适应变化，不局限于
Fedora 哦～

**GPT 及安装**

从 Fedora 16 开始，将**在全新的硬盘上默认使用 [GPT (GUID Partition
Table)](http://en.wikipedia.org/wiki/GUID_Partition_Table)
分区表**。简单的来说，GPT
是取代只允许四个主分区（或三个主分区一个扩展分区）的 MBR(Master Boot
Record) 分区表的新分区表格式，最早有 Intel 提出作为 EFI （BIOS
替代品，常见于各类 Intel Mac）的一部分，并且成为现在 UEFI 的一部分。

同时 Fedora 16 LiveCD 的 Anaconda
只具备将文件系统复制到目标主机的能力，于是很自然的意味着通过 LiveCD
的安装要求目标磁盘使用 GPT 分区表，使用 DVD （亦可用 [Fedora LiveUSB
Creator](https://fedorahosted.org/liveusb-creator/) )则无这些限制。

用 LiveCD 在使用 BIOS 的机器上安装时由于 GPT 的要求将需要创建一个大小为
1M 的 BIOS
分区，自动分区模式默认创建，手动分区模式若不创建的话无法继续。

目前 M$ 的 XP(64bit)/Vista/2008/7 在 BIOS 上仅有使用 GPT
分布表的硬盘做为数据盘的能力，没有引导 GPT
分区表硬盘的作为系统盘的能力。

目前 GRUB2 在 EFI（常见于 Intel Mac，注意和 UEFI 区分）上有 Bug，所以
**Fedora 16 在 EFI 的设备上依然使用来自 Intel 的 GRUB-EFI** 。

以上几点加起来，意味着：

-   **LiveCD 安装仅适用于单独安装或者或后来安装支持 GRUB2+GPT 的 Linux
    发行版（比如 Ubuntu），不适合与其他依然基于 GRUB+MBR 的 Linux
    发行版或 M$ 系统共存。**
-   **若是依然想使用 LiveCD 在为 MBR 分区表的硬盘上覆盖安装老版本 Fedora
    或与已有支持 GRUB2+GPT 的 Linux 发行版（比如
    Ubuntu）共存，可以尝试使用 [GPT fdisk 将 MBR 无损转换成
    GPT](http://www.rodsbooks.com/gdisk/mbr2gpt.html)（未亲自尝试，风险自担）**
-   **如果机器上有其他 GRUB+MBR Linux 发行版或 M$
    系统，亦或准备后来安装这些系统，请使用 DVD 或依据它生成的
    [LiveUSB](https://fedorahosted.org/liveusb-creator/)。**

*参考来源：*[Bugzilla](https://bugzilla.redhat.com/show_bug.cgi?id=704244)
[MSDN](http://msdn.microsoft.com/en-us/windows/hardware/gg463525)

**GRUB2 默认引导内核**

GRUB2 与 GRUB 单点配置文件的方式不同，它通过读取类似 udev/systmed
风格的一系列预制配置文件模板外加 `/etc/default/grub`
自定义变量文件，然后用 grub2 工具生成最后的配置文件
`/boot/grub2/grub.cfg`（**强烈建议不要手动编辑该文件**）。

由于无法确定每次调用 grub2-mkconfig
后生成菜单的顺序，所以指定默认的引导内核会稍微复杂些：

1.  编辑 `/etc/default/grub` 文件，添加 `GRUB_DEFAULT=saved` 变量；
2.  运行 `grub2-mkconfig -o /boot/grub2/grub.cfg` 来刷新配置文件；
3.  使用 `grub2-set-default ` 的方式来指定默认引导内核；

如果要查询当前设置的话，使用 `grub2-editenv list` 既可。

**PS:**现在每个内核都生成对应的 Recovery Mode 引导选项。

*参考来源：*[Fedora Wiki](https://fedoraproject.org/wiki/Grub2)

**Radeon 开源驱动 HDMI 音频输出**

开源 Radeon 驱动的 HDMI 音频输出支持在 Linux Kernel 3.0
开始被默认禁用了，所以在 Fedora 16 默认的 Linux Kernel 3.1
内核下需要手动添加内核参数引导打开

和上面操作 GRUB2 的方式类似：

编辑 `/etc/default/grub` 文件，

这次为已有的变量增加一个值 `radeon.audio=1`，例如：

    GRUB_CMDLINE_LINUX="quiet rhgb radeon.audio=1"

之后运行 `grub2-mkconfig -o /boot/grub2/grub.cfg` 重新生成配置文件即可。

根据报道，目前的 HDMI
音频输出是逆向工程出来的，存在可能导致显示器黑屏的兼容性问题，故禁用。新的
AMD 官方的开源实现方案正在 IP 审核中，完成后将推送至内核。

注意**使用 AMD Catalyst
闭源驱动的朋友无须设置此项**。另外期待有朋友补上可用的 NVIDIA HDMI
音频输出的设置……

*参考来源：*[Phoronix](%20http://phoronix.com/forums/showthread.php?62635-No-HDMI-sound-after-upgrade-to-Kubuntu-11.10-with-my-hd4770)

**简体中文配置**

Red Hat 国际化组对Fedora系统中的字体进行了大量的改进，根据bug
reports和用户反馈，特将常见的问题和解决方案在下面列出:

以前 `~/.fonts.conf` 的美化方案不再适用， 请将个人用户目录下的
`~/.fonts.conf`
重命名，然后以简体中文重新登陆系统，看看系统默认的中文字体是否美观耐用。

简体中文字体的**位图字体和反锯齿字体的切换**：

-   `su -c 'zenheiset aa'` 切换到反锯齿字体
-   `su -c 'zenheiset bitmap'` 切换到位图字体

如果您**偏好英文界面同时使用简体中文**，请将以下环境变量加入到
`~/.bash_profile`:

    export PANGO_LANGUAGE=en:zh_CN

**PS:** 这部分以 GNOME 为主，KDE 的情况尚待补充，不过根据这个 [QT
Bug](https://bugreports.qt.nokia.com//browse/QTBUG-716)
来看似乎也没有完整支持 `~/.fonts.conf` 的美化。

*参考来源：*[邮件列表](http://lists.fedoraproject.org/pipermail/chinese/2011-November/008329.html)
