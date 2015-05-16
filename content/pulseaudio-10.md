Title: PulseAudio 1.0
Date: 2011-09-28 13:29
Author: lovenemesis
Category: Desktop Stuff
Tags: pulseaudio
Slug: pulseaudio-10

用户态的声音服务器 PulseAudio 发布 1.0 正式版本。

本次发布主要目的是使版本号标识更加明了，下一次的重要变更将使用 2.0
的版本号。同时宣布以后的**版本发布将主要由 Colin Guthrie 完成**，因为
Lennart 目前的精力放在 systemd 上。

主要功能：

-   试验性的基于 DBus 的控制协议。
-   支持音频输入流的独立控制。
-   支持音频原生 Passthrough ，比如高级音响设备。
-   实现回音消除，在 Empathy 3.2
    中已经默认启用。[详细说明](http://arunraghavan.net/2011/08/hello-hello-hello/)
-   再次提供对于 Windows 平台的支持。
-   改善对于 RTP 流的重采样率检测算法。
-   移除 pabrowse 和 libpulse-browse。

[发布公告原文](http://www.freedesktop.org/wiki/Software/PulseAudio/Notes/1.0)

关于 PulseAudio 的设计方面的疑问，可以[参考本站先前对于作者 Lennart
的采访报道](http://linuxtoy.org/archives/interview-creater-of-systemd-and-pulseaudio-lennart.html)。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=OTk0NQ)
