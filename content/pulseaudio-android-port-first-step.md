Title: PulseAudio Android 移植初步实现
Date: 2012-05-01 06:47
Author: lovenemesis
Category: Embedded
Tags: Android, pulseaudio
Slug: pulseaudio-android-port-first-step

还记得本站之前报道过的 [PulseAudio 和 Android AudioFlinger
之间的对比](http://linuxtoy.org/archives/pulseaudio-vs-audioflinger.html)么？现在
Collabora 已经初步实现了 PulseAudio Android
版本的基本功能，甚至**包括远程回放**！

通过一个 Wrapper 将对于 Android 原生的 `AudioTrack` 的请求翻译为
libpulse 客户端 API 的格式，PulseAudio 毫无意外的完成了音频回放的任务。

除了之前比对文章中指出的系统占有率和音质方面的优势，使用 PulseAudio
带来的一个额外好处就是系统级别的网络音频传输。而这一部分也已经实现了！

[PulseAudio Android
版本远程音频回放演示](http://youtu.be/o5-phFVfZnQ)([朝内镜像](http://v.youku.com/v_show/id_XMzg5NDgyNzU2.html))

作者 Arun Raghavan 表示下一步的工作是开始迁移 AudioFlinger
的策略配置文件到 PulseAudio
策略配置格式，从而实现按需设备选择和统一化音量调整等功能。

当然，这一切都无需应用程序本身做任何变更，无需修改一行代码就可以实现类似
DLNA 的远程音频回放功能。

[博客原文](http://arunraghavan.net/2012/04/pulseaudio-on-android-part-2/)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTA5NDM)
