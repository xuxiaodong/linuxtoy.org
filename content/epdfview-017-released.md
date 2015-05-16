Title: ePDFView 0.1.7 发布
Date: 2009-03-03 10:46
Author: toy
Category: Apps
Tags: ePDFView, PDF
Slug: epdfview-017-released

轻巧型 [PDF 文档阅读工具
ePDFView](http://linuxtoy.org/archives/epdfview.html)
在时隔两年后发布了新的 0.1.7
版本。该版本支持选取文本、并可以将其复制到剪贴板，添加了一些类似 vi
的键盘绑定、修正了内存泄漏及崩溃问题、以及更新了简体中文、繁体中文等翻译。

以下为 ePDFView 0.1.7 更新日志，供参考：

> New features
>
> * Text selection and copying to clipboard (Igor Vagulin).
>
> Interface improvements
>
> * Loading from the command line does not resize the page more than
> necessary (Igor Vagulin).  
>  * Added more keybindins (many authors).  
>  * The focus is set to the document when loading.  
>  * Added 6-in-1 page print layout (Pablo Mazzini)
>
> Bug fixes
>
> * Fixed some memory leaks (Tilman Sauerbeck).  
>  * Removed some segfaults while selecting printer options.  
>  * Removed crashes in Gtk+ 2.10 (zhou sf)  
>  * Added support to compile with poppler 0.8.0.  
>  * Added support to compile with GCC 4.3 (Yves-Alexis).  
>  * Fixed hang in "Loading..." with Ubuntu Gutsy.

你可以从 ePDFView 主页下载该版本。

[ePDFView](http://trac.emma-soft.com/epdfview/wiki/Download)
