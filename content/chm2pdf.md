Title: chm2pdf — 将 CHM 转换为 PDF
Date: 2007-08-30 14:14
Author: toy
Category: Apps
Slug: chm2pdf

使用 [chm2pdf](http://code.google.com/p/chm2pdf/) 这个简单的 Python
脚本，你可以将 CHM 文件转换为 PDF
文件。我尝试了一下，效果还可以。由于我手头没有中文的 CHM
文档，所以未作这方面的测试。或许，感兴趣的朋友可以自己试试。

**chm2pdf 的安装**

在安装 chm2pdf 之前，你需要准备好它所用的依赖，主要包括：

-   chmlib
-   pychm
-   htmldoc
-   pdftk

然后[下载 chm2pdf 0.0.2
的安装包](http://chm2pdf.googlecode.com/files/chm2pdf-0.0.2.tar.gz)，并执行下列指令：  

` tar zxvf chm2pdf-0.0.2.tar.gz cd chm2pdf-0.0.2/ sudo python setup.py install`

**使用 chm2pdf**

chm2pdf 是命令行程序，其用法为：

`chm2pdf [input file] [output filename]`

例如，如果你要将 test.chm 转换为 test.pdf，那么可以执行以下命令：

`chm2pdf test.chm test.pdf`

**Updated:** 据 lerosua、Le.s.eohn 二位网友测试，目前 chm2pdf 不支持中文
chm 文档的转换，这真是一件遗憾的事。
