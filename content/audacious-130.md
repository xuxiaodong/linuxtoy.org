Title: Audacious 1.3.0
Date: 2007-01-30 20:08
Author: toy
Category: Apps
Slug: audacious-130

[Audacious](http://audacious-media-player.org/) 是一个衍生自 BMP (
beep-media-player ) 的音乐播放器，感觉像经典的 Winamp。和 XMMS
相比，我认为 Audacious
更好一些，因为它支持更多好用的插件，且包含更好的设置管理器。

Audacious 的最新版 1.3.0
即将放出，该版本不仅会给用户带来新的特性，而且增加了好些新的插件。官方提供的完整列表如下：

> **New plugins:**
>
> * The wavpack plugin, which supports WavPack format files.  
>  * The alarm plugin, which is a port of XMMS-Alarm.  
>  * The metronom plugin, which provides a Metronome.  
>  * The stdio plugin, which supports file:// streams.  
>  * The tta plugin, which supports TrueAudio format files.  
>  * The curl plugin, which provides an http and https transport.  
>  * The mms plugin, which connects audacious to libmms for mms://
> streams.  
>  * The statusicon plugin, which minimizes audacious to the tray.  
>  * The rovascope plugin, which is like the "intelligent visualizer"
> in Winamp.
>
> **Enhancements to plugins:**
>
> * The mpgdec plugin supports seeking in HTTP streams now.  
>  * The console plugin now supports AY, KSS, HES and SAP files.  
>  * The modplug plugin now builds libmodplug inline.  
>  * The paranormal plugin now includes a SuperScope implementation, a
> scripted blitter, and an implementation of AVS' "Trans / Dynamic
> Movement".  
>  * The scrobbler plugin now supports the Gerpok service, which is a
> last.fm alike, and has experimental support for Hatena.  
>  * The vorbis plugin was heavily refactored.
>
> **New translations:**
>
> * Bulgarian  
>  * Serbian
>
> **New core features/plugin updates:**
>
> * The playlist code has been rewritten using conditional variables,
> which has resulted in speed improvements for the playlist code
> overall.  
>  * The behaviour for detecting filemagic has been redone and is now
> more scalable.  
>  * DoubleSize support has been improved significantly.  
>  * Race conditions in produce\_audio() have been corrected.  
>  * The playlist editor is now properly drawn in shaded mode.  
>  * Automatic character detection now supports encapsulated UTF-8
> strings.  
>  * GnomeVFS support has been removed, and a new plugin-based
> transport layer has been added.  
>  * The controlsocket code is no longer stack-dependant.  
>  * Behaviour regarding conversion of %20 in the playlist has been
> improved.  
>  * Window decorations can now be enabled.  
>  * The .po files have been simplified.  
>  * Support for multiple playlists has been added.  
>  * The Jump-to-File code has been rewritten and now supports
> searching with regular expressions. In addition, the search is done
> without GTK redrawing the list for every result, and as a result is
> realtime.  
>  * The UI has been severely reworked, notable enhancements include UI
> Manager, Search and Select, and much more.  
>  * A configuration backend for libmcs has been added.  
>  * Audacious now supports the XDG BASEDIR standard.  
>  * A lot of legacy XMMS and BMP code has been removed or replaced.  
>  * Debugging tools have been added for debugging memory management.  
>  * A safe signalling implementation has been completed.  
>  * A voiceprint visualization mode has been added.  
>  * Support for changing the tint of the graphics in skins has been
> added.  
>  * Many deprecated GDK calls have been updated.
>
> **Enhancements to audtool:**
>
> * The playback-seek-relative action has been fixed.
>
> **As usual, memory leak and reliability improvements.**

Download [Audacious 1.3.0](http://audacious-media-player.org/Downloads)
