Title: 问题：如何在 ext4 分区下恢复删除的文件
Date: 2009-12-14 09:01
Author: lovenemesis
Category: AskLinuxtoy
Tags: ext3grep, ext4, giis, undelete
Slug: help-how-to-recover-deleted-file-under-ext4

相信浏览这里的朋友们都有或多或少的数据恢复的经验，不过如何在新近的 ext4
文件系统上恢复已经删除的文件呢？

事情起因（仅为BS XX 的 M$ Office
而存在，**可以略过**）昨日在下的女友不慎在 OpenOffice.org
中将刚刚写好的中文 doc 文件保存成 Word 95 格式，由于 XX 的 Word 95
不支持 Unicode
字符，该文档再次打开的时候全部变成问号了……于是全部希望就被寄托在先前导出的
PDF 文件。但是该 PDF 文件已经被 Shift + Del 了……怎么办？如何恢复？

这种情况肯定每个人都遇到过，尽管无论在终端还是GUI下都会提醒，但总是在习惯性的输入或点击
Yes 后才反应过来……

Google 了许久，恢复误删除文件的方案集中在以下几个：

[undelete](http://www.stud.tu-ilmenau.de/~mojo/undelete.html) 仅适合
ext2 和 ext3；

[giis](http://sourceforge.net/projects/giis/) 不能恢复安装 giis
之前删除的文件；

[ext3grep](http://code.google.com/p/ext3grep/) 仅限 ext3；

[R-Linux](http://www.data-recovery-software.net/Linux_Recovery.shtml)
唯一标注支持 ext4 的，但是需要有 Win32 系统才能运行……

难道在 Linux 系统上就没有一个适合 ext4
文件系统恢复误删除文件的解决方案么？ 肯定存在，只是没找到……

故再次请教诸位常逛 LinuxTOY 的朋友们，希望能指点一个可行的方案。

在下先谢过啦～
