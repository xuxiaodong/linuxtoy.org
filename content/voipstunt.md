Title: Linux 下使用 VoipStunt
Date: 2007-06-26 18:53
Author: toy
Category: Tutorials
Slug: voipstunt

很快要出国，最近开始关注比较合算的网络电话，[Skype](http://www.skype.com/)
太贵，很多人都推荐这个：<http://www.voipstunt.com/>，看了一下的确不错，打国内算下来才
5 分钱一分钟，而且前段还是免费的。很多人说 Linux 下不能用
VoipStunt，但是我看到它提供了 sip 的访问，想想 Linux 下支持 sip
的东西不少，应该没问题，于是注册了账号，充了 5 欧元，开始折腾。

首先想到 Ubuntu 自带的那个
[Ekiga](http://ekiga.org/)，但这玩意太让我失望了，pc-phone
功能居然只能用 Ekiga.net
自己的账号才开放。搜了搜新立得，找到了这么个东西：[Twinkle](http://www.twinklephone.com/)，试了一下果然可以完美支持
VoipStunt（指电话功能，看余额什么的是不成）。

设定如下图（NAT 设置请根据自己的网络类型设定，如需要 Stun，服务器是
Stun.Voipstunt.com）：

[![VoipStunt](http://i.linuxtoy.org/i/2007/06/voipstunt_s.jpg)](http://i.linuxtoy.org/i/2007/06/voipstunt.jpg)

其他没什么可设定的，如果有防火墙的，自己去 VoipStunt
网站看需要打开哪些端口，另外如果你遇到 alsa
不能用，一用软件就死的情况，请都设定成 oss，然后平时开始注意积累 rp。

Twinkle 功能还算丰富，应该可以支持其他的 sip
服务商，大家可以试试看，另外这个是有电话本的，就在拨号键左边，别漏了。

[撰文/Matri Ning]
