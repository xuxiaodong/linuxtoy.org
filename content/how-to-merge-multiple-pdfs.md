Title: 如何合并多个 PDF 文档
Date: 2007-01-28 17:19
Author: toy
Category: Tutorials
Slug: how-to-merge-multiple-pdfs

从网上下载的 PDF
格式的电子文档，有时候包括多个部分，虽然这样有利于传输，但在阅读时却有不便之处。如果我们将其合并到一起，不仅使问题迎刃而解，而且也便于文档的保存。

在 Linux 中将多个独立的 PDF
文档合并到一起，是很简单的事情。为了完成后面的操作，你需要事先在系统中安装好
Ghostscript 和 PDFtk 这两个软件：  
`sudo apt-get install gs pdftk`

打开终端，并粘贴下列命令：  

`gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=firstANDsecond.pdf -dBATCH first.pdf second.pdf`

需要说明的是，此示例将 first.pdf 和 second.pdf 这两个 PDF 文档合并成
firstANDsecond.pdf
文件。请根据你的实际情况更改这些名称。另外，除了合并两个文件之外，你也可以合并三个、甚至更多。

(via [New Linux
User](http://www.newlinuxuser.com/merge-multiple-pdfs-into-one-file/),
thanks!)
