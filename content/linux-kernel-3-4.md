Title: Linux Kernel 3.4
Date: 2012-05-21 11:21
Author: lovenemesis
Category: Kernel
Slug: linux-kernel-3-4

Linux 内核 3.4 版本发布。

新内核带来了如下改善：

-   新增 btrfs-restore
    工具，允许从受损文件系统中提取数据并保存至其他安全位置，不执行修复操作。
-   允许在 btrfs 文件系统下使用大于 4kb 的元数据块。
-   改善了 btrfs 文件系统和 Linux
    页缓存的交互，并降低了内存消耗，大幅度提升了元数据操作性能。
-   增加了对 Nvidia GeForce 600 'Kepler'，AMD RadeonHD 7xxx 和 Trinity
    APU 以及 Intel Medfield GMA500 的支持。
-   增加 **X32 ABI**，在 64 位模式下提供 32 位的
    Pointer，允许对内存容量要求不高的程序在享受 64
    位带来的更多寄存器的同时避免 64 位 Pointer 带来的额外内存开销。
-   **X86 CPU 驱动自动检测**，允许按照 CPUID 功能位按需加载对应模块。
-   device-mapper
    增加检验启动路径，允许在启动过程中校验目标引导系统块设备的完整性。
-   perf 工作增加 gtk2 图形化前端，使用 `perf report --gtk` 启动。
-   增加名为 Yama 的安全模块。
-   增加对 QNX6 文件系统的只读支持。

[完整英文更新日志](http://kernelnewbies.org/Linux_3.4)
