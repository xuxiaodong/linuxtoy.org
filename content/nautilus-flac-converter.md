Title: Nautilus-Flac-Converter: 将 FLAC 转换成 Ogg
Date: 2008-01-03 09:59
Author: toy
Category: Apps
Slug: nautilus-flac-converter

[Nautilus-Flac-Converter](http://nautilus-flac.sourceforge.net/) 是
Nautilus 文件管理器的音频转码扩展。使用它，你可以直接在 Nautilus 中将
FLAC 音乐文件转换成 Ogg
格式。目前，该扩展支持转换的格式还比较单一，不过，作者计划在未来使用
GStreamer 多媒体框架，那将允许你转换更多的音频文件类型。

Nautilus-Flac-Converter 需要 Nautilus 2.12.0 以上版本和
Vorbis-Tools。Fedora 用户可以通过下列指令来安装
Nautilus-Flac-Converter：

`yum install nautilus-flac-converter`

其他 Linux 用户需要[下载 Nautilus-Flac-Converter
的源代码](https://sourceforge.net/project/showfiles.php?group_id=158972)自行编译：

    tar jxvf nautilus-flac-converter-0.0.3.tar.bz2
    cd nautilus-flac-converter-0.0.3/
    ./configure
    make
    make install

在安装完成后，注销系统并重新登录，然后右击 FLAC 文件，通过“Convert FLAC
to Ogg...”菜单就可以打开如下对话框了：

![Nautilus-Flac-Converter](http://i.linuxtoy.org/i/2008/01/nautilus-flac-converter.png)

该对话框允许你设置 Ogg 的品质及保存目录。单击“OK”按钮即开始转换。
