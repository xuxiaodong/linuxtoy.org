Title: 基于 wxWidgets 的 C/C++ IDE CodeLite 2.0 发布
Date: 2009-11-19 16:45
Author: toy
Category: Apps
Tags: CodeLite, IDE
Slug: codelite-20-released

{ 撰文/guest }

对于刚刚接触编程的人来说，Vim 和 Emacs 需要一段时间的学习才能上手，一款
VS  
风格的可视化 IDE 还是有必要的。在这里我要介绍的就是这样一款基于
wxWidgets  
的跨平台 C/C++ IDE -- CodeLite。

个人比较喜欢 IDE 的补全，就先介绍下曾经使用过的一些 IDE 的补全：

* OmniCppComplete，Vim 的补全插件，需要 Ctags，对于 Boost
这样大的库，有时一旦我按下快捷键令其补全时，会对 include/boost
文件夹进行扫描，非常慢（我的配置中没有 path
内容，有谁指点我为什么？），有些补全结果集中很多内容不符合上下文。

* NetBeans，实时分析补全，很强大，不但补全代码，还能补全
include，且代码的补全是根据 include
情况和预定义的预处理进行的（对于条件编译代码，不是一股脑全部进入补全结果集，仅有预处理后真正被编译的部分才进入补全结果集，很强大），需要装个巨大的
Java 平台和一堆依赖。

* VS 很强大，不能在 Linux 下用。

* CodeBlocks，同为基于 wxWidgets 的跨平台 C/C++
IDE，发展的也很不错，我经常使用，代码补全似乎也是实时分析的，补全能力也很强，但仅支持预处理的替换（比如
\\\_GLIBCXX\\\_STD 替换成 std），不支持完全的预处理指令。

* CodeLite：在 1.x 系列中，CodeLite 需手动指定 include 路径生成 tag
数据库，然后指定当前加载哪些库（类似于 Vim + Ctags），到了 2.0
系列中，CodeLite 只需指定 include 路径，而 tags 的生成是根据 #include
指令分析而按需加载的（无需手动生成），与 NetBeans
相似，也可以指定预处理定义，没有 include 的内容也不会进入补全结果集。

另外 CodeLite 集成 wxformBuilder，方便进行 wxWidgets 的 GUI
开发；可以自定义 Makefile 生成命令（比如我先用 cmake 生成
Makefile）；集成 Cscope；有类似于 Eclipse 的 quickoutline
和全局符号搜索，方便在当前文件或整个工程中搜索、跳转到定义、声明；使用
continous build 插件，后台自动编译修改的文件，编译错误无需整个工程 build
时就可显示（VS 2010 才有这个）。

如果大家对这个项目感兴趣可以尝试一下。

附上网址：

* [CodeLite](http://www.codelite.org)  
* [CodeBlocks](http://www.codeblocks.org) (推荐使用其 nightly build)

{ Thanks guest. }
