Title: CharTr - 不错的思维导图工具
Date: 2008-07-12 08:00
Author: toy
Category: Apps
Tags: CharTr, Labyrinth, Mind mapping
Slug: chartr

[CharTr](http://code.google.com/p/chartr/)
是一款非常不错的思维导图工具。CharTr 并不是从零开始写的，它基于
[Labyrinth](http://linuxtoy.org/archives/labyrinth.html) 0.3
的代码，并从
[VYM](http://linuxtoy.org/archives/vym_setup_and_usage.html) 和
[VIM](http://linuxtoy.org/search/vim) 中获得了一些灵感。

[![CharTr](http://i.linuxtoy.org/i/2008/07/chartr-thumb.png)](http://i.linuxtoy.org/i/2008/07/chartr.png)

跟 Labyrinth 只具备基本的思维导图功能不同，CharTr
提供了一些十分不错的功能，主要包括：

-   类似 [VYM](http://linuxtoy.org/archives/vym_setup_and_usage.html)
    的节点样式
-   可以折叠节点
-   除文本外，支持在笔记中嵌入音频和图像
-   可以插入数学公式
-   可设定颜色
-   能够自动保存
-   能够输出 svg、png、pdf、ps 等格式
-   支持搜索节点
-   具有类似 VIM 的快捷键

CharTr 需要 python、pygtk、cairo、gstreamer、python-plastex、numpy
等依赖。在[下载 CharTr](http://code.google.com/p/chartr/downloads/list)
并解包之后，可通过如下指令来运行程序：

`python chartr.py`

[感谢 fcicq 朋友提供线索]
