Title: Command-T: 在 Vim 中快速导航文件
Date: 2010-05-09 18:23
Author: toy
Category: Apps
Tags: Command-T, Vim, Vim plugin
Slug: command-t

[Command-T](https://wincent.com/products/command-t) 是一款很不错的 Vim  
插件，该插件允许你在 Vim 中快速导航文件，以用于后续的编辑处理。

![commandt](http://i.linuxtoy.org/images/2010/05/commandt.png)

**安装 Command-T**

在下载
[Command-T](http://www.vim.org/scripts/script.php?script\_id=3025)  
后，你可以按如下的步骤来安装：

vim command-t-0.6.vba  
:so %  
cd ~/.vim/ruby/command-t  
ruby extconf.rb  
make

**Command-T 的用法**

通过 `:CommandT` 命令呼出 Command-T 窗口，在底部的 >>  
提示后输入字符可以缩小匹配的文件范围。使用 Ctrl-j/Ctrl-k  
进行下上移动选择，一旦选好即可按 Enter 来打开文件。
