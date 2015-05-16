Title: 给 iPod 转视频的脚本
Date: 2008-08-13 09:53
Author: toy
Category: Apps
Tags: iPod, Nautilus, Scripts
Slug: toipod-script

[撰文/bones7456 <[欢迎访问作者的
blog](http://bones7456.blog.ubuntu.org.cn)>]

由于新买了个 iPod touch，这几天认真钻研了下它的视频格式，搞了个 Nautilus
脚本，使用 Mencoder 做后端。以后想把某个视频文件转成 iPod
的格式的话，直接在 Nautilus 里面右键点文件-脚本-toIpod 就可以搞定了。

脚本的特点：

-   借助 MPlayer 的强大，支持 N 多的源格式 (已测试: avi rmvb mov flv)。
-   支持 srt/ass 格式的外挂字幕。
-   自动缩放画面比例到适合 ipod touch 的 480*320，如果是 ipod shuffle
    之类的话，可以自己修改下脚本。
-   可视化的进度提示
-   转换速度较快
-   默认保存到当前目录，可修改脚本，输出到统一目录，方便管理。会自动加上
    \_ipod.mp4 的后缀名。

使用方法，从[这里下载](http://linuxfire.com.cn/~lily/toIpod)该脚本，保存到
~/.gnome2/nautilus-scripts/，并加可执行权限。

截图：

![iPod](http://i.linuxtoy.org/i/2008/08/ipod.png)

PS:
如果压缩出来的字幕有乱码，请参照[我以前的文章](http://bones7456.blog.ubuntu.org.cn/2008/08/04/mencoder_srt/)，建个
~/.mplayer/mencoder.conf 文件，写上一行 subcp=cp936 就好了。

[[原文链接](http://bones7456.blog.ubuntu.org.cn/2008/08/12/toipod/)]
