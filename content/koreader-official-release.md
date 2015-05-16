Title: Koreader 正式发布
Date: 2013-03-31 10:46
Author: liangsuilong
Category: News
Tags: Kindle, Koreader
Slug: koreader-official-release

Kindle 上的开源阅读器 Koreader 正式发布。感谢 Qingping Hou 和 Xin
Huang 的来稿。

### Overview

我们希望在我们的阅读设备上能够享受这些自由：

1.   数字内容不被局限于特定厂商的专有系统的自由。
2.  用户可以获得阅读器软件运行细节，保障数字内容不被非法窥探的自由。
3.  用户修改阅读器软件外观和功能的自由。

[Koreader](https://github.com/koreader/koreader/) 正是让我们获得这些自由的一个尝试。[Koreader](https://github.com/koreader/koreader/) 在
GPLv3 协议下发布，支持开放文档格式
PDF、DJVU、EPUB，个人文档转化为这些开放格式后不会因为特定厂商的消失而使文档失效；任何有兴趣了解 [Koreader](https://github.com/koreader/koreader/) 运行细节的人都可以拿来研究并修改、添加自己想要的功能。

[Koreader](https://github.com/koreader/koreader/) 项目来源于 [Kindlepdfviewer](https://github.com/koreader/kindlepdfviewer/)，并重写了 [Kindlepdfviewer](https://github.com/koreader/kindlepdfviewer/) 界面层的大部分代码，使模块化程度更高。理论上 [Koreader](https://github.com/koreader/koreader/) 能够运行在所有基于
Linux
的阅读设备上。如果你想要移植 [Koreader](https://github.com/koreader/koreader/) 到其他阅读器上的话，请参考项目的 [Wiki](https://github.com/koreader/koreader/wiki) 页面：[如何移植
Koreader
到其他系统。](https://github.com/koreader/koreader/wiki/porting)

### Feature List

机型支持：

Kindle Touch、Kindle PaperWhite （K3，DXG，K4 的支持还在完善中）

格式支持：

PDF, DJVU, EPUB, HTML, MOBI, TXT, ZIP, CBZ, FB2, RTF, XPS, CHM, DOC

### 功能支持：

见参考[4]。

### Architecture

[Koreader](https://github.com/koreader/koreader/) 底层的文档解析和渲染使用了优秀而且成熟的开源实现：

-   PDF
    文档的解析渲染使用小巧快速、低内存占用的 [MuPDF](http://www.mupdf.com/)。
-   DJVU 文档的解析渲染使用了 DJVU
    格式的开源实现 [DjVuLibre](http://djvu.sourceforge.net/)。
-   EPUB 和其他标记文档使用 CoolReader
    的渲染引擎 [CREngine](http://coolreader.org/crengine.htm)。
-   使用 [K2pdfopt](http://www.willus.com/k2pdfopt/) 来优化 PDF/DJVU
    文档在小屏幕设备上的排版。效果见[这里](http://vislab.bjmu.edu.cn/blog/hwangxin/2012/10/read-scanned-pdfs-with-kindlepdfviewer/#i-2)。
-   其他开源库如 luafilesystem, popen\_nonshell
    以及 [freetype](http://www.freetype.org/) 等等。

[Koreader](https://github.com/koreader/koreader/) 界面层和逻辑层使用嵌入式脚本语言
Lua 编写，运行时通过 LuaJIT
即时编译为机器码来提升运行效率。[KOReader](https://github.com/koreader/koreader/) 自带一套超轻量级的GUI框架，可直接运行在支持桢缓存（FrameBuffer）设备的阅读器上，也可以通过 [SDL](http://www.libsdl.org/) 获得跨平台的运行支持。  
**  
**
[Koreader](https://github.com/koreader/koreader/) 自带一个设备模拟器，方便开发者在桌面系统进行开发。有关开发的详情请参考项目 [Wiki](https://github.com/koreader/koreader/wiki) 和 [README](https://github.com/koreader/koreader/blob/master/README.md)。

### 参考链接：

1.  [KOReader: a document reader for PDF, DJVU, EPUB, FB2, HTML, ...
    (GPLv3)](http://www.mobileread.com/forums/showthread.php?t=209276)
2.  [Dcument reader for Kindle, based on muPDF/djvulibre/CREngine,
    GPLv3](http://www.mobileread.com/forums/showthread.php?t=157047)
3.  [Librerator – multi-format e-reader, fork of
    KindlePDFViewer](http://www.mobileread.com/forums/showthread.php?t=198742)
4.  [Koreader/Kindlepdfviewer 更新日志，功能建议和 Bug
    反馈](http://www.hi-pda.com/forum/viewthread.php?tid=1078988)
5.  [让 Kindle 支持扫描版 PDF
    重排](http://vislab.bjmu.edu.cn/blog/hwangxin/2012/10/read-scanned-pdfs-with-kindlepdfviewer/)

### 

### 

### 

### 

<div>

</div>
