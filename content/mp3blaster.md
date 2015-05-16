Title: 使用 Mp3blaster 从命令行播放音乐
Date: 2008-01-01 10:25
Author: toy
Category: Apps
Slug: mp3blaster

[Mp3blaster](http://mp3blaster.sourceforge.net/) 是一款基于控制台的 MP3
播放器。由于它的界面是文本模式的，所以不需要任何图形环境就可运行。Mp3blaster
支持播放 mp3、ogg、wav 等格式的音乐文件。同时，Mp3blaster 也具有 CD
样式的按钮，使你能够对 MP3
进行播放、停止、暂停、下一首之类的操控。当前，Mp3blaster 能够在 UNIX
类操作系统中运行，包括 Linux、*BSD 等。

[![Mp3blaster](http://i.linuxtoy.org/i/2008/01/mp3blaster-thumb.png)](http://i.linuxtoy.org/i/2008/01/mp3blaster.png)  
*Mp3blaster 截图 (点击可放大)*

在安装好 Mp3blaster 后，可以使用如下命令播放文件夹中的所有 MP3：

`mp3blaster *.mp3`

或者，你也可以先启动
Mp3blaster，再通过它的“选择文件”功能来选取要播放的音乐文件。

关于 Mp3blaster 的更多用法，可能你需要 man mp3blaster 一下。

Mp3blaster 在目前大多数 Linux 发行版中应该都能找到。当然，你也可以[获取
Mp3blaster 最新版本 3.2.3
的源代码](http://sourceforge.net/project/showfiles.php?group_id=154673)。
