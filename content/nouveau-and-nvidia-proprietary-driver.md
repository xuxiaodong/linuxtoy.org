Title: Nouveau 与 NVIDIA 闭源驱动的简短对比
Date: 2010-05-05 08:59
Author: toy
Category: Reviews
Tags: nouveau, NVIDIA
Slug: nouveau-and-nvidia-proprietary-driver

{ 撰文/guest }

本人显卡 6600LE，显示器 AOC F22，Nouveau 驱动是 2.6.34-rc4  

版内核附带的（编译进内核而不是作为模块），内核启动后即进入最佳分辨率，X  
启动后也是最佳分辨率。且在与终端的切换过程中完全没有任何闪烁。日常的
2D  
使用没有任何问题，甚至能够开启 Cairo-compmgr 和 Compiz。运行  
Neverball、Chromium-bsu 和 Supertux2 会有强烈的三角形闪烁，Quake3  
在看到第一帧后会死机（不是指刚进游戏界面，而是指底图载入后开战）。

近日换回了 NVIDIA 闭源驱动，突然发现了一个问题：NVIDIA 闭源驱动的 xv
输出速度没有 Nouveau 的快！测试片源是 VeryCD 上 1440x1080 的 Eureka
Seven，我的 CPU 是 AMD64 单核
3000+，显卡没有硬解压功能，因此在卡与不卡的临界点上差别很明显。用
Nouveau 驱动 MPlayer 可以流畅播放视频，但是换回了 NVIDIA
之后却卡很多，时常画面停滞或是一片黑（都没有后台任务）!另外我测试发现
gtk-perf 在 Nouveau 驱动时也比较快，总测试时间在 10s 内，而 NVIDIA
驱动则在 10s 以上。

以上测试均不是很严谨，有兴趣的同学可以严格对比一下二者的差别。

{ Thanks guest. }
