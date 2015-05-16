Title: Samba 服务器连接方法探讨
Date: 2010-05-07 12:44
Author: toy
Category: Tips
Tags: Samba
Slug: samba-connect

{ 撰文/[逸飞](http://www.billdeng.com) }

Samba  

服务器是文件共享的利器。在不同的系统及桌面环境下，其连接方式和效果却有所不同，如果不了解，要用好还不容易呢。[清风博客](http://www.billdeng.com)逸飞发现以下几种不同的连接方法及其效果，不揣鄙陋，与诸君共飨。

**一、服务器连接**

1. 根据 IP 地址直接连接，这种方法最快速，错误少。如果 IP
地址固定不变的话推荐用这种方法。

Windows 系统下在资源管理器地址栏输入：`\\\\192.168.0.2`

Linux 系统下在文件管理器地址栏输入：`smb://192.168.0.2`

(请使用您自己的 Samba 服务器地址)。

根据 Samba
服务器设置，你也许可以直接进入服务器存取资料，也可能需要用户名和密码。

2. 根据服务器名称连接。这种方法容易记忆，而且与 IP 地址无关，比较灵活。

Windows 系统下在资源管理器地址栏输入：`\\\\samba-server`

Linux 系统下在文件管理器地址栏输入：`smb://samba-server`

(请使用您自己的 Samba 服务器名)。

**二、不同系统及文件管理器的连接效果**

1. 据[清风博客](http://www.billdeng.com)逸飞的观察，在 Windows
下的连接最方便好用。连接上 Samba
服务器后，可以把服务器目录映射为本地磁盘，其使用效果基本上与本地磁盘完全一样。

2. 鹦鹉螺 (Nautilus)，基于 GNOME 的 GVFS 虚拟磁盘方法。所打开的 Samba
服务器上的文件先存于 GVFS 文件系统，完成后再传到 Samba
服务器，也比较方便。但是 Nautilus 的操作方法及灵活性上比 Konqueror 和
Dolphin 差了很远，这是比较不爽的地方。

3. Konqueror 和 Dolphin，基于系统临时目录的挂载方法。打开的 Samba
服务器上的文件暂存在系统 /var/tmp
目录下。如果文件作了修改，并不能直接保存在 Samba
服务器里，只能先保存在本机上，然后再转移到 Samba
服务器上。这个比较痛苦。

**三、CIFS，Linux下的终极 Samba 连接**

Samba 植根于 Linux，怎么可能反倒让 Windows 更为便利？ 其实 Linux
提供了一个最好的 Samba 服务器连接方法，就是 CIFS。

如果是 Ubuntu 系统，默认并没有安装这个组件，先把它装上：

# apt-get install smbfs

先在本地目录下新建若干子目录，然后可以将 Samba
服务器上的任意目录挂载到这些目录下，使用效果跟本地目录完全一样。挂载成功后，无论是
Nautilus、Konqueror、Dolphin，甚至 Terminal
终端都可以访问这些目录及操作这些目录下的文件。

# mount -t cifs //192.168.0.2/the/folder/you/wish /your/local/folder -o
user=user,passwd=passwd,iocharset=utf8

{ Thanks 逸飞. }
