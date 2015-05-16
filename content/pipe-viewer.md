Title: pv: 管道查看器
Date: 2009-12-09 16:07
Author: hmy
Category: Cli
Tags: pv
Slug: pipe-viewer

管道是 Linux 的 Shell  
里面用的很多的东西，利用 [pv](http://www.ivarch.com/programs/pv.shtml)
这个软件，可以查看通过管道的内容的流量和大小等等，然后用于统计显示。

例如：

pv

可以显示解包的进度。

另外一个例子：

tar cf - /usr |pv|gzip >/tmp/usr.tgz

可以显示压缩的进度。

详细的介绍看[这里](http://www.ibm.com/developerworks/cn/aix/library/au-spunix\_pipeviewer/)。
