Title: 在 Archlinux 中安装 Scim-Python 输入法
Date: 2008-04-26 09:16
Author: toy
Category: Tutorials
Tags: Archlinux, Installation, scim-python
Slug: installing-scim-python-in-archlinux

下面是我在 Archlinux 中安装 [scim-python
输入法](http://linuxtoy.org/archives/scim-python.html)的过程，
希望能够和大家分享一下。选择安装 scim-python 的一个原因是 Fcitx 好像和
FF3 配合得不是很好，另外就是 Fcitx 的词库没有 scim-python 庞大。

安装 scim-python 之前，首先需要安装

`pacman -S scim`

之后

`yaourt pyenchant`

然后从
[http://code.google.com/p/scim-python](%20http://code.google.com/p/scim-python)
中[下载最新的代码](http://scim-python.googlecode.com/files/scim-python-0.1.11.tar.gz)。

将 scim-python-0.1.11.tar.gz 解压之后，执行如下命令  

` $ cd scim-python-0.1.11 $ ./autogen.sh --prefix=/usr $ make $ sudo make install`

就将 scim-python 安装好了。

之后安装 scim-bridge。如果不安装 scim-bridge
的话，某些程序是无法启动的。 比如说 Thunderbird。

`yaourt scim-bridge` 就可以安装了。

安装好之后， 需要更新一下 /etc/gtk-2.0/gtk.immodules 里面的内容。执行
gtk-query-immodules-2.0 将输出重定向到 /etc/gtk-2.0/gtk.immodules
就可以了。

然后需要手工修改一下 /etc/gtk-2.0/gtk.immodules 文件的内容，删掉和 scim
相关的那两行（保留和 scim-bridge 相关的那两行）。如果不删除 scim
相关的那两行的话， 注销之后我这里看到的情况是无法进入 X Windows
了，可能是和 scim-launcher 这个进程有关系。

之后修改 .bashrc， 添加


    export XIM=scim
    export XIM_PROGRAM=scim

    export GTK_IM_MODULE=scim-bridge
    export XMODIFIERS="@im=scim"

就可以了。

**编注**：这里不推荐在 Archlinux 中直接编译安装
scim-python，更好的解决方式是使用
[AUR](http://aur.archlinux.org/packages.php?ID=15548) (由 latteye
同学贡献)。

[撰文/leeight]
