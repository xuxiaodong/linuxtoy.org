Title: scrot 从入门到精通
Date: 2007-01-07 11:41
Author: toy
Category: Tutorials
Slug: mastering-scrot

无论是撰写技术教程，还是展示桌面或应用，恐怕
[scrot](http://linuxbrit.co.uk/scrot/) 都是必不可少的工具。scrot
是屏幕抓图工具中的~~皎皎~~佼佼者，它小巧而不失为强大，精练而不缺少灵活。

scrot 主要用在命令行下，它使用 imlib2 库来抓取并保存图像。在 Ubuntu
中，可以使用 `sudo apt-get install scrot` 指令来安装 scrot。scrot
的使用格式为：`scrot [options] [file]`。

一般用法

就一般而言，使用 scrot
可以抓取整个桌面、某个指定的窗口、以及选择的矩形区域。

1.  抓取桌面：`scrot desktop.png`，该命令将当前的整个桌面抓取下来，并保存为
    desktop.png 文件。可以在当前的目录中找到此图像文件。
2.  抓取窗口：`scrot -bs window.png`，选项 b 使 scrot
    在抓取窗口时一同将外边框抓取下来，而 s
    选项则让用户选择所要抓取的是何窗口。
3.  抓取区域：`scrot -s rectangle.png`，在执行此命令后，使用鼠标拖曳的矩形区域将被
    scrot 抓取下来。

高级使用

对于普通的抓取使用 scrot 的基础便足以应付了。但在某些特殊情况之下，使用
scrot 抓取图像需要讲究一些技巧。

1.  延时抓取：`scrot -cd 10 menu.png`，此命令中的 d
    选项用于延时抓取图像，其后的 10 代表延时 10 秒；前面的选项 c
    显示倒计时。在抓取菜单或是命令提示时，该技巧将充分展示其魔力。
2.  生成缩图：`scrot -t 50% thumb.png`，这个命令在抓取图像的同时生成该图像的缩略图。选项
    t 将打开此功能，其后的 50% 为原图的缩放百分比。
3.  更改品质：`scrot -q 70 quality.jpg`，此命令中的 q
    选项用于更改所抓图像的品质，其数值介于 1-100 之间，默认为
    75。数值越大，意味着图像品质越高；同时，图像的压缩率也就越低，占用空间越大。
4.  操作抓图：`scrot action.png -e 'mv $f ~/images/'`，该命令将抓取的图像移动到
    ~/images/ 目录。显然，操作图像的功能由 e 选项开启，其中的 $f
    代表原图的路径／文件名。

以上示例皆指定了需要保存的抓图的文件名称。实际上，如果不指定名称，那么
scrot
在抓取图像后会自动使用当前的日期时间、宽度高度的组合来生成文件名称。
