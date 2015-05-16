Title: Audio-convert-mod: 3 步搞定 Linux 下的音频转换
Date: 2008-04-24 09:54
Author: toy
Category: Apps
Tags: Audio-convert-mod
Slug: audio-convert-mod

如果你需要在 Linux 下进行音频格式转换，那么
[Audio-convert-mod](http://www.diffingo.com/content/view/13/47/lang,en/)
是一个值得一用的工具。Audio-convert-mod
简单易用，转换音频格式文件只需三步即可搞定。另外，使用 Audio-convert-mod
可执行批量转换。目前，Audio-convert-mod 支持
MP3、OGG、FLAC、WAV、AAC/MP4/M4A、MAC/Monkey's Audio/APE、MPC
(Musepack)、WV (wavpack) 等音频格式的编码和解码。

Audio-convert-mod 的当前版本为 3.45.2，提供有源码包和 RPM 包。安装
Audio-convert-mod 需要 gawk 和
file。此外，为了获得上述音频格式的编码/解码支持，需要安装一些常用的编码/解码器，比如：lame
用于 MP3 转换、vorbis-tools 用于 OGG 转换、flac 用于 FLAC 转换、mac 用于
APE 转换等等。

在启动 Audio-convert-mod 后，通过点击 File → Show Features 菜单可以查看
Audio-convert-mod
所支持的音频格式是否可用。如果显示为绿色则表示支持；若为红色则表示不支持，需要安装相应的编码/解码器。

[![audio-convert-mod-features](http://i.linuxtoy.org/i/2008/04/audio-convert-mod-features-thumb.png)](http://i.linuxtoy.org/i/2008/04/audio-convert-mod-features.png)

**Audio-convert-mod 使用过程**

下面让我们来看一下 Audio-convert-mod 的基本使用步骤：

1、选择文件

[![audio-convert-mod](http://i.linuxtoy.org/i/2008/04/audio-convert-mod1-thumb.png)](http://i.linuxtoy.org/i/2008/04/audio-convert-mod1.png)

如上图所示，点击 Add 按钮来选择要转换的音频文件，或者点击 Add directory
来选择一个包含多个音频文件的目录。如果列表中包含不想转换的音频文件，随时可以点击
Remove 按钮来移除它。

2、转换设置

[![audio-convert-mod](http://i.linuxtoy.org/i/2008/04/audio-convert-mod2-thumb.png)](http://i.linuxtoy.org/i/2008/04/audio-convert-mod2.png)

在第二步，需要选择输出的音频格式及其比特率。另外，也可根据实际情况设置其他选项，如针对源文件、目标文件存在、元数据、输出文件夹设置相应选项。

3、开始转换

[![audio-convert-mod](http://i.linuxtoy.org/i/2008/04/audio-convert-mod3-thumb.png)](http://i.linuxtoy.org/i/2008/04/audio-convert-mod3.png)

当转换设置完成后，点击 Next 即开始音频格式的转换过程。

**一些缺憾**

我感觉 Audio-convert-mod 还存在一些缺憾，比如在转换 APE 时无法利用 CUE
文件执行分割操作，不过，我们可以使用 shntool
这个命令行工具来完成；另外，不能将转换设置保存为预置文件
(虽然有个保存为默认值的选项，但还是不够方便和灵活)，因而也就无法作多次的重复调用。
