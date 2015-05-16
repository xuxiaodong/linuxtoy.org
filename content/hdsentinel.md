Title: HDSentinel：你的硬盘健康吗？
Date: 2008-11-10 09:43
Author: toy
Category: Apps
Slug: hdsentinel

因为硬盘承载着我们的重要数据，所以时常查看硬盘的健康状况是很有必要的。要达成此目的，你可以使用
[HDSentinel](http://www.hdsentinel.com/hdslin.php)
这个命令行程序。HDSentinel 支持 IDE、S-ATA（SATA II）、SCSI、USB
等类型的硬盘，利用它你可以即时查看硬盘的健康信息。HDSentinel
输出的信息十分简明，让人一目了然。身边常备
HDSentinel，可以使你及早防范，以免造成重要数据的丢失。

**下载及安装**

首先，你可以从 <http://www.hdsentinel.com/hdslin/hdsentinel.gz> 下载
HDSentinel。然后使用以下命令解包：

`gunzip hdsentinel.gz`

你将得到 hdsentinel 二进制文件。接着，为它赋予可执行权限：

`chmod a+x hdsentinel`

并拷贝到 /usr/local/bin 目录：

`cp hdsentinel /usr/local/bin`

**一般使用**

在执行 `hdsentinel` 后（注意需要 root
权限），你可以获得类似下面的输出信息：

Hard Disk Sentinel for LINUX console 0.02 (c) 2008 info@hdsentinel.com  
Start with -r [reportfile] to save data to report, -h for help

Examining hard disk configuration ...

HDD Device 1: /dev/sda  
HDD Model ID : ST380815AS  
HDD Serial No: 6QZ25EF2  
HDD Revision : 3.AAD  
HDD Size : 76319 MB  
Interface : S-ATA  
Temperature : 35 °C  
Health : 100 %  
Performance : 100 %  
Power on time: 234 days, 9 hours  
Est. lifetime: more than 1000 days

从中，我们除了可以了解到硬盘健康状况之外，还可以了解诸如硬盘大小、温度、性能等其他信息。

**进阶使用**

如果你想把 HDSentinel
输出的信息保存下来，不用复制和粘贴，只需执行以下命令即可：

`hdsentinel -r report.txt`

在 report.txt
文件中，你将可以了解到更为全面的信息，包括硬盘信息、S.M.A.R.T 信息等。

Linux 中，有另一个包
smartmontools，也可以让你查看硬盘的相关信息，具体参见 bread
的《[Ubuntu中的Load/Unload Cycle
Count问题及解决方案](http://linuxtoy.org/archives/ubuntu-harddisk.html)》一文。
