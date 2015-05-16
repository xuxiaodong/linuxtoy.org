Title: NVIDIA 显卡驱动 180.37 放出
Date: 2009-03-07 16:32
Author: toy
Category: Apps
Tags: NVIDIA
Slug: nvidia-18037-is-out

紧接着上月发布的
[180.35](http://linuxtoy.org/archives/nvidia-18035driver-released.html)
版本，NVIDIA 在今天针对 Linux 平台放出了 180.37
显卡驱动。总的来说，这是一个 bug 修订版本，其中主要修正了几个与 OpenGL
相关的问题，同时对 VDPAU 也有所更新。

以下为 NVIDIA 180.37 的 Release Highlights：

> * Fixed a problem that caused signals to be blocked in some
> applications.  
>  * Fixed a problem that could cause Xid errors and display corruption
> in certain cases when OpenGL is used to render to redirected windows,
> for example when Java2D is used with the -Dsun.java2d.opengl=true
> option.  
>  * glGetStringi(GL\_EXTENSIONS, i) no longer returns NULL in OpenGL
> 3.0 preview contexts.  
>  * Fixed a problem that caused the screen to flicker momentarily when
> OpenGL applications exit unexpectedly on GeForce 6 and 7 series GPUs.  
>  * Fixed an X server crash when an X client attempts to draw
> trapezoids and RenderAccel is disabled.  
>  * Improved recovery from certain types of errors.  
>  * VDPAU updates:  
>  o Fixed corruption on some H.264 clips.  
>  o Update documentation.  
>  o Fixed VC-1 decoding on 64-bit platforms.  
>  o Improved handling of invalid H.264 streams.  
>  o Fixed a problem that caused surfaces to be marked as visible too
> early when the blit presentation queue is in use.

该显卡驱动支持 Linux x86 及 x86\_64 架构，可从 NVIDIA 的 [FTP
站点](ftp://download.nvidia.com/XFree86/Linux-x86/180.37/)（[x86\_64](ftp://download.nvidia.com/XFree86/Linux-x86_64/180.37/)）下载。

[via [NV
News](http://www.nvnews.net/vbulletin/showthread.php?p=1951107)]
