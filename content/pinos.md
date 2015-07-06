Title: Pinos：实现摄像头共享
Author: lovenemesis
Date: 2015-07-06
Category: Desktop
Tags: pinos
Slug: pinos
Summary: 当下桌面 Linux 实现视频聊天或屏幕录制的应用不少，但是能做到将屏幕和摄像头捕获内容同时捕获的却没有几个。Pinos 既是一个将在 Fedora Workstation 中引入的实验性方案，尝试解决这个问题。

Pinos 想要解决的问题和当初 PulseAudio 的类似：

1. 允许多个应用共享摄像头资源
2. 提供方便上层应用开发使用的 API

具体来说包括：

* 允许在多个不同的应用程序之间快速切换摄像头设备，或者将多个来源不同的视频流合并成一个
* 支持包括屏幕桌面在内的多类型视频来源
* 提供良好的 GStreamer 集成
* 为了方便实际应用，提供简单的音频处理

那么对于未来的 Fedora Workstation，Pinos 能带来哪些看得见摸得着的改善呢？

* GNOME 内嵌的屏幕录像可以通过 Pinos 实现一边录制屏幕，一边录制来自摄像头的视频和声音，这点对于录制网上教学视频十分方便，减少了后期制作的麻烦
* 提供对于沙箱化应用的视频输入设备访问支持，当下直接访问 V4L2 内核 API 的方式并不适合沙箱化应用

由于尝试解决类似的问题，Pinos 原本叫 PulseVideo，不过现在依据主要作者 Wim Taymans 家乡一个附近小镇的命在改叫 Pinos, Wim Taymans 同时也是 Gstreamer 的联合创始人之一。

[初步源代码](http://cgit.freedesktop.org/~wtay/pinos/)

[更多详情及消息来源](https://blogs.gnome.org/uraeus/2015/06/30/introducing-pulse-video/)