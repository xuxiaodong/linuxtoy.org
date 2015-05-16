Title: digiKam 0.9.2 Beta 1
Date: 2007-05-06 18:56
Author: toy
Category: Apps
Slug: digikam-092-beta-1

KDE 桌面环境中的数字照片管理软件 [digiKam](http://www.digikam.org/)
于最近启动了新版本的测试周期。目前，digiKam 已经放出了 0.9.2 的第一个
Beta 版供用户下载、测试并反馈。digiKam 0.9.2 的正式版预计下月中旬推出。

![digiKam](http://i.linuxtoy.org/i/2007/05/digikam-logo.png)

与上一个版本 0.9.1 相比，digiKam 0.9.2 Beta 1 的更新情况如下：

> General :  
>  - DigikamImagePlugins have been merged into digiKam. It is easier to
> release one package for all and nobody will search for promised
> features that are not installed anymore. Image plugins translations
> are hosted to digikam.po file instead a .po file for each tool.  
>  - New depency to libkdcraw shared library used to decode RAW file.
> This library is shared between digiKam and kipi-plugins. The internal
> dcraw version used is 8.60. digiKam now supports all recent digital
> camera RAW files released at PMA 2007.  
>  - Make icon size in sidebars configurable to allow more entries to be
> presented.  
>  - Reduce icon size of album view and make them configurable using a
> slider in status bar.  
>  - Removing direct Exiv2 library depency. libkexiv2 interface is used
> everywhere instead.  
>  - A new plugin 'Vivid', similar to Velvia type filters is part of
> Color Effect plugin.
>
> Album GUI :  
>  - Add Zoom/Scrooling functions with preview mode. Speed incease.
>
> Image Editor :  
>  - Usability improvement : a new pan tool is available on the right
> bottom corner of the status bar to navigate on large pictures.  
>  - Blowup and Resize tools have been merged.  
>  - Unsharp Mask, Refocus, and Sharpen tools have been merged to a new
> Sharpness Editor.  
>  - Reorganize menu structure  
>  - persistant selection in all zoom mode.  
>  - Add new option to fit on current selection.  
>  - Red Eyes Correction tool have been completly re-written. There is a
> preview and the capability to taint the eye pupil with a customized
> color. The new eye pupil can be blurred to smooth the result.  
>  - Solarize plugin is now a "Color Effects" pack including Solarize,
> Velvia (new plugin), Neon, and Edge effects.  
>  - Black & White converter now support a lots of B&W analog camera
> film types (Agfa, Ilford, Kodak). A new 'strength' setting can
> simulate the amount of Lens filters effect.  
>  - Update internal CImg library to 1.1.9. The Greycstoration algorithm
> used by Restoration, Inpainting and Blowup plugins is faster and
> optimized.
>
> Showfoto :  
>  - The thumbbar is now resizable. The thumbnails contents can be
> redimensionned in live.  
>  - The thumbbar items can show a full configurable tool tip like
> digiKam album icon tems tool tip.

如果你对 digiKam 感兴趣的话，那么可从其主页获取 0.9.2 Beta 1 的源代码。

- [Download digiKam 0.9.2 Beta
1](http://sourceforge.net/project/showfiles.php?group_id=42641)
