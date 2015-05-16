Title: FTP 客户端 gFTP 获得更新
Date: 2008-12-01 09:54
Author: toy
Category: News
Tags: FTP Client, gFTP, GTK+
Slug: gftp-gets-update

基于 GTK+ 界面的图形化 FTP 客户端 [gFTP](http://gftp.seul.org/)
于近日获得了更新。新版本对网络方面的代码进行了清理，支持通用 SSL
证书，添加了 Tango
风格的图标主题，以及修正了段错误、国际化等方面的缺陷。

![gFTP](http://i.linuxtoy.org/images/2008/12/gftp.jpg)

以下是 gFTP 的更改记录，供参考：

> * Cleanups to the networking code  
>  * Fixed several segfaults.  
>  * Several i18n fixes  
>  * Added support for wildcard SSL certificates  
>  * Fixes for downloading files using SFTP where the user doesn't have
> write access to the file.  
>  * Disable some features of the remote FTP server is a VMS server or
> OS/400  
>  * Fixed Solaris compile problem and pty issue under HPUX  
>  * Updated to use FSPLIB 0.9  
>  * Added Tango styled icon theme  
>  * The menus are now a little closer to other GNOME applications  
>  * New/updated language translations: ar bg ca cs da de dz el en\_CA
> en\_GB el es fi fr gl gu he hu it ja ko lt lv mk nb ne nl no oc pt\_BR
> pt\_po ro ru rw sv uk zh\_HK zh\_TW

你可从 [gFTP 官方网站](http://gftp.seul.org/)下载该更新版
2.0.19，包括源码包和 deb 二进制包。
