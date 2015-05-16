Title: Skype 2.1 Beta PulseAudio 设置
Date: 2009-09-03 22:31
Author: lovenemesis
Category: Instant Messenger
Tags: pulseaudio, Skype
Slug: skype-21-beta-pulseaudio-configuration

前段时间 Skype 放出了 Linux 2.1 Beta 版本，带来了对于 PulseAudio
的支持。在论坛上看到很多朋友由于 PulseAudio
设置不当遇到无法正常通话或者程序崩溃的情况，在此分享下本人的 Skype
音频设置。

以下内容在 Fedora 11 i686 PulseAudio 0.9.15 测试通过。

首先，强烈建议还原 PulseAudio 到已有的设置。 PulseAudio
做为一个新生的音频服务器，尚存在着一些不完善的地方，于是网上流传着各种
PulseAudio 的 Tweak 指南。其中的部分 Tweak 可能会影响 Skype 和
PulseAudio 的沟通。在此建议若不是有特别需要的话，请将 PulseAudio
还原到发行版默认配置。

然后，参看截图

[![](http://i.linuxtoy.org/images/2009/09/screenshot-options-400x232.png)](http://i.linuxtoy.org/images/2009/09/screenshot-options.png)

中文版的位置是在“选项”-“声音设备”-“允许 Skype
自动调整我的混音器级别”。**关键：将鼠标指针指向的那个位置取消勾选。**

最后，依次进行 Make a test sound 和 Make a test call
，进行声音测试。如果一切正常，那么恭喜你，Skype 2.1 Beta 和你 PulseAudio
将和平共处了～

[Skype Linux Community 原帖  
](http://forum.skype.com/index.php?showtopic=411431&view=findpost&p=1891341)
