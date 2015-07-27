Title: Plasma Mobile & Ubuntu Phone
Author: lovenemesis
Date: 2015-07-26
Category: Embedded
Tags: kde, ubuntu
Slug: plasma-mobile-and-ubuntu-phone
Summary: 上周末 KDE 社区发起了它们的智能手机操作系统，同时关于 Ubuntu Phone 的先期报道也浮出了水面。

根据[KDE Dot](https://dot.kde.org/2015/07/25/plasma-mobile-free-mobile-platform)上的消息，这款名为 [Plasma Mobile](http://plasma-mobile.org/) 的移动操作系统目标是提供一个“自由、用户友好、尊重隐私且高度可定制化的手机操作系统”。

从其官网有限的内容看，它使用了 libhybris 实现利用厂商针对 Android 系统提供的图形驱动，但是上层使用 Wayland 作为显示服务器。现阶段它可以通过 `apt-get` 的方式安装部分针对屏幕优化过的 Qt5 程序。除了原生 Qt5 程序以外，它的路线图上还标明了**未来会支持 Android、Ubuntu Quick、GNOME 等各类应用程序**。目前官方给出了适用于 Nexus 5 的试验镜像。

KDE 社区之前对于移动版的关注点一直是面向平板的 Plasma Active，只可惜那款曾经叫做 Spark 的众筹平板因为种种原因胎死腹中了。只是原文评论中不断有人问及的如何做到 Android 应用支持这个问题上，开发者闪烁其词的方式让人感觉不是那么安心啊。在此衷心希望这次能有所结果，当下来看开发者目标宏大，不知执行起来如何了。

再看可以说半个同门兄弟的 Ubuntu Phone（核心技术同样是 libhybris 及 Qt5）。搭载 Ubuntu Phone 系统的魅族 MX4 开发板近期在欧洲市场上市了，[Business Insider](http://www.businessinsider.com/meizu-mx4-ubuntu-edition-review-2015-7)上也给了先期评测报道，一切符合预期：有惊喜，但缺应用。不过作为 Geek 的你和我显然无法满足这个主要面向管理和金融人士的站点的报道。若是您有幸抢到（没错，是要在官网抢的）了搭载 Ubuntu Phone 的魅族 MX4，不妨分享您的感受，可以评论，亦可以发 Pull Request。