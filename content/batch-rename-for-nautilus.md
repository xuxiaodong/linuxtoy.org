Title: 在 Nautilus 中执行批量重命名操作
Date: 2007-02-05 13:38
Author: toy
Category: Tutorials
Slug: batch-rename-for-nautilus

在 Nautilus
中执行文件重命名操作时，通常只能针对单个的文件进行。不过，我们可以通过一个名为
[rename.py](http://andrey.thedotcommune.com/download/rename.py) 的
Nautilus
脚本来实现针对多个文件的批量重命名操作。这一点在对于需要重命名大量的图片文件时显得极为有效。

你可以按照如下的步骤来使用 rename.py 这个 Nautilus 脚本：

1.  将下载后的 rename.py 放到 `~/.gnome2/nautilus-scripts/` 目录中。
2.  赋予 rename.py 可执行权限：`chmod +x rename.py`。
3.  在你能够使用该脚本前，你可能需要重新启动 Nautilus
    程序，或者注销当前的 GNOME 桌面会话。另外，如果你没有安装 Python 和
    zenity 的话，也需要将他们安装好。
4.  假定你需要对 10 张 png
    格式的图片文件进行批量重命名操作，那么首先选中这些图片文件，然后选择右键菜单中的“Scripts ->
    rename.py”便会打开下面的对话框。  
    ![Batch Rename](http://i.linuxtoy.org/i/2007/02/batch-rename.jpg)  
    比如，你可以在其中输入 image[1].png，确定后这 10 张图片就按照
    image1.png、image2.png……image10.png 这样的序列命名了。

