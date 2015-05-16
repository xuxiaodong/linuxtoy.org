Title: 更改 Ubuntu 系统的预设程序
Date: 2006-11-23 20:58
Author: toy
Category: Tutorials
Slug: change_default_program

在默认情况下，Ubuntu 系统会为用户预设程序。就拿文本编辑器来说吧，Ubuntu
预设的是 Nano，对某些朋友来说，使用 Vim
可能更得心应手些。那么如何更改这些预设的程序呢？

你可以使用 `sudo update-alternatives --config editor`
命令来更改默认的文本编辑器。在我的系统中，执行该命令后输出结果如下：  

`   Selection    Alternative -----------------------------------------------           1    /usr/bin/vim           2    /bin/ed *+        3    /bin/nano`

按照提示，输入数字 1 即可将当前默认的 Nano 更改为 Vim。

事实上，update-alternatives 命令还可以配置 FTP、Telnet、rsh
等预设程序。更多的你可以查看 /etc/alternatives 目录。
