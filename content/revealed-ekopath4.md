Title: 揭晓：EKOPath 4
Date: 2011-06-14 23:22
Author: lovenemesis
Category: Development
Tags: ekopath4
Slug: revealed-ekopath4

前几天[对于 Dirndl
的竞猜](http://linuxtoy.org/archives/guess-what-is-dirndl.html)结果由
Phoronix 公布了，是 EKOPath 4 编译器族。

根据[新闻公告](http://www.pathscale.com/ekopath4-open-source-announcement)，EKOPath
4 是一款适**用于 Intel 64 和 AMD 的 C, C++ 和 Fortran
的高性能编译器组**，本次将以 GPL v3 协议开源免费分发，提供
Linux、FreeBSD 和 Solaris 版本二进制和源代码下载。

同时**依照 GPL v2 开源的还有 PathDB 调试器**。

此外，在今年三月 PathScale 还**依据 BSD 协议开源了 libcxxrt C++
运行库**。

但是，其**适用于 CUDA 计算的 ENZO 以及 Boost 库 EKOPath Boost
依然是闭源且需要付费使用**的。

**PS：**

那么这个 EKOPath 4 会取代 GCC 目前在 Linux
系统中的地位么？个人认为在可见的将来不会，理由如下：

1.  **社区的成长需要时间和空间**，尽管开源了，但是 EKOPath
    的发展还是牢牢掌控在 PathScale 手中的。
2.  对于**一般程序使用 EKOPath 4 编译不会带来显著性能提升**。
3.  **尚未能完全编译 Linux 桌面发行版中的所有组件**，Linux
    内核也需要一个小补丁。
4.  **GCC 并不是停滞不前**的，可以借助这个机会互相学习，比如在 OpenMP
    方面。

同样，如果乐观的话在 2011 冬季就会出现一部分专门用 EKOPath4
定制的发行版，侧重于高性能计算领域；而 2012 冬季的主流发行版可能就会收录
EKOPath 4 编译器和 PathDB 调试器，如同现在 LLVM
一样作为另一个编译器选择存在。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=article&item=pathscale_ekopath4_open#=1)
