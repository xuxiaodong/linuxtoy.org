Title: youtube-dl：从 YouTube.com 上下载视频
Date: 2006-08-15 09:28
Author: toy
Category: Apps
Slug: youtube_dl

当我们观看 [YouTube](http://www.youtube.com)
上的视频时，难免不碰到漫长等待的情况。这时候，我们可以考虑将其下载后再观看。但手动从
YouTube
上下载视频谈何容易，如果有下载工具帮助我们可能会更好。今天，我就为大家介绍一个专门从
YouTube 上下载视频的小工具——youtube-dl。

youtube-dl 是用 Python 所写的命令行程序，它的使用过程是这样的：

1.下载程序

`wget http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl`

2.让其可执行

`chmod a+x youtube-dl`

3.命令行选项

使用 `./youtube-dl -h` 可以查阅到，常用的有：

*-o　下载视频文件的保存名称  
*-u，-p　用户名和密码，有的视频可能需要 YouTube 网站的注册用户才能下载

4.使用实例

`./youtube-dl http://www.youtube.com/watch?v=AnFUGyvclOw`

这将下载名为 AnFUGyvclOw.flv 的视频文件。

`./youtube-dl -o myvideo.flv http://www.youtube.com/watch?v=AnFUGyvclOw`

这样就会把下载的视频文件以 myvideo.flv 的名称保存。

5.播放视频

使用 mplayer、vlc 等皆可。
