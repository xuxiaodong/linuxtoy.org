Title: 小技巧: 使用一条命令来创建并转到新目录
Date: 2010-05-11 09:50
Author: toy
Category: Cli
Tags: Bash
Slug: mkcd

Lifehacker 介绍了一个有用的 Linux  

命令行小技巧，通过此技巧你仅需一条命令便可在创建新目录的同时并转到该目录。

将以下内容加入到 ~/.bashrc 文件中：

# mkdir, cd into it  
mkcd () {  
mkdir -p "$*"  
cd "$*"  
}

接着执行 `source ~/.bashrc` 即可。然后，你就可以使用 mkcd  
来创建新目录并转到该目录了。例如：

mkcd test

这将在创建 test 目录后立即转到该目录。

{ via
[Lifehacker](http://lifehacker.com/5535495/create-and-change-to-a-new-directory-in-one-command)
}
