Title: Magic Linux 2.5 alpha2 提供下载
Date: 2009-05-31 16:40
Author: toy
Category: Distros
Tags: Magic Linux
Slug: magic-linux-25-alpha2

作为国内的社区发行版 [Magic Linux](http://www.magiclinux.org/)
于昨日开始提供 2.5 alpha2 版本下载，以便用户测试。Magic Linux 2.5 alpha2
主要对安装程序和系统进行了更新，其中包括：

安装程序

1.
修正ext3分区支持的问题（默认使用128的inode\\\_size以保持兼容性，但256的inode\\\_size也没有问题）  
2. 添加ext4分区支持（可以做为/boot）  
3. 将rpm的默认压缩方式改为lzma。

系统

1. rpm升级到4.7.0并默认采用lzma压缩  
2. 工具链升级到gcc 4.4.0+glibc 2.10.1  
3. 内核升级到2.6.28.10  
4. 首次启动向导添加了一个编码转换向导  
5. 升级了qsopcast+sopcast  
6.
修正了自alpha1以来发现在的一部分Bug，具体的可以查看www.magiclinux.org/bugs  
7. 其它的一些修改。  
8. kde4升级到4.3beta1+

Magic Linux 2.5 alpha2
的已知问题及下载地址可从其[发布公告](http://www.linuxfans.org/bbs/thread-188827-1-1.html)中找到。

{ 感谢 djpj2046 朋友提示 }
