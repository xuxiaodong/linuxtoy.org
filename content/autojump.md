Title: autojump: 在命令行下快速更改目录
Date: 2009-02-16 18:48
Author: toy
Category: Apps
Tags: autojump, cd
Slug: autojump

在命令行下，笔者通常使用 cd 命令来更改目录。不过，大多数情况下，cd
命令都需要使用者提供必要的路径信息方能达成目的。autojump
克服了这一点，它能够自动维护包含用户所使用目录的数据库，然后你只需输入 j
外加要更改目录名称的一部分便可快速跳转到该目录。

![autojump](http://i.linuxtoy.org/images/2009/02/autojump.png)

如果你不明白笔者在说什么，那么不妨看一看上面的截图。通过 `jumpstat`
可以查看数据库的具体内容。例如，当笔者想要将目录更改到
/home/xiaodong/bin/wog 时，只要执行 `j wo` 就可以了。

autojump 的源代码发布在 GPLv3 许可下，可由 git 取得。一般的 Linux
发行版用户可通过执行其中的 install.sh 脚本来安装 autojump，Archlinux
用户也可从 yaourt 安装。

[autojump](http://github.com/joelthelion/autojump/tree/master)
