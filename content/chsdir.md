Title: 终端下拼音补全中文名称和路径
Date: 2009-12-11 17:59
Author: toy
Category: Cli
Slug: chsdir

{ 撰文/BiFF }

在 Linux 下打字飞快的朋友，遇到中文目录和文件名立马就慢下来了，  
有 2 种选择：

1. 切换成中文输入一两个汉字，然后按 TAB 补全  
2. 动用鼠标复制

现在有第三种选择了 :)

用拼音补全命令行中的中文名称和路径

实验目录如下：

biff@lenovo:/domain/WorkSpace$ ls  
SVN培训 全球眼 浙江建行 浙江农信

使用: (输完后按 TAB 键自动补全)

cd S 进入[SVN培训]  
cd q 进入[全球眼]  
cd z 自动补全[浙江]  
cd zj 提示[浙江建行 浙江农信]备选  
cd 浙江j 进入[浙江建行]  
cd zjj 进入[浙江建行]  
cd zj1 进入[浙江建行]  
cd zj2 进入[浙江农信]

这第 3 种方法是前两种方法不能比的，自已用了半个月了，超爽！

共享给大家，有意见再改。

[下载软件包](http://easyscripts.googlecode.com/files/chsdir\_20090921.tar.gz)，解压，参考
install.sh 进行安装(不需要 root 权限)。

{ Thanks BiFF. }
