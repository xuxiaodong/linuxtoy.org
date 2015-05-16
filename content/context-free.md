Title: Context Free：迭代图编译器
Date: 2008-02-21 22:35
Author: MDZ
Category: Apps
Slug: context-free

[Context Free](http://www.contextfreeart.org/index.html)
是一个比较有趣的编译器，它能够把一些指令代码编译生成图形，而且拥有迭代特性，使我们仅通过短短的几行代码就能够绘制出漂亮的图形。

[![red
heart](http://i.linuxtoy.org/i/2008/02/full_1078.thumbnail.jpg)](http://i.linuxtoy.org/i/2008/02/full_1078.jpg)[![Explosion](http://i.linuxtoy.org/i/2008/02/full_1084.thumbnail.jpg)](http://i.linuxtoy.org/i/2008/02/full_1084.jpg)[![Black](http://i.linuxtoy.org/i/2008/02/full_1086.thumbnail.png)](http://i.linuxtoy.org/i/2008/02/full_1086.png "Black")

Context Free 的用法比较简单，编译之后它会产生一个 cfdg
的可执行程序。如果执行 ./cfdg 而不加参数，那么它将显示帮助文档。Context
Free 源码包中提供了 30 多个 cfdg
文件，用来生成演示图形。为了方便大家，我写了一串脚本（假定当前目录为
Context Free 源码目录下）：

``  $ make                    # 编译 Context Free $ mkdir demo            # 新建 demo 目录 $ files=`ls input/*.cfdg |cut -d. -f1 |cut -d/ -f2`          # 注意这里的反引号，在 Esc 键下方 $ for i in $files; do ./cfdg -s 800 input/${i}.cfdg demo/${i}.png; done       # 将 Context Free 提供的演示文档统统编译成 png 图像 ``

这样就在当前目录的 demo 中生成了大小均为 800*800px 的一系列 png
图像，赶快动用你最爱的图片浏览器浏览一下吧！如果你想自己写写代码，学习文档在
<http://www.contextfreeart.org/mediawiki/index.php/CFDG_HOWTO> 站点。

Context Free 依赖于 g++、flex、bison 以及 libpng
库，这些都可以在源中检索到，安装好后就可以使用我刚才的脚本编译漂亮的图形啦。

下载 Context Free：[tgz
格式](http://www.contextfreeart.org/download/ContextFreeSource2.1.tgz)
或 [zip
格式](http://www.contextfreeart.org/download/ContextFreeSource2.1.zip)
