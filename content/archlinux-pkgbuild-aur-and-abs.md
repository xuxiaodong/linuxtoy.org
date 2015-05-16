Title: Archlinux 的灵魂──PKGBUILD、AUR 和 ABS (1)
Date: 2008-02-28 10:30
Author: Ning Bao
Category: Featured
Slug: archlinux-pkgbuild-aur-and-abs

本文由读者 Ning Bao 所撰写，其中包括 Archlinux 的 PKGBUILD、AUR 及 ABS
等内容。这是该文的第一部分，主要介绍 PKGBUILD 和 makepkg。既然现在有
Ning Bao 朋友来做这件事情，那么我的《打造完美的 Linux 桌面──Arch Linux
2007.08-2》就算完结了。等 Ning Bao
朋友写完后，我打算出个全面修订的电子版本，方便大家阅读。

作者 / Ning Bao

**第一部分：PKGBUILD 和 makepkg**

其实，我使用 Archlinux
的时间并不是很长。可是，就是在这半年的时间内，我感觉我学到了很多的东西，对
GNU/Linux 有了更多的了解，也在这个过程中深深地爱上了 Archlinux
这个发行版。

首先声明一下，我不是一个程序员，从来没有写过真正的 Code，顶多是写一点
scripts，或者做一些简单的网页什么的。和很多人一样，我对计算机的接触是从
DOS/Windows 开始的。Windows 的图形界面很容易学。可是时间长了，Windows
就会运行的越来越慢，我的硬盘上也就会有很多我根本不知道是什么的东西。而且，在
Windows
上很多东西都是设定好的，改变起来非常不容易。不要跟我提注册表，那个东西实在是让我一头雾水。还有，大部分
Windows
上的软件都不是自由软件。这意味着人们很难了解这些软件内部的情況，你可能在毫无察觉的情况下就中了病毒或木马。

所以，为了能够完全了解和控制我每天工作生活要用的计算机，我开始学着使用
GNU/Linux。我一开始是用 Mandriva（那个时候还叫 Mandrake Linux）。后来是
Ubuntu（也包括其他一些 Debian 为基础的发行版）。Wow！我一用上 Ubuntu
就有了完全不同的感觉。特别是非常好用的
apt-get，加上庞大的自由软件库，让我大开眼界。可是在使用 Ubuntu
一段时间以后，我发现这个平台实在和 Windows 非常相似。Gnome 和 KDE
的界面都是在模仿 Windows。更糟糕的是，Ubuntu
会在一开始安装一些乱七八糟的东西，大大影响了我的电脑的运行速度。我需要一点一点把我不用的东西去掉，这个过程真的很不爽。我开始问自己为什么要放弃
Windows 呢？

Ubuntu
有一个很大很好的用户社区，很多问题都可以在讨论区得到解决。然而，Ubuntu
的用户完全要依赖 Maintainer。我就有过这样的经历，在发现一个 Bug
后得到很多其他人的确定，可是 Maintainer
迟迟不作修改。还有，也许有很多人都很想用一个比较新的软件，但是大家都要等到有人能够而且愿意作
Maintainer 之后，这个软件才会在 Repository
里出现。我或许能够在调试后自己从源代码编译，可是我要如何和别人分享我的成果呢？

其实，各种 Linux
发行版在本质上没有什么不一样。大家使用的软件都是要从源代码编译生成可以运行的二进制码。如果没有
rpm、apt-get 或者
pacman，我们也是可以快乐生活的。只不过，我们的生活会变得麻烦一些。如果要从源码安装一个软件，我们通常是要做如下的步骤：  

` wget http://somewhere.org/source/package.tar.gz（下载源代码） tar xvzf package.tar.gz （解压缩） cd package （进入源代码目录） ./configure （设定） make （编译） make install （安装）`

如果我们要像这样安装一个两个软件是没有什么问题的。但是如果我们要对付成百上千的软件／类库的话，这样的土办法是行不通的。于是出现了不同的
Linux
发行版，他们之间的区别只是在于如何管理成百上千的软件，特别是不同软件／类库之间互相依存的关系，也就是
dependency 的问题。

大多数 Linux 发行版都是以二进制包为基础的，这其中又分 Redhat（还有
SUSE、Fedora 等）、Debian（还有 Ubuntu、PCLinux 等）和 Slackware
阵营。为了解决管理大量软件包的问题，这些发行版采取了这样一个办法。他们找了一群大牛程序员来作
Maintainer，这些 Maintainer
负责把源代码编译成二进制码，加上一些控制信息（比如如何安装、dependency
等），然后一起打包放在服务器上。所以，最终用户根本不用接触源代码。如果你有兴趣的话，你可以抓一个
Debian 的 DEB 文件下来研究一下：  
` wget http://somewhare.org/package.deb ar vx package.deb`

你会发现你多了三个文件：  
` debian-binary control.tar.gz data.tar.gz`

然后再用 tar tzvf 命令看一看 control.tar.gz 和 data.tar.gz
里面有什么东东，你就明白神奇的 dpkg/apt-get 是怎么一回事情了。

二进制包固然是很方便，但是这种办法有一个很大的问题。那就是最终用户受到
Maintainer 很大的控制。比如说，我们并不知道 Maintainer
在编译的过程中是如何设定的（./configure）。如果我们要用不同的设定，就要自己从源代码从头开始。另外，如果某一个
Maintainer
心术不正，在二进制包里面加了木马程序，我们这些最终用户是很难查觉的。还有，设想一下如果某一个
Maintainer 外出休假了，那么你的软件也就不能及时更新了。

所以，也有一些发行版采取了完全不同的办法，这些发行版是以源代码为基础的。Gentoo
就是其中的代表。如果你用过 Gentoo 你就会知道 ebuild
文件。你如果有兴趣，可以从 http://gentoo-package.com 抓一个 ebuild
文件研究一下。你会明白 Gentoo 的用户其实从 Gentoo 得到的只有这些 ebuild
文件，在每一个 ebuild
文件里包含了安装使用一个软件需要的所有信息（从哪里下载源代码、如何编译、如何安装还有
Dependency 的问题等）。之后，Gentoo 的用户用 emerge 命令按照 ebuild
文件的指示编译、安装一个软件。这样做的好处是，Gentoo
的用户可以一目了然地了解每一个软件的编译、安装的过程。如果需要的话，Gentoo
的用户可以修改 ebuild，按照自己的需要编译一个软件。

我也用过 Gentoo。不过对于我这样的初学者，Gentoo
实在是太复杂了，有太多的参数要设定，ebuild
的编写也不是那么简单。还有，Gentoo
几乎不提供任何二进制包，所以绝大部分的软件都要从源代码编译，这是一个非常慢的过程。其实在大部分情况下，用户对一些软件的设定都是差不多的，没有必要让每一个
Gentoo 的用户都从头编译。所以，我需要找到一个发行版，既有 Debian
的易用性，又有 Gentoo 的灵活性。

我因此找到了 Archlinux。那么 Archlinux
又是如何解决从源代码到二进制码的问题呢？Archlinux 使用了 makepkg
这样一个工具。makepkg 会按照 PKGBUILD
文件生成一个二进制包。有些时候，makepkg 还需要 install
文件（主要用来显示提示信息、备份用户设置等）和其他的配置文件。那么
PKGBUILD 是什么呢？PKGBUILD 和 Gentoo 的 ebuild
一样，包含了安装使用一个软件需要的所有信息。下面是
dwm（一个非常非常简捷、高效的窗口管理器）的 PKGBUILD 文件：


    # Contributor: Dag Odenhall <dag.odenhall@gmail.com>
    # Contributor: Grigorios Bouzakis <grbzks@gmail.com> 是谁写了这个 PKGBUILD
    pkgname=dwm 软件名称
    pkgver=4.7                                  
    pkgrel=1 版本信息
    pkgdesc="A dynamic window manager for X"            
    url="http://www.suckless.org/wiki/dwm" 软件说明和网站
    arch=('i686' 'x86_64') 适用平台
    license=('MIT') 版权
    depends=('libx11') Dependency  
    install=dwm.install install 文件
    source=(http://www.suckless.org/download/$pkgname-$pkgver.tar.gz   
       config.h) 要下载的源文件
    md5sums=('827b128514a3edb87e208e84fee0eb3f'
             '395e9a25f65605c4891e74c644b91530') md5 验证码

    build() {
      cd $startdir/src/$pkgname-$pkgver

      cp ../config.h .

      make X11INC=/usr/include/X11 X11LIB=/usr/lib/X11 || return 1
      make PREFIX=/usr DESTDIR=$startdir/pkg install || return 1

      install -m644 -D LICENSE $startdir/pkg/usr/share/licenses/$pkgname/LICENSE &&   
     install -m644 -D README $startdir/pkg/usr/share/doc/$pkgname/README
    } 编译的过程

我们可以注意到在“编译的过程”这个部分，很多代码都和我们在 shell
里编译的命令一样。对！Archlinux 不要求用户学习太多新的东西，PKGBUILD
很容易理解，因为里面都是基本的 shell 命令。

好，我们把 PKGBUILD，dwm.install 和 config.h（dwm 比较特殊，config.h
包含所有的配置信息，所以要在编译之前提供。其他的软件大多依靠外部的配置文件，像是
.bashrc 等）放在一个新的目录里之后。我们执行：

`makepkg`

之后，你会发现这个目录里出现了一些新的东西，包括：  
` dwm-4.7-1-x86_64.pkg.tar.gz dwm-4.7.tar.gz`

两个文件，还有两个目录  
` src pkg`

通过比较这些文件、目录里的内容和 PKGBUILD，你就会明白 makepkg
到底做了些什么：

1.  根据 source 里的内容下载了源代码文件 dwm-4.7.tar.gz；
2.  通过 md5 验证码确定下载的源代码文件和 PKGBUILD
    的作者使用的是一致的；
3.  把源代码文件解压缩到 ./src/$pkgname-$pkgver （也就是
    ./src/dwm-4.7）；
4.  按照 build() 里的内容编译源代码，并把编译好的内容放在 ./pkg 里；
5.  在 ./pkg 里加上其他的一些信息，包括 .PKGINFO 和 .INSTALL，也就是
    dwm.install 的拷贝；
6.  把 ./pkg 里面的内容打包形成 dwm-4.7-1-x86\_64.pkg.tar.gz。

那么，我们有了一个 .pkg.tar.gz
这样一个二进制包之后，我们要如何安装呢？我们要使用这样一个命令：

`pacman -U dwm-4.7-1-x86_64.pkg.tar.gz`

这个命令又完成了那些事情呢？

1.  首先，二进制包被解压缩；
2.  按照 .INSTALL 的内容执行一定的命令；
3.  二进制包里面的内容会被拷贝到相应的目录（你注意到二进制包内的目录结构了吗？）；
4.  在 /var/lib/pacman/local 这个目录中建立 dwm-4.7-1 这样一个目录；
5.  这个目录里包含了四个文件 depends、desc、files 和 install;
6.  depends 记录了 dependency，desc 是软件说明，files
    记录了每一个安装到系统上的文件的路径，install 就是 .INSTALL 的拷贝。

从这以后，pacman 正是通过检查 /var/lib/pacman/local
里的内容来管理软件包的。比如说，在执行 pacman -R dwm 的过程中，pacman
首先在 /var/lib/pacman/local 找到了 dwm-4.7-1 这个目录，然后根据 files
的内容删除已安装的内容。Dependency 也是通过 depends 计算的。

OK！我已经解释了 PKGBUILD 的基本结构和 makepkg 的过程。基本上是两步：从
PKGBUILD 到 .pkg.tar.gz
包，再从二进制包安装到系统。这样一种办法有很多好处。首先，PKGBUILD
非常方便用户交流。我的一个 PKGBUILD
如果编译成功了，就可以给别人用。PKGBUILD
的内容一目了然，不但有助于学习，也再不用担心木马的问题了。

另外，我通过一个小例子展现 Archlinux 的灵活性在哪里。比如，我要对 dwm
有自己的设置，也就是自己的
config.h，那我应该怎么做呢？我会做如下的事情：

1.  编辑 config.h，另存为 myconfig.h；
2.  编辑 PKGBUILD，把所有的 config.h 替换为 myconfig.h；
3.  把 pkgrel 变成 2。

之后通过 makepkg，我会得到一个文件
dwm-4.7-2-x86\_64.pkg.tar.gz，这个和原来的 dwm-4.7-1-x86\_64.pkg.tar.gz
可以区别开。我可以安装
dwm-4.7-2-x86\_64.pkg.tar.gz，如果有问题我还可以通过 pacman -U
dwm-4.7-1-x86\_64.pkg.tar.gz
来安装原来的二进制包。我还可以用同样的办法生成一系列的 .pkg.tar.gz
包，这在软件的安装调试过程中非常有用。

好了，今天就讲到这里。有些人也许变得更疑惑了，因为在 TOY 的“[打造完美的
Linux 桌面 — Arch Linux
2007.08-2](http://linuxtoy.org/search/Arch+Linux+2007.08-2)”系列中并没有提到
PKGBUILD 的问题，所有的软件都是通过 pacman -S 来安装的。

没关系，如果你理解了 makepkg 和 PKBGUILD，那么在我下一次谈到 AUR 和 ABS
之后，你就能完全明白了。
