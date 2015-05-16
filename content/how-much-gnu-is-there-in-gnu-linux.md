Title: GNU/Linux 中到底有多 GNU ？
Date: 2011-06-06 21:41
Author: lovenemesis
Category: Reviews
Tags: gnu, Linux
Slug: how-much-gnu-is-there-in-gnu-linux

按照 Free Software Foundation 的说法，Linux 的全称应该是
GNU/Linux。那么一个常见的 Linux 发行版究竟有多 GNU 呢？

Pedro Côrte-Real 在他的博客中发表了一份**以代码行为单位对于 Ubuntu 11.04
中 main 仓库包含软件 GNU 比例（仅限由 Ubuntu 打包的部分，不包括从 Debian
继承的）**的分析，参见下图：

[![](http://linuxtoy.org/img/2011/06/gnutotalsplit.png "gnutotalsplit")](http://linuxtoy.org/img/2011/06/gnutotalsplit.png)

由图中可见红色部分的 **GNU 软件仅占了 8%**（指**由 Free Software
Foundation 起领导作用**）。注意其中 GNOME 并未包含其中，因为 GNOME
有自己的基金会和管理团队。

从中可以发现：

1.  内核的代码行和 GNU 软件代码行数量相当。
2.  其他各类小型的项目贡献的代码行实际上占据了过半的比例。

针对其中的 8% 部分，Pedro Côrte-Real 又进行了更深的分析，见下图：

[![](http://linuxtoy.org/img/2011/06/gnusplit.png "gnusplit")](http://linuxtoy.org/img/2011/06/gnusplit.png)

从中可以很明显的看出，glibc/gcc/binutils/gdb 的组合占据了 GNU
软件代码中的绝大部分。对于某些最终用户来讲，可以比较容易的找到这些组件的非
GNU 替代品，除了 gdb。

作者同时还公布了自己进行[代码比较的程序源代码](https://github.com/pedrocr/codecomp)。

*消息来源：*[Pedro Côrte-Real
个人博客](http://pedrocr.net/text/how-much-gnu-in-gnu-linux)
