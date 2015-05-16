Title: Vi 提示：在 Vi 编辑器中搜索 man 页
Date: 2006-11-25 17:14
Author: toy
Category: Tutorials
Slug: vi_tip

虽然标题说的是在 Vi 编辑器中搜索 man 页，其实在 Vim、GVim
中是同样有效的。对于编写脚本或是浏览源代码时，这个小的技巧将非常有用。它让你不必离开
Vi 窗口便可以查看 man 页的内容。方法很简单，将光标放到需要搜索 man
页的关键字的首字母上，然后按 Shift - K 就可以了。在阅读完 man
页之后，可以按 q 返回 Vi 的编辑窗口。另外，有些 man 页包含章节，如
SUDO(8) 这样的，可以先按数字 8，再按 Shift - K 来搜索 man 页。

[
[Source](http://lne.blogdns.com/lbe/archives/10/searching-man-page-inside-vi-editor/),
thanks! ]
