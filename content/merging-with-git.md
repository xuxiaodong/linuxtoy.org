Title: 使用 vimdiff 作 git 合并工具的技巧
Date: 2009-05-26 18:20
Author: vern
Category: Tips
Tags: Git, Vimdiff
Slug: merging-with-git

{撰文/vern}

编辑 ~/.gitconfig 文件

[merge]  
tool = whatever\_you\_want  
[mergetool "whatever\_you\_want"]  
# cmd = "gvim --noplugin --remote-tab-silent \\"+set
buftype=nowrite\\"  
\\"$PWD/$MERGED\\" && sleep 1;\\  
# gvim --remote-send \\":split $PWD/$REMOTE:set  
buftype=nowrite:vertical diffsplit $PWD/$LOCAL:vertical diffsplit  
$PWD/$BASE:set buftype=nowritel\\""  
# cmd = "gvim --noplugin \\"$PWD/$MERGED\\" \\  
# +\\":split $PWD/$REMOTE\\" +\\":set buftype=nowrite\\" \\  
# +\\":vertical diffsplit $PWD/$LOCAL\\" +\\":set buftype=nowrite\\"
\\  
# +\\":vertical diffsplit $PWD/$BASE\\" +\\":set buftype=nowrite\\"
\\  
# +\\":wincmd l\\""  
cmd = "vim --noplugin \\"$PWD/$MERGED\\" \\  
+\\":split $PWD/$REMOTE\\" +\\":set buftype=nowrite\\" \\  
+\\":vertical diffsplit $PWD/$LOCAL\\" +\\":set buftype=nowrite\\"
\\  
+\\":vertical diffsplit $PWD/$BASE\\" +\\":set buftype=nowrite\\" \\  
+\\":wincmd l\\""

运行 git mergetool 后的截图

![vimdiff](http://lh6.ggpht.com/\_oKL9t7fM3TU/Shuw3vrgyGI/AAAAAAAAAq4/ZO6A7gypn\_s/s800/vimdiff.png)

参考
[merging-with-git](http://stackoverflow.com/questions/585844/merging-with-git-mergetool)
