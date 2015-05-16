Title: 通过 PulseAudio 实现局域网音乐播放
Date: 2014-12-03 23:01
Author: lovenemesis
Category: Music Player
Tags: pulseaudio
Slug: local-network-audio-playback-via-pulseaudio

PulseAudio
的一大特点就是支持网络音频流。经过几年的发展，现在通过简单的鼠标点击，即可实现局域网内远程音乐播放，甚至支持
Android 手机。

#### PulseAudio 服务器配置 ####

恕我愚钝，通过[这篇报道](http://fedoramagazine.org/how-to-play-audio-on-another-fedora-system/)才知道有了
`paprefs` 这样便捷的图形化配置工具，使得 PulseAudio
音频服务器的网络流配置十分方便。在此以 Fedora 21
为例简单介绍下如何实现两个使用 PulseAudio 做为音频服务器吧：

1.
从软件仓库安装[图形化配置工具](https://apps.fedoraproject.org/packages/paprefs)和
[PulseAudio 局域网 UPnP
支持](https://apps.fedoraproject.org/packages/pulseaudio-module-zeroconf)：

`sudo dnf install paprefs pulseaudio-module-zeroconf`

2. 安装完成后，启动 `paprefs` ，在 “Network Server”
选项卡内允许来自网络的请求访问本地音频设备，允许设备在网络可见，同时建议勾选“允许匿名访问”。

[![network-server](http://lt-file.b0.upaiyun.com/files/2014/12/network-server1-300x158.png)](http://lt-file.b0.upaiyun.com/files/2014/12/network-server1.png)

3. 若是还想允许手机访问的话，可以也一并勾选了下面两个 DLNA/UPnP
相关的选项。

到这里，本机的 PulseAudio
音频服务器配置完成且已经发布到局域网内，可以供其他主机或设备访问了。下来分别针对
Linux 发行版和 Android 手机客户端的配置进行说明。

#### 安装有 Linux 发行版的电脑 ####

1. 在对于局域网内的其他使用 Linux 发行版的机子，依据各自发行版的情况安装
`paprefs` 和 PulseAudio 的 UPnP
组件即可。无需和做为服务器的发行版一致，只要是使用 PulseAudio
做为音频服务器都可。

2. 类似的，启动 `paprefs`，在 “Network Access”
选项卡里勾选第一项，将网络中的可见音频设备显示在本地设备列表中。

[![network-access](http://lt-file.b0.upaiyun.com/files/2014/12/network-access-300x158.png)](http://lt-file.b0.upaiyun.com/files/2014/12/network-access.png)

3.
之后打开“控制中心”，选择“声音”，此时在“输出”选项卡中应该可以看见局域网中的服务器上的声音设备了，选择它即可。

[![audio-device](http://lt-file.b0.upaiyun.com/files/2014/12/audio-device-300x222.png)](http://lt-file.b0.upaiyun.com/files/2014/12/audio-device.png)

4. 接下来的事情就很简单了，打开 Rhythmbox 或者任何支持 PulseAudio
输出的音乐播放软件，让音乐响起来！此时声音即从配置为服务器的主机发出，而非本机。

#### Android 系统智能手机 ####

很遗憾 [Android 系统目前还是用的
AudioFlinger](https://linuxtoy.org/archives/pulseaudio-vs-audioflinger.html)，所以无法类似电脑那样直接唤起
PulseAudio 做为客户端。不过如果您在服务器配置时勾选了 DLNA/UPnP
选项，亦可以将 PulseAudio 服务器当作 [DLNA
媒体渲染器](linuxtoy.org/archives/linux-dlna.html)
处理，实现局域网音频回放。

目前常见的国外品牌（Samsung、HTC、LG 等）的 Android
智能手机的内置音乐播放器中都增加了 DLNA 服务支持，若是您的手机固件不包含
DLNA 服务支持，可以使用
[BubbleUPnP](https://play.google.com/store/apps/details?id=com.bubblesoft.android.bubbleupnp)
实现。在此以 Sony Xperia 系列手机上的 Walkman 音乐播放器为例演示：

1. 在电脑上完成服务器端配置后，在 Xperia 上打开 Walkman
播放器。点击右上角的 **Throw** 图标。

2. 在可选设备列表中，选择新出现的那个 Audio/Video 设备。

3. 之后播放的歌曲即从配置了 PulseAudio 服务的电脑中飘出。

具体方式如下图所示：

[![throw](http://lt-file.b0.upaiyun.com/files/2014/12/throw-140x250.png)](http://lt-file.b0.upaiyun.com/files/2014/12/throw.png)

#### 总结 ####

PulseAudio
音频服务器提供很多便捷的功能，如果您有所注意的话，它甚至还提供对于
AirTunes 设备的访问支持。如果有这方面条件的童鞋，不妨在评论中分享下配置
PulseAudio 及 AirTunes 的经验。
