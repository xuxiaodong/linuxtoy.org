Title: LLVM 3.3 发布
Date: 2013-06-18 17:34
Author: lovenemesis
Category: Development
Tags: LLVM
Slug: llvm-3-3-release

编译器族 LLVM 发布 3.3 版本，带来了 64 位 ARM 支持和完整 C++'11 支持。

如果您还不知道或不清楚 LLVM
究竟是什么，[点击此在线阅读开源应用程序框架对应章节](http://www.aosabook.org/en/llvm.html)。

本次发布新功能有：

-   增加对 AArch64 和 AMD R600 系列 GPU 架构以及 IBM S390
    的支持，并改善了对 PowerPC 和 MIPS 的支持。
-   自动向量器得到改善，并应用了新的 SPL 向量器，默认优化级别为 3 。
-   C/C++ 前端实现了完整 C++ 11 支持。

[源代码下载](http://llvm.org/releases/download.html#3.3)

目前 LLVM 3.3 及其 GCC 用优化器族 DragonEgg 已经现身 Fedora 19。

[官方发布公告](http://lists.cs.uiuc.edu/pipermail/llvm-announce/2013-June/000046.html)
