Title: 玩转 MPlayer
Date: 2007-02-12 10:37
Author: toy
Category: Featured
Slug: playing-around-with-mplayer

MPlayer 是我在 Linux
系统中用到的相当好的媒体播放程序，它因支持播放广泛的音频/视频文件格式而著称。本文所要探讨的，除却一般的使用方法之外，更包括一些鲜为人知的提示和诀窍。相信在阅读此文后，你的多媒体播放体验将会增色不少。

**播放文件**

使用 MPlayer 播放媒体文件最简单的方式是：

`mplayer <somefile>`

MPlayer
会自动检测文件的类型并加以播放，如果是音频文件，则会在命令行中显示该播放文件的状态信息；而假如是视频文件的话，则会打开一个新的播放窗口。

**倒退与快进**

在播放文件的时候，你可以通过以下三组快捷键来对播放进程进行倒退与快进操作：

-   左方向键和右方向键：分别执行倒退 10 秒和快进 10 秒操作
-   下方向键和上方向键：分别执行倒退 1 分钟和快进 1 分钟操作
-   下翻页键和上翻页键：分别执行倒退 10 分钟和快进 10 分钟操作

**播放 DVD**

虽然 MPlayer 不支持 DVD 菜单，但是却能够播放 DVD。你可以这样播放 DVD：

`mplayer dvd://<titlenumber>`

你需要使用实际的数字来替换 <titlenumber>，如 1、2、3 等。

**使用字幕**

当播放电影文件时，你可以指定字幕文件：

`mplayer -sub <somesubtitlefile> <somefile>`

在播放 DVD 电影时，你也可以通过指定语言代码来使用字幕：

`mplayer dvd://<titlenumber> -slang nl,en`

这样，MPlayer
就会优先使用荷兰语字幕，如果该语言不可用，则再使用英语字幕。

**有用的快捷键**

以下是 MPlayer 中一些有用的快捷键：

-   f－当播放视频时，在全屏和窗口模式之间切换。你也可以在命令行中使用 -fs
    选项，以便让 MPlayer 开始在全屏模式中播放。
-   o－在播放视频时切换 OSD（OnScreen Display）模式。
-   p 或 Space－暂停／继续播放。
-   q 或 Esc－退出 MPlayer。在 GUI 模式时，Esc 不会退出，仅停止播放。
-   / 和 * 或 9 和 0－减小或增大音量。
-   m－静音切换。
-   T（通常是 Shift + t）－播放窗口置顶切换。
-   b 和 j－在可用的字幕间循环。
-   x 和 z－调整字幕的延迟时间。
-   I（Shift + i）－显示播放电影的文件名称。
-   1 和 2－调整对比度。
-   3 和 4－调整亮度。
-   5 和 6－调整色度。
-   7 和 8－调整饱和度。

**生成索引**

有时候，有些视频文件（主要是 AVI
文件）包含损坏的索引，或者根本就没有索引。这种情况通常是由下载文件不正确或未完成造成的。幸运的是，MPlayer
能够生成正常播放文件所需的索引。通过使用 -idx 选项，你可以告诉 MPlayer
来生成索引：

`mplayer -idx <somefile>`

有时候文件虽然包含索引，但却已损坏。那样的情况，你可能需要 MPlayer
强制生成索引：

`mplayer -forceidx <somefile>`

根据视频文件的大小，生成索引需花费一定的时间。但在此后，文件应该能够正常播放。

**纠正错误的音频／视频同步**

有些视频文件（主要是 flv 文件）由于编码的问题，会给 MPlayer
带来音频／视频同步的麻烦。这有两种可能情况：

-   MPlayer 会尝试修复，但同步问题却更遭。
-   MPlayer 会尝试修复那些正确的，因此没有必要同步。

对于第一种情况，你应当让 MPlayer 努力修复同步问题：

`mplayer -autosync 30 -mc 2.0 <somefile>`

而对于第二种情况，你不应当允许 MPlayer 去修复同步问题：

`mplayer -autosync 0 -mc 0 <somefile>`

将上述命令中的 autosync 设置为正值就会让 MPlayer
逐渐调整音频／视频的同步。值越高，MPlayer 越快地修复它。mc 选项指定
MPlayer 纠正每帧要多少秒。值越高，MPlayer
越认为接近修复音频／视频同步。设置为 0 则阻止 MPlayer 修复。

**在慢系统上使用 MPlayer**

MPlayer 允许在旧的或慢的系统上使用低 CPU
功率来播放视频文件。你可以使用 -framedrop 选项：

`mplayer -framedrop <somefile>`

当播放 MP3 或 OGG Vorbis
文件时，你可能感受到一定的缓冲，这将影响你的音乐体验。那样的话，你可以尝试使用
libmad（MP3）或 Tremor（OGG Vorbis）音频解码器。你可以这样来检测它们：

对于 MP3：

`mplayer -ac help | grep mad`

如果上面的命令返回的结果像这样：

`mad         libmad    working   libMAD MPEG layer 1-2-3  [libmad]`

那么你可以使用 libmad 播放 MP3：

`mplayer -ac mad <somefile>`

在 OGG 的情况中，你可以使用同样的技巧来检测 tremor 音频解码器是否可用：

`mplayer -ac help | grep tremor`

**播放流媒体**

如果 MPlayer
无法自动找到播放列表或直接的流媒体文件，你可以尝试使用 -playlist 选项：

`mplayer -playlist <file or url>`

同时你也可以设置较大的缓存：

`mplayer -cache 8192 -playlist <file or url>`

指定缓存大小的单位是 KB，上面的命令将允许 MPlayer 使用 8 MB
缓存。你可以使用 -cache-min 选项来改变 MPlayer 占用缓存的百分比：

`mplayer -cache 8192 -cache-min 50 -playlist <file or url>`

**循环播放**

如果你想让媒体文件循环播放，可以使用 -loop 选项：

`mplayer -loop 3 <somefile>`

上面的命令将播放 <somefile> 3 次，然后才退出。

`mplayer -loop 0 <somefile>`

上面的命令将永远重复播放 <somefile>。

**改变播放速度**

你可以使用 -speed 选项来改变 MPlayer 播放媒体文件的速度。值为
1.0，意味着正常速度；0.5 意味着慢两倍；2.0
意味着快两倍。像这样指定选项：

`mplayer -speed 2.0 <somefile>`

**改变采样率**

使用 -srate 选项你可以改变 MPlayer 输出的采样率：

`mplayer -srate 48000 <somefile>`

**将音频输出为 wav 文件**

你可以将视频文件中的音频部分输出为 wav 文件：

`mplayer -ao pcm <somefile>`

这将输出名为 audiodump.wav 的音频文件。你也可以为输出的 wav
文件指定名称：

`mplayer -ao pcm:file=<filename>.wav <somefile>`

**使用 ASCII 方式观看电影**

虽然无用，但却很好玩。有两个库文件支持该特性：aa 和 caca。使用
libaa，你只能在黑白 ASCII 中观看电影。而 libcaca 支持色彩。然而，libaa
支持更广泛。你可以像这样使用 libaa 观看电影：

`mplayer -vo aa <somefile>`

如果你想使用 libcaca：

`mplayer -vo caca <somefile>`

**将电影输出为系列图片**

MPlayer 也能将电影输出为一系列的图片：

`mplayer -vo jpeg <somefile>`

注意：上面的命令将产生数量巨大的 jpeg 文件。输出的 jpeg
文件名看起来像这样：00000001.jpg、00000002.jpg、00000003.jpg 等等。

你也可以输出其他的格式。只需将命令中的 jpeg 替换成 ppm、png、tga 等。

**指定纵横比**

当你在宽屏中播放电影时，可能想要使用 16:9 的纵横比：

`mplayer -aspect 16:9 <somefile>`

在非宽屏中，你可以使用 4:3 的纵横比。

**将选项放置到 MPlayer 的配置文件中**

对于一般用户来说，该配置文件位于 ~/.mplayer/config；全局的配置文件在
/etc/mplayer/config。不同的值使用行分隔，如：


    # MPlayer config file
    srate=48000
    ao="pcm:file=dumpedaudio.wav"

[[via](http://www.linuxtutorialblog.com/post/tutorial-playing-around-with-mplayer)]
