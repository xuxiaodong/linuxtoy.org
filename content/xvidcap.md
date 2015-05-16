Title: Xvidcap：屏幕录像机
Date: 2006-10-28 19:19
Author: toy
Category: Apps
Slug: xvidcap

[Xvidcap](http://xvidcap.sourceforge.net)
是一个可将屏幕上的操作过程录制下来并保存为视频的小工具。对于需要制作产品演示和教学的朋友来说，这个屏幕录像机十分实用。Xvidcap
支持生成 avi、mpeg、asf、flv、swf、mov
等视频格式，可以应用在各种场合。录制的区域也可以随意选择，显得非常方便。

Xvidcap 现在的版本为
[1.1.4rc2](http://sourceforge.net/project/showfiles.php?group_id=81535&package_id=83441&release_id=454382)，有源码包和
deb 包可用。下面以 deb 包为例来说明 Xvidcap 的安装及使用过程。

下载 Xvidcap 1.1.4rc2 的 deb 包后，使用以下指令安装：

`sudo dpkg -i xvidcap*.deb`

现在启动
Xvidcap，在首选项中对视频进行设置，如所采用的视频格式及编码器，保存文件名称等。如果需要录制声音，也可对音频部分进行相应配置。

![Xvidcap Setting](http://i.linuxtoy.org/i/2006/10/xvidcap_setting.png)

然后选择需要录制的区域，注意有红色的方框指示。点击 Xvidcap
控制栏中的红色按钮就可开始视频的录制过程了。录制结束后，可以用相应的播放工具播放。

![Xvidcap](http://i.linuxtoy.org/i/2006/10/xvidcap.png)
