Title: Vim Multiple Cursors: 为 Vim 添加 Sublime Text 的多重选取特性
Date: 2013-06-30 20:14
Author: toy
Category: Apps
Slug: vim-multiple-cursors

相信用过 Sublime Text 编辑器的朋友一定对它的“多重选取”功能印象深刻吧。  
这项功能能够达到“一处编辑，多处更改”的神奇效果。如果你是一个 Vim 控，  
那么不必羡慕 Sublime Text 用户，因为现在有了 [Multiple Cursors][m]  
这款 Vim 插件。

![vim](http://lt-file.b0.upaiyun.com/files/2013/06/mulcur.gif)

在装好 Multiple Cursors 之后，通过按 `Ctrl + n` 来多重选取。一旦  
选取完成，便可配合 Vim 既有的命令对其进行编辑处理。最后，按 `Esc`
可以  
退出多重选取状态。

此外，你也可以使用 `MultipleCursorsFind` 命令通过正则表达式来进行  
多重选取和编辑。

[m]: https://github.com/terryma/vim-multiple-cursors
