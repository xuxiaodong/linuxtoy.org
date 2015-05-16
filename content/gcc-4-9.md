Title: GCC 4.9
Date: 2014-04-23 13:49
Author: lovenemesis
Category: Development
Tags: GCC
Slug: gcc-4-9

GNU 编译器集合 GCC 4.9 发布，带来了 OpenMP 4.0 支持和大量 ARM
支持的改善。

更新亮点有：

-   最新的 OpenMP 4.0 支持。
-   大幅度改善了连接时优化(LTO)，以编译打开 Debug 的 Firefox
    为例，内存需求从 15G 下降到 3.5G，连接用时从 1700 秒减少到 350 秒。
-   支持输出彩色的诊断信息。
-   大量 ISO C11 更新。
-   初步实现了部分 C++14 功能。
-   完整实现 Google Go 1.2.1 版本。
-   大量针对 ARM 架构的改善，包括针对 Cortex-A57 和 Cortex-A53
    的调优和初步 big.LITTLE 支持，优化对 64 位 ARM 的支持等。
-   Intel AVX-512 支持，代号 Silvermont 和 Broadwell 的新处理器支持。
-   `march=generic` 将主要针对 Core 和 Bulldozer 核心架构优化。
-   增加针对 AMD 新的 Excavator 核心的调优选项。
-   支持 Power ISA 2.07，增加针对新的 Power8 处理器的调优选项。

[官方发布公告](http://gcc.gnu.org/gcc-4.9/changes.html)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTY3MDE)
