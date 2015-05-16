Title: nVidia 发布 180.35 版本驱动
Date: 2009-02-26 10:42
Author: lovenemesis
Category: Drivers
Tags: nouveau, NVIDIA
Slug: nvidia-18035driver-released

nVidia 昨日发布了官方驱动
180.35，延续了这一两个月来快速发布的势头。然而与先前仅仅是将 Beta 版变成
Release 版的行为不同，此次带来了新的功能：GeForece 8 及以后产品全系列的
VC-1/WMV VDPAU 加速回放支持！

除了在 VDPAU 上的功能添加以外，还添加了对 GeForce GT 120、GeForce G100
和 Quadro FX 3700M 的支持，修复了 Maya
僵死的问题。同时还有一些细微的针对 OpenGL 3.0 的修正。

*完整的官方更新日志见下面引用：*

* Added support for the following GPUs:  
o GeForce GT 120  
o GeForce G100  
o Quadro FX 3700M  
* Fixed a bug that caused Maya to freeze when overlays are enabled.  
* Fixed an interaction problem with some applications that use memory
tracking libraries.  
* Added support for RG renderbuffers in OpenGL 3.0.  
* Added support for OpenGL 3.0 floating-point depth buffers.  
* Fixed a problem that caused Valgrind to crash when tracing a program
that uses OpenGL.  
* VDPAU updates:  
o VDPAU now supports VC-1/WMV acceleration on all GPUs supported by
VDPAU; see the README for details.  
o Expand the documentation of VDPAU's VdpVideoMixer, in particular
regarding how to use the deinterlacing algorithms. Explicitly document
"half rate" deinterlacing, which should allow the advanced algorithms to
run on more low-end systems. See vdpau.h.  
o Implement a "skip chroma deinterlace" option in VDPAU, which should
allow the advanced deinterlacing algorithms to run on more low-end
systems. See vdpau.h.  
o Enhance VDPAU to correctly handle some forms of corrupt/invalid MPEG
streams on some GPUs.  
o Fix VDPAU to prevent some cases of "display preemption" in the face
of missing H.264 reference frames on some GPUs.  
o Fix VDPAU to correctly handle VC-1 skipped pictures with missing
start codes on some GPUs.  
o Fix VDPAU to correctly handle WMV "range reduction" on some GPUs. A
minor backwards-compatible API change was made for this; see vdpau.h's
documentation for structure field VdpPictureInfoVC1.rangered.  
o Fix VDPAU wrapper library to print dlerror() messages when problems
occur, which will simplify debugging of driver loading issues.

*引用结束*

[32位版本下载](ftp://download.nvidia.com/XFree86/Linux-x86/180.35/)  
[64位版本下载](ftp://download.nvidia.com/XFree86/Linux-x86_64/180.35/)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=NzA5MQ)

**再讯：**  
Fedora 11 将使用逆向工程的开源 Nouveau 驱动替代 nVidia 官方 2D 开源驱动
nv 成为使用 nVidia 显卡的默认驱动。为了以防万一 Nouveau 出现差错，nv
驱动依然会被安装。

此举在某种意义上是对 nVidia 目前极为有限的开源策略的一个试探，希望
nVidia 能重新审视自身的开源策略。  

详情请见[这里](http://fedoraproject.org/wiki/Features/NouveauAsDefault)。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=NzA4Ng)
