Title: 从*.EXE文件中提取图标: WineIcons
Date: 2008-12-06 14:26
Author: lovenemesis
Category: Apps
Tags: icon, Wine
Slug: wineicons

使用 WINE 的朋友有时会遇到这样的问题：应用程序的图标包含到 EXE
可执行文件里了，没法单独提取。尽管现在 WINE
可以截获在安装过程中生成的图标文件，但面对有些没有安装程序的绿色软件就没有办法。WineIcons
这个小工具可以解决从可执行文件中提取图标的问题。  

WineIcons 是一款专门为 WINE 设计的 Win32 应用程序，可以从 ICO、EXE 和
DLL 文件中提取图标并直接保存成所有桌面环境都支持的 PNG
格式，支持图标透明，支持调节生成 PNG
文件的平缓度。面对有些单个可执行文件中包含多个图标文件的情况也能很好的支持。尽管它是一款需要
WINE
才能运行的程序，但是作者提供了方便的安装脚本，可以集成到系统中。如果不再需要了，也有方便的卸载脚本可用。

WineIcons 在 GPL 协议下发布，二进制版本用合法的 Borland Delphi 5
Standard 编译。  
主界面截图：  

[![](http://i.linuxtoy.org/images/2008/12/wineicons.png)](http://i.linuxtoy.org/images/2008/12/wineicons.png)

[官方主页](http://wineicons.sourceforge.net/)  
[SourceForge
下载](http://sourceforge.net/project/showfiles.php?group_id=153917)
