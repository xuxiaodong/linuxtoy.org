Title: Plasma video wallpaper: KDE 4 视频壁纸
Date: 2009-09-23 14:45
Author: toy
Category: Apps
Tags: KDE 4, Plasma, Wallpaper
Slug: plasma-video-wallpaper

Plasma video wallpaper 可将播放的视频设置为桌面壁纸，目前支持  
AVI、MKV、OGG、MPG、MPEG、OGV、MP4、OGM、ASF、FLV、WMV
等格式。该插件可从  

[KDE-Look](http://kde-look.org/content/show.php/Animated+Video+Wallpaper?content=112105)下载。纯粹玩而已，没什么实际用途，纯粹尝鲜~

[![Plasma video  

wallpaper](http://i.linuxtoy.org/images/2009/09/plasma-video-wall-thumb.png)](http://i.linuxtoy.org/images/2009/09/plasma-video-wall.png)

**安装**

Dolphin 解压，进入 plasma-video-wallpaper 文件夹，按 F4，编译安装：

cmake .  
make  
sudo make install

然后右击桌面-桌面设置-类型-Video。

后续要卸载的话：

sudo rm /usr/lib/kde4/wallpapervideo.so  
sudo rm /usr/share/kde4/services/video.desktop

{ Thanks [qii](http://www.twitter.com/qiheizhiya). }
