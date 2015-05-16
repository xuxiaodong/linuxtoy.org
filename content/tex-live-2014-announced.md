Title: TeX Live 2014 发布
Date: 2014-06-23 10:40
Author: lovenemesis
Category: Text Processing
Tags: TeX
Slug: tex-live-2014-announced

TeX Live 2014 已于 2014 年 6 月 14 日发布。*感谢 Alick 来稿*

以下为[中文版官方文档](http://www.tug.org/texlive/doc/texlive-zh-cn/texlive-zh-cn.pdf)中的版本更新信息（有少许编辑）：

2014 年我们收到了 Knuth 的又一个 TeX
修正，这影响了所有的引擎，但可能唯一可见的变化是在启动时恢复显示的
`preloaded format` 字符串。根据 Knuth
的说法，这个字符串现在反应的是在启动时应该被默认载入的格式，而不是在二进制程序中预载入的未
dump 格式，该格式可能被很多方法覆盖。

pdfTeX: 新的警告忽略参数
`\\pdfsuppresswarningpagegroup`；用来制造词间空白 (interword space)
的新命令：`\\pdfinterwordspaceon`, `\\pdfinterwordspaceoff`,
`\\pdffakespace`，它们可以帮助 PDF 文本重新排版 (reflowing)。

LuaTeX: 对于字体载入和断字 (hyphenation)
有明显的变化和修正。最大的增加是一个新的引擎 `luajittex`
(http://foundry.supelec.fr/projects/luajittex) 和它的相关变体
`texluajit` 和 `texluajitc`。它使用的是一个即时编译的 Lua 编译器 (在
TUGboat 文章 http://tug.org/TUGboat/ tb34-1/tb106scarso.pdf
有详细介绍)。`luajittex` 还在开发中，所以并没有在所有平台提供，也比
luatex 要不稳定许多。我们及其作者都不建议使用它，除非为了试验 Lua
代码的即时编译 (JIT) 这样特殊的目的。

XeTeX: 现在所有平台 (包括 Mac) 都支持所有的图像格式了。避免使用 Unicode
兼容性 decomposition fallback（但允许其他的变体）；为了与先前版本 XeTeX
的兼容，优先于 Graphite 字体使用 OpenType 字体。

MetaPost: 支持了一个新的数字系统
`decimal`（十进制），还包括一个配套的内部 `numberprecision`； 在
`plain.mp` 有 Knuth 对 `drawdot` 的新定义； SVG 和 PNG 输出的 bug
修正，等等。

独立的 `pstopdf` ConTeXt
实用程序会在这个版本后被去除，因为和系统同名程序有冲突。但你仍然可以通过
`mtxrun --script pstopdf` 命令来执行它。

`psutils` 被它新的维护者大幅更新了。使得许多很少使用的工具 (`fix*`,
`getafm`, `psmerge`, `showchar`) 都只在 `scripts/`
目录中提供，而不作为所有用户访问的应用程序（如果以后发现这么做有问题，我们还可以改进）。另外，还加入了一个新脚本
`psjoin`。

MacTeX 这个 TeX Live 的重新发行版不再包括可选的，只在 Mac 下提供的 Latin
Modern 和 TeX Gyre
字体包，因为用户现在已经很容易在自己的系统下安装这些字体了。来自
ImageMagick 的 `convert` 程序也被去除了，因为 TeX4ht (具体说来是
`tex4ht.env`) 现在直接使用 Ghostscript 了。

包含中文、日文和韩文的 `langcjk`
集合被拆分为独立的语言集合，使得每个的大小更合理。

平台：加入了 `x86\_64-cygwin`，去除了 `mips-irix`；Microsoft
不再支持 Windows XP，所以我们的程序也可能在以后不支持这个系统。

部分额外平台提供了定制二进制包 ()。此外，为节省空间部分平台没有在 DVD
中提供，但可以通过网络安装。

[官方主页](http://tug.org/texlive/)
