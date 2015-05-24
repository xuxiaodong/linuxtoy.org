Title: pinfo: 强大的 manpage/Texinfo 查看软件
Date: 2011-01-29 10:01
Author: lovenemesis
Category: Featured
Tags: pinfo
Slug: pinfo-manpage-texinfo-viewer-part-2

紧接着[上一篇](http://linuxtoy.org/archives/pinfo-manpage-texinfo-viewer-part-1.html)，开始介绍
pinfo 查看软件。*感谢 cheer_xiao 投稿*

在 Debian/Ubuntu 下用

`sudo apt-get install pinfo`

在 Fedora 下用

`pkcon install pinfo`

在 Arch 下用

`sudo pacman -S pinfo`

在 FreeBSD 下用

`cd /usr/ports/misc/pinfo && make install clean`

即可安装。

pinfo
的源码包很小，有环境的同学可以在[这里](https://alioth.debian.org/frs/download.php/3351/pinfo-0.6.10.tar.bz2)下载、编译。

pinfo 默认采用类似字符界面浏览器 lynx 的键绑定模式，而 lynx
的键绑定又是仿照 vi 的。默认键绑定将在下面几个实例中予以讲解。

我们先试试 `pinfo man`。这里打开的是 `man` 的 manpage（因为她没有
Texinfo 文档）。效果如图：

[![pinfo](http://linuxtoy.org/img/2011/01/pinfo-man-head.png)](http://linuxtoy.org/img/2011/01/pinfo-man-head.png)

看起来和 `man` 的界面挺像的，基本操作和 `man`
的区别也不大。上、下键用于滚屏，也可以使用 vi 风格的 j 和
k。空格键下翻一整屏。不过不能按回车键下滚一行——它已经被用作跟随链接的快捷键了。另外，vi
风格的按 g 到最前、G 到最后，默认也不支持。不过可以用 Home 和 End
键到最前和最后。

现在让我们按 End 键到最后，这里有不少链接：

[![pinfo](http://linuxtoy.org/img/2011/01/pinfo-man-tail.png)](http://linuxtoy.org/img/2011/01/pinfo-man-tail.png)

稍一研究发现，绿色的是指向其它 manpage
的，紫色的是指向邮件地址（实际上外部地址都是这样）的，最下面的红色链接是当前选中的链接。如果按上键或者
k，不会向上滚屏，而是选中了上一个链接。按若干次上键或 k，选中 `less`：

[![pinfo](http://linuxtoy.org/img/2011/01/pinfo-man-follow-less.png)](http://linuxtoy.org/img/2011/01/pinfo-man-follow-less.png)

现在按回车或者右键即可跳到 `less` 的
manpage。返回呢？按左键即可。就和浏览器的操作方法一样，因为说过它的键绑定是从
lynx 借来的。按 q 键退出，按 / 键搜索，这和 `man` 和 vi
都一样。不过不顺手的是，“搜索下一个”默认绑定到 f 和 0，而不是
n，不过当然很容易重新配置。

不过顾名思义，pinfo 主要还是用来看 Texinfo 文档的。 现在我们在终端里面打
`pinfo pinfo`：

[![pinfo](http://linuxtoy.org/img/2011/01/pinfo-pinfo.png)](http://linuxtoy.org/img/2011/01/pinfo-pinfo.png)

默认的键绑定方案在 Configuration > Configuration file > Example config
file
中。不难看出来，上半部分是颜色配置，下半部分是键绑定配置。这个默认的配置文件保存在
`/etc/pinforc` 下。（Ubuntu 下用 APT 安装的是在这里。自己编译的在
`/usr/local/etc/pinforc`
下。其它发行版可能不同，请读者补充。）要定制键绑定，把它复制为
`~/.pinforc` 再做修改即可。很值得一提的是 Vim
7.3（这是我使用的版本，不知是哪个版本开始有的）自带有 `pinforc`
的语法高亮，`COLOR_RED`、`BOLD`
这类关键字会直接显示成相应的颜色和风格（红色、加粗），十分方便。

pinfo 的 Texinfo
页面十分友好，掌握以上基本操作之后同学们就可以自己学习啦。在最后再送上几个小技巧：

pinfo 会先搜索 Texinfo 文档，找不到时才显示 manpage。以下命令强制显示
`ls` 的 manpage：

`pinfo -m ls`

带 `-m` 时也可以指定 manpage
的区段。以下命令显示第二区段（系统调用）中的 `stat`：

`pinfo -m 2 stat`

用 `man -k` 可以搜索 manpage。`pinfo -m -k`
也可以，而且会把搜索的结果显示成一个个超链接，十分方便。下面是
`pinfo -m -k what` 的截图：

[![pinfo](http://linuxtoy.org/img/2011/01/pinfo-key-what.png)](http://linuxtoy.org/img/2011/01/pinfo-key-what.png)

因为 `pinfo -m` 和 `man` 接受的参数相同，我现在干脆把 `man` 设成了
`pinfo -m` 的别名：

`alias man="pinfo -m"`

PS.
刚才看了看[预备知识篇](http://linuxtoy.org/archives/pinfo-manpage-texinfo-viewer-part-1.html)的[四楼评论](http://linuxtoy.org/archives/pinfo-manpage-texinfo-viewer-part-1.html#comment-191420)，Adaptee
同学给出的[链接](http://htop.sourceforge.net/index.php?page=faq)中
`htop` 的作者也是这么做的，所见略同啦。

最后，发现 pinfo 似乎还缺少一个很关键的功能，即“搜索上一个”，在 `man` 和
vi 中绑定到 N。不知是在下未发现还是 pinfo 自身的问题，请读者指教。如果是
pinfo 自身的问题，她的源码比较简单，有精力和能力的同学不妨自己动手 hack
之。

截屏中使用的终端是
[ROXTerm](http://roxterm.sourceforge.net/)，终端字体是 Monaco。

[pinfo 主页](http://pinfo.alioth.debian.org/)

[SVN 访问](//svn.debian.org/svn/pinfo)

（完）
