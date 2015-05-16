Title: 介绍 urxvt 插件一枚: vim-scrollback
Date: 2010-08-13 16:52
Author: vern
Category: Cli
Slug: vim-scrollback

这个插件和 urxvt 自带的 searchable-scrollback
插件一样提供了一种在终端的命令行输出结果中搜索或复制关键字的快捷方式，vim-scrollback
将这种快捷方式 Vim 行为化了。

简单来说，通过这个插件，你可以用 Vim 的方式操纵终端。假设你在命令行查看
ls 的 man
手册，看到有一个网址，你想用浏览器看看这个网址，但你又懒得去动鼠标:

    1. Alt-v 启用 vim-scrollback 模式
    2. 移动光标到网址处
    3. 键入 gf 两个字符
    4. Esc 或 Ctrl-C 可退出 vim-scrollback 模式

**支持普通模式**

    h j k l
    w e b
    0 _ $
    ctrl-u ctrl-d
    gg G

**支持可视模式**(甚至支持列模式)

    V v ctrl-v
    gv

**支持搜索**(遗憾的是不支持中文搜索)

    / - searches up
    ? - searches down
    n - next in current direction
    N - next in opposite direction
    * - search for word under the cursor

**其他更多**

    gf - 允许你打开当前光标下的超级链接

如果你感兴趣，可以从[这里](http://github.com/ervandew/vimfiles/raw/master/urxvt/vim-scrollback)下载
vim-scrollback 保存到本地某目录下，配置 ~/.Xresources 或 ~/.Xdefaults
添加下面几行内容:

    urxvt.perl-lib: /Your/Path/vim-scrollback
    urxvt.perl-ext-common: vim-scrollback
    urxvt.vim-scrollback-paste: none
