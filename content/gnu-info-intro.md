Title: GNU info 简介
Date: 2009-06-27 19:00
Author: toy
Category: Apps
Tags: GNU info
Slug: gnu-info-intro

{撰文/[lvscar](http://lvscar.info)}

前阵子开始学习
[Lisp](http://en.wikipedia.org/wiki/Lisp\_programming\_language)，找了一圈书籍文档后发现最适合的就藏在
[Emacs](http://www.gnu.org/software/emacs/) 神器里 (Help-More
Manuals-Introduction to Emacs Lisp)。;-)

这份文档以 [Textinfo](http://en.wikipedia.org/wiki/Texinfo)
格式编排，[info](http://en.wikipedia.org/wiki/Info\_(Unix)) 程序或 Emacs
下的 info 模式是阅读 Textinfo 文档的标配。与之前熟悉的
man，html，pdf，chm 阅读体验相比，info 阅读有些门槛，得花点时间熟悉。

相对于 man page;Textinfo
支持目录，层次化节点关系，节点间的交叉链接，(info 比 html
早两年被创造出来) 等结构化文档概念。这使得它更适合复杂文档或电子书。

info
程序有自己的一套快捷键机制。熟悉了这套快捷键机制并在脑中有文档结构概念后，浏览文档会比在浏览器方便得多。以下是常用的几个:

* spc (空格)：向下滚屏，至末尾后进入下一个文档节点  
* backspace (退格): 和空格相反，向上滚屏，至顶端后进入上一个文档节点  
* l : 回朔浏览历史，等同于浏览器中的回退。  
* n : 进入文档节点数中同级别的下一个节点 (*如果该节点包含子节点，n
会略过他们)  
* p : 和 n 相反，进入文档节点数中同级别的上一个节点  
* t：进入顶层结点  
* u : 进入上一层节点  
* b : 移动到本节点的顶端  
* m : 如果节点包含目录 (往往是下一层节点的索引)。给出提示让你选择进入  
* f : 如果节点包含交叉链接给出提示让你选择进入。(用 l 可以返回原节点)  
* i : 列出正在看的文档的所有索引标题让你选择进入  
* s : 对文档以你键入的词进行搜索。

Linux 下的很多软件都包含有漂亮的 info 文档。下次 man 之前，不防 info
试试。

依靠 Firefox 的 [Mouseless](http://www.mouseless.de/)
插件，浏览网页时基本上可以离开鼠标。可由于 html
中没有上下级结构，浏览只能是视觉驱动。而在 info
里，浏览过程能转换成结构驱动。我很喜欢这种体验。

就像以 CLI 替代 GUI 进行 OS 操作，付出学习成本，你能收获更多。
