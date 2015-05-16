Title: Linux 下可用的 Divx/Xvid 字幕内封软件
Date: 2009-04-21 22:20
Author: lovenemesis
Category: Apps
Tags: divx, subtitle
Slug: usable-divx-xvid-subtitle-remuxer-under-linux

现在购买的 DVD 播放器几乎都具有 Divx/Xvid
文件播放功能，可以直接播放下载的 Xvid 格式的 AVI
电影节目，丰富了家庭客厅生活。但是其中支持外挂 SRT 或者 IDX/SUB
字幕的屈指可数。固然可以使用 Divx 公司提供的工具将字幕内封生成 DIVX
格式文件，但是那软件是 Win32 Only。 Linux 下怎么内封字幕呢？

本文就介绍一款可在 Linux 下运行的 Divx/Xvid 字幕软件，可以从 AVI 和
SRT（或者 IDX/SUB）文件生成内封字幕的 DIVX
格式文件。该格式文件可以在常见的带有 Divx/Xvid/MPEG4 回放的 DVD 播放器和
SONY PS3 上正确播放。而这个过程仅仅需要**5分钟**！

这里使用的是软件叫
[AVIAddXSubs](http://www.calcitapp.com/AVIAddXSubs.php) 。目前的 9.1
版本只有 896K，十分小巧。  
尽管该软件是一款 Win32 下的软件，但是作者在页面上注明了 Linux 和 Intel
Mac OS X 系统的用户可以使用 WINE 或者 Crossover 软件运行。

Fedora 的用户可以使用 yum 轻松安装 wine：

`su -c 'yum install wine'`

Wine 安装后，解压刚才得到的 AVIAddXSubs 压缩包，双击其中的
AVIAddXSubs.exe 即可运行。

以下截图是在 Fedora 10 i686 + WINE 1.1.19 下，**无需安装任何额外 win32
运行库或字体**。

主界面 Create Divx with Subtitles：

[![](http://i.linuxtoy.org/images/2009/04/screenshot-aviaddxsubs-v91-269x300.png)](http://i.linuxtoy.org/images/2009/04/screenshot-aviaddxsubs-v91.png)

在该界面最下方选择需要内封的 AVI 格式的影片文件。将 SRT(或者 IDX/SUB)
格式的同名文件（当然后缀名不同）放置在同一目录即可，无需再次选择。如果不在
Output Files 中设置路径的话生成的 divx 文件默认与源文件在同意目录下。

配置界面1 Configuration 1：

[![](http://i.linuxtoy.org/images/2009/04/screenshot-aviaddxsubs-v91-1-269x300.png)](http://i.linuxtoy.org/images/2009/04/screenshot-aviaddxsubs-v91-1.png)

由于通常的得到的简体中文字幕编码都是 GB2312 的，所以在配置页面中设置
Character Set 为 GB2312，Language 为 Chinese
(zh)。中国大陆地区的一般电视为 PAL 制式的，在右侧的 Subtitle Bitmap
中选择 720*576 (PAL) 即可。其余保持默认。

之后切换回主界面 Create Divx with Subtitles，点击最下方的 Create
Subtitled DivX Files
即可。由于不进行任何转码，只需**不到5分钟的时间**，一个可以在
Divx/Xvid/MPEG4 兼容设备上播放的 Divx 文件就生成了。**注意该 Divx
文件只有在使用 Divx 官方的 Divx Player
播放时才可显示内封字幕**，经测试用 VLC Media Player 或者 SMPlayer
都不能显示内封字幕。

用 U盘或者其他任何方式将其复制到客厅的播放设备上，打开它，然后像使用 DVD
那样用遥控器选择字幕，即可与全家人共享有中文字幕的 Divx 电影了！  
**字幕会显示在屏幕下方黑色空白处，并不会挡住影片画面。**

在 Sony PS3 Firmware 2.7.0 测试通过，效果很完美。

*特别推荐此软件的原因：*

1.  该软件可以在 Linux 下通过 wine
    运行，完全绿色，无需额外运行库或外带字体；
2.  该软件相比同类其他软件，避免了调用 Divx SDK 可能引起的诸多
    Bug，对中文长路径名支持良好；
3.  该软件对于中文字幕支持良好，没有出现字幕断节或乱码现象；
4.  该软件具有其他诸如同时封装8条字幕轨和 srt2sub
    转换等高级功能，参考附带的 Readme.htm 文件。

