Title: 使用 alias 来简化命令行输入
Date: 2006-11-09 13:40
Author: toy
Category: Tutorials
Slug: alias

alias（中文称为“别名”）允许使用更加简短的名称来重新定义 Linux 中的 Shell
命令，从而简化命令行的输入。如果经常与 CLI 打交道，那么使用 alias
不仅会节省时间，而且也能提高效率，真是一举两得的好事。

-   基本用法：
    alias
    的基本使用方法为：`alias 新的命令='原命令 -选项/参数'`。举例说明，`alias l=‘ls -lsh'`
    将重新定义 ls 命令，现在只需输入 l 就可以列目录了。
-   获知别名：
    直接输入 `alias` 命令会列出当前系统中所有已经定义的命令别名。
-   删除别名：
    要删除一个别名，可以使用 `unalias` 命令，如 `unalias l`。

