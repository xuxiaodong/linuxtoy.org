Title: tmux：GNU screen 替代品
Date: 2008-12-03 19:30
Author: toy
Category: Apps
Tags: Screen, tmux
Slug: tmux

[tmux](http://sourceforge.net/projects/tmux) 是一个与 [GNU
screen](http://linuxtoy.org/archives/screen.html)
类似的程序，可作为后者的替代品使用。tmux 采用 BSD
许可授权，其最新版本（当前是 0.5）的源代码可从 [SourceForge
网站](http://sourceforge.net/project/showfiles.php?group_id=200378&package_id=237972&release_id=641107)下载。

![tmux](http://i.linuxtoy.org/images/2008/12/tmux.png)

如上图所示，启动 tmux
后，在窗口底部有状态行显示，其中包括已创建的窗口列表、当前窗口（使用 *
表示）等。

与 GNU screen 相似，tmux
也使用快捷键来执行相关操作。要创建一个新的窗口，可以按 C-b c，即先按
Ctrl-b，再按 c。在各个窗口间切换可使用下列快捷键：

-   C-b n 切换到下一个窗口
-   C-b p 切换到上一个窗口
-   C-b 0、C-b 1……C-b n 切换到第 n 个窗口

分离会话可执行 C-b d 。

通过 `man tmux` 可以获得更详尽的 tmux 使用指南。

[感谢 fcicq 同学推荐]
