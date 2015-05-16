Title: emacs 缩进提示线
Date: 2012-01-18 23:26
Author: Kardinal
Category: Tips
Tags: Emacs, lisp
Slug: emacs-indent-vline

一般认为，lisp
中层层叠叠的括号，会给阅读者带来诸如头晕、恶心、呕吐等种种的不适，是难于阅读的主因。

但是经过仔细的研究，我发现，括号再多，也只不过让人恶心呕吐而已……而吐啊吐啊，你终究会习惯的……  
真正使人头晕的，是 lisp 那狂野的缩进。

多数编程语言中，缩进宽度是固定的，通常为四个或者八个空格。而 lisp
中，宏、函数、特殊形式的缩进规则都不相同；  

参数写在当前行或者下一行，缩进也不相同，凡此种种……缩进少则一个空格，多则N个空格，lisp
的缩进总是那么的飘逸、那么的空灵、那么的放纵不羁爱自由

后来我发现，scite
里面的缩进提示线相当的拉风……在有提示线的情况下，我的视力和智商都提高了
8%，于是又开始折腾可怜的 emacs

[![](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a298.png)](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a298.png)

当然也有按照固定宽度缩进的版本

[![](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a2982.png)](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a2982.png)

竖线其实是 xpm 图片排出来的，在字符界面下，用“|”来代替。  

代码比较长，就不贴了，用力按[这里](https://github.com/ran9er/init.emacs/blob/master/20_aux-line.el)

load 之后，(indent-vline)是固定宽度的缩进提示线，找到 " \\\\(
\\\\)"，定义了匹配缩进的宽度……

(indent-vline-lisp) 是 lisp 缩进提示线，也可以自己传递参数……但是对于
lisp 来说，默认的参数已经挺好了

->>-------------------------2012-01-23--1--22:59:48---------------------------->

改进了下，可以使用正则表达式匹配位置，画不同的线

[![](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a2983.png)](http://linuxtoy.org/img/2012/01/e697a0e6a087e9a2983.png)
