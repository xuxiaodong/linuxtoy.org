Title: 短消息：Kernel 2.6.35, Nvidia OpenGL 4.1 Driver 等
Date: 2010-08-04 18:59
Author: lovenemesis
Category: Distros
Tags: Chromium, Kernel, NVIDIA, OpenGL, opensolaris
Slug: briefing-kernel-2635-nvidia-driver-opengl41-etc-al

最近开源界变化多多，更新慢了，只好整合成筐。请各位见谅！*感谢 Petty
来稿*

**Linux Kernel [发布 2.6.35 版](http://lkml.org/lkml/2010/8/1/188)**
。该版本主要对 Btrfs 文件系统和 Radeon
的电源管理做了改善，同时提供了在多个 CPU 间无缝网络负载平衡和 Intel
显卡的高清解码 VAAPI 支持。  
详细变化可以参考 [KernelNewbies](http://kernelnewbies.org/Linux_2_6_35)
。

**NVIDIA 最近也发布新驱动**，其中 256.44 版本添加了对 GeForce GTX 400
系列显卡的支持，而 256.38.02 则为最近发布的 OpenGL4.1
标准提供了初步支持。不过 OpenGL
的标准一再提升也给开源驱动开发者带来了压力，目前开源驱动对于 OpenGL 3
标准的实现才初具规模。详情请参考[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=ODQ2NQ)
。

**掌握在 Apple 手里的字体 hinting 算法专利过期了**，于是以前这个被放置到
freetype-freeworld 分支中算法正式合并入 Freetype 2.4.0 版本。详情请参考
[LinuxJournal](http://www.linuxjournal.com/content/prettier-fonts-way)

[本站以前的相关讨论](http://linuxtoy.org/archives/google-chrome-dev-updated-to-402881.html)

**Illumos 项目在 OpenSolaris 基础上成立**。由于 Oracle 对于 OpenSolaris
发展方向一直不明确，并且也没有与开发者社区进行任何沟通。失望的
OpenSolaris Governing Board
已提出自行解散。一部分OpenSolaris开发者（主要为原nexenta成员）开始自行
Fork 成立了 Illumos 项目。项目计划实现 NFS/CIFS
锁管理，内核级的加密框架，并且提供更多的驱动支援。详情请参考
[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=ODQ3MQ)。

**Google Chrome / Chromium 浏览器最近将设置界面移入 Web
中**。看来跨平台浏览器将原先独立的窗口转变为标签页的方式目前成为避免窗口管理器麻烦的首选解决方案，至少
Firefox 4 和 Chrome/Chromium 都这么选择了：

[![](http://linuxtoy.org/img/2010/08/screenshot-google-chrome-options-google-chrome.png)](http://linuxtoy.org/img/2010/08/screenshot-google-chrome-options-google-chrome.png)

注意需要加上 `--enable-tabbed-options` 才可使用此特性。详情请参考
[WebUpd8](http://www.webupd8.org/2010/08/chromium-options-window-moved-in.html)
