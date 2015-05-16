Title: Mozilla IonMonkey
Date: 2012-09-13 15:53
Author: lovenemesis
Category: Web Browser
Tags: Firefox, javascript, jit, Mozilla
Slug: mozilla-ionmonkey

Mozilla 的猴子家族迎来新成员，开发人员宣布为长时运行 JavaScript
程序设计的 JIT(即时编译) 解析器 IonMonkey 初步完成。

[Mozilla 开发人员 David Anderson
在博客中](https://blog.mozilla.org/javascript/2012/09/12/ionmonkey-in-firefox-18/)表示Firefox
的 JavaScript 引擎 SpiderMonkey 一直以来所用的 JIT 技术（包括老的
TraceMonkey 和新的 JagarMonkey）都是直接将 JavaScript 翻译成机器码。相比
C++ 或者 Java 等生产环境编译器，这都缺失了一个全局性优化的环节。

新开发的 IonMonkey 则引入了一个中间层，其工作流程如下（LLVM 附体？）：

1.  将 JavaScript 翻译成中间表示层 IR（intermediate representation）
2.  使用各种算法对 IR 进行优化。
3.  将优化过的 IR 翻译成机器码。

特别值得一提的是，IonMonkey
在设计之初已经充分考虑了平台抽象化，现在**已经实现对 x86, x86\_64 和 ARM
指令集的支持**。

David Anderson
会在接下来的博客中详细描述在第二步中应用的优化算法，感兴趣的朋友可以跟进。目前有：

-   Loop-Invariant Code Motion (LICM) 循环外无用代码移除。
-   Sparse Global Value Numbering (GVN) 冗余代码移除。
-   Linear Scan Register Allocation (LSRA) 寄存器分配规划，也被用于
    HotSpot JVM 和 LLVM 中。
-   Dead Code Elimination (DCE) 无用指令移除
-   Range Analysis 范围分析，移除不必要的边界检测

显而易见的这些优化需要付出一定的时间代价的，所以**仅在长时运行的
JavaScript 中应用**，短时的 JavaScript 的 JIT 任务依然还是交给
JagarMonkey 完成。

根据 [Mozilla 自己 Kraken
的测试](http://krakenbenchmark.mozilla.org/)，IonMonkey 带来了 26%
的性能提升。

目前 IonMonkey 已经应用于 [Firefox Nightly
版本](http://nightly.mozilla.org/)中，将随着 Firefox 18
的发布而投入广泛使用。Firefox 18 将在 11 月 20 日发布 Beta 版本。

*消息来源：*[Ars
Technia](http://arstechnica.com/information-technology/2012/09/mozilla-beefing-up-javascript-performance-with-new-jit-compiler/)
