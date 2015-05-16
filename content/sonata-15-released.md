Title: Sonata 1.5 发布
Date: 2008-04-04 09:12
Author: toy
Category: Apps
Tags: MPD, Releases, Sonata
Slug: sonata-15-released

[Sonata](http://sonata.berlios.de/) 是一款我颇为喜欢的 MPD
客户端。该音乐播放客户端给人的感觉是简洁而优雅。近日，作为 Sonata
的开发者，Scott Horowitz 通过邮件列表发布了新的 Sonata 1.5
版。这是一个包含许多变动的版本，最主要的是，Sonata 现在使用新的
Python-mpd 这个 Python
接口，对于程序执行速度的提升十分明显。另外，Sonata 1.5
还改善了界面，并修正了若干 bug。

Sonata 1.5 的详细更改记录为：

> + Replace album view with genre view for library  
>  + Display covers for albums in artist/genre views  
>  + Add menu items and shortcuts for playing library items after
> add/replace  
>  + Allow setting artwork for streams  
>  + Optional stylized album art with cases (Aidan)  
>  + New, faster python mpd interface (jat)  
>  + --popup argument to popup song notification (requires D-Bus)
> (Oleg)  
>  + Show 'Untagged' artists/genres in their respective library views  
>  + Allow DND of cover art from a web browser (Артем)  
>  + Allow DND of music from a file manager into playlist (requires mpd
> 0.14)  
>  + Preserve column percentages for current tab across window resizing  
>  + Speed up mpd-related commandline arguments  
>  + Switch back to last tab on second cover art click  
>  + Retain selection in lists after removing items  
>  + Hidden config option to expand notebook tabs (tabs\_expanded)  
>  + Set ServiceProxy cachedir for lyrics to work around ZSI bug  
>  + Add Estonian translation (Mihkel)  
>  + Bug: Fix multimedia keys for gnome 2.22  
>  + Bug: Fix artwork for artists/albums with "/" in them (e.g. AC/DC)  
>  + Bug: Fix egg trayicon with vertical system tray  
>  + Bug: Weird bug in library-view  
>  + Bug: Prevent failure to load if tab positions are saved as None  
>  + Bug: Fix non-ascii characters in files for non-utf8 filesystems
> (zap)  
>  + Bug: Prevent crash with certain locales like turkish (jat)  
>  + Bug: Using filter causes playlist to jump to the top  
>  + Bug: Fix AudioScrobblerQuery (kigurai)

目前，你可以从这里[下载 Sonata 1.5
的源代码](http://sonata.berlios.de/download.html)。稍后，适用于各主流
Linux 发行版的二进制包可能也会跟进。
