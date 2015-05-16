Title: Linux Kernel UKSM 3.3
Date: 2012-04-28 02:11
Author: lovenemesis
Category: Featured
Slug: linux-kernel-uksm-33

Linux UKSM 是国人自主研发的一个 Linux
内核相关项目，这个项目对服务器和桌面应用都可以显著的减少 Linux
系统冗余的内存，已经在 RHEL6、CentOS 6、Ubuntu 12.04
等系统充分验证和测试过。*感谢项目作者 Figo.zhang 来稿*

现代的计算机内存中的数据是越来越多，Linux 内核机制 KSM(Kernel Samepage
Merging) 使得应用程序（特别是 KVM
虚拟机）能够合并相同内存的页面，但是其使用麻烦，并且速度很慢。UKSM(Ultra
KSM)
是国人在此基础上的极大改进。通过使用了更高级的算法，UKSM的新特性包括：

-   全系统扫描，**用户透明**：能扫描所有应用程序（包括 KVM
    虚拟机）中匿名映射区域的页面，不需要开发者修改一行程序就能从中获益。
-   极大提高了工作效率，其页面合并的速度，**最高可比原本的 KSM 快 20
    倍以上**。
-   **非常节省CPU**，如果系统当中没有冗余页面，那么其 CPU
    占用几乎观察不到，而一旦系统当中出现了冗余的内存的时候，它又能快速发现加以消除。

简单的概括，就是它能减少你系统当中的冗余的内存，虽然你的内存可能够用，但是，当代Linux都是把空闲内存作为文件缓存的，你有更多的空闲内存，你的文件系统也就越快！

具体的评测[请看这里](http://kerneldedup.org/projects/uksm/benchmarks/)，评测数据显示，其效率相当给力！

现在 UKSM 已经发布了最新的内核 v3.3，并且提供主流发行版本（centos
6/ubuntu 12.04/Fedora
16/Archlinux/）内核基础上UKSM补丁过的[内核安装包下载](http://kerneldedup.org/projects/uksm/download/)

欢迎广大网友们使用，并反馈意见！

[项目官方站点](http://kerneldedup.org/)
