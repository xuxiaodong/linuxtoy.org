Title: 复活百度 MP3 下载机器人脚本
Date: 2009-03-04 11:30
Author: toy
Category: Apps
Tags: Baidu, MP3
Slug: baidu-mp3-download-script

[撰文/[albert748](http://cookinglinux。cn/)]

以前的那些 MP3 下载脚本已经早就不能用了，看着百度 MP3
的歌曲目录眼馋得很，又懒得去一个一个下载。虽然我看不懂
JS，不过没有关系，借助前辈们的代码，做一些换血，重新复活这个脚本。在此感谢他们！

这个脚本使用 Python+shell 实现。shell 脚本是专门用来解密百度 MP3
链接的，Python 是下载管理。

1.  删除了下载函数，我觉得不太稳定，改为调用 wget 下载。
2.  修改了 Python 获得真实链接的方式，改为获取 shell 的输出。
3.  使用 mid3iconv 工具一步到位转换编码，不然 Linux 下又要乱码满屏飞了。

需要安装 mid3iconv 和 wget：

`sudo apt-get install python-mutagen wget`

如果以后有空的话，再写一个 GUI 吧。

[Baidu MP3 下载脚本](http://cookinglinux.cn/bai-mp3-downloader.html)
