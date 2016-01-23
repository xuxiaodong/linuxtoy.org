Title: Bash 4.0 和 Readline 6.0 发布
Date: 2009-02-24 16:35
Author: toy
Category: Cli
Tags: Bash, Readline, Shell
Slug: bash-40-and-readline-60

Bash 4.0 已经发布。除了修正 Bash 3 分支中的重要缺陷之外，该版本也添加了一些值得提及的新特性。这主要包括：

-   关联数组
-   改进了可编程完成函数
-   case-modifying 单词扩充
-   复合进程
-   支持 `**` 特别 glob 模式
-   增加了 shell 语法及重定向

与此同时，Readline 库也发布了新的 6.0 版本，其中引入了一些新的变量，包括 rl\_sort\_completion\_matches、rl\_completion\_invoking\_key、history-size（用户可设置）、revert-all-at-newline 等；同时增加了几个函数，实现了新的菜单完成代码。

Bash 4.0 及 Readline 6.0 的详细更改内容，你可以参阅其[发布公告](http://www.mail-archive.com/cygwin@cygwin.com/msg94439.html)。

[Bash](http://ftp.gnu.org/gnu/bash/) &
[Readline](http://ftp.gnu.org/gnu/readline/)

[via [LWN](http://lwn.net/Articles/320353/) & [Solidot](http://linux.solidot.org/linux/09/02/24/0258249.shtml)]
