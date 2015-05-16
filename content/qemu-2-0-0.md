Title: QEMU 2.0.0
Date: 2014-04-18 11:02
Author: lovenemesis
Category: Virtual Machine
Tags: Qemu
Slug: qemu-2-0-0

开源的虚拟及模拟工具 QEMU 发布 2.0.0 版本，增加了在 ARM 64 位支持。

部分更新要点有：

-   支持 64 位 ARM 处理器，支持全部 ARMv8 指令集，除了可选的 CRC
    和加密指令集。
-   支持全志 A10 的开发板。
-   支持 Q35 x86 的 CPU 热拔插。
-   提升执行大量浮点运算或 SIMD 指令时 Win 客户机的性能。
-   支持在线快照合并，virtio-rng 热拔插，直接 NFSv3 访问等小改善。

[官方发布公告](http://article.gmane.org/gmane.comp.emulators.qemu/267615)

*消息来源：*[LWN](http://lwn.net/Articles/595301/rss)
