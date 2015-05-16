Title: 细说 Vim 7 之新特性
Date: 2006-09-19 19:34
Author: toy
Category: Tips
Tags: Vim
Slug: vim_7_new_features

Vim 7 的发布距离我们也有很长一段时间了。与旧版本相比，在 Vim 7
中新增了多项重要的特性。你真的了解并使用了这些新特性吗？[All about
Linux](http://linuxhelp.blogspot.com) 上的 *[A visual walk through of a
couple of the new features in Vim
7.0](http://linuxhelp.blogspot.com/2006/09/visual-walk-through-of-couple-of-new.html)*
一文，将给你有用的提示。

-   使用拼写检查功能

    Vim 7 内置了一项与 Microsoft Word
    类似的拼写检查功能，使用该功能可以检查出所拼写词语的错误。在默认情况下，这项功能是没有开启的。若是使用
    GVim 的话，可通过“Tools -> Spelling -> Spell check
    on”菜单命令开启。Vim
    一旦发现拼写错误的词语，则以红色的波浪线标记。而使用以下命令可以执行拼写检查功能的相关操作：

    -   :set spell－开启拼写检查功能
    -   :set nospell－关闭拼写检查功能
    -   :]s－移到下一个拼写错误的单词
    -   :[s－作用与上一命令类似，但它是从相反方向进行搜索
    -   z=－显示一个有关拼写错误单词的列表，可从中选择
    -   zg－告诉拼写检查器该单词是拼写正确的
    -   zw－与上一命令相反，告诉拼写检查器该单词是拼写错误的
-   使用括弧高亮显示功能
    此特性在编码时非常具有帮助。对于如“{”、“}”之类的配对括弧，Vim 7
    将高亮显示它们。如果不喜欢，可以使用“:NoMatchParen”命令禁用该功能。
-   使用自动补完功能
    这是一个非常酷的特性。当你在写代码的时候，可以使用该功能帮助你自动完成标记、关键字等等。此功能支持
    C、(X)HTML（包含 CSS）、JavaScript、PHP、Python、Ruby、SQL、XML
    等语言。在插入模式中，连续按“[Ctrl+x]
    [Ctrl+o]”组合键可以打开该功能。你可以从弹出的列表框中进行选择。
-   使用分页（tabs）功能

    此功能可让 Vim 同时打开多个文档进行编辑。其命令如下：

    -   :tabe /path/to/file.txt－在一个新的 tab 页中打开文件
    -   :tabnew－新建一个 tab 页
    -   :tabs－查看 tab
        页列表，通过“>”显示当前窗口、“+”显示可修改的缓冲区
    -   :tabc－关闭当前的 tab 页
    -   :tab split－在当前缓冲区使用新的 tab 页打开文件
    -   :tabn－切换到下一个 tab 页
    -   :tabp－切换到上一个 tab 页
    -   :tabr[ewind]－转到第一个 tab 页
    -   :tabf[irst]－与上一命令作用相同
-   使用撤销分支功能
    Vim 7 包括了一个让用户跳转到任何编辑点之前或之后的新特性。如使用
    :earlier 10m 可以返回到 10 分钟以前的编辑状态，又如使用 :later 5s
    可以跳转到 5 秒以后的编辑点。另外，可以使用 :undolist
    命令查看缓冲区存在的撤销分支列表。而通过 :undo < number>
    命令则能够移到撤销的某个分支。

（Via All about Linux, thanks!）
