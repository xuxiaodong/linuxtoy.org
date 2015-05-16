Title: PulseAudio VS. AudioFlinger
Date: 2012-01-17 13:02
Author: lovenemesis
Category: Embedded
Tags: Android, audioflinger, pulseaudio
Slug: pulseaudio-vs-audioflinger

来自 [Collabora](http://www.collabora.com/projects/pulseaudio) 的 Arun
Raghavan 将 PulseAudio 移植到了 Android 系统上，并和 Android
系统目前的声音服务器 AudioFlinger 进行了一番比较。

关于 PulseAudio 本站已经多次介绍，不再赘述。AudioFlinger 是 Google 为
Android 系统重头开始设计的音频服务器，既可以工作在 ALSA
之上亦可以工作在由硬件厂商提供的 HAL
(硬件抽象层)之上（适用于不想开源音频处理驱动的厂商）。它做为
`mediaserver ` 进程的一个线程在后台运行，为包括 NDK
程序在内的所有系统声音事件提供服务。

以下**所有测试基于使用 Andorid 4.X 系统的 Galaxy Nexus 得出**。

**CPU 占有率比较**

使用不同采样率的音频文件比较在重采样过程中 AudioFlinger（AF） 和
PulseAudio（PA） 的 CPU 占有率差异。注意实际的重采样工作由为 NEON
优化过的
`resample `库完成，这里比较的是引入声音服务器带来的额外损耗。设备硬件原生采样率为
48kHZ，`top` 观测值。

44.1 kHz

48 kHz

AF

PA

AF

PA

1%

1%

2%

0%

可以发现 AF 在 48kHz 原始采样率时占有率提升到 2%，原因是 AF
默认输出给硬件抽象层的频率为 44.1 kHZ，于是发生了 48kHZ -> 44.1kHz ->
48kHz 这一个不必要的重新采样过程。而这方面 PA
则直接传递匹配采样率文件，于是占有率保持为 0%。

**在面对重采样 CPU 占有率方面，PA 表现更佳。**

**客户端内存占用比较**

比较服务进程的内存占有率意义甚微，特别是在 AF 还是 `mediaserver `
的一个线程的情况下。于是这次观测的是客户端内存占有率，使用 `top` 观测
[Resident Set Size](http://en.wikipedia.org/wiki/Resident_set_size)（纯
RAM 值）。

44.1 kHz

48 kHz

AF

PA

AF

PA

2600 kB

3020 kB

2604 kB

3020 kB

**在客户端内存占用方面，AF 表现更佳。**

**电源节能**

电源消耗通过比较每秒唤醒次数（wakeups-from-idle per
second）得出。要说明的是，由于测试设备位于 USB
除错模式，所以比通常使用中的要偏高。

首先使用 [PowerTop](https://gitorious.org/android/powertop)的测试结果：

44.1 kHz

48 kHz

Idle

AF

PA

AF

PA

79.6

107.8

87.3

108.5

85.7

其次是使用 `vmstat`的测试结果：

44.1 kHz

48 kHz

Idle

AF

PA

AF

PA

190

266

215

284

207

从以上数据可以看出 PA 的每秒唤醒次数相比 AF 要少，其原因在于 PA
使用的基于时序的调度技术。

**在电源节能方面，PA 表现更佳。**

**延迟**

相信[很多人都能注意到 Android
系统的延迟问题](http://code.google.com/p/android/issues/detail?id=3434)，Arun
Raghavan 表示经过调优后 Galaxy Nexus 能实现的 AF 最小延迟为 176 ms，而
PA 默认配置下即可达到 20ms 的最小延迟。

**在减少延迟方面，PA 表现更加。**

**功能**

目前 AF 实际上将电源管理部分的工作交由 HAL
解决，在留给厂商自由空间的同时也增加了可能的代码重复。而 PA
在基于时序的调度则在软件层面最优化的电源管理，可以**简化一部分厂商的工作**，特别是在大多数主机板都针对
Android 和嵌入式 Linux 的情况下会避免二次开发。

另外 **PA 允许将音频直接传输到今年 CES
流行的网络电视**上，该功能对于常见的高清压缩音频格式（AC3,
DTS）也有不错的支持。

**功能多样性方面，PA 更具潜力。**

**结论及展望**

从以上比较中可以看出 PA 相比 AF 具有相当的优势。

Arun Raghavan 目前正在和上游合作，改善 Android 构建系统，**简化构建使用
PA 的 Android 系统的步骤**。此外下一步还将研究**如何使得 PA 调用 Android
一些特有的功能**，比如 Binder IPC 和 ashmem 共享内存机制，更好的优化 PA
在 Android 平台的表现。

[更多详细内容](http://arunraghavan.net/2012/01/pulseaudio-vs-audioflinger-fight/)

**PS：**如果你还不知道的话，PulseAudio 是 HP webOS
、N900/Maemo5、N9/MeeGo 手持设备上的声音服务器。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTA0MzY)
