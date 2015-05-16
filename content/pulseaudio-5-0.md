Title: PulseAudio 5.0
Date: 2014-03-04 16:11
Author: lovenemesis
Category: Desktop Stuff
Tags: pulseaudio
Slug: pulseaudio-5-0

音频服务器 PulseAudio 发布 5.0 版本，带来了对 BlueZ 5.0 的支持。

新版本的变化有：

-   对于 BlueZ 5.0 A2DP 的支持。
-   重新实现了 Tunnel 模块。
-   提供了针对原生 systemd-journal 日志系统的接口。
-   不再依赖 libbluetooth ，gettext 换而使用上游 0.18.1+ 而非 Glib
    版，依赖的 alsa 版本降为 1.0.19。
-   大量错误更新。

[详细更新日志](http://www.freedesktop.org/wiki/Software/PulseAudio/Notes/5.0/)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTYxOTg)

**PS:** 从中看出的一个“有趣”细节是 BlueZ 5 中移除了负责蓝牙音频输入的
HSP 和 HFP 支持，且并不向后兼容 BlueZ
4。由于一些沟通的问题，部分项目和发行版可能在未了解变化的前提下就升级至
BlueZ 5 版本，导致用户的蓝牙配置失效或者功能丢失。该版本 PulseAudio
对于蓝牙音频输出使用 BlueZ 5
A2DP，而对于有语音通话需求的蓝牙耳麦仍将继续使用 BlueZ
4。在下一个版本中将通过 oFono 代理实现 BlueZ 5 下的蓝牙耳麦支持。
