Title: Mp3Wrap：合并 MP3
Date: 2008-12-04 19:30
Author: toy
Category: Apps
Tags: MP3, Mp3Wrap
Slug: mp3wrap

如果你需要将多个 MP3 音频文件合并在一起，那么不妨试试
[Mp3Wrap](http://mp3wrap.sourceforge.net/)。Mp3Wrap
不需要进行解码/编码，合并 MP3 的速度相当快。

Mp3Wrap 是一个命令行工具，其语法格式为：

`mp3wrap [options]  OUTPUTFILE  f1.mp3  f2.mp3  [f3.mp3]...`

例如，有两个名为 file1.mp3 和 file2.mp3 的 MP3
文件，要把它们合并起来，只需执行如下命令：

`mp3wrap out.mp3 file1.mp3 file2.mp3`

这样，在当前目录下就会生成 out\_MP3WRAP.mp3 这个已合并的 MP3
文件。注意，Mp3Wrap 在文件名中加入了 MP3WRAP 字串（可供
[Mp3Splt](http://linuxtoy.org/archives/mp3splt.html) 使用）。

合并超过两个以上的 MP3
也是可以的，只需在上面的命令末尾直接追加相应文件即可。

有合就有分，分割 MP3 可以选用 [LinuxTOY](http://linuxtoy.org) 以前介绍的
[Mp3Splt](http://linuxtoy.org/archives/mp3splt.html)。
