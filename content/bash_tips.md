Title: Bash 提示五则
Date: 2006-10-02 09:39
Author: toy
Category: Tutorials
Slug: bash_tips

这是我所见过的 Bash 提示当中非常 Cool 的几个，使用它们能够让你充分地享受到 CLI 的高效，并免除重复输入的麻烦，从而节省大量地时间。

1.  清屏

    一般来讲，为了清屏，我们通常使用 `clear` 命令。你有没有试过它的快捷键 `Ctrl+L`？个人认为使用组合键操作更快捷。

2.  逆向搜索

    有时候我们需要重新执行先前输入的命令。那么，在使用快捷键 `Ctrl+R` 后输入命令，Bash 将为你自动完成。

3.  命令置换

    谁都避免不了输入错误命令的情况，不要紧，可以使用 `^texttosobstitute^sobstitution` 来置换。比如，你输入了一个 `sudo apt-get updkte` 的错误命令，Bash 当然无法执行它了，这时可以通过输入 `^updkte^update`（或 `^k^a`）来纠正错误。

4.  重复上次的操作

    如果你想要重复执行上次的命令，那么只需输入 `!!` 即可。

5.  重复上次的参数

    如果你想要重复使用上次所用命令的参数，则可以使用 `!$`。举个例子，假如你上次执行的命令为 `ls -lsh`，那么，现在可以用 `ls !$` 来达到同样的目的。

[via [kratorius::code](http://kratcode.wordpress.com/2006/10/01/bash-tips/)]
