Title: Wine 1.1.25 发布
Date: 2009-07-08 18:46
Author: lovenemesis
Category: Emulator
Tags: Wine
Slug: wine-1125-released

开源的 Win32 API 实现 wine 近日发布了 1.1.25 版本，该版本改善了 OpenGL
的内存管理，并且可以自动清理失效的桌面菜单项。

该版本有如下变化：

-   大量的本地化文件更新
-   在记事本中支持多种 Unicode 编码
-   提升内存管理，尤其是针对 OpenGL
-   自动清理桌面菜单项
-   开始 windowscodecs DLL 的实现工作
-   诸多 Bug 修正

[发行摘要](http://www.winehq.org/announce/1.1.25)  

[源代码下载](http://prdownloads.sourceforge.net/wine/wine-1.1.25.tar.bz2)

**Fedora 11 i586 RPM 下载**

[wine-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-1.1.25-1.fc11.i586.rpm)

[wine-alsa-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-alsa-1.1.25-1.fc11.i586.rpm)

[wine-capi-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-capi-1.1.25-1.fc11.i586.rpm)

[wine-cms-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-cms-1.1.25-1.fc11.i586.rpm)

[wine-core-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-core-1.1.25-1.fc11.i586.rpm)

[wine-desktop-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-desktop-1.1.25-1.fc11.i586.rpm)

[wine-esd-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-esd-1.1.25-1.fc11.i586.rpm)

[wine-jack-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-jack-1.1.25-1.fc11.i586.rpm)

[wine-ldap-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-ldap-1.1.25-1.fc11.i586.rpm)

[wine-nas-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-nas-1.1.25-1.fc11.i586.rpm)

[wine-oss-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-oss-1.1.25-1.fc11.i586.rpm)

[wine-pulseaudio-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-pulseaudio-1.1.25-1.fc11.i586.rpm)

[wine-tools-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-tools-1.1.25-1.fc11.i586.rpm)

[wine-twain-1.1.25-1.fc11.i586](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-twain-1.1.25-1.fc11.i586.rpm)

Fedora 11 SRPM 下载

[wine-1.1.25-1.fc11.src](http://files.getdropbox.com/u/464139/Wine-fe/1.1.25-fc11/wine-1.1.25-1.fc11.src.rpm)

**友情提示：**  
Fedora Wine 本版本中 nas、jack 和 esd 不再默认安装，同时 alsa 和 oss
也被分拆开。

**只需要安装
wine、wine-capi、wine-cms、wine-core、wine-desktop、wine-ldap、wine-pulseaudio、wine-tools
和 wine-twain 即可满足一般使用需求。  
**

建议优先使用

`su -c 'yum remove wine-core'`

删除老版本，再安装本次新版本。
