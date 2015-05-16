Title: GIMP 2.4.2 发布
Date: 2007-11-21 15:31
Author: toy
Category: Apps
Slug: gimp-242-released

图像处理软件 GIMP 在今天发布了 2.4.2 版。GIMP 2.4.2 是针对 2.4
稳定分支的更新版本，其中没有添加任何新特性，仅仅是修正各种 bug。GIMP
2.4.2 主要移除了损坏及无效的 HSV
图形脚本，修订了种种错误，并更新了一些翻译。

![GIMP](http://i.linuxtoy.org/i/2007/10/gimp24.jpg)

GIMP 2.4.2 更改记录如下：

- removed broken and useless HSV Graph script (bug #491311)  
- update the histogram when a color correction tool is cancelled (bug
#493639)  
- fixed a crash with certain plug-in or script descriptions (bug
#492718)  
- corrected a tooltip (bug #495564)  
- fixed a crash when GIMP is run without any modules (bug #495863)  
- fixed error handling in the TIFF plug-in  
- fixed a problem with Sample points  
- fixed a crash when merging layers in indexed image (bug #495990)  
- update the histogram when painting (bug #494049)  
- fixed another problem with merge operations on indexed images (bug
#496437)  
- fixed crash in TIFF plug-in when saving indexed images (bug
#497103)  
- changed defaults so that a system monitor profile is only used when
the  
user explicitely enabled this feature (bug #496890)  
- fixed endless loop when running equalize on transparent areas (bug
#497291)  
- fixed heap corruption in GimpColorScale widget that caused a crash in
the  
Compose plug-in (bug #399484)  
- fixed use of background color in Particle Trace script (bug
#498282)  
- set the image menu insensitive when there's no image opened (bug
#498511)  
- translation updates (ca, et, it, lt, pt, pt\_BR, sr, sv)

[GIMP 2.4.2 的源代码](ftp://ftp.gimp.org/pub/gimp/v2.4/)可到这里下载。
