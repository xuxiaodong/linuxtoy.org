Title: Manpages 彩色化又一法
Date: 2010-01-24 09:41
Author: toy
Category: Cli
Tags: Manpage, Vim
Slug: color-manpages

{ 撰文/shaohao }

在 LinuxTOY 上面确实能找到不少好东西。前段时间想把 Manpages
彩色化，LinuxTOY  
一找，还真有，[彩色版本的
Manpages](http://linuxtoy.org/archives/colored-manpages.html)，当然还有用
most 工具的。  
不过我发现了另一种 Manpages  
彩色化解决方案，用——Vim，主要是看中它的快速跳转功能。

把下面的代码加入到 ~/.bashrc 里面：

# Use VIm as man pager  
vman () {  
export PAGER="/bin/sh -c \\"unset PAGER;col -b -x | \\  
vim -R -c 'set ft=man nomod nolist' -c 'map q :q' \\  
-c 'map ' -c 'map b ' \\  
-c 'nmap K :Man =expand(\\\\\\"\\\\\\")' -\\""

# invoke man page  
man $1

# we muse unset the PAGER, so regular man pager is used afterwards  
unset PAGER  
}

然后用 vman 就能看彩色版的 Manpage 了，当然了，你依然能用 man
看黑白版本。

最绝的是，用 Vim 的解决方案，当你在 Manpage 中看到 See Also
关键字后，你可以使用“Ctrl+]”快速跳转到 See Also 提供的参考指令中。  
例如：

vman grep

然后转到最后，光标指到 See Also 提供的 xargs(1)
参考指令上，然后“Ctrl+]“就能立刻查看 xargs 的 Man 文档了。  
（P.S. 但是不知道怎么跳回去-\_-）

{ Thanks shaohao. }
