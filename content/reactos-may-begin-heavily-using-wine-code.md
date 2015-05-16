Title: 开源的 WinNT 系统 ReactOS 将大量使用 Wine 代码
Date: 2010-01-20 17:38
Author: toy
Category: News
Tags: ReactOS
Slug: reactos-may-begin-heavily-using-wine-code

{ 撰文/guest }

本文内容基本上是  
的概要翻译，有兴趣者可看原文。

Arwinss is an alternative implementation of the core Win32 subsystem  
components.

大意是说 ReactOS 要重写其 Win32 子系统实现，且要大量使用 Wine 代码。

作者首先介绍了下 ReactOS 的现状：

+ 30+ 开发者 10+
年的开发，时间与人力充足，但仍达不到预期结果。原因何在？  
+ Win32 及 Windows 的设计是 boss 级怪，需要 10x 资源  
+ 仅有小部分 Win32 与 WinXP 相一致，其余大部分皆不兼容  
+ N 多重大 bug 已存在多年未被解决  
+ 因此 ReactOS 急需一个根本性的解决方案

接下来作者说明了为何及如何以再次重写其实现来解决这一问题，  
而不能够再等待数年。

当前 ReactOS 的实现 = 古老 Wine 代码 + 古老 ReactOS 特定代码 +  
一些优秀的新代码，其中 Wine 部分过于古老以至于与新的 Wine  
代码同步完全是浪费时间。

完全从零重写 Win32 子系统需要数年时间，事实上这也是 ReactOS
过去的尝试失败的原因。  
而尽可能重用 Wine 的代码则提供了一个可能的解决方案。

然后作者讨论了其技术上的可行性，  
大意是说 Wine 模块化优秀，可重用性强。对于关注点之一的图形部分，  
虽然 Wine 依赖于 X11，但有着其抽象隔离层，因此 ReactOS
完全可以使用其代码，并  
使用其自有的快速图形驱动。

之后作者说明了共享 Wine 代码所带来的好处，  
Wine 新版本中数百开发者的贡献，只需 30 分钟的合并与测试即可获得。

超过 Wine 所列举支持的 13495 个程序立时得到支持，而 ReactOS 的设计  
还可以运行那些由于硬件保护、驱动的相关问题而不能在 Wine 上运行的程序。

同时由于 ReactOS 系统级别的 Win32 实现，还能够克服 Wine 的如下缺点：

+ 糟糕的 NT 内核模拟  
+ 与 Wineserver 的缓慢通信  
+ Unix 依赖性  
+ ...

最后作者说明了这一工作的重要性：

+ 与 30+ 开发者 10+ 年相比，1 人 2 月即可完成一个可用的版本，开发迅捷  
+ 一次修复 N 多 bug  
+ 立时令 ReactOS 进入实际应用水平

截至发稿时期，ReactOS 0.3.11 版仍未支持 NTFS（现支持 FAT，路线图中 NTFS
将在  
0.5 版本中提供支持），这也是我未在物理电脑上尝试的原因。不过随着
ReactOS 与 Wine  
的共享，也许在未来的某一天，我们真的能够用上这个开源的、自由的 Win32
实现。

关于 ReactOS 为何选择重写一个 WinNT（这包含了
WinNT/2K/XP/2K3/Vista/7）而不是改进 Linux  
以及与 POSIX 系统、 Win32
系统关系如何等问题请参见其[介绍](http://www.reactos.org/zh/about.html)。

{ via
[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Nzg4OQ).
Thanks guest. }
