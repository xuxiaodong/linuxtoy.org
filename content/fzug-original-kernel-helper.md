Title: FZUG原创作品:内核助手
Date: 2009-01-21 13:16
Author: lovenemesis
Category: Apps
Tags: Fedora, kernelhelper
Slug: fzug-original-kernel-helper

来自 FZUG 的 AzureSky 编写了一款可以图形调节内核参数的小程序，某人戏称为
Linux 优化大师。目前正在测试阶段，欢迎大家测试反馈。

*以下内容转载自[论坛原帖](http://bbs.fedora-zh.org/showthread.php?t=1001)：  
*  
简介：  

内核的可调参数一共有几百个，这个软件为大家提供一些实用的调节，目前基本完成了网络部分的编写。

目前完成的功能:  
1) base 页 的基本信息显示（这个好像没什么好说 - -!）  
2) network 的所显示的功能都实现了，但是 network
的参数还有很多的，如果你知道哪些实用参数，而我没有添加的，请告诉我
^\_^。

3）kernel 的所显示的功能都实现了。

用法：  
如果没有安装 gtkmm 和 libglademm 的，先 yum install gtkmm24
libglademm24  
解压，  
终端下 su  
然后 make install （不用 make 了，我已经编译好的，嘎嘎）  
然后输入 kernel\_helper

删除软件， make clean

ps：  
1）目前需要找 ps 高手帮忙做几个标题图，图标之类的东西，  

2）由于内核的可调参数太多了，凭一人之力收集，有点困难，如果你知道有哪些好的参数，可以提出来，

谢谢

如果有发现什么bug，记得提出来阿，  
*转载结束*

**提醒：新手慎重使用！**

截图及下载请移步至[论坛原帖](http://bbs.fedora-zh.org/showthread.php?t=1001)。
