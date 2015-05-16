Title: Colourshell：给 shell 命令着色
Date: 2006-08-01 14:16
Author: toy
Category: Apps
Slug: colourshell

[Colourshell](http://chezphil.org/colourshell/)
是一个非常有意思的脚本，顾名思义，使用它可以给你的 shell
命令着色，效果不错。

[![colourshell](http://static.flickr.com/65/156427880_b7dda7ff25_m.jpg)](http://www.flickr.com/photos/xxd/156427880/ "Photo Sharing")

使用方法：

1.临时使用，在终端中使用如下命令：`.  colourshell.sh`。注意：点后面有一个空格。

2.永久使用，打开 .bashrc 和 .bash\_profile 这两个文件，添加下面的代码：  
` if [ "$PS1" ] then   source /path/to/colourshell.sh fi`

注意：你需要根据 colourshell.sh 所保存的真实路径对上述代码作出修改。

[下载地址](http://svn.chezphil.org/colourshell/trunk/colourshell.sh)
