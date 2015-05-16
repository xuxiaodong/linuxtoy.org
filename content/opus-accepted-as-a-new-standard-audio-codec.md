Title: Opus 音频编码正式标准化
Date: 2012-09-13 17:29
Author: lovenemesis
Category: News
Tags: Mozilla, opus
Slug: opus-accepted-as-a-new-standard-audio-codec

先前提到过在 [Firefox 15 中引入的 Opus
音频编码](http://linuxtoy.org/archives/firefox-15-beta.html)被正式接纳为新的国际互联网音频标准。

Opus 由 Mozilla 和 Xiph.org 主导开发，得到了 Skype 和 Broadcom
的帮助。它完美融合了 Skype 的 SILK 低比特率语音编码和 Xiph.org 的 CELT
的高比特率低延迟音乐编码技术，实现了一种压缩音频编码覆盖从语音通话到高质量音乐流的目标。且看下图

[![](http://lt-file.b0.upaiyun.com/files/2012/09/opus-quality.png "opus-quality")](http://lt-file.b0.upaiyun.com/files/2012/09/opus-quality.png)

音质方面，在**低比特率状态下继承了 SILK
的优秀表现，在高比特率下听音测试表明也胜过
HE-AAC，且具有低延迟的特性**。

Opus 可以封装到现有的 Ogg 容器中，通过指定 `codec` 来和 vorbis
编码的音频区分，推荐使用扩展名 `.opus` 。

**此外最重要的是 Opus 将被作为 WebRTC
的一部分应用在未来的网络视频聊天中。**

目前 [GStreamer Bad Plugins
0.10.23](http://gstreamer.freedesktop.org/news/#2012-02-21T14:00:00Z) 和
[VLC 2.0.4](http://trac.videolan.org/vlc/ticket/7185)
已经提供了对该音频编码的支持。[Fedora](https://apps.fedoraproject.org/packages/opus)
及 [Ubuntu](https://apps.ubuntu.com/cat/applications/libopus0/)
仓库中也已经打包了相关的编码包和开发工具。

[Opus 英文维基百科](http://en.wikipedia.org/wiki/Opus_(audio_format))

[Opus 官方站点](http://www.opus-codec.org/)

*消息来源：*[Ars
Technia](http://arstechnica.com/gadgets/2012/09/newly-standardized-opus-audio-codec-fills-every-role-from-online-chat-to-music/)
