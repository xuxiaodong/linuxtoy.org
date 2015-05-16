Title: Zsh 使用技巧一则: 文件关联
Date: 2009-03-23 19:07
Author: toy
Category: Cli
Tags: Zsh
Slug: zsh-tip

在图形化的文件管理器中，通常我们只要单击/双击某个文件，文件管理器就会调用相应的程序来打开该文件。其实，这样的文件关联在
Zsh 中也可以实现。具体操作步骤如下：

1. 添加下列内容到你的 $HOME/.zshrc 文件中：

autoload -U zsh-mime-setup  
zsh-mime-setup

2. 以关联扩展名为 png 的图像文件为例，假设要通过
[pho](http://linuxtoy.org/archives/pho.html) 程序来查看，那么在
$HOME/.zshrc 中可以这样定义：

alias -s png=pho

我们以 alias 的形式来实现文件关联，其中 png 为要关联文件的扩展名，=
右边的 pho 为关联的程序。这里的 -s 必不可少。

要关联其他类型的文件，只需如法炮制即可。

3. 为了使 .zshrc 生效，需要 source 该文件。

现在，在 Zsh 中，例如要查看 linuxtoy.png 文件，只要输入该文件名（可按
Tab 自动补完）并按回车，Zsh 便会自动调用 pho 来打开。
