Title: lrcdis: 外挂式显歌词
Date: 2009-03-12 18:00
Author: toy
Category: Apps
Tags: lrcdis
Slug: lrcdis

lrcdis 是由
[xiooli](http://joolix.com/)、solcomo、[bones7456](http://li2z.cn/category/lrcdis/)、[oldherl](http://www.oibh.org/?78103)
等同学编写的一个 Bash
脚本，该脚本允许你以外挂方式来显示歌词。目前，lrcdis 支持 Linux
下的大多数音乐播放器，包括 Rhythmbox、Amarok、Quod
Libet、Exaile、Audacious、MPD、MPlayer、MOC 等等。

![lrcdis](http://i.linuxtoy.org/images/2009/03/lrcdis.png)

首次运行 lrcdis，它将在 $HOME/.config 目录下建立配置文件
lrcdis.conf。通过此文件，你可以决定歌词以何种模式显示（有
CLI、OSD、notify、fifo
等选择）、下载歌词的保存位置、使用哪一个音乐播放器等。

当你使用上述音乐播放器中的一款播放歌曲时，lrcdis 将根据该歌曲的 ID3
标签或文件名来自动下载歌词，并以你指定的模式显示，整个过程由脚本自动完成，无需你额外操心。

lrcdis 可从 Google Code 下载。

[lrcdis](http://code.google.com/p/lrcdis/)
