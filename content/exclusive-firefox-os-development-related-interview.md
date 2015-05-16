Title: 【独家】Firefox OS 应用开发独家访谈
Date: 2013-09-24 13:50
Author: lovenemesis
Category: Featured
Tags: firefoxos
Slug: exclusive-firefox-os-development-related-interview

如早先所述，在下前往参加了 [Firefox OS
应用开发课堂西安站](http://linuxtoy.org/archives/firefox-os-app-workshop-xian.html)的活动，并利用活动间隙针对
Firefox OS 相关问题采访了 Mozilla 的社区经理和工程师。

下文中 `Q` 即黑日白月，`A` 则为 Mozilla 社区经理 Rachel Zhang 或工程师
Wei Deng。

*Q: 现在搭载 Firefox OS
的手机已经在部分地区上市了，消费者/运营商/合作伙伴的反响如何？*

**A:** 现在搭载 Firefox OS
手机的确已经在南美和欧洲国家上市了，同时ZTE也在eBay开始向全球多个国家和地区销售ZTE
OPEN，具体发售国家请前往eBay网站查询。但是主要面向对象还是开发者和手机发烧友，普通消费者购买还相对较少，但是从今年6月在上海举办的亚洲移动通信展的表现来看，消费者对于Firefox
OS手机的兴趣也非常浓厚

*Q: 我们知道 Firefox OS
目标是人均收入较低的国家和地区，走平价亲民路线。按照这个定义，中国也属于此范畴。但似乎中国也已成为高端智能手机的主要消费国。Mozilla
对于中国市场怎么看待？有进入的计划呢？*

**A:**
的确中国市场的情况比较特殊，市场中存在着大量低端智能手机和山寨机。Mozilla
对于中国地区的计划现在还不便透露。

*Q: 全球各地的像这种形式的 Firefox OS 应用开发工作室已经举办了不少。相比
Mozilla 也得到了不少开发者的反馈。开发者最常问及的问题是什么？对于
Firefox OS 最大的期望又是什么呢？*

**A:** 开发者通常首先会问到什么时候手机能上市。（大笑

对于开发者特别是 Web 开发者来说，Firefox OS
对于他们最大的吸引力就是能运用现有的 Web
开发知识构建移动平台的应用软件，而无需再重新学习，并且所开发的应用可以跨平台使用。

*Q: 对于和 Firefox OS 一样被视为移动操作系统领域变更性力量的 Ubuntu for
Mobile 在前段时间通过 Edge 的 Crowd Funding
活动获得了媒体的大量关注，Mozilla 对此怎么看？*

**A:** Mozilla 秉承 Openness, Innovation, Opportunity
的理念，欢迎任何进入移动操作系统领域的选手，因此我们并不把 Canonical
当作竞争对手。同时我们相信我们前卫的理念对于开发者也是有相当吸引力的。

*Q: 相比 Android 初期，Firefox OS
现在在传统渠道诸如书籍方面的材料还比较少，似乎 MDN
是唯一的开发参考资料。Mozilla
有没有计划发展更多的培训或参考资料方面的合作，比如 Thought Works？*

**A:** Firefox OS 或者说 Boot 2 Gecko 计划对于 Mozilla
的工程师团队是一个巨大的挑战，在过去的两年里以及未来的一段时间内，我们将主要集中精力在架构设计和代码的编写上，文档还在不断的更新和完善当中。
MDN 上的文档资料一直是及时更新的，可以反映 Firefox OS
的最新发展状况，是开发者们的第一选择。

此外 Firefox OS
还处于早期阶段，部分内容可能变化的比较快。而传统渠道诸如书籍出版周期比较长，很有可能到最终读者拿到手的时候，其中某个章节的内容已经和撰写时大为不同了。所以当前我们依然推荐以
MDN 的资料为准。  
顺便提一下，MDN
是一个开放的社区，欢迎有中文地区的贡献者加入进来帮助我们完成其中内容的本地化工作。

*Q: 当下 Emscripten 的配置搭建还是比较复杂的，特别是对于 Win 平台来说。
Mozilla 有没有打算针对出品相应的 Toolkit 解决这个问题呢？*

**A:** 的确如此，不过 Emscripten 当前面向的群体还是具有相当技术水平的
Geek，一般开发者暂时还没有使用 Emscripten 构建 Firefox OS
应用的需求。对于这些人来说，搭建 Emscripten 并不是很难的事情。

当然，Emscripten 是一个开放的项目，有这样的需求完全可以前往其站点提交
Feature
Request。相信有能力的社区贡献者会响应此需求或者提供更简便的解决方案。

*Q:得到三星/英特尔支持 Tizen 系统也宣称是使用了 Web
技术移动操作系统，相比 Tizen， Firefox OS 有什么不同和优势呢？*

**A:** 在 Firefox OS 平台上基于 HTML5 的 Web
应用开发是一等公民，我们从一开始就没有考虑像 Tizen 那样亦支持使用 Qt
开发的本地原生应用。因为我们深信通过在相关项目诸如 Web API
方面的努力，纯粹的 Web 应用可以实现达到甚至超过本地原生应用的性能。

*Q: 当下 Firefox OS 在 Gonk 层大量应用了来自 Android
的技术，其中有些部分并不怎么开放，比如闭源 GPU
驱动。在未来有没有考虑使用开源显卡驱动以及 Wayland？*

**A:** 这个问题要分开看。对于 Mozilla
来说，其实完全不介意将这部分代码开放，主要是硬件厂商在这一点上比较坚持。它们担心在开放了驱动源码后竞争对手从中可以窥视出其硬件设计，对其形成威胁。

当下 Mozilla 的精力还是主要集中在完善 Firefox OS
平台的实现，暂时没有大力推进开源显卡驱动及 Wayland 计划。

*Q: 多问一下，最近 Intel 推出了适用于手机的 Bay Trails 芯片，其中 GPU
驱动部分是开源的。有没有考虑过相比 ARM 平台更为开放的 X86 微型化平台？*

**A:** 实际上最近 Firefox OS 底层 Gonk 部分对于 X86
的支持已经开始了，不过究竟未来会不会推出基于 X86 的 Firefox OS
手机现在说还为时过早。

*Q: 最后一个问题，什么时候能在国内买到 Firefox OS 开发机？*

**A:** 一般人都第一个问。（大笑

当下 Firefox OS
开发机已经在其他国家和地区上市了，你也可以在今天活动现场看到，机子本身已经没有什么问题了。由于我们特殊的国情，完成一系列审批手续需要较为复杂的过程。不过想要尝鲜的朋友可以先从
eBay 中预定，已经可以寄往中国。

[部分现场活动照片](https://plus.google.com/photos/117914792059519512651/albums/5927072382672140129)([朝内镜像](http://photo.weibo.com/1139341480/albums/detail/album_id/3626050444762986))
