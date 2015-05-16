Title: nas：网络声音服务
Date: 2008-08-31 16:32
Author: hmy
Category: Apps
Tags: NAS
Slug: nas

[撰文/hmy]

nas 即 Network Audio
System。有时候有多个电脑，但是只有一个音响系统。可以在有音响的机器上跑
nasd。然后其他机器通过 8000/tcp 把声音信号发过去播放。nasd
是监听在默认的 8000/tcp 端口。

在客户端，比如用 mplayer 访问 nas 系统，需要在编译 mplayer 的时候支持
nas。然后用下面方法播放：

`# AUDIOSERVER=tcp/10.0.0.2:8000 mplayer -ao nas file.avi`

**参考**

<http://www.radscan.com/nas.html>
