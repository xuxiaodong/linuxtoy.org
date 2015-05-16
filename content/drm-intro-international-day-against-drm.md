Title: DRM 和桌面 Linux 暨国际反 DRM 日
Date: 2012-05-05 14:39
Author: lovenemesis
Category: Featured
Slug: drm-intro-international-day-against-drm

2012 年 5 月 4 日是[国际反 DRM
节日](http://www.defectivebydesign.org/dayagainstdrm/)。那么什么是 DRM
呢？它和桌面 Linux 应用又有什么关系呢？

明确一下，这里所说的 DRM 是 Digital Rights Management
(数字版权管理)的缩写，和 Linux 显示渲染结构中的 [Direct Render
Manager](http://dri.freedesktop.org/wiki/DRM) 不同。

**DRM
是硬件厂商、发布商和版权持有者用来限制产品销售后使用方式的访问控制技术**，目的是**保护版权所有者的合法权益**。  
参考以下应用情景如下：

1.  在 Apple iTunes 中购买的影片类资源仅能在和购买账户相关联的 Apple
    设备上回放。之前购买的 MP3 音乐也有类似限制，现已取消。
2.  EA
    发行的很多游戏，比如《命令与征服4》，必须要联网进行认证后才可进行游戏。
3.  正版蓝光电影需要使用 HDCP 认证的显示设备才能回放。

其中前两种情形分别代表了在内容和应用程序方面执行 DRM
的结果。这样的措施带来了一些问题：

-   为什么通过 iTunes 购买的合法电影不能在我的 Android 设备上观看？
-   为什么玩家不可以在没有互联网连接的时候进行单机游戏？

基于以上的问题，自由软件基金会建议 DRM 称为 Digital Restriction
Management
（数字限制管理）比较合适，认为这些举动已经超出了“保护版权所有者合法权限”所必要的范围了。**DRM
已经成为压制同行业竞争者的手段，严重影响并限制了合法消费者的使用体验。**但是，**自由软件基金会并不反对对于版权内容的合理保护**，实际上，整个开源协议的基石就是基于现有版权保护系统的。

当下桌面 Linux 平台已经具备了一些对于要求 DRM 的内容访问的支持：

-   通过 Adobe Flash 可以在线点播使用 DRM 保护的付费视频。
-   可以通过 Amazon CloudReader 阅读有 DRM 保护的电子书籍。
-   通过序列号方式认证的商业软件如 CrossOver 等工作良好。
-   没有出现类似 SecureRom 之类的过分 DRM 实现。

最开始提到的第三种情况测复杂很多。蓝光播放的特殊性要求从操作系统和配套硬件方面都实现加密，对用户完全不透明。实际上，目前
Win Vista/7 是目前唯一能播放正版蓝光电影的操作系统，微软曾表示在 Vista
开发过程中投入了相当大的精力和结构上的调整满足蓝光的回放要求。**Linux 和
OS X 都由于缺乏操作系统层面对所需 DRM 的支持而无缘**。

鉴于无需操作系统层面支持的 [Linux 正版 DVD 合法回放的软件才由 Fluendo
在不久前实现](http://www.fluendo.com/shop/product/fluendo-dvd-player/)，在未来相当长的时间内恐怕都见不到正版蓝光的
Linux 支持了。

**总结**

桌面 Linux 在仅需应用程序层面的 DRM
随着标准化和跨平台软件的发展在逐步改善，尚未出现 Win 系统上过分 DRM
执行的情况；系统级别的 DRM 则依然遥遥无期。

另外，O'Reilly 为了庆祝今天[无 DRM
图书/视频五折](http://shop.oreilly.com/category/deals/day-against-drm.do)，**仅此一天**。

**参考内容**

[维基百科](http://en.wikipedia.org/wiki/Digital_rights_management)

[ZDNet
报道](http://www.zdnet.com/blog/hardware/can-linux-on-the-desktop-and-drm-ever-coexist/13055)

[H Open
报道](http://www.h-online.com/open/features/Linux-and-Digital-Rights-Management-DRM-746607.html)

**常见问题**

**GPLv3 是反对 DRM 的么？**

GPLv3 实际上并不反对对内容的保护，GPLv3 反对的对于进行反 DRM
工作的程序员限制，如
DMCA（数字千年版权法案）。针对逐渐开始的使用硬件执行 DRM
的一般消费者设备，GPLv3 协议要求厂商在执行 DRM
的同时应该提供用户安装自定义软件的自由。[更多阅读](http://www.zdnet.com/blog/burnette/gplv3-myth-3-gpl-forbids-drm/354)

**现在不是有 Desura 了么？它和 Stream 有什么不同？**

Desura 目前仅是一个分发平台，平台本身并未强制执行 DRM。通过 Desura
分发的游戏实际上可以脱离 Desura 运行的。Steam 则有所不同，它本身具备执行
DRM 的要求和能力，绝大部分通过 Steam 安装的游戏是无法离开 Steam 运行的。

**这是不是意味着 Linux 无法使用蓝光了？**

不是，Linux 依然可以播放无 DRM 的蓝光光碟，并且可以使用一些程序比如 Nero
4 Linux 生成无 DRM 的蓝光光盘，可以在普通的蓝光机上播放。

**PS:** 另外，由于 5 月 4 日的英文 May the Fourth 发音与 Star Wars
中的台词 May the Force Be with You
（愿原力与你同在）十分相近，所以这一天也常被 Star Wars
粉丝庆祝。比如今天 [Amazon
就针对相关周边进行促销活动](http://www.amazon.com/gp/goldbox/ref=cs_top_nav_gb27)。
