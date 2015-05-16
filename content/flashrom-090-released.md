Title: Flashrom 0.9.0 发布
Date: 2009-05-06 18:01
Author: toy
Category: News
Tags: Flashrom
Slug: flashrom-090-released

[BIOS 刷写工具 Flashrom](http://linuxtoy.org/archives/flashrom.html)
于近日发布了 0.9.0 版本，该版本为大家带来了以下亮点：

* Parallel, LPC, FWH and SPI flash interfaces.  
* 157 flash chip families and half a dozen variants of each family.  
* Flash chip package agnostic. DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32,
TSOP40 and more have all been verified to work.  
* 75 different chipsets, some with multiple flash controllers.  
* Special mainboard enabling code for dozens of nonstandard
mainboards.  
* No physical access needed. root access is sufficient.  
* No bootable floppy disk, bootable CD-ROM or other media needed.  
* No keyboard or monitor needed. Simply reflash remotely via SSH.  
* No instant reboot needed. Reflash your ROM in a running system,
verify it, be happy. The new firmware will be present next time you
boot.  
* Crossflashing and hotflashing is possible as long as the flash chips
are electrically and logically compatible (same protocol). Great for
recovery.  
* Scriptability. Reflash a whole pool of identical machines at the
same time from the command line. It is recommended to check flashrom
output and error codes.  
* Speed. flashrom is much faster than vendor flash tools.  
* Supports Linux, FreeBSD, DragonFly BSD, Solaris, Mac OS X.

参考其[发布公告](http://www.coreboot.org/pipermail/coreboot/2009-May/047636.html)可以了解详情。

[Flashrom](http://qa.coreboot.org/releases/)
