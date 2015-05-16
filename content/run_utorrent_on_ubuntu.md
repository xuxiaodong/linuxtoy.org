Title: 在 Ubuntu 中运行 µTorrent
Date: 2007-01-09 18:50
Author: toy
Category: Apps
Slug: run_utorrent_on_ubuntu

[µTorrent](http://www.utorrent.com/) 是 Windows 下流行的 BitTorrent
客户端，它具有小巧精悍的特点，深受用户的喜爱。对于不满意当前 Linux 下的
BitTorrent 客户端的朋友而言，这是一个不错的替代方案。

[![µTorrent](http://i.linuxtoy.org/i/2007/01/utorrent_s.png)](http://i.linuxtoy.org/i/2007/01/utorrent.png)  
*µTorrent 正运行在 Ubuntu 中*

要让 µTorrent 在 Ubuntu 中运行起来，首先免不了的是安装 Wine：  
`sudo apt-get install wine`

接下来，我们需要对 Wine 作一些配置，在终端中执行 `winecfg` 可以打开 Wine
的配置窗口。

在 Applications 选项卡下面的 Windows Version 中选择 Windows
XP。然后切换到 Drives 选项页，点击其中的 Autodetect
按钮。操作完成后，单击 Apply 按钮，并点击 OK 关闭窗口。

µTorrent 的最新版本是
1.6，网站提供有独立程序和安装程序，此处建议下载独立程序
utorrent.exe。如果需要语言包，也可一并下载。

如果是在 utorrent.exe 的当前目录，那么现在在终端中执行
`wine utorrent.exe` 就可以在 Ubuntu 中运行 µTorrent 了。
