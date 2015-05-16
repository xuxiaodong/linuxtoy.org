Title: GRUB 2.00
Date: 2012-06-28 13:17
Author: lovenemesis
Category: Development
Tags: GRUB
Slug: grub-2-00

经过十年多的开发，GNU 通用 引导器 GRUB 发布 2.00 版本。

部分新功能包括：

-   支持通过显示器 EDID 信息读取视频模式设定。
-   新的 EHCI / AHCI / ESCC 序列 / EFI 驱动。
-   新的文件系统和磁盘类型支持，包括 ExFAT, LZOP, Squash4 和 RomFS 等。
-   支持引导 FreeDOS 和 Plan9。
-   支持在使用 [Coreboot](http://www.coreboot.org/Welcome_to_coreboot)
    的设备上引导。
-   支持 Windows 的 Ntldr/bootmgr，PXE 链式引导和 Darwin 11 (Mac OS X
    10.7 - Lion) 的引导协议。

[完整 GRUB2
发布日志](http://lists.gnu.org/archive/html/grub-devel/2012-06/msg00093.html)

值得注意的是 [Canonical 将不会在 Ubuntu 12.10 中使用 GRUB2 实现
SecureBoot
下的引导](http://www.phoronix.com/scan.php?page=news_item&px=MTEyNDY)，原因是担心其
GPLv3 协议会要求其公开私钥。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTEyODc)
