Title: Linux 文件结构
Date: 2011-10-06 23:23
Author: lovenemesis
Category: Screenshots
Tags: fhs
Slug: linux-file-structure

想了解 Linux 文件系统树形结构，却又不愿翻阅 FHS 的朋友，可以参考
[skill2die4
制作的这张简图](http://www.secguru.com/files/linux_file_structure.jpg)。

此图算是 FHS 的图形化版本，简要的说明了 Linux
系统中各个目录的用途及层级关系，适合初学者使用参考。不过其中较新的如
`/run` 目录并未在其中出现。

[![](http://linuxtoy.org/img/2011/10/linux_file_structure.jpg "linux_file_structure")](http://linuxtoy.org/img/2011/10/linux_file_structure.jpg)

[**朝内下载链接**](http://dl.dbank.com/c0z6lv5ppm)

进阶阅读材料： [FHS](http://www.pathname.com/fhs/)

[消息来源](https://plus.google.com/u/0/112490285360955160152)

PS：

做为参考，这是 Fedora 16 Beta i686 上的文件结构：

    /
    |-- bin
    |-- boot
    |-- dev
    |-- etc
    |-- home
    |-- lib
    |-- lost+found
    |-- media
    |-- mnt
    |-- opt
    |-- proc
    |-- root
    |-- run
    |-- sbin
    |-- srv
    |-- sys
    |-- tmp
    |-- usr
    `-- var

同时 squeeze 童鞋提供了在 Debian 下的目录结构，参见[20
楼](http://linuxtoy.org/archives/linux-file-structure.html#comment-250537)，在此表示感谢！
