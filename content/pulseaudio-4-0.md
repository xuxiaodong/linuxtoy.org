Title: PulseAudio 4.0
Date: 2013-06-04 12:16
Author: lovenemesis
Category: Desktop Stuff
Tags: pulseaudio
Slug: pulseaudio-4-0

被广泛应用的用户态声音服务器 PulseAudio 发布 4.0
版本，改善低延迟算法以及跟 JACK 同时运行时的设备交接过程。

相比之前 [3.0 版本](http://linuxtoy.org/archives/pulseaudio-3-0.html)
本次更新有如下变化：

-   改善算法，在低延迟环境下事件处理速度更快。
-   改善在通用设备和 ARM NEON 的上混音实现。
-   将默认重采样器换为 speex-float-1 以降低 CPU 占用。
-   重新编写了蓝牙设备处理模块，提高了稳定性并降低了维护复杂性。
-   平滑了与 JACK 同时运行时设备交接的过程，可以更好的相处。
-   新增音量自动降低模块（编者注：类似 Android
    上在播放音乐时对来电音量的处理），当高优先级的音频流接入时自动降低其他音频流的音量，当高优先级音频流结束时自动恢复其他音频流音量。音频流优先级由客户端决定。该模块并未默认加载。
-   修复了噪音消除器的一些架构问题。
-   为命令行工具增加在 Bash 和 Zsh 下的自动补全。
-   修复了在 Solaris 和 OS X 平台下的问题。
-   大量的文档和本地化更新。

[Tar
包下载](http://freedesktop.org/software/pulseaudio/releases/pulseaudio-4.0.tar.xz)

SHA1 码：`9f0769dcb25318ba3faaa453fd2ed0c509fa9c5c`

[详细更新日志](http://www.freedesktop.org/wiki/Software/PulseAudio/Notes/4.0/)

[邮件列表发布公告](http://lists.freedesktop.org/archives/pulseaudio-discuss/2013-June/017467.html)
