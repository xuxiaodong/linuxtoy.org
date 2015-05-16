Title: Vimperator 2.0 alpha 一瞥
Date: 2008-12-29 17:58
Author: toy
Category: Apps
Tags: Vimperator
Slug: first-look-at-vimperator-20-alpha

作为圣诞节的礼物，[Vimperator](http://linuxtoy.org/archives/vimperator.html)
团队在上周发布了 Vimperator 2.0 alpha 2，以供用户测试反馈。因为 alpha 2
在笔者的 Firefox 3.0.5 上并不能良好运作，所以笔者只得折回去用 alpha
1。好在从 alpha 1 开始，Vimperator 2.0
的功能便已冻结，后续版本只是做除错和修正处理，所以笔者仍然有机会体验
Vimperator 2.0 的所有新增功能。

Vimperator 2.0 给笔者印象较深的几个地方在于：

-   **数字化标签**
    在 Vimperator 2.0 中，可以使用 guioptions=nN
    选项来开启数字化的标签，n 与 N
    的区别只在于数字在标签中显示的位置不同。这是一项十分有用的功能，之前笔者便在
    [Firefox 的 Add-on
    丛林](http://linuxtoy.org/category/apps/firefox-extension)中寻找类似功能的
    Add-on，试了好几个都不合意，最终只得放弃。该功能使得笔者能够结合 gt
    在众多已打开的标签间快速跳转。
-   **颜色方案支持**
    用过 Vim 的朋友都知道通过 :colorscheme
    可以即时更换默认的颜色方案。现在，Vimperator 2.0
    也拥有了这项功能。Vimperator 的 colorscheme 文件放于
    $HOME/.vimperator/colors 目录中，既可执行 :colorscheme
    命令临时调用，也可将其写入 Vimperator 的配置文件
    $HOME/.vimperatorrc。
-   **改进的自动补完功能**
    Vimperator 2.0
    已对自动补完功能进行了改进，新的自动补完功能更加智能，且包含范围更加广泛。
-   **增强了 Hints 系统**
    Vimperator 的 Hints
    系统使用户无需动用鼠标便可对网页中的链接进行操作。在 Vimperator 2.0
    中，Hints 系统已得到增强，如用于 frame 的 ;f、新的
    ;b、支持双字节和多行输出等。

相比上个版本 Vimperator 1.2，Vimperator 2.0
有着许多改进和变化，有新增的命令和选项，也有的选项更改和移除了。更重要的是，Vimperator
正在变得越来越强大。无论怎样，笔者在 Vimperator 2.0
中可以感受到开发者的用心，它值得每一个 Vimperator 用户去尝试和探索。

[Vimperator](http://vimperator.org/trac/wiki/Vimperator)
