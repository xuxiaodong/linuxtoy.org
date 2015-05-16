Title: Ubuntu 8.04 (Hardy Heron) LTS 发布及下载
Date: 2008-04-24 19:05
Author: toy
Category: Distros
Tags: Releases, Screenshots, Ubuntu
Slug: ubuntu-804-hardy-heron-lts-download

早在 4 月 21 日，Canonical Ltd. 公司便在伦敦公布了开发代号为“Hardy
Heron”的 [Ubuntu](http://www.ubuntu.com/) 8.04 LTS
正式版。不过，直到今天，Ubuntu 8.04 LTS 的 ISO
映像文件才提供下载。这里的 LTS 即 Long-Term Support 的缩写，它指的是同
Ubuntu 6.06 一样，Ubuntu 8.04 将获得长期支持。具体来说，Ubuntu 8.04
桌面版本可以获得 3 年的安全更新支持，而对 Ubuntu 8.04
服务器版本的支持则长达 5
年。无论是普通的桌面使用者，还是服务端用户，Ubuntu 8.04
对他们来说都是一个极其重要的版本。

**核心更新**

在此，我们回顾一下在 Ubuntu 8.04 中的重要更新。首先，Ubuntu 8.04 采用
[2.6.24 版的 Linux
内核](http://linuxtoy.org/archives/linux-kernel-2624-released.html)，这对于无线网络、蓝牙等硬件设备的支持可以说上了一个新的台阶。其次，Ubuntu
8.04 的 X window system，亦即 [X.org 为 7.3
版](http://linuxtoy.org/archives/xorg-73-released.html)，它使显示器的分辨率设置更为方便。再次，Ubuntu
8.04 的默认桌面环境 [GNOME 更新到了
2.22](http://linuxtoy.org/archives/first-look-at-the-gnome-222.html).1，另外还包括
[KDE 3.5.9](http://linuxtoy.org/archives/kde-359-released.html)/[KDE
4.0.3](http://linuxtoy.org/archives/kde-403-released.html)、[Xfce
4.4.2](http://linuxtoy.org/archives/xfce-442-released.html) 等多种选择。

[![ubuntu-gnome](http://i.linuxtoy.org/i/2008/04/ubuntu-gnome-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/ubuntu-gnome.jpg)[![ubuntu-kde4](http://i.linuxtoy.org/i/2008/04/ubuntu-kde4-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/ubuntu-kde4.jpg)[![monitor](http://i.linuxtoy.org/i/2008/04/monitor-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/monitor.jpg)

特别值得提及的是，Ubuntu 8.04 整合了 PolicyKit 和
PulseAudio。前者不仅增强了 Ubuntu
的可用性及安全性，而且使普通用户也有机会执行需要管理员权限的系统程序。当然，进一步的设置还是需要
Unlock，不过对普通用户来说已经相当具有亲和力。而后者将 PulseAudio 作为
Ubuntu
默认的声音服务器，从而实现了一些较高级的特性，如不同的应用程序可以调节不同的音量、能够将音频流传输到其他计算机等。

[![policykit](http://i.linuxtoy.org/i/2008/04/policykit-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/policykit.jpg)[![authorizations](http://i.linuxtoy.org/i/2008/04/authorizations-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/authorizations.jpg)[![pulseaudio](http://i.linuxtoy.org/i/2008/04/pulseaudio-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/pulseaudio.jpg)

**新的应用**

Ubuntu 8.04 将 [Firefox 网络浏览器更新到了 3.0 Beta
5](http://linuxtoy.org/archives/firefox-30-beta-5.html)、图像处理软件
GIMP 更新到了 2.4.5、[办公套件 OpenOffice.org 更新到了
2.4](http://linuxtoy.org/archives/openofficeorg-240.html)、[矢量绘图软件
Inkscape 更新到了
0.4.6](http://linuxtoy.org/archives/inkscape-046-released.html)、Totem
更新到了 2.22、Compiz Fusion 更新到了
0.7.4……在更新已有程序的基础上，Ubuntu 8.04 引入了一些新应用，包括
[Brasero
光盘烧录软件](http://linuxtoy.org/search/brasero)、[Transmission
BitTorrent 下载软件](http://linuxtoy.org/search/transmission)、[Vinagre
远程桌面软件](http://linuxtoy.org/archives/vinagre.html)、Uncomplicated
Firewall (简称 ufw) 防火墙软件、World Clock GNOME 面板小程序。

[![firefox](http://i.linuxtoy.org/i/2008/04/firefox-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/firefox.jpg)[![gimp](http://i.linuxtoy.org/i/2008/04/gimp-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/gimp.jpg)[![openoffice](http://i.linuxtoy.org/i/2008/04/openoffice-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/openoffice.jpg)  

[![brasero](http://i.linuxtoy.org/i/2008/04/brasero-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/brasero.jpg)[![transmission](http://i.linuxtoy.org/i/2008/04/transmission-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/transmission.jpg)[![vinagre](http://i.linuxtoy.org/i/2008/04/vinagre-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/vinagre.jpg)

**其他改进**

此外，Ubuntu 8.04 还带来了其他许多新特性和改进，主要包括：

-   ActiveDirectory (活动目录) 集成：通过 Likewise Open 工具可以将
    Ubuntu 无缝集成到活动目录网络中，用户使用他们的 AD 证书就能登录
    Ubuntu 操作系统，并访问其服务。
-   iSCSI 支持：iSCSI Initiator 已被完全整合到内核，并允许 Ubuntu 将
    iSCSI 目标作为块设备挂载。
-   内存保护：这项功能可以帮助用户防护 RootKits 及其他恶意代码。
-   SELinux 支持。
-   umenu：一个简单的启动程序。
-   KVM 虚拟化得到了进一步的增强，添加了 libvirt 和 virt-manager。
-   Wubi：便于从 Windows 中安装 Ubuntu。
-   LTSP：alternate CD 提供一个快速安装 LTSP 终端服务器的选项。

[![umenu](http://i.linuxtoy.org/i/2008/04/umenu-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/umenu.jpg)[![wubi](http://i.linuxtoy.org/i/2008/04/wubi-thumb.jpg)](http://i.linuxtoy.org/i/2008/04/wubi.jpg)

**下载 Ubuntu 8.04**

Ubuntu 8.04 包括桌面版本和服务器版本，其 ISO 映像文件可从如下地址下载：

-   [桌面版 Live CD，适合
    i386](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-desktop-i386.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-desktop-i386.iso))：需要体验
    Ubuntu 和图形化安装模式的选这个。
-   [桌面版 Live CD，适合
    amd64](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-desktop-amd64.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-desktop-amd64.iso))：同上。
-   [桌面版 Alternate install CD，适合
    i386](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-alternate-i386.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-alternate-i386.iso))：从文本模式安装
    Ubuntu，需要定制的选这个。
-   [桌面版 Alternate install CD，适合 amd
    64](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-alternate-amd64.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-alternate-amd64.iso))：同上。
-   [服务器版，适合
    i386](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-server-i386.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-server-i386.iso))：需要安装
    Ubuntu 服务器的选这个。
-   [服务器版，适合
    amd64](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-server-amd64.iso.torrent)
    ([iso](http://releases.ubuntu.com/releases/8.04/ubuntu-8.04-server-amd64.iso))：同上。

你也可以下载 Ubuntu 8.04 的衍生版本，包括
[Kubuntu](http://releases.ubuntu.com/releases/kubuntu/8.04)、[Kubuntu
with
KDE4](http://cdimage.ubuntu.com/kubuntu-kde4/releases/8.04/)、[Xubuntu](http://cdimage.ubuntu.com/xubuntu/releases/8.04/)、[Ubuntu
Studio](http://cdimage.ubuntu.com/ubuntustudio/releases/8.04/)、[Edubuntu](http://releases.ubuntu.com/releases/edubuntu/8.04)
等等。

**下一个版本**

在 Ubuntu 8.04 之后的下一个版本将是 Ubuntu 8.10，开发代号为“[Intrepid
Ibex](http://linuxtoy.org/archives/ubuntu-810-name-announced-the-intrepid-ibex.html)”。可以预见，Ubuntu
8.04 发布后，Ubuntu 官方将立即开始 Ubuntu 8.10
的开发工作，该版本预计今年 10 月推出。
