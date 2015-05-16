Title: 解决 UNetbootin 引导故障
Date: 2013-06-12 21:38
Author: toy
Category: Tips
Slug: unetbootin-error

今天在使用 [UNetbootin][u] 制作完成 Debian 7.0
的启动优盘后，没想到引导时系统报了如下错误：

    Failed to load libutil.c32
    Failed to load COM32 file menu.c32

究其原因，UNetbootin 在将 [Syslinux][s]
这个引导加载程序安装到优盘时，貌似漏掉了两个文件。解决起来也很简单，只需从
Syslinux 安装目录下找到 libutil.c32 和 libcom32.c32
这两个文件，并将其复制到优盘根目录即可。


    # cp /usr/share/syslinux/lib{util,com32}.c32 /mnt/udisk

其中，`/mnt/udisk` 为优盘挂载点。

系统：Funtoo  
UNetbootin 版本：584  
Syslinux 版本：5.01

[u]: http://unetbootin.sourceforge.net  
[s]: http://www.syslinux.org
