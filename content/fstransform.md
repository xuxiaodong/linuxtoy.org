Title: 使用 fstransform 无损转换文件系统
Date: 2012-10-15 14:26
Author: toy
Category: Tools
Slug: fstransform

当我们想要改变 Linux
下已有分区的文件系统类型时，除了备份数据重新格式化之外，似乎别无他法。但
[fstransform][f] 的出现将打破这一局面。fstransform
允许我们就地、无损地将一种文件系统类型转换成另一种，比如从 `jfs` 变为
`ext4`。

目前，fstransform 已经支持下列文件系统类型：

* ext2  
* ext3  
* ext4  
* reiserfs  
* jfs  
* xfs

在未来我们希望看到 fstransform 能够支持更多的文件系统类型。关于
fstransform 的详细说明，可查看其源码包中的 README 文件。

[f]: http://sourceforge.net/projects/fstransform/
