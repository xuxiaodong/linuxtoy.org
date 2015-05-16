Title: Plowshare: 从命令行下载 Megaupload、Rapidshare 等网盘上的文件
Date: 2010-03-21 13:32
Author: toy
Category: Apps
Tags: Plowshare
Slug: plowshare

[Plowshare](http://code.google.com/p/plowshare/)  
是一款专门针对网盘进行下载/上传的 Linux 命令行工具。目前，Plowshare  
支持当下的许多网盘服务，包括
Megaupload、Rapidshare、2Shared、4Shared、ZShare,  

Badongo、Divshare.com、Depositfiles、Mediafire、Netload.in、Storage.to,  
Uploaded.to、Uploading.com、Sendspace、Usershare、X7.to 等等。

Plowshare  

支持使用代理，也可以下载包含链接列表的文件。一般情况下，可以通过如下命令来进行下载：

plowdown http://www.domain.com/path/to/file.rar

若需使用代理，只需 export http\\\_proxy 环境变量即可：

export http\_proxy=http://xxx.xxx.xxx.xxx:80

下载包含链接列表的文件（一行一个链接）：

plowdown file\_with\_links.txt

Plowshare  
可从其[项目主页](http://code.google.com/p/plowshare/downloads/)下载。
