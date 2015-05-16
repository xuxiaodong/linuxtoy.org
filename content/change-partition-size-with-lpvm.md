Title: 用 LPVM 来修改用 Wubi 安装 Ubuntu 时分配的硬盘大小
Date: 2008-08-04 15:26
Author: toy
Category: Tips
Tags: LPVM, Ubuntu, Wubi
Slug: change-partition-size-with-lpvm

[撰文/lilo <[作者的 blog](http://apit.blogbus.com/)>]

可能有不少人遇到这个问题：看到介绍说用wubi来装ubuntu既方便又安全。第一次用ubuntu的时候又对他要求的空间分配又没什么概念，就随手给了个5，6g心想应该是够了。结果安几次软件升级几次发现分给的空间迅速被用完。然而Wubi分配的空间实际上是一个大的文件，没有办法直接扩充。这里介绍一个工具能够方便的重新分配Wubi安装的Ubuntu的空间。

到这里[下载LPVM的deb包](http://lubi.sourceforge.net/lvpm.html)，在Ubuntu下可以直接安装。

这个软件主要就是辅助Wubi用户来将Wubi安装的Ubuntu复制到整个硬盘分区或者扩展Wubi分配的大小。这里主要介绍一下他重新分配大小的功能。

其实LPVM重新分配大小的原理很简单。他在你安装Wubi的分区内按用户的需求生成一个新的.disk文件，再将用户当前的Ubuntu使用的.disk文件全部复制到新的文件中。

根据这个我们可以很容易发现有几个重要的注意事项：

-   新分配的空间必须比原来Wubi分配的空间要大，否则无法正确的完成复制。
-   在你安装Wubi的分区必须有足够的剩余空间。

LPVM不能直接在原来的.disk文件上扩展，而必须要单独生成新的文件。假如你原来Wubi分配的空间是5G,你现在想要把他分配到10G，那么请注意你安装Wubi的分区必须有15G以上的空间才能保证LPVM正常的工作。

着重讲以上几点的原因是貌似LPVM不会自己检查这些问题，如果不能满足这些条件LPVM仍然会工作但是生成的.disk文件往往有问题。

接下来介绍下基本操作：

1.  下载LPVM的deb包，在Ubuntu下直接运行安装。可以在系统菜单－>系统工具－>LPVM找到它。
2.  运行LPVM，会出现下面的窗口：  
    ![lpvm.png](http://i.linuxtoy.org/i/2008/08/lpvm.png)
3.  我们要重新分配大小，选择resize。
4.  输入你希望的新的大小。
5.  然后等LPVM自己生成和复制文件了。
6.  注意这个过程需要相当长的时间...而且他的进度条不会正常的一直往前走，所以需要一点耐心。
7.  之后会弹出完成画面，并告诉你需要自己手动用新的.disk文件覆盖原来的。
8.  重新启动进入你的Windows，找到安装Wubi的目录。我的是在D:/ubuntu下面。

那么里面会找到一个disks文件夹。里面应该有new.disk，swap.disk，和一个new.disk。将root.disk剪切出去备份起来，把new.disk重命名为root.disk，重启进入Ubuntu即可。

[[原文链接](http://apit.blogbus.com/logs/26934027.html)]
