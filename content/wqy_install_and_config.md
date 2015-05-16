Title: 文泉驿的安装及配置
Date: 2006-12-24 16:14
Author: toy
Category: Tutorials
Slug: wqy_install_and_config

文泉驿点阵宋体在几天前发布了 0.8 测试版，从官方提供的截图来看，在 Linux
中的效果还是很不错的。受此影响，我也在自己的 Ubuntu
中进行了尝试，以下是安装及配置的点滴。

[![WenQuanYi](http://i.linuxtoy.org/i/2006/12/wqy_s.jpg)](http://i.linuxtoy.org/i/2006/12/wqy.jpg)  
*使用文泉驿点阵宋体显示中文及英文*

文泉驿项目分别提供了 PCF、DEB、RPM
三种格式的点阵宋体安装包。由于我本人使用 Ubuntu 发行版，所以下载的是 DEB
安装包。下载的文件名称为 wqy-bitmapfont\_0.7.9-5\_all.deb。

接着，便可以使用 `sudo dpkg -i wqy-bitmapfont_0.7.9-5_all.deb`
指令来安装文泉驿点阵宋体。

现在，启动 GNOME 的字体配置程序，在其中选择 WenQuanYi Bitmap
Song，已经基本上可以看到效果了，但还不够完善，需要做进一步的配置。

我使用的是英文区域，要删除 30-debconf-no-bitmaps.conf
才能全部生效。其实，30-debconf-no-bitmaps.conf
本身只是一个链接。删除操作可用指令
`sudo rm /etc/fonts/conf.d/30-debconf-no-bitmaps.conf`。也许中文区域不需要此操作。

另外，在 /etc/fonts/fonts.conf 文件中加入 WenQuanYi Bitmap
Song，注意放置顺序应在其他中文字体之前。

完成以上所有操作，需要注销一次系统，然后再重新登录才能看到最终的效果。

Download link:

[WenQuanYi Bitmap Song 0.8 beta](http://wenq.org/index.cgi?BitmapSong)
