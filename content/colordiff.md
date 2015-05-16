Title: ColorDiff：高亮显示 Diff 输出
Date: 2008-02-24 09:50
Author: toy
Category: Apps
Slug: colordiff

在 Linux 下，使用 diff
命令可以对文件进行比较，从而了解其差异。不过，diff
命令的输出结果以同色显示，对于这种差异的表现可能不够强烈。好在我们还可以通过
[ColorDiff](http://colordiff.sourceforge.net/) 来加以改善。ColorDiff
是一个 Perl 脚本，它通过不同的颜色来高亮显示 diff
命令的输出结果，非常显眼。

![ColorDiff](http://i.linuxtoy.org/i/2008/02/colordiff.jpg)

ColorDiff 适用于 Linux 及 BSD 系统，目前已被包含到
Debian、Ubuntu、Gentoo、Arch Linux、Fedora、FreeBSD
等发行版中。你可以从中直接加以安装。

ColorDiff 的用法较简单。如果你要比较两个文件 file1 和
file2，那么可以执行如下命令：

`colordiff file1 file2`

你也可以将 ColorDiff 用于 diff 命令的管道输出：

`diff -u file1 file2 | colordiff`

ColorDiff 的最新源代码 1.0.7
可从[这里下载](http://colordiff.sourceforge.net/colordiff-1.0.7.tar.gz)。

[感谢 [fcicq](http://www.fcicq.net/wp/) 朋友推荐]
