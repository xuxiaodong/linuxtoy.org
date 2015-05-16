Title: rdesktop：Linux 下的远程桌面客户端
Date: 2007-08-10 08:00
Author: toy
Category: Apps
Slug: rdesktop

[rdesktop](http://www.rdesktop.org/) 是一个在 Unix/Linux 下访问 Windows
远程桌面的客户端程序。当前，rdesktop 所支持的 Windows 系列版本包括
NT、2000、XP 和 2003。通过使用 rdesktop
所实现的远程桌面协议（RDP），你可以在 Unix/Linux 系统中呈现 Windows
桌面，并进行相应的操作。

![rdesktop](http://i.linuxtoy.org/i/logo/rdesktop.png)

不像 Citrix ICA 这种商业程序，rdesktop
对服务器没有什么扩展要求。[rdesktop 目前的最新稳定版本为
1.5.0](http://prdownloads.sourceforge.net/rdesktop/rdesktop-1.5.0.tar.gz?download)，你可以从源代码安装它，也可以使用下列命令直接从所用的
Linux 发行版中安装：

`apt-get install rdesktop`

或者，

`yum install rdesktop`

前一命令针对 Debian/Ubuntu 系统，后一命令则适用于 Fedora 系统。

若要连接 Windows 远程桌面，那么可执行以下指令：

`rdesktop [options] server[:port]`

例如，连接服务器 IP 地址为 192.168.0.100 的 Windows 桌面，并以 16
位色全屏显示，可以使用 `rdesktop -f -a 16 192.168.0.100`。关于 rdesktop
更为详细的用法，可以查询 man rdesktop。

**Updated:** 如果结合使用 seamlessrdp，可以让 rdesktop
实现更加好玩的效果：你能够从 Linux 中直接执行 Windows
桌面中的应用程序，就好像运行 Linux 中的原生程序一样。其实现方法如下：

1.  [下载
    seamlessrdp.zip](http://www.cendio.se/files/thinlinc/seamlessrdp/seamlessrdp.zip)，并将其提取到
    C:\\seamlessrdp。
2.  从 Linux 中执行 Windows 桌面的程序，如 IE：

    `rdesktop -A -s "C:\seamlessrdp\seamlessrdpshell.exe C:\Program Files\Internet Explorer\iexplore.exe" <IP>:3389 -u administrator -p password`

    其中，IP 为服务器所在的 IP 地址。

此方法的实现可详细参考 [Ubuntu
Wiki](https://help.ubuntu.com/community/SeamlessVirtualization)。

[感谢华华提示]
