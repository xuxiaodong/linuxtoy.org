Title: Gentoo 11.2 LiveDVD
Date: 2011-08-09 09:26
Author: cheer_xiao
Category: Distros
Tags: Gentoo, Live
Slug: gentoo-112-livedvd

堪称 Linux 桌面软件展板的 Gentoo LiveDVD 于 2011-8-7 发布了 11.2
版。Gentoo LiveDVD 带来大量软件更新：

-   系统包：Linux kernel 3.0 (包括 Gentoo 的 patch)、辅助工具
    Speakup、Bash 4.2, GLIBC 2.13-r2, GCC 4.5.2, Binutils 2.21.1, Python
    2.7.2 and 3.2, Perl 5.12.4 等等等等；
-   大量 DE 和 WM：KDE 4.7.0, GNOME 3.0.0, Xfce 4.8, Enlightenment
    1.0.8, Openbox 3.5.0, Fluxbox 1.3.1, XBMC 10.1 Awesome 3.4.10, and
    LXDE-Meta 0.5.5；
-   办公软件、图形软件和编辑器：LibreOffice 3.3.3, XEmacs 21.5.31 GVim
    7.3.244, Abiword 2.8.6, Scribus 1.3.9, GIMP 2.6.11, Inkscape 0.48.2,
    Blender 2.57, XSane 0.998 等等；
-   浏览器：Mozilla Firefox 5.0, Chromium 13.0 Arora 0.11.0, Opera
    11.50.1074, Epiphany 3.0.4, Seamonkey 2.2 等等；
-   通讯软件：Pidgin 2.9.0, Quassel 0.7.2, Mozilla Thunderbird 5.0,
    Claws Mail 3.7.9, QTwitter 0.10.0, Irssi 0.8.15 等等等等；
-   开发工具：KDevelop 4.2.3, KDESvn 1.5.5, Qt-creator 2.2.1, Bluefish
    2.0.3 等等等等；
-   多媒体软件：Amarok 2.4.3, MPlayer 1.0\\\_rc4, MPlayer2 2.0,
    DVDAuthor 0.6.14, LAME 3.98.4, FFmpeg 0.6.90, GNOME-MPlayer 1.0.4,
    SMPlayer 0.6.9 等等。

带来以下给力特性：

-   使用 AUFS 实现可写文件系统；现在可以在 LiveDVD 里面 emerge 了；
-   用户家目录($HOME)持久化：在  LiveDVD 中按 F9
    即可了解更多。（话说我不是很确定这是什么，怀疑是把 $HOME
    写到硬盘中；请用过的同学指正。）

Gentoo LiveDVD 11.2 有两个版本：x86/x86\\\_64 hybrid 和 x86\\\_64
multilib。前者可以引导 32 位或 64 位机器，后者只用于 64 位机器。

*消息来源*：[发布公告](http://www.gentoo.org/news/20110807-livedvd.xml)
