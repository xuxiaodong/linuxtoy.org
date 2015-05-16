Title: Ubuntu for Android
Date: 2012-02-22 17:21
Author: lovenemesis
Category: Distros
Tags: Android, Ubuntu
Slug: ubuntu-for-android

Canonical 正式宣布针对手持设备厂商的 Ubuntu for Android 方案。

Ubuntu for Android 宣称具有：

-   为接入扩展底座的 Android 手机提供完整的桌面生产力套件。
-   可以容易的和当前正在开发的 Android 手机整合。
-   具备经 Adobe, Citrix, VMWare 授权的商业应用程序。
-   可以提升多核 CPU 和多核 GPU 手机的销售。
-   加快对于 4G 网络的接纳程度。
-   Canonical 和 Linaro 一起提供领先的 Linux ARM 支持。
-   目标是企业级瘦客户端以及新近的“第一台个人电脑”市场（意指个人拥有的第一台电脑）。
-   Ubuntu 和 Android 运行同一个内核，同时运行并访问存储数据。

基本硬件要求：

-   运行 Android 2.3+ 系统。
-   **双核 1Ghz CPU**。
-   显卡具备**支持 Open GL, ES/EGL 的 X Windows 驱动**。
-   2GB 的操作系统镜像空间。
-   具备**辅助视频缓存的 HDMI 输出**。(PS: 指的支持同时手机屏幕和 HDMI
    双屏显示，并非常见于朝内平板上的单一 HDMI 输出)
-   支持 USB Host 模式
-   512M 内存。

[视频演示](http://youtu.be/AyeFcldavTk)([朝内镜像](http://v.youku.com/v_show/id_XMzU1MjQ3OTIw.html))

片中使用手机为 [Moto Atrix
4G](www.motorola.com/Consumers/US-EN/Consumer-Product-and-Services/Mobile-Phones/Motorola-ATRIX-US-EN)。

看完官方的宣传文字，来看看**非官方的 FAQ** 吧～

**Ubuntu for Android 不是一个 Android 程序，无法直接以 APK
的方式安装到现有手机上。**它需要和 Android ROM
深度集成，也就是为何它的**主要面向对象是手机制造商**，一般用户无法像 PC
版本那样只要下载某个压缩包就可以在 Android 手机上使用。

另一方面，由于有对显卡硬件驱动的特殊要求，也**不是一般下游 ROM
打包者(CyanogenMod 等)可以做到**的。由于 Android
使用了自己特有的显示协议，不是所有的 Android 手机的 GPU 都具有满足 Unity
工作需求的 X Windows 驱动。

**Ubuntu for Android 实际效果尚待检验。**原因如下：

-   由于**在接驳扩展底座时 Ubuntu for Android 将和 Andorid
    系统同时运行**，目前给出的硬件配置双核 1GHz + 512M
    内存条件下比较艰难，主要目标应该还是年底会推出的**四核1.5GHz + 2G
    内存的机器**。
-   目前来讲 ARM 处理器的性能甚至和 X86 架构的 Atom
    处理器相比还是孱弱，面对 WebGL 游戏和复杂的 JavaScript
    应用依然力不从心。
-   当下糟糕的 SoC GPU X 驱动支持和性能将影响 Ubuntu for Android
    的部署。当然如果能借此推动厂商改善也未尝不是好事。
-   Ubuntu ARM 架构上的实际应用远没有 Ubuntu X86
    上丰富，最重要的办公套件 LibreOffice 缺席（有 KOffice 系列，但是尚在
    Alpha 阶段），Chromium 的 ARM 也未成熟。甚至 Canonical 宣称的“具备经
    Adobe, Citrix, VMWare 授权的商业应用程序”也是指的在 Ubuntu X86
    平台上，有偷换概念之嫌。

**总结**

尽管 **Ubuntu for Android 所有组件都会依照 GPLv3 或者 LGPLv3
发布**，但是当下它主要针对手机硬件厂商，**而非开源软件社区或者独立开发者**。再次希望接下来能有针对
Android ROM 制作者或者 SoC GPU 驱动社区开发者的更多内容。

It's a good step for Canonical, but not sure if it's a good step for all
Linuxers, at least for now.

[Ubuntu for Android 官方宣传页](http://www.ubuntu.com/devices/android)

[Mark Shuttleworth 博客](http://www.markshuttleworth.com/archives/1011)

**PS:**偶然发现 [Canonical 在 Ubuntu for Android 中将 Rhythmbox 重名为
Ubuntu Music Player，将 Shotwell 重命名为 Ubuntu Photo
Gallery](http://www.ubuntu.com/devices/android/features-and-specs)，不知何故……
