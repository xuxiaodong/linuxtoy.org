Title: 5 个 cd 命令小帖示
Date: 2010-04-28 12:16
Author: toy
Category: Cli
Tags: cd
Slug: 5-cd-command-tips

cd 是 Linux 命令行下最常用的命令之一。但是你真的了解 cd 命令的所有用法吗？我将在本文中向你介绍几个本人常用的 cd 命令小帖示，它们可以让你提高操作效率。

<!-- PELICAN_END_SUMMARY -->

1. `cd`

    不带任何参数，直接执行 cd 命令，这将转到你的 home 目录。其效果和 `cd ~` 相同。

2. `cd -`

    在 cd 命令后跟一个短横线，将转到你上一次访问的目录。这跟 `cd ..` 不同，后者将转到上一层目录。

3. `cd ~user`

    这条命令和 `cd ~` 很相似，不过它是转到 user 的 home 目录。

4. `cd old new`

    该 cd 命令带两个参数，其作用是将上次所执行 cd 命令中的 old 替换成 new  并予以执行。比如我先前 cd 到 /usr/bin 目录，现在我想 cd 到 /opt/bin 目录，则可以执行：

        cd usr opt

5. `$CDPATH`

    这是一个与 $PATH 类似的环境变量，我们可以将经常访问的目录赋值给该变量，多个目录使用 : 分隔。这样，我们就可以直接 cd 到这些目录。对于需要频繁访问的深层次目录，这极为有效。例如：

        CDPATH="$HOME/.config:$HOME/.config/uzbl"

补充一点，以上帖示在 **zsh** 中测试通过。其他 shell 可能会稍有不同。
