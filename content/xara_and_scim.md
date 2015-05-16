Title: 解决 Xara Xtreme 与 SCIM 的冲突问题
Date: 2006-09-22 08:55
Author: toy
Category: Tutorials
Slug: xara_and_scim

[![xara](http://i.linuxtoy.org/i/xara_s.png)](http://i.linuxtoy.org/i/xara.png)

前几天在安装好 [Xara Xtreme](http://www.xaraxtreme.org)
之后，无论怎么弄，Xara Xtreme
就是出不来，终端给出的提示是“Aborted”。百思不得其解。后来想到自己的系统中装有
SCIM，于是很自然地联想到 Xara Xtreme 与 SCIM
可能存在冲突问题。关于这一点，已经有些程序吃过 SCIM 的苦头了。本想将
SCIM 一换了之，怎奈我早已习惯了 SCIM 的输入。看来只好硬着头皮上了。

当我通过在终端中输入指令 export GTK\_IM\_MODULE=XIM 后，Xara Xtreme
顺利启动。于是心中释然。但这毕竟不是什么终究解决之道，每次启动都输入还是很麻烦的。所以又考虑弄过脚本来执行恐怕要方便些。其实，这个脚本很简单的，名字随意，我叫它
xara，在其中填入下列内容：

    #!/bin/bash

    export GTK_IM_MODULE=XIM

    xaralx

我就不解释了，一看就会明白的。再让这个 xara 可以执行：chmod +x
xara，这样，在终端中直接输入 ./xara 就能够启动 Xara Xtreme
了。更进一步地，我们还可以做一个链接：

    sudo ln -s /home/toy/xara /usr/bin/xara

注意将其中的 toy 换成你的用户名。现在只需通过在终端输入 xara 就可以了。
