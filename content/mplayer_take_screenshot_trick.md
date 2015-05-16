Title: MPlayer 截屏必杀技
Date: 2006-11-15 09:34
Author: toy
Category: Tips
Tags: mplayer
Slug: mplayer_take_screenshot_trick

以往，当我们需要截取在 [MPlayer](http://www.mplayerhq.hu)
中播放的电影画面时，一般需要借助于第三方的截屏工具。其实，MPlayer
本身便具有这方面的功能，只是通常不为常人所知晓罢了。昨天，在与好友
[Dark](http://dark.supercn.net) 的共同努力之下，终于让我们挖出了 MPlayer
的隐秘截屏功能。

要激活 MPlayer 或 GMPlayer 的截屏功能，需要使用下列命令：  
`mplayer[gmplayer]  $s -vf screenshot movie.file`

我将试图对该命令作出解释：

-   $ 用于指定截屏时所用的快捷键。MPlayer 默认的截屏按键是 s。但这个 s
    键可能在 GMPlayer 中已被占用，通过 $
    选项可以临时指定一个不同的按键。

    设置截屏快捷键的更加牢固地做法，是利用 input.conf 文件。input.conf
    文件原始位于 /etc/mplayer/ 中，其作用是定制 MPlayer
    的快捷键。在使用时需要复制到 $HOME/.mplayer 目录。在 input.conf
    中设置按键的格式为
    `快捷键 命令 值`，例如：`S screenshot 0`。其中，值为 0
    时生成单一的屏照，值为 1 时则生成一系列连续的屏照。

    该选项为可选，如果不用，MPlayer 会采用默认配置。

-   vf 即 video filter，通过搭载 screenshot 参数，以便使 MPlayer
    在播放电影时能够截取屏照。
-   movie.file 为播放的电影文件。

MPlayer 默认会将截取的屏照保存到播放的电影文件的目录中，生成的文件类似
shot0001.png、shot0002.png……等。

对于 GMPlayer
而言，通过命令行加载选项可能显得不够方便，我们可以通过编写如下脚本：  
` #!/bin/bash gmplayer $S -vf screenshot`

还可以将电影文件与该脚本关联，这样方便直接调用。

另外，Dark 兄提到通过修改 GMPlayer 的菜单项目来达到启动即加载 video
filter 的目的，有兴趣的可以一试。

［参考资料：[1](http://lists.mplayerhq.hu/pipermail/mplayer-dev-eng/2005-September/036729.html)
[2](http://www.mplayerhq.hu/DOCS/HTML/en/faq.html#id2540181)
[3](http://www.mplayerhq.hu/DOCS/tech/slave.txt)］

［备注：以上方法在 Ubuntu Edgy Eft + MPlayer 1.0pre8 环境中测试通过。］
