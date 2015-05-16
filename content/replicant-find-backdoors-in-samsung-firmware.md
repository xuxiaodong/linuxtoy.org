Title: Replicant 发现三星手机固件植入可疑后门
Date: 2014-03-13 11:58
Author: lovenemesis
Category: Android
Tags: replicant
Slug: replicant-find-backdoors-in-samsung-firmware

基于 AOSP 的[自由 Android 衍生版
Replicant](https://linuxtoy.org/archives/replicant-22-sdk.html)
开发者近日发现在 Samsung 出品的 Galaxy
系列手机固件中存在可疑后门程序，允许远程通过调制解调器控制系统 I/O。

简单来说，智能手机上除了运行一般程序及用户交互的应用处理器，还有一个专门负责通讯模块操作的通讯处理器。尽管运行在应用处理器上的系统，比如
Android 是开源或部分开源的，但通讯处理器上的操作系统部分几乎都是来自 SoC
提供的闭源私有固件。本次 Replicant 发现的疑似后门程序正是在这部分。

Replicant 开发者在多款 Samsung
出品的手机上发现其订制版的固件中负责与通讯处理器交互的部分实现了一个私有
IPC，**允许通讯处理器对主系统文件系统执行读、写及删除操作**。由于这个过程在底层且通讯处理器几乎全时运作，**有意者可以实现在用户完全不知情的状况下远程操作文件系统**。新近机型由于
[SELinux
的引入](https://linuxtoy.org/archives/se-android.html)无法访问用户分区的个人数据，但是较早的机型则处于完全暴露状态中，任由他人修改。

Replicant
开发者依据现在掌握的情况，已经对其出品的固件进行了修改，阻断了通讯处理器的文件系统
I/O 操作请求。类似的操作亦可被其他固件比如 CM 在未来采用。

其他要点：

-   受影响机型：**Nexus S**, Galaxy S, Galaxy S2, Galaxy Note, Galaxy
    Tab 2, Galaxy S 3 及 Galaxy Note 2，其中 Galaxy S 的后门甚至以 root
    权限运行。
-   后门藏匿在 `libsec-ril.so` 库文件中，该文件仍被几乎所有当下针对
    Samsung 手机的第三方固件包含，包括 CM。所以**即便使用 CM
    固件，您依然会受到该后门操纵**，直到第三方固件开发人员应用 Replicant
    的补丁。
-   现阶段没有发现该后门的植入有任何法律或用户相关的用途，但不排除在事情进一步明朗之后发现是由于某地区法律上的要求而部署的。

[FSF
官方](http://www.fsf.org/blogs/community/replicant-developers-find-and-close-samsung-galaxy-backdoor)针对此事件也发出了自己的声音，并号召用户要求
Samsung Mobile 公开解释该问题。

[详细分析报告](http://redmine.replicant.us/projects/replicant/wiki/SamsungGalaxyBackdoor)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTYyODE)
