Title: GPL 与 Apple App Store
Date: 2011-02-09 20:15
Author: lovenemesis
Category: Reviews
Tags: appstore, GPL
Slug: gpl-and-apple-app-store

从 "VLC for iPhone 下架 iOS App Store" 说到 "SPlayerX 在 Mac App Store"
开售。

不管消费者因为什么原因购买了 Apple 的桌面或者移动产品，他/她都不得不面对
QuickTime 那极为有限的视频回放功能。于是各种 iOS 和 OS X
平台上的视频回放解决方案应运而生。此时 Apple “首创” 的 App Store
就成了用户获取第三方视频回放软件的流行方式，然而这个过程并不是皆大欢喜的，尤其是对于使用
GPL 分发的开源视频播放器来说。

**背景阅读：**

-   [VLC for iPhone 被从 iOS App Store
    移除](http://www.h-online.com/open/news/item/VLC-iOS-developers-fight-back-1167821.html)。
-   [VLC for iPhone
    开发者回应质疑。](http://www.h-online.com/open/news/item/VLC-iOS-developers-fight-back-1167821.html)
-   [射手影音登陆 Mac App
    Store，定价1.99美元](http://blog.splayer.org/index.php/2011/02/splayerx-landing-on-mac-app-store/)
    。
-   [MPlayerX
    作者谢绝射手影音的捐赠。](http://blog.splayer.org/index.php/2011/02/splayerx-landing-on-mac-app-store/#remark1)

由于在下并不是任何 Apple 软件开发者or用户，所以对于具体 App Store
的规则并不十分清楚，**在此希望有 Apple
平台软件开发的朋友进一步说明**。不过在经过咨询后，得到他人指点前往阅读了
[Adium](http://adium.im/) (OS X Pidgin-like IM based on Libpurple Port)
[邮件列表的相关讨论](http://adium.im/pipermail/devel_adium.im/2011-January/007973.html)。在此与诸位朋友分享一下：

简单来讲，在 App Store 中分发 GPL 协议的软件产品面临如下问题：位于 App
Store 中的软件的再分发受到严格限制，该项和 GPL
协议中无条件的分发相冲突。

于是若是要在 App Store 中分发基于 GPL
软件产品库的话，所基于软件库的作者(比如 ffmpeg 的贡献者们) 可以：

-   发起侵权诉讼。
-   依据 GPL 中所赋予的权利剥夺该代码使用者的使用权。

不过解决方法也是存在的：

-   向每个贡献者发起授权请求，获得在 App Store
    分发的授权。**难点：**在拥有庞大贡献者团体的大型项目一一通知每个人几乎不可能，并且只要一个人不同意就无效。
-   请求 Apple 修改 App Store 的软件分发条例。**难点：**无论从 Apple
    的历史和现今的盈利模式来看，修改该条例的可能性为零。

于是乎，若是要在 Apple App Store 上合法的分发自己的 GPL
程序，有如下要点需要注意：

-   收费是允许的，但是**别忘记提供获取源代码的方式**。
-   既然是 GPL
    软件，就要注意**不要在分发时包含没有源代码的二进制文件**。
-   如果自己的 GPL 程序使用了其他 GPL
    组件，**需要获得组件作者授权才可以**。
-   **避免使用由大型社区维护的 GPL
    组件**，因为一一获得组件作者授权近乎不可能。

希望该小短文对于希望对 Apple App Store
的开源软件开发者起到一定的提醒作用，同时期待有朝一日能在与 GPL
协议兼容的 Android Market 上见到你们的作品。
