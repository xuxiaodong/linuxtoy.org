Title: Anjuta DevStudio 2.3.0 放出
Date: 2007-11-03 08:00
Author: toy
Category: Apps
Slug: anjuta-devstudio-230-is-out

适用于 GNOME 桌面的集成开发环境 [Anjuta DevStudio](http://anjuta.org/)
在今天放出了 2.3.0 版。这是 Anjuta DevStudio 2.4.0（开发代号
Tornado）的首个开发版。此版本与旧版本相比，添加了许多新的特性，主要包括
beefed up
调试器支持、新的图标、新的文件管理器插件、与文档整合得更为友好的 glade
设计器、重新组织了首选项、改进了代码助手、以及为语言绑定改进了插件框架等等。

[![Anjuta
DevStudio](http://i.linuxtoy.org/i/2007/09/anjuta_s.png)](http://i.linuxtoy.org/i/2007/09/anjuta.png)

Anjuta DevStudio 2.3.0 的详细更新记录如下：

* Support for GError in interfaces.  
* Big improvements in debugger.  
* On demand preferences dialog (faster startup) and moved to Edit  
submenu.  
* Moved plugins and shortcuts settings inside General preferences
page.  
* Move preferences menu from Settings to Edit submenu.  
* Got rid of Settings submenu.  
* Updates for glade-3 recent releases.  
* Sort preferences pages on title.  
* Introduced document-interface and reorganized documents handling
such  
that documents tab can now hold any 'document' and not just editors.  
* Glade files are now opened as documents, so they behave just like  
editors.  
* Do not display registers list if not available  
* Big fixes in glade plugin.  
* Fixed lots of memory leaks (thansk valgrind)  
* Change the address of FSF in various files  
* Cleaned up message view (#458041)  
* Cleaned up message view  
* Removed some deprecated widgets.  
* New and better (uses gnome-vfs) file-manager plugin  
* Big improvements in autocompletion, both in scintilla and
sourceview  
editors.  
* Whole lot of new icons for toolbars and plugins.  
* Added preference option to set the gdl switcher style  
* Function tooltips are finally supported in sourceview.  
* Added nicer icons for document manager and debugger.  
* New incremental "Quick Search" bar in the document manager  
* Improvements in plugin framework.  
* Added API for commands override in build interface

- [下载 Anjuta DevStudio 2.3.0](http://anjuta.org/downloads)
