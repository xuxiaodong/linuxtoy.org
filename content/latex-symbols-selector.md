Title: LSS：撰写 LaTeX 的辅助工具
Date: 2007-01-18 21:32
Author: toy
Category: Apps
Slug: latex-symbols-selector

LSS 的全称为 LaTeX Symbols Selector，它是一个可以帮助我们在撰写 LaTeX
文档时向其中插入特殊符号的辅助工具。如果你经常需要在自己所写作的 LaTeX
文档中插入特殊符号的话，使用此软件应该会为你节省不少力气。

[![LSS](http://i.linuxtoy.org/i/2007/01/lss_s.png)](http://i.linuxtoy.org/i/2007/01/lss.png)

LSS
将所有的特殊符号进行分类汇整，使用者不仅可以随意拷贝这些符号，而且能够直接插入到
gVIM 中，十分方便。LSS 总共包括了 478 种 LaTeX
特殊符号，可以说是基本上涵盖了各个方面。不仅如此，LSS 还支持许多的 AMS
符号。

如果要在 gVIM 中使用 LSS，那么可以将下列内容放到 ~/.vimrc 文件中：  
`autocmd BufWinEnter *.tex imap <F8> <Esc>:silent !lss &<cr>a`

这样，当使用 gVIM 写作 .tex 文档时，便可以直接按 F8 键来调用 LSS
以便插入特殊符号。

Download [LSS 0.1.1](http://clay.ll.pl/lss/)

(Thanks onetwothree!)
