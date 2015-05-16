Title: TeX Live 2013 发布
Date: 2013-06-19 12:04
Author: yutangbaihe
Category: Text Processing
Tags: TeX
Slug: tex-live-2013-released

TeX Live 2013 于 2013 年 6 月 18 日发布。

**以下是来自中文文档的版本更新情况**：

发行版布局：为了简化，顶层的 `texmf/` 目录被并入 `texmf-dist/`。

现在 TEXMFMAIN 和 TEXMFDIST 这两个 Kpathsea 变量都被指向 texmf-dist了。

为了简化安装合并了许多小的语言集合。

MetaPost: 加入对 PNG 输出和 (IEEE 双精度) 浮点数的原生支持。

LuaTeX: 升级到 Lua 5.2，包含一个新的库 （pdfscanner） 来处理外部 PDF
页面内容，以及其他功能 (见主页)。

XeTeX (见其主页了解更多信息):

-   使用 HarfBuzz 库替代 ICU 进行字体排版。(仍然使用 ICU
    来支持输入编码、双向排版，以及可选的 Unicode 断行。)
-   使用 Graphite2 和 HarfBuzz 来替代 SilGraphite 进行 Graphite 排版。
-   在 Mac 上，使用 Core Text 替代 (Apple 不再建议使用的) ATSUI。
-   在名称相同的情况下有限使用 TrueType/OpenType 字体而不是 Type1 字体。
-   修正偶尔出现的 XeTeX 和 xdvipdfmx  字体查找不匹配的问题。
-   支持 OpenType math 间距调整。

xdvi: 现在使用 FreeType 替代 t1lib 进行字体渲染。

microtype.sty: 对 XeTeX 的部分支持 (protrusion) 和对 LuaTeX 的支持
(protrusion, font expansion, tracking)，已经其他改进。

tlmgr: 新的 pinning 操作以方便配置多个仓库；参见 `tlmgr --help`
的对应章节，或者[在线文档](http://tug.org/texlive/doc/tlmgr.html#MULTIPLE-REPOSITORIES)。

平台: armhf-linux, mips-irix, i386-netbsd, 和 amd64-netbsd
被重新加入；powerpc-aix 被去除。部分额外平台提供了定制二进制包
[(http://tug.org/texlive/custom-bin.html](http://tug.org/texlive/custom-bin.html))。此外，为节省空间部分平台没有在
DVD 中提供，但可以通过网络安装。

[项目主页](http://www.tug.org/texlive/)
