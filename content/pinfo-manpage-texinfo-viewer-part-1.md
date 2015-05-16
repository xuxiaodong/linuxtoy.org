Title: manpage 和 Texinfo
Date: 2011-01-28 16:31
Author: lovenemesis
Category: Reviews
Tags: pinfo
Slug: pinfo-manpage-texinfo-viewer-part-1

这是 pinfo 教程的预备知识篇：manpage 和 Texinfo。 *感谢 cheer\_xiao
来稿*

注：本文中的 Linux 均指 GNU/Linux。

**什么是 manpage？**

**manpage** 的大名想必大家都有所耳闻，在此仅为新手科普一下。

在终端下打 `man xxx` 即可获得 **`xxx`** 程序的使用手册，如
`man ls`、`man man`。很多软件安装好之后也会带有 manpage，如在已经安装了
vim 的机器上可以打 `man vim`。manpage 的源码采用一种古老的唤作
[troff](http://zh.wikipedia.org/wiki/Troff) 的文本格式，一般放置在
`/usr/share/man` 或 `/usr/local/share/man`下。`man`
这个程序的作用也就是搜索相应的 manpage，然后在用户面前呈现出来。manpage
不光可以呈现在终端中，还可以翻译成其它格式，如[这里](http://linux.die.net/man/1/ls)就是
Linux 下的 `man ls` 翻译成 html
之后的结果（[这里](http://www.freebsd.org/cgi/man.cgi?query=ls)还有
FreeBSD 的版本）。

manpage 的主题也不局限于**用户命令**(user command)
的手册，系统调用(system call)、API，甚至文件格式也有相应的
manpage，它们被安排在不同的**区段**(section) 中。用 `man n xxx`
即可获得第 n 区段 xxx 主题的 manpage。如在 Linux 下，`man 1 stat`
得到的是 GNU 工具集中的用户命令 `stat` 的手册，`man 2 stat` 得到的则是
Linux 系统调用 `stat` 的手册。各个区段的说明可以参见英文维基的
[相关条目](http://en.wikipedia.org/wiki/Manpage#Manual_sections)。

manpage 在 *nix 世界广为使用，Linux、BSD 的所有系统调用以及 GNU
的工具集（`ls`、`cp` 这类 Linux 环境下的常用命令均在此列）都带有详尽的
manpage。不过 manpage 的主要用途是用作参考，一般不太适合初学者。

值得一提的是，troff
格式过于古老，很多时候不能满足需要，自然有不少后起之秀想要取而代之，如
OpenBSD 就于 2010 年宣布将尽量采用
mandoc（[维基](http://en.wikipedia.org/wiki/Mandoc)
[官网](http://mdocml.bsd.lv/)）格式来写
manpage。另一个后起之秀就是下面说到的 GNU 的 info。

**什么是 Texinfo？**

`man ls` 的最后一节“See Also”中说道：

The full documentation for ls is maintained as a Texinfo manual. If the
info and ls programs are properly installed at your site, the command  
info coreutils 'ls invocation'  
should give you access to the complete manual.

不光是 `ls`，GNU 工具集的其它程序的 manpage
后面均有类似的话，说完整版的手册是一个 Texinfo 文档，需要用 `info`
命令察看。

`info` 和 Texinfo 是何方神圣？从名字上可以看出，Texinfo 和排版格式 TeX
有着渊源。Texinfo 和 LaTeX 一样，都是 TeX 的扩展格式，区别在于 LaTeX
长于公式的排版、印刷，而 Texinfo 则专注于软件手册。Texinfo 相比于 troff
最明显的优势在于支持超链接，而且可以很方便地输出 html、pdf
等多种格式。现在 GNU 网站上提供的 pdf 文档大多都是用 Texinfo
文档生成的。

实际上，GNU 在很久以前就决定用 Texinfo
作为标准的手册格式了，可惜回应者寥寥，大家还是习惯书写和察看 troff
格式的 manpage。究其原因，一是软件手册主要还是在终端下察看，而这方面
Texinfo 除了支持超链接外，优势并不多；二是 GNU 提供的 Texinfo 察看软件——
`info` 的操作方式不兼容
`man`，使得不少用户大为不爽。因此这么多年过去了，troff 格式的 manpage
仍然是 *nix 世界软件手册的事实标准。

好了，介绍完 manpage 和 Texinfo，下一次我们要介绍的就是 `pinfo`
——很好很强大的 manpage 和 Texinfo 察看软件。
