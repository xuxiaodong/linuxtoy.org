Title: 使用GNOME Sound Recorder抓取当前音频输出
Date: 2010-04-26 17:14
Author: shuge.lee
Category: Tips
Tags: record
Slug: grab-audio-with-gnome-sound-recorder

使用GNOME Sound Recorder抓取当前音频输出教程。

安装 gnome-extra/gnome-media

<div class="code">

    emerge gnome-extra/gnome-media

</div>

安装 dev-python/gnome-media-python （可选）

<div class="code">

    USE='examples' emerge dev-python/gnome-media-python

</div>

Applications -> Sound & Video -> Volume Control -> Preferences

在弹出的窗口里，勾选“ Digital ”，按Close。

[![](http://i.linuxtoy.org/images/2010/04/20100426-286x357-200x249.png)](http://i.linuxtoy.org/images/2010/04/20100426-286x357.png)

为了获得最好的录音效果，  
在 Playback 标签页里，点击“ Microphone
”下的喇吧图标禁用它（显示带一个红色交叉，表示禁用它）；  
设置 Master 音量为80%左右，PCM 音量为50左右。

[![](http://i.linuxtoy.org/images/2010/04/20100426-509x345-300x203.png)](http://i.linuxtoy.org/images/2010/04/20100426-509x345.png)

点击 Recording 标签页，  
点击 Digital 下的喇吧图标启用它（不显示带一个红色交叉，表示启用它）。  
设置音量为50%左右。

[![](http://i.linuxtoy.org/images/2010/04/20100426-505x343-300x203.png)](http://i.linuxtoy.org/images/2010/04/20100426-505x343.png)

随便打开一个播放器播放音乐，

Applications -> Sound & Video -> Volume Control ->

运行 Sound Recorder
，点击红色按钮录音，按方形按钮停止录音，按三角型按钮回放。

[![](http://i.linuxtoy.org/images/2010/04/20100426-400x339-294x250.png)](http://i.linuxtoy.org/images/2010/04/20100426-400x339.png)

（完）
