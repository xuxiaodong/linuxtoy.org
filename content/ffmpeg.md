Title: FFmpeg — 屏幕录制工具
Date: 2006-06-16 22:08
Author: toy
Category: Apps
Slug: ffmpeg

在我看来，FFmpeg
绝对是一个很酷的应用。那么，它究竟有什么用呢？简单地讲，FFmpeg
相当于一个屏幕录像机。你可以使用它将屏幕上的操作过程录制下来，然后再将其播放给别人看。我们可以利用它制作教学影片、产品演示等等。以下是补丁、编译、使用步骤。

1.下载源码包

`wget http://linuxtoy.org/ files/src/ffmpeg-0.4.9-p20051216.tar.bz2`

2.解压

`tar xvjf ffmpeg-0.4.9-p20051216.tar.bz2`

3.转到解压的目录

`cd ffmpeg-0.4.9-p20051216`

4.下载补丁文件

`wget http://i.linuxtoy.org/files/src/ffmpeg-0.4.9-p20051216.diff`

5.应用补丁

`patch -Np1 -i ffmpeg-0.4.9-p20051216.diff`

6.准备编译环境

`sudo apt-get install build-essential xlibs-dev`

7.配置

`./configure --extra-ldflags=-L/usr/X11R6/lib --enable-x11grab --enable-gpl`

8.编译

`make`

9.使用

`./ffmpeg -vcodec mpeg4 -b 1000 -r 10 -g 300 -vd x11:0,0 -s 1024x768 ~/test.avi`

其中，-vd x11:0,0 指录制所使用的偏移为 x=0 和 y=0，-s 1024×768
指录制视频的大小为 1024x768。录制的视频文件为
test.avi，将保存到用户主目录中。其他选项可查阅其[说明文档](http://ffmpeg.mplayerhq.hu/ffmpeg-doc.html)。

如果你只想录制一个应用程序窗口或者桌面上的一个固定区域，那么可以指定偏移位置和区域大小。使用`xwininfo -frame`命令可以完成查找上述参数。

你也可以重新调整视频尺寸大小，如：`./ffmpeg -vcodec mpeg4 -b 1000 -r 10 -g 300 -i ~/test.avi -s 800×600 ~/test-800-600.avi`。

[[via](http://ubuntu.wordpress.com/2006/06/08/how-to-create-a-screencast-in-ubuntu/)]
