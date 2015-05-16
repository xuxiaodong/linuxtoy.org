Title: 开源界的大变化: LLVM Clang libc++ LLDB 
Date: 2010-06-12 19:22
Author: lovenemesis
Category: Featured
Tags: libcxx, lldb, LLVM
Slug: big-changes-llvm-clang-libcxx-lldb

近日， LLVM 项目和开发者 Chris Lattner 获得 [ACM 颁发的 SIGPLAN
软件系统奖](http://blog.llvm.org/2010/06/llvm-receives-first-ever-sigplan.html)，将这个由
Apple 主导的 BSD 系开源项目推到了开源界的焦点。**本文由 comicfans44
撰写**，介绍下 LLVM 项目中的两个新组件： libcxx 和 lldb 。

首先声明，**本文在除去技术上的相关介绍较为准确外，其他内容多为臆测，仅供参考**。

近期来，apple在llvm相关的项目上下了很大的力气，虽然大家对apple有褒有贬，不过这几个项目都是BSD风格的许可证，可算是为开源界的一次“革命”贡献了自己的力量。为什么说apple所做是“革命”呢？

**clang，基于llvm的C/C++/Objective C/C++编译器**

其目标是快速的编译、有效的内存使用、友好的IDE集成、集成静态语言分析、基于语意的补全...[前文有所介绍](http://linuxtoy.org/archives/llvm-and-clang.html)，不再赘述。前些时clang完成了[boost库的编译](http://www.boost.org/development/tests/release/developer/summary.html)
，向生产级别的C++编译器又迈进了一步 。

**libc++**

如同每个C++编译器套装都自带一份对应的C++标准库一样，clang 在可使用GNU
libstdc++作为标准库之后，开始了自己的C++标准库编写项目，这就是[libc++](http://libcxx.llvm.org)。

libc++以[C++0x](//www.open-std.org/jtc1/sc22/wg21/docs/papers/2010/n3092.pdf)
为目标，同样以BSD风格的llvm许可证发布，其特性及目标除了“编译/执行速度快”和“占用内存小”之外，还可在如异常对象、
RTTI（Runtime Type Identification
运行时类型识别）和内存分配等低级特性上与GCC的libstdc++保持 ABI兼容性。

其项目主页上说明了从头编写一个C++标准库的原因：

*以多年来的代码编写经验来看（包括曾实现过标准库），由于
C++0x中部分特性的加入（如右值引用）及不同电脑配置（如多核）的差异，为达到提升性能的目标可能需要打破与旧版之间的
ABI兼容性主线的GNU
libstdc++切换至GPLv3协议，而libc++（臆测应是也指clang）不能使用。仅能在
GPLv2授权的GNU libstdc++
4.2上继续开发0x标准库。与其fork代码后再修改，还不如从头开始写起。此外
GNU libstdc++ 与对应版本的
g++紧密绑定，不利于移植。STLPort和Apache的libcxx都已经停止开发，且缺少0x支持。且以开发者的经验（同样是GNU
libstdc++开发者的经验）而言，添加C++0x的支持（右值引用，move-only
语意）几乎需要修改每一个类和函数，还不如重写。*

目前libc++可在OSX i386/x86\_64上使用g++-4.2和clang工作

当前libc++完成了N3092草案中85%的实现和测试，C++98
已经完全达成，C++0x中缺失的主要部分是（用于优雅的获取子线程计算结果），
（正则表达式），和（大量实用的随机数生成器和分布生成器）

本以为libcxx已经完善了
apple的编译器替换计划（个人臆测...），没想到又出现了
**[LLDB](http://lldb.llvm.org) 基于LLVM的 debugger**

新一代高性能调试器，集成LLVM反编译器和Clang表达式解析器等高阶组件，用于C/C++
/Objective-C 程序的调试，同样以LLVM许可证发布。

同样，为何从头写一个debugger？  

因为当前的开源调试器仅在常见的C程序调试中可如预期般工作（臆测是说GDB吧...），而复杂的C++表达式解析、重载、模板、多线程等非传统调试场景中无法可靠工作。LLDB即是要提供更友好的调试体验，其目标是解决长期来困扰debugger的问题，令你考虑如何调试你的程序问题，而不是考虑debugger的不足。

从长远考虑，debugger不应重复开发其自己的C/C++解析器、类型系统、了解所有目标调用约定细节、实现自己的反汇编器。相信实用LLVM中已有的库，很多问题将迎刃而解，而
debugger则可将其注意力放在进程控制有效的符号读取、索引，线程管理等debugger专属的问题上。

**目标包括：**

-   基于库的设计，可由IDE、命令行程序或其他分析工具集成
-   基于python的脚本化，使用插件体系
-   良好的多线程调试支持
-   尽可能使用已有的编译器技术和相关库
-   良好支持C/C++/Objective-C

就clang、libcxx、lldb
都是首先在OSX上测试这点来说，我窃以为三个项目的主要推动者是apple（个人观点仅供参考），我对许可证相关内容并不了解，抛开这个问题而综合以上几个项目来看，apple是要重新定义开源界（起码是在OSX上）中最基础的工具链体系了。

对于开源界来说，GCC是软件编译的基石，而GDB是最常见的调试器（也有很多其他debugger直接或间接基于GDB）这一情况几乎已成为标准但LLVM项目在多种编程语言中的应用为开源界带来了一股新的气息，相比GCC，GDB这样编译为执行程序而推崇以标准输入输出与其他程序交互的程序而言，clang和lldb基于共享库的程序组织能够在代码级别上达成项目间的成果共享，为与编译器打交道的程序员提供了一种新的选择：使用带有具体含义的API，而不是用各种的正则来解析协定好的文本格式。

也许在不久后的将来，我们将会看到一套完整的、基于llvm的C/C++/Objective-C/C++工具链：clang的语意语境补全、静态语言分析、libcxx和clang的C++0x支持、基于lldb的良好调试体验。而这一套工具链，则完全替代了开源界传统的GCC/GNU
libstdc++/GDB工具链，所以可谓是一场“革命”了。

这令我想到了“最牛的程序员-- 我心目中的编程高手”一文中的一段话:  
其实，D爷爷当初也没想过C会风行世界。他开发C的初衷和Eric S.
Raymond在Cathedral and
Bazaar里阐述的一样，就是要消除自己对现有工具的不爽之处。

我没有这么牛，不过就体验而言，用Eclipse中带有语意语境的补全，java代码几乎是只敲着回车完成的。再加上即时的编译检查，确确实实的提升了我的工作效率。结合clang的介绍令我对现有的开源C/C++的IDE功能有了这样一种观点：重复发明车轮的行为太多了，而没有哪种车轮能达到Eclipse中java
语意语境的准确性和完整性。因为C/C++编译规则的复杂性（预处理、C++模板实例化、名称查找规则），如果想达到完全的准确和完整，就和编写完整的编译器差不多了。而我想现在不论
ctags+omnicppcomplete(vim)，cedet的semantic(Emacs，仅作简单测试，未深入配置，如有说法错误还请指正)，还是codeblocks/codelite等IDE中集成的语言分析模块，都达不到GCC的语意理解级别，但clang的出现提供了这一可能。在clang的源码路径中，已经有了一个供emacs使用实验性的、基于Clang的语意补全插件（未尝试，如有人尝试希望共享下）。

以上内容可算是apple在开源界一次“革命”的个人解读了，愿clang/libcxx/lldb
能为将来开源界的编程体验带来如apple的UI般舒服而人性化的改变，为古老而不断改变的Unix世界/开源界带来新的气息。而关于clang/libcxx/lldb就介绍到这里，如有因许可证而会引起的相关问题还欢迎了解的同志介绍下。
