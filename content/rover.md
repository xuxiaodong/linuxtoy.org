Title: Rover: 基于终端的文件浏览器
Date: 2015-06-06 17:28:55
Authors: toy
Category: Cli
Tags: rover, vi
Slug: rover

在终端下对文件进行管理，除了一般的 `cd/ls/cp/mv/rm` 等命令之外，使用专门的工具不仅操作便利而且也比较快速，Rover 即是一例。Rover 使用 C 结合 ncurses 库编写而成，具有类似 vi 的按键绑定，并可通过 `$PAGER/$EDITOR` 设置的程序来查看或编辑文件。

<!-- PELICAN_END_SUMMARY -->

![Rover](http://linuxtoy.org/images/2015/06/rover.png)

执行 `rover` 后，`j/k` 下上移动，`l/h` 进入所选或返回父目录，按空格则查看文件，`e` 编辑文件。Rover 的其他用法可以看看其 Manpage。

Rover 用下来给人的感觉真是相当简单和轻快，若你对它感兴趣，不妨通过 [GitHub][g] 获取其源代码。

[g]: https://github.com/lecram/rover
