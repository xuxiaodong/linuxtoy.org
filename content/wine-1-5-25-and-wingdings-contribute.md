Title: Wine 开发版 1.5.25 发布,同时召唤社区对 wingdings 字体做贡献
Date: 2013-03-04 20:54
Author: ihipop
Category: Emulator
Slug: wine-1-5-25-and-wingdings-contribute

<div>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif">Wine
项目近期发布了最新的开发版 Wine 1.5.25。本版本继续完善了 Mac
上的后端驱动的开发[注1]，具体包括如下更新：</span>

</div>

<div>

-   <span style="font-family: arial,helvetica,sans-serif">Mac
    后端驱动对光标的正确支持。</span>
-   <span style="font-family: arial,helvetica,sans-serif">RichEdit
    对从右往左文本支持的修复。</span>
-   <span style="font-family: arial,helvetica,sans-serif">wingdings
    字体实现的初始版本[注2]。</span>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif"></span>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif">Wine 1.5.25
总共修复了 40 个 bug，其中包括：</span>

</div>

<div>

-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    19678](http://bugs.winehq.org/show_bug.cgi?id=19678)：灵格斯翻译软件无法启动；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    26775](http://bugs.winehq.org/show_bug.cgi?id=26775)：《Ace of
    Spades》音效不正常；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    24669](http://bugs.winehq.org/show_bug.cgi?id=24699)：《文明V》
    启动时崩溃；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    23227](http://bugs.winehq.org/show_bug.cgi?id=23227)：《特警雄鹰》崩溃问题；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    32697](http://bugs.winehq.org/show_bug.cgi?id=32697)：Word 2003
    公式编辑器崩溃问题；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    32709](http://bugs.winehq.org/show_bug.cgi?id=32709)：《福尔摩斯的遗嘱》启动时崩溃；</span>
-   <span style="font-family: arial,helvetica,sans-serif">[Bug
    33071](http://bugs.winehq.org/show_bug.cgi?id=33071)：Adobe Reader
    XI 无法安装的问题。</span>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif">……</span>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif">  
</span>

</div>

<div>

<span
style="font-family: arial,helvetica,sans-serif">源代码可以从[这里](http://prdownloads.sourceforge.net/wine/wine-1.5.25.tar.bz2)获取。
二进制包正在构建中，稍后将出现在各自相应的[下载位置](http://www.winehq.org/download)。</span>

</div>

<div>

<span
style="font-family: arial,helvetica,sans-serif">更多信息请查阅：<http://www.winehq.org/announce/1.5.25></span>

</div>

<div>

<span style="font-family: arial,helvetica,sans-serif">  
</span>

</div>

<div>

*<span style="font-family: arial,helvetica,sans-serif">[注1]：Mac
后端驱动是 Wine 项目不久之前新引入的技术，旨在替换 Mac 上的
X11后端驱动，一旦 Mac 后端驱动完成，Wine for Mac 将不再依赖
XQuart。</span>*

</div>

<div>

*<span style="font-family: arial,helvetica,sans-serif">[注2]：此前 Wine
已有 symbol 字体的自由实现，非 M$ 平台的办公软件，**如 WPS、Libreoffice
对特殊符号的支持可以从这些中受益**。Wine 项目开发字体使用的工具是由 Wine
社区 fork
出来的一个 [FontForge](http://fontforge.org/editexample.html) 版本：<http://source.winehq.org/git/fontforge.git/></span>*

</div>

<div>

*<span
style="font-family: arial,helvetica,sans-serif">（欢迎大家一起来为
wingdings 字体做贡献，这项工作不需要编程能力、并且能使多个项目受益哦~
创建字体的文档参见：<http://wiki.winehq.org/CreateFonts>）</span>*

</div>

------------------------------------------------------------------------

消息来源 [wine-zh](http://www.freelists.org/list/wine-zh)
