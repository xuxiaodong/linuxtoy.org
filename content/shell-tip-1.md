Title: Shell 小技巧一则
Date: 2011-05-26 00:49
Author: vern
Category: Cli
Slug: shell-tip-1

经常与 Shell 为伍的你是不是也会经常碰到下面这些情境：

    1$ mv /somewhere/file /your/folder/
    2$ vi /your/folder/file

要保存某些文件到特定目录，然后开始查看/编辑

    1$ cp /somewhere/foo.c /somewhere/foo.c.orig
    2$ vi /somewhere/foo.c

或者先备份某个文件，然后开始捣鼓

    1$ tar zcvf archives.tgz /somewhere/folder /and/somewhere/file1 /and/somewhere/file2
    2$ scp archives.tgz someone@somewhere.org:~/blabla/

或者要打包某些目录/文件，然后上传什么的。在上面这些情境中，当你输入第二条命令时，可以试试像这样:

    1$ mv /somewhere/file /your/folder/
    2$ vi Alt-.file

按住 Alt
再按点，你会发现上一条命令的最后一个参数已经被自动输入了，继续输入 file
回拆。

    1$ cp /somewhere/foo.c /somewhere/foo.c.orig
    2$ vi Alt-1+Alt-.

先按 Alt 再按数字键 1，保持 Alt
键不松，再按点，帮助你补全上一个命令的第一个参数。

    1$ tar zcvf archives.tgz /somewhere/folder /and/somewhere/file1 /and/somewhere/file2
    2$ scp Alt-2+Alt-. someone@somewhere.org:~/blabla/

先按 Alt 再按数字键 2，保持 Alt
键不松，再按点，自动补全上一个命令的第二个参数。

用 zsh 的同学要设置一下，5 个应该足够了。

    bindkey "^[1"  digit-argument
    bindkey "^[2"  digit-argument
    bindkey "^[3"  digit-argument
    bindkey "^[4"  digit-argument
    bindkey "^[5"  digit-argument
    bindkey "^[-"  neg-argument

这些个数字参数在使用时，bash 是从左往右正数的，zsh 是从后往前逆数的。即

    $ touch 1a 2b 3c 4d 5e

bash 的 Alt-1 是 1a，Alt-2 是 2b。zsh 的 Alt-1 是 5e，Alt-2 是
4d，Alt--1 (Alt-负1) 是 1a，Alt--2 (Alt-负2) 是 2b。
