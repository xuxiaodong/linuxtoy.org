Title: Dolphin 插件: 音频文件缩略图
Date: 2009-11-06 16:36
Author: toy
Category: Apps
Tags: Dolphin
Slug: dolphin-plugin-audio-thumbs

{ 撰文/[qii](http://www.twitter.com/qiheizhiya) }

在 KDE-Apps 上看到一个蛮好玩的东西  

[AudioThumbs](http://kde-look.org/content/show.php/AudioThumbs?content=114885)。作用就是在
Dolphin  

预览模式下用音频文件（MP3、FLAC）里嵌入的封面作为这个文件的图标显示，如同用视频文件的缩略图做图标。

下载 audiothumbs，编译安装，如果你是 Archlinux：

yaourt -S audiothumbs

Dolphin - 设置 - 配置 Dolphin - 常规 - 预览，勾选 Audio Files。

[![Dolphin](http://i.linuxtoy.org/images/2009/11/thumb-dolphin.png)](http://i.linuxtoy.org/images/2009/11/dolphin.png)

然后点工具栏上的“预览”按钮。

当然有些音频文件是没有嵌入封面的，想嵌入的话可以用  
[Kid3](http://www.kde-apps.org/content/show.php/Kid3?content=10415)。

如果你是 Archlinux，这样

yaourt -S kid3-qt

在 Kid 里打开音频文件，然后从 Dolphin 里直接拖封面图片到右下角。

[![Kid](http://i.linuxtoy.org/images/2009/11/thumb-kid.png)](http://i.linuxtoy.org/images/2009/11/kid.png)

然后保存下，Dolphin 里预览就显示出来了。

[![Dolphin](http://i.linuxtoy.org/images/2009/11/thumb-dolphin\_preview.png)](http://i.linuxtoy.org/images/2009/11/dolphin\_preview.png)

{ [Source](http://qiii2006.blogbus.com/logs/50395052.html). Thanks qii.
}
