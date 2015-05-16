Title: 短消息：Broadcom Crystal HD & Android Trojan
Date: 2011-01-02 11:50
Author: lovenemesis
Category: News
Tags: broadcom, geinimi
Slug: briefing-broadcom-crystal-hd-and-android-trojan

FFMpeg 及 Mplayer 实现 **Broadcom Crystal HD
高清硬件解码**支持；**Android 木马** Made in China。

[Broadcom Crystal
HD](http://www.broadcom.com/products/features/crystal_hd.php)
是一款独立的高清硬件解码方案，通过 PCIE 接口链接。在 2010 年间 Gstreamer
、Xine 和 XMBC 已经实现了对 **Broadcom Crystal HD
加速芯片**的支持，但是直到最近应用最为广泛的 FFMpeg 解码器组及 Mplayer
播放器在 **70015 加速芯片**(非淘宝上所销售的 70012
版本！)支持才实现。根据作者的博客，目前已经实现了除去 Divx 3.11 以外的
H264、 VC1 等众多格式的支持。值得一提的是相比 NVIDIA VDPAU 的解决方案，
**Broadcom Crystal HD 的 [Linux
驱动程序](http://www.broadcom.com/support/crystal_hd/)是开源**的，并且不限制系统
GPU 及 CPU 的限制。
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=ODk2Ng)
[详细阅读](http://intr.overt.org/blog/?p=117)

一款来自中国的木马会感染部分 Android
平台应用程序，将用户的通讯录、IMEI码及 SIM
卡号码等敏感信息发送至远程服务器。感染方式与 Win
平台上的木马通过网络传播不同，这款称之为 **Geinimi
的木马需要与目标程序进行重新封装**才可，并且在**安装时会请求不限制权限**。**中文应用软件商店中的
Monkey Jump 2, S#e#x Positions, President vs. Aliens, City Defense 及
Baseball Superstars 2010 已被确认感染，Google 官方 Android Market
中的这些游戏不受影响。**在此提醒诸位使用 Android
平台手机的朋友**在安装第三方来源的软件时一定要注意权限！**
[消息来源](http://www.h-online.com/open/news/item/Android-trojan-collects-personal-data-1162008.html)
[详细阅读](http://blog.mylookout.com/2010/12/geinimi_trojan/)
