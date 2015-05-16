Title: cgvg——命令行下的代码查看工具
Date: 2010-02-24 11:33
Author: toy
Category: Apps
Tags: cgvg
Slug: cgvg

{ 撰文/[alexmajy](http://jonnymajy.spaces.live.com) }

今天给大家介绍一个命令行下查看代码的小工具——cgvg。cgvg 是由程序员 Joshua
Uziel  
为程序员编写的代码查看工具。简单的说，cg
的功能是递归地在当前目录下进行类似于  
grep 的模式匹配查找，然后将结果输出到控制台。vg  
的功能是用默认编辑器打开并定位到 cg
上次搜索得到的某一结果。这里的截屏给出了  
cgvg 使用的一个例子。

[![cgvg](http://i.linuxtoy.org/images/2010/02/cgvg-thumb.png)](http://i.linuxtoy.org/images/2010/02/cgvg.png)

虽然平时我也在 Vim 下用吴垠同学介绍到的 grep 插件[1]，而且 Vim
下也有文件管理插件，但在有些情况下我还是要在 Shell 里面执行一下 find-  
grep-vim，再加上比较喜欢 cgvg
清晰的输出显示和简洁的命令接口，我最终决定将其纳入自己的 Linux-box
中。Archlinux 和  
Ubuntu 的应该可以从源里直接安装，我的系统是 Ubuntu 9.10，直接 `sudo
apt-get  
install cgvg` 就可以了。

PS: 之前一直想自己写个 Shell
脚本自动化这个过程，不过一直不知道自己平时在瞎忙什么。如果你和我一样是个比较懒惰的
Linux 用户，那么从今天起装上 cgvg
开始更加高效的生活，并把那个自动化条目从你的 Todo list
上去掉吧，哈哈。BTW，估计 Emacs
帮派可能不太需要这个东东，据说他们完全生活在 Emacs 中：）感谢 alex 分享
cgvg。

参考：

[1] [手把手教你把 Vim 改装成一个 IDE
编程环境(图文)](http://blog.csdn.net/wooin/archive/2007/10/31/1858917.aspx)  
[2]

{ Thanks alexmajy. }
