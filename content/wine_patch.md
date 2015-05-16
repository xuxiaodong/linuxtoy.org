Title: Wine 中文输入法补丁
Date: 2007-01-13 11:22
Author: toy
Category: Tutorials
Slug: wine_patch

Wine 最近的几个版本，包括 0.9.28、0.9.29 都与 SCIM 输入法存在冲突。当在
Wine 出的程序中开启 SCIM 时，会导致该程序死掉。以下是解决 Wine 与 SCIM
输入法冲突问题的办法。

首先到 Wine 的 source dir 下找到 dlls/winex11.drv/x11drv\_main.c
文件，并使用编辑器将其打开。然后，搜索以下代码：  
`if (!XInitThreads()) ERR( "XInitThreads failed, trouble ahead\n" );`

你只需将这行注释掉重新编译即可。

jarlyyn 网友已经把 winex11.drv.so 文件单独编译了，你可以从 [Ubuntu
中文论坛](http://forum.ubuntu.org.cn/viewtopic.php?p=181459#181459)下载该文件（含
0.9.28 和 0.9.29 两个版本）。解压缩后用 root 权限覆盖 /usr/lib/wine/
下的同名文件就可以了。

(Thanks jarlyyn!)
