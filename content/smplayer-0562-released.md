Title: SMPlayer 0.5.62 发布
Date: 2007-11-20 09:51
Author: toy
Category: Apps
Slug: smplayer-0562-released

如果你在 Linux 中使用
[MPlayer](http://linuxtoy.org/archives/playing-around-with-mplayer.html)
来播放各种格式的媒体文件的话，那么你应该试试
[SMPlayer](http://linuxtoy.org/archives/smplayer.html)。SMPlayer
是一个超越 GMPlayer 且非常好用的 MPlayer 前端界面。SMPlayer
于昨日发布了最新的 0.5.62 版。

SMPlayer 0.5.62
主要添加了一些新的选项，可以将播放列表窗口停靠在主窗口的左边或右边，能够识别
MPlayer
的版本，纵横比设置可以正常工作，为鼠标滚轮添加了新的功能等。完整的更改记录如下：

* Added two new options for the subtitle menu: Size+ and Size-. They
change the subtitle size.  
* Added a new option in Preferences->Performance for H.264 videos:
Skip loop filter (the famous "-lavdopts skiploopfilter=all").  
* Now the middle click button is also configurable. The default action
is mute.  
* Now it's possible to dock the playlist on the left and right sides
of the main window.  
* Now smplayer can identify the mplayer version (or svn revision) and
change the behavior of some functions according to it.  
* Added in Preferences->General options to choose the initial audio &
subtitle tracks.  
* Now the aspect ratio settings should work when using the mplayer own
window.  
* Added two more functions for the mouse wheel: change the playback
speed and "no function" (the mouse wheel will do nothing).  
* Added a new option in Preferences->General->Audio that allows to
change the playback speed without altering the pitch (requires at least
MPlayer dev-SVN-r24924).  
* Added the option -mini, which will display a GUI with less buttons.  
* (Windows only) Added the audio types to the associations section in
preferences.  
* Added the Greek translation.

SMPlayer 0.5.62 除了源码包之外，也提供有 rpm、deb
等二进制包可用。你可以从[这里下载它们](http://smplayer.sourceforge.net/downloads.php?tr_lang=en)。
