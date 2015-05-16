Title: NVIDIA 发布 185.19 Beta 驱动
Date: 2009-04-07 17:26
Author: toy
Category: Apps
Tags: NVIDIA
Slug: nvidia-18519-beta

{撰文/zsl1005}

继 3 月份 NVIDIA 的显卡驱动 5 连发之后，今天 NVIDIA 又推出了最新款 185
系列 185.19 Beta 驱动，在添加一系列新特性的同时，还修正了大量 bug。

其中有两个重要特性与用户密切相关：

1. VDPAU 视频加速特性可以利用显卡的 turbocache
功能所划分的系统内存了，但暂时仅限集成显卡，如 mcp 系列。  
2. 支持小于 32x32 的 pixmaps 直接缓存到显存中，该特性将显著提高 Firefox
等软件的拖动时的性能，且在 NV News 论坛上得到了用户的证实。

以下为该版本驱动的更改日志，供参考：

* Added support for the following new GPUs:  
* Quadro FX 3800  
* Quadro FX 1800  
* Quadro FX 380  
* Quadro FX 580  
* GeForce GTS 250  
* GeForce GT 140  
* GeForce GT 130  
* GeForce 9600 GSO 512  
* Fixed SDI presentation time queries returning unexpected values.  
* Removed the 'AllowDFPStereo' X config file option, which is now
enabled  
by default.  
* Fixed a bug that caused certain programs to hang when multiple
threads  
call functions in libdl at the same time.  
* Fixed a driver crash when OpenGL applications use an extremely
large  
number of textures.  
* Text rendering to PseudoColor windows with the glyph cache enabled
no  
longer causes GPU errors.  
* The X driver now allows pixmaps smaller than 32x32 pixels to be
placed in  
video memory.  
* Fix a problem that prevented the driver from retraining a
DisplayPort  
link after a device is hotplugged.  
* nvidia-bug-report.sh now automatically gzips the resulting log
file.  
* Fix VDPAU to eliminate some cases of GPU hangs when decoding H.264
video  
on G84, G86, G92, G94, G96, or GT200 GPUs, and supplying a DPB missing
some  
reference frames.  
* The VDPAU presentation queue now syncs to VBLANK in the blit path.
The  
environment variable VDPAU\_NVIDIA\_SYNC\_DISPLAY\_DEVICE selects which
display to  
sync to when TwinView is enabled; see the README for details.  
* On systems using integrated graphics, VDPAU now uses system RAM
instead  
of video RAM for many purposes. This should prevent "out of resources"
problems  
in most cases, even when the video RAM carve-out is configured as low
as 128M.  
* Added support for Quad-Buffered Stereo in the main plane
simultaneously  
with the Color Index Overlay; i.e., both Stereo GLX FBConfigs and Color
Index  
Overlay FBConfigs can be advertised and used at the same time, though
no single  
GLX FBConfig contains both Stereo and Overlay capabilities.

下载地址：

* X86:  
* X86\_64:

{ via [Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px) }
