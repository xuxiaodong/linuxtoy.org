Title: 使用 Wipe 安全的删除文件
Date: 2007-07-23 16:05
Author: toy
Category: Apps
Slug: wipe

如果你想要从 Linux
系统中安全可靠的删除不愿被他人查看的文件，那么不妨来试试
[Wipe](http://wipe.sourceforge.net/)。Wipe
是个命令行工具，在使用它之前，你可以通过 apt、yum 之类的工具进行安装。

![Wipe](http://i.linuxtoy.org/i/2007/07/wipe.jpg)

**删除文件**

如需对某个机密的文件进行安全删除，你可以执行以下指令：

`wipe file.txt`

**删除目录**

Wipe 也支持对目录进行安全删除操作，你只需添加 r 选项即可，例如：

`wipe -r /home/user/test/`

更多 Wipe 的选项可以通过 man wipe 查询。
