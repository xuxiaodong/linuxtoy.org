Title: LLVM 3.0
Date: 2011-11-30 10:35
Author: lovenemesis
Category: Development
Tags: LLVM
Slug: llvm-30

编译器族 LLVM 3.0 即将发布，带来众多改善。

如果您还不知道或不清楚 LLVM
究竟是什么，[点击此在线阅读开源应用程序框架对应章节](http://www.aosabook.org/en/llvm.html)。

**Clang C/C++ 编译器更新**

-   改善编译程序的稳定性，提升对于 C++0x (C++ 2011) 标准的支持。
-   增加了对部分 C1x 中功能的支持。
-   改善对于 Objective-C 的支持。

**DragonEgg 插件更新**

-   可以用来直接取代 GCC 4.6 中的优化器。
-   **不再需要特殊打过补丁的 GCC，使用主线中的 GCC 4.5/4.6 即可**。
-   试验性的 **LLVM 优化器和 GCC 优化器共存**选项。
-   提供对于 C, C++, Fortran, 和 AD 语言的完整支持，以及对 Java,
    Objective-C, Objective-C++, 和 Google Go 的部分支持。

此外，还引入了对 **x86 AVX 指令集（在 AMD Bulldozer 和 Intel Sandy
Bridge 引入）**的支持，并且大幅度提升 **ARM Cortex-A9 NEON
指令集**的性能。

[官方发布日志](http://llvm.org/docs/ReleaseNotes.html)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTAyMDk)
