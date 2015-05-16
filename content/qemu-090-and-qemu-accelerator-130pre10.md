Title: QEMU 0.9.0 & QEMU Accelerator 1.3.0pre10
Date: 2007-02-06 18:05
Author: toy
Category: Apps
Slug: qemu-090-and-qemu-accelerator-130pre10

[QEMU](http://fabrice.bellard.free.fr/qemu/)
这个开源的虚拟机应用程序在昨天放出了新的 0.9.0 版，同时，QEMU
的加速模块（KQEMU）也更新到了 1.3.0pre10。令人高兴的是，这次 KQEMU 采用
GPL version 2 许可发布了全部的源代码。

其中，QEMU 的主要更新包括：

> - Support for relative paths in backing files for disk images  
>  - Async file I/O API  
>  - New qcow2 disk image format  
>  - Support of multiple VM snapshots  
>  - Linux: specific host CDROM and floppy support  
>  - SMM support  
>  - Moved PCI init, MP table init and ACPI table init to Bochs BIOS  
>  - Support for MIPS32 Release 2 instruction set (Thiemo Seufer)  
>  - MIPS Malta system emulation (Aurelien Jarno, Stefan Weil)  
>  - Darwin userspace emulation (Pierre d'Herbemont)  
>  - m68k user support (Paul Brook)  
>  - several x86 and x86\_64 emulation fixes  
>  - Mouse relative offset VNC extension (Anthony Liguori)  
>  - PXE boot support (Anthony Liguori)  
>  - '-daemonize' option (Anthony Liguori)

而 KQEMU 的新版本则支持 x86\_64 的完全虚拟化了。

Download [QEMU 0.9.0 & KQEMU
1.3.0pre10](http://fabrice.bellard.free.fr/qemu/download.html)
