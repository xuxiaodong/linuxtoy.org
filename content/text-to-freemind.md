Title: text-to-freemind: 将缩进文本转换成freemind
Date: 2008-07-31 00:11
Author: lwl
Category: Cli, Productivity
Tags: convert, freemind, Python
Slug: text-to-freemind

[text-to-freemind](http://uwstopia.nl/blog/2007/10/text-to-freemind-released)是一个python脚本，
用来将缩进的文本转换成[freemind](http://freemind.sourceforge.net/wiki/index.php/Main_Page)的mm格式，实际上就是一个xml了。作者**Wouter
Bolsterlee**今天刚更新了版本，节点里面可以换行，这样可以避免以前那样有太长的节点。

因为我的笔记本内存只有256M，如果同时上网和使用freemind，
就会比较慢。而我又喜欢用freemind来整理思路，所以这个脚本
正好满足我的需求。

用法非常简单，编写一个文本文件，每一行就是一个节点。
除第一行以外，所有行都以TAB缩进，视缩进的多少而定节点与前面节点的关系。
例子如下：

>       Root node
>           First level
>               Subnode
>                   Subsubnode
>                       Subsubsubnode
>               Subnode
>           Another first level
>               Subnode with some longer text
>               Another subnode with even longer text,\nbut fortunately it can be wrapped onto\nmultiple lines.
>           中文也可以
>               长句中没有问题\n又是一行\n再来一行

长句子中间可以用\\n来换行。 使用text-to-freemind转换成freemind的mm格式。

`text-to-freemind test.mm.txt > test.mm`

最后才用freemind来观察、输出结果。

值得一提的是作者还提供了一个make文件，可以用来自动转换整个目录中的*.mm.txt*文件。

[![](http://i.linuxtoy.org/i/2008/07/screenshot-20080731_0036.png)](http://i.linuxtoy.org/i/2008/07/screenshot-20080731_0036.png)

-   [代码下载](http://uwstopia.nl/geek/projects/text-to-freemind/text-to-freemind.uws/)，可以直接下载，
    或者使用*bzr branch http://...*。
-   [text-to-freemind](http://uwstopia.nl/blog/2007/10/text-to-freemind-released)

