Title: QEMU 0.9.1 发布
Date: 2008-01-08 10:18
Author: toy
Category: Apps
Slug: qemu-091-released

[QEMU](http://fabrice.bellard.free.fr/qemu/)
是一个开放源代码的虚拟机应用程序。最近，该软件发布了 0.9.1
版。新版本包括许多改进和增强，如支持从主机目录引导 TFTP、针对 Solaris 的
Tap 设备模拟、支持选择 CPU 模型、支持 MIPS 64 位 FPU、支持 Xscale PDA
模拟、支持 ColdFire 系统模拟、支持 MIPS64、支持只读 Parallels
磁盘映像、支持 SVM (x86) 虚拟、支持 CRIS 模拟等等。

![QEMU logo](http://i.linuxtoy.org/i/2008/01/qemu.png)

QEMU 0.9.1 的详细更改情况如下：

- TFTP booting from host directory (Anthony Liguori, Erwan Velu)  
- Tap device emulation for Solaris (Sittichai Palanisong)  
- Monitor multiplexing to several I/O channels (Jason Wessel)  
- ds1225y nvram support (Herve Poussineau)  
- CPU model selection support (J. Mayer, Paul Brook, Herve Poussineau)  
- Several Sparc fixes (Aurelien Jarno, Blue Swirl, Robert Reif)  
- MIPS 64-bit FPU support (Thiemo Seufer)  
- Xscale PDA emulation (Andrzej Zaborowski)  
- ColdFire system emulation (Paul Brook)  
- Improved SH4 support (Magnus Damm)  
- MIPS64 support (Aurelien Jarno, Thiemo Seufer)  
- Preliminary Alpha guest support (J. Mayer)  
- Read-only support for Parallels disk images (Alex Beregszaszi)  
- SVM (x86 virtualization) support (Alexander Graf)  
- CRIS emulation (Edgar E. Iglesias)  
- SPARC32PLUS execution support (Blue Swirl)  
- MIPS mipssim pseudo machine (Thiemo Seufer)  
- Strace for Linux userland emulation (Stuart Anderson, Thayne
Harbaugh)  
- OMAP310 MPU emulation plus Palm T|E machine (Andrzej Zaborowski)  
- ARM v6, v7, NEON SIMD and SMP emulation (Paul Brook/CodeSourcery)  
- Gumstix boards: connex and verdex emulation (Thorsten Zitterell)  
- Intel mainstone II board emulation (Armin Kuster)  
- VMware SVGA II graphics card support (Andrzej Zaborowski)

你可以从这里[下载 QEMU 0.9.1
的源代码及二进制包](http://fabrice.bellard.free.fr/qemu/download.html)。
