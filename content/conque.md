Title: Conque: 在 Vim 中运行 Shell
Date: 2010-06-23 17:46
Author: toy
Category: Apps
Tags: Conque, Shell, Vim
Slug: conque

熟悉 GNU Emacs 的朋友想必都知道在其中可以使用内嵌的 Shell，这是非常方便的。虽然我们不能在 Vim 中直接使用 Shell，但是利用 [Conque](http://code.google.com/p/conque/) 这款 Vim 插件可以达到同样的目的。事实上，Conque 不仅允许我们在 Vim 的编辑缓冲区运行诸如 Bash 此类的 Shell，而且对于其它的命令行程序同样适用，如 mysql、ipython 等。

<!-- PELICAN_END_SUMMARY -->

![conque](http://i.linuxtoy.org/images/2010/06/conque.png)

如果你下载的是 [Conque 的 vimball](http://code.google.com/p/conque/downloads/) 包，那么只需执行以下命令即可完成安装：

```
vim conque_X.X.vba  
:so %  
:q
```

其中，X.X 为 Conque 的版本号。

要在 Vim 的编辑缓冲区运行 Bash，则可以执行：

    :ConqueTerm bash
