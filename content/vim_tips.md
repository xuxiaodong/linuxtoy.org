Title: Vim 也玩取词翻译
Date: 2006-09-12 18:52
Author: lerosua
Category: Tutorials
Slug: vim_tips

感谢读者 [lerosua](http://my.donews.com/lerosua) 与我们分享在 Vim 中取词翻译的技巧：

本人当然不只是用 Vim 来编辑文件，也有很多时候用来看英文文件的，如各种源码包里的 README、INSTALL、TODO 等。这里面就有许多不认识的单词了，用星际译王当然可以翻译了，只是运用了鼠标，效率差许多了。于是想到在 Vim 里取词翻译。这其实没什么技术含量的。

1.  安装一个字符下的翻译软件。

    星际译王的子项目 sdcv 找个你装得上的版本装。源码装也只不过是

        ./configure ; make ; sudo make install

    三步而已。一些特定的发行版可能不能编译通过。所以说是找个你装得上的版本装。本人 Redhat AS 4 编译 0.40 通过。最新的 0.42 通不过。glibc 要求的太高了。然后安装词典。如果是已经安装过星际译王的，sdcv 会默认使用它的词典。都是同一作者嘛。

2.  配置 Vim。

    在你的 ~/.vimrc 里加上这句。注意快捷键是 ctrl + \ ，如果你配置文件已经用过了，请选择另外的键。

        nmap :!sdcv “” =expand(””)

    现在在 Vim 里读 README，遇到不会的单词就按 Ctrl + \\ ，它就调用 sdcv 来翻译。爽！呵呵！:)
