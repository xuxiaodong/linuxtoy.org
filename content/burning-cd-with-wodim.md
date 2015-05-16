Title: 使用 wodim 在命令行下烧录光盘
Date: 2008-12-26 18:35
Author: toy
Category: Cli
Tags: cdrkit
Slug: burning-cd-with-wodim

我们以前介绍的 [Linux
光盘烧录工具](http://linuxtoy.org/category/apps/cd-burner)多为图形化的程序，今天来看看如何使用
wodim 在命令行下烧录光盘。wodim 包含在 [cdrkit](http://cdrkit.org/)
中，如果你在自己的系统中找不到 wodim 命令的话，那么只要安装 cdrkit
这个包就可以了。

对于可反复擦写的光盘来说，在烧录之前，可以使用如下命令先擦除光盘上已有的内容：

`# wodim -v dev=/dev/cdrw blank=fast`

执行该命令后，最后的输出信息为：

Starting to write CD/DVD at speed 4.0 in real BLANK mode for single
session.  
Last chance to quit, starting real write in 0 seconds. Operation
starts.  
Performing OPC...  
Blanking PMA, TOC, pregap  
Blanking time: 48.583s

假设我现在想要将 install-x86-minimal-2008.0.iso 这个 ISO
映像文件烧录到光盘，则可以执行：

`# wodim -v dev=/dev/cdrw install-x86-minimal-2008.0.iso`

同样，我们可以看到最后的输出信息：

Starting to write CD/DVD at speed 4.0 in real TAO mode for single
session.  
Last chance to quit, starting real write in 0 seconds. Operation
starts.  
Waiting for reader process to fill input buffer ... input buffer
ready.  
Performing OPC...  
Starting new track at sector: 0  
Track 01: 79 of 79 MB written (fifo 100%) [buf 96%] 4.2x.  
Track 01: Total bytes read/written: 83396608/83396608 (40721 sectors).  
Writing time: 137.829s  
Average write speed 3.9x.  
Min drive buffer fill was 96%  
Fixating...  
Fixating time: 61.887s  
BURN-Free was never needed.  
wodim: fifo had 1314 puts and 1314 gets.  
wodim: fifo was 0 times empty and 1110 times full, min fill was 94%.

要完整的了解 wodim 的用法，当然是 man 一下。
