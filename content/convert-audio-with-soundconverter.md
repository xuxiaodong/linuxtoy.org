Title: 使用 SoundConverter 转换音频
Date: 2007-02-19 14:19
Author: toy
Category: Tutorials
Slug: convert-audio-with-soundconverter

[SoundConverter](http://soundconverter.berlios.de/) 是一款适用于 GNOME
桌面环境的音频转换工具，它采用 GStreamer 作为后端，支持将 Ogg
Vorbis、AAC、MP3、FLAC、WAV、AVI、MPEG、MOV、M4A、AC3、DTS、ALAC、MPC、Shorten、APE、SID
等音频格式转换为 WAV、FLAC、MP3、Ogg Vorbis 等类型的文件。

支持批量转换和尽可能多的格式，是 SoundConverter
的两大特色。此外，它也具有配置转换后的文件保存位置、自动应用文件命名规则、可调整的音频质量（视输出的音频格式而定）等其他功能。

SoundConverter 的安装可以通过一句 `sudo apt-get install soundconverter`
指令搞定。在安装完成后，你可以从 声音 & 视频 -> SoundConverter
菜单项目来启动它。

在使用上，SoundConverter
亦很简单。首先需要对选项进行设置。如下图所示，包括文件的保存位置、命名、转换格式等在内的项目都是可供设置的。

![SoundConverter
Setting](http://i.linuxtoy.org/i/2007/02/soundconverter-setting.jpg)

具体到要转换文件时，既可以选择单个的文件进行转换，也可以通过指定一个文件夹来执行批量转换，如下图。

![SoundConverter](http://i.linuxtoy.org/i/2007/02/soundconverter.jpg)

另外，在 KDE 桌面环境中有一个类似的程序名叫
[soundKonverter](http://kde-apps.org/content/show.php?content=29024)，推荐
KDE 下的朋友使用。
