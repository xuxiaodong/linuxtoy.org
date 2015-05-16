Title: Manpages 彩色版
Date: 2007-06-24 21:44
Author: toy
Category: Tutorials
Slug: colored-manpages

Manpages 为手册页之意，在 Linux 中，若你遇到问题，可通过 man
指令即时查询这些 Manpages 以获取帮助。Nico Golde
介绍的方法很有意思，它可让我们平时司空见惯的 Manpages
一下子变得充满色彩起来。这个彩色版本的 Manpages 读起来令人感觉更加醒目。

[![Man](http://i.linuxtoy.org/i/2007/06/man_s.png)](http://i.linuxtoy.org/i/2007/06/man.png)

*Manpages 彩色版*

要实现这个彩色版的 Manpages 并不难，只需按以下步骤执行即可：

1.  在你的主目录创建 .terminfo
    目录，并转到该目录：`mkdir ~/.terminfo/ && cd ~/.terminfo`
2.  从作者网站获取 terminfo
    描述文件：`wget http://nion.modprobe.de/mostlike.txt`
3.  使用 tic 命令编译 mostlike.txt
    文件（编译后可删除）：`tic mostlike.txt`
4.  定义别名：`alias man="TERMINFO=~/.terminfo/ LESS=C TERM=mostlike PAGER=less man"`

现在使用 man 指令就可以读到彩色版的 Manpages 了。如果你需要修改 terminfo
文件，则可以使用 `infocmp mostlike`。

[[via](http://nion.modprobe.de/blog/archives/569-colored-manpages.html)]
