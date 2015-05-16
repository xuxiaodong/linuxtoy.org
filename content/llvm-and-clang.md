Title: LLVM 与 Clang 介绍
Date: 2010-02-09 20:42
Author: toy
Category: Apps
Tags: Clang, LLVM
Slug: llvm-and-clang

{ 撰文/guest }

[LLVM](http://llvm.org) 是 Low Level Virtual Machine  

的简称，这个库提供了与编译器相关的支持，能够进行程序语言的编译期优化、链接优化、在线编译优化、代码生成。简而言之，可以作为多种语言编译器的后台来使用。如果这样还比较抽象的话，介绍下
[Clang](http://clang.llvm.org/) 就知道了：Clang 是一个 C++ 编写、基于
LLVM、发布于 LLVM BSD 许可证下的  
C/C++/Objective C/Objective C++ 编译器，其目标（之一）就是超越 GCC。

Clang 开发事出有因，Wiki 介绍如下：

> Apple 使用 LLVM 在不支持全部 OpenGL 特性的 GPU (Intel 低端显卡)
上生成代码 (JIT)，令程序仍然能够正常运行。之后 LLVM 与 GCC
的集成过程引发了一些不快，GCC 系统庞大而笨重，而 Apple 大量使用的
Objective-C 在 GCC 中优先级很低。此外 GCC 作为一个纯粹的编译系统，与 IDE
配合很差。加之许可证方面的要求，Apple 无法使用修改版的 GCC 而闭源。于是
Apple 决定从零开始写 C family 的前端，也就是基于 LLVM 的 Clang 了。

Clang 的特性：

1. 快：通过编译 OS X 上几乎包含了所有 C 头文件的 carbon.h
的测试，包括预处理 (Preprocess)，语法 (lex)，解析 (parse)，语义分析
(Semantic Analysis)，抽象语法树生成 (Abstract Syntax Tree) 的时间，Clang
是 Apple GCC 4.0 的 2.5x 快。(2007-7-25)  
2. 内存占用小：Clang 内存占用是源码的 130%，Apple GCC 则超过 10x。  
3.
诊断信息可读性强：我不会排版，推荐去[网站](http://clang.llvm.org/features.html#expressivediags)观看。其中错误的语法不但有源码提示，还会在错误的调用和相关上下文的下方有~~~~~和^的提示，相比之下
GCC 的提示很天书。  
4. GCC 兼容性。  
5. 设计清晰简单，容易理解，易于扩展增强。与代码基础古老的 GCC
相比，学习曲线平缓。  
6. 基于库的模块化设计，易于 IDE 集成及其他用途的重用。由于历史原因，GCC
是一个单一的可执行程序编译器，其内部完成了从预处理到最后代码生成的全部过程，中间诸多信息都无法被其他程序重用。Clang
将编译过程分成彼此分离的几个阶段，AST
信息可序列化。通过库的支持，程序能够获取到 AST
级别的信息，将大大增强对于代码的操控能力。对于 IDE
而言，代码补全、重构是重要的功能，然而如果没有底层的支持，只使用 tags
分析或是正则表达式匹配是很难达成的。

当然，GCC 也有其优势：

+ 支持 JAVA/ADA/FORTRAN  
+ 当前的 Clang 的 C++ 支持落后于 GCC，参见  
。（近日 Clang 已经可以自编译，见  
）  
+ GCC 支持更多平台  
+ GCC 更流行，广泛使用，支持完备  
+ GCC 基于 C，不需要 C++ 编译器即可编译

相信介绍到这里大家能够对 Clang 和 LLVM 有所了解了。除去 Clang
之外，LLVM  
还被用在 Gallium3D 中进行 JIT 优化，Xorg 中的 pixman 也有考虑使用 LLVM  
来优化执行速度，[llvm-lua](http://code.google.com/p/llvm-lua/) 使用
LLVM 来编译  
Lua 代码，[gpuocelot](http://code.google.com/p/gpuocelot/wiki/LLVM)
使用 LLVM 可以令 CUDA 程序无需重新编译即可运行在多核 X86CPU、IBM
Cell、支持 OpenCL 的设备之上...  
我个人感觉 Apple 在开源界口碑较差（也许是我的错觉？），不过 Apple
也为开源界贡献了不少，Webkit，OpenCL（虽说只是个标准），Clang。我最为佩服的是虽然出身于命令行之上的
Unix
族系统，但有魄力写出自成体系的图形栈，其图形界面优美而人性化，可谓也为开源界贡献了自己的精神与思想。  
对于 Clang 这个很有潜力的项目，我希望其 C++ 支持（尤其是 template
支持）能够早日完善。因为 GCC 在 template 出错时的诊断信息如同小说一般...

{ Thanks guest. }
