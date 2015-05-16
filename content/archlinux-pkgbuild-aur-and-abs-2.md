Title: Archlinux 的灵魂──PKGBUILD、AUR 和 ABS (2)
Date: 2008-02-29 09:29
Author: Ning Bao
Category: Featured
Slug: archlinux-pkgbuild-aur-and-abs-2

这是《Archlinux 的灵魂──PKGBUILD、AUR 和 ABS》一文的第二部分，主要介绍
AUR 和 ABS。上接第一部分：[PKGBUILD 和
makepkg](http://linuxtoy.org/archives/archlinux-pkgbuild-aur-and-abs.html)。

作者 / Ning Bao

**第二部分：AUR 和 ABS**

我非常高兴看到我关于 PKGBUILD 和 Makepkg 的文章在
[LinuxTOY](http://linuxtoy.org)
受到了欢迎。我想先针对一些读者的回复谈一点题外话。我先声明我一点也没有要诋毁
Debian 或 Gentoo
的意思，他们都是非常伟大的发行版，都有自己的特色。其实大多数的发行版都可以自己去定制，从而达到类似的目的。比如说，有的人提到
Gentoo 也有二进制包，比如像 Openoffice
这样的怪物。然而，我个人以为比较不同的发行版关键是要看它最核心的设计思想。比如说，Gentoo
根本就不是为了使用二进制包设计的。你要是都想用二进制包，就别费劲用
Gentoo 了。关于 Debian
阵营的发行版，我也想讲几句。正如一些朋友的回复所讲，DEB/apt-get
是非常好的管理工具，软件库也非常的大。我的笔记本现在还在用 elive，也是
Debian 的分支。我不喜欢 Debian
系列的发行版的原因不是它不能定制，而是他们非常依靠
Maintainer。我们可以自己做 DEB 包，然后呢？你的 DEB
包什么时候才能进入软件库呢？还有，只有你自己知道你的 DEB
是怎么做的，别人不能了解你编译打包的过程。Debian 本身打包的过程没有
Archlinux 的 PKGBUILD 来的简单明了。只要比较 Debian 的 Maintainer 手册和
Archlinux 的 Wiki 就可以看出这一点。

选择什么样的发行版完全是要看个人需要。我选择
Archlinux，是因为它当初设计的时候就是要满足“KISS Rule”，也就是“Keep It
Simple, Stupid”。或者说像爱因斯坦讲得：“Everything should be made as
simple as possible, but no simpler”。Archlinux
的所有配置基本都是非常相似的脚本，加上简单灵活的 PKGBUILD 和
pacman，其实关于 Archlinux
本身真的没有太多新的东西要学习。大家有兴趣可以看看“Arch Compared To
Other Distros”。Archlinux
实际上是强迫用户从零开始自己定制自己的系统，在这个过程中也就真正了解了
Linux 本身。

好了，现在言归正传谈一谈 AUR 和 ABS。

AUR 是指 Archlinux User-community Repository，也就是 Archlinux
用户社区的软件库。我们现在回忆一下在 Archlinux
中我们把源代码变成可以运行的二进制码需要哪些文件。我们需要：PKGBUILD，可能还有
.install 文件，加上一些补丁和必要的配置文件（像 dwm 的
config.h）。这样就足够了！当你成功使用 PKGBUILD
编译安装了一个新软件之后就可以通过 AUR
和其他的人分享你的成果了。具体的步骤是：

1.  `tar -zcvf package.tar.gz package-dir` 把 package-dir
    中所有所需的文件打包（包括 PKGBUILD，.install，patch 和其他的 config
    等）
2.  前往 <http://aur.archlinux.org> 选择"Submit”（参照下图），并把你的
    package.tar.gz 上传

[![Arch
build](http://i.linuxtoy.org/i/2008/02/arch-build1-thumb.jpg)](http://i.linuxtoy.org/i/2008/02/arch-build1.jpg)

AUR 会自动根据你的 PKGBUILD 内容把你的 Package 加到 AUR
里来。就是这么简单！那么有人会问：“别的用户要如何使用 AUR 呢？”

这个就更简单了，我们还是用一张截图来解释：

1.  首先下载“Tarball”（红色的圈圈），这个 Tarball
    和你上传的内容是一样的，无非是 PKGBUILD 什么的；
2.  `tar xvzf package.tar.gz` 然后解压缩；
3.  然后的步骤你应该知道了，那就是 makepkg 还有 pacman -U。

不过需要提醒的是，为了对自己负责，你应该在编译之前读一下 PKGBUILD 和
.install 的内容，确定里面没有恶意的代码。另外，我建议你一般不要以 root
的身份进行 makepkg。其实，makepkg 本身也做了这样的限制，你不加— asroot
的选项是不能 makepkg 的。这是因为，makepkg 会执行 PKGBUILD 里 build()
部分的代码。想一想，如果有人在 build() 这部分加了这么一句“rm -r
/home”，你就死定了！

如果你注意到，在每个 AUR Package
的网页上都有投票（绿色的圈圈）和回复的功能（蓝色的圈圈）。这些是帮助用户反馈意見的。

[![Arch
build](http://i.linuxtoy.org/i/2008/02/arch-build2-thumb.jpg)](http://i.linuxtoy.org/i/2008/02/arch-build2.jpg)

有些性急的朋友可能要问这个 AUR 和 pacman
取得的二进制包有什么联系？你应该记住，只要是
Archlinux，所有的东西一定是从 PKGBUILD 开始的。你通过 pacman
得到的二进制包也是从 PKGBUILD 编译而成的。在你的 /etc/pacman.conf 有很多
Repository 的设置，其中的 [core] 和 [extra] 是由 Archlinux
的核心成员维护的，这些软件库里的软件由于特别重要，每个人都要用，所以
Archlinux 的开发人员把二进制包提前做好，你就可以通过 pacman
取得了。然而，和 Debian 的 Maintainer
机制不一样，最终的用户可以很容易的了解这些软件的编译过程。如果需要的话，最终用户可以改变设置，重新编译这些软件。最典型的情形就是自己编译
kernel 的时候。这要通过 ABS 来解释清楚。ABS，也就是 Archlinux Build
System。首先我们要安装 ABS：

1.  `pacman -S abs`
2.  `vi /etc/abs/abs.conf` 编辑 ABS 的配置文件；
3.  你会看到这样一行 SUPFILES=(core extra !unstable community
    !testing)，把你需要的 Repo 之前的 ! 去掉；
4.  然后以 root 身份执行 abs

之后又要如何使用 ABS 呢？ABS 所作的事情无非是把所有 Repo 里的软件的
PKGBUILD 下载到你本地的硬盘中。这些 PKGBUILD 都放在了 /var/abs
中。你能通过 pacman 直接安装的二进制包其实也都是按照 ABS
的内容编译的。下面我还是用 dwm 的例子解释 ABS 的使用：

1.  `su`
2.  `cd /var/abs` 你可以看到这个目录里有 core，extra，community
    三个子目录，正如 abs.conf 中的设定；
3.  `mkdir local` 建立一个 local 目录，用来放你自己需要的软件的 PKGBUILD
4.  `chown username:usergroup ./local makepkg` 要以非 root 身份进行
5.  `exit` 退出 su
6.  `cd local`
7.  `cp -r ../community/x11/dwm ./` 从 ABS 中拷贝 dwm 的内容
8.  `cd dwm`

下面不用我说了，你在这个目录里可以看到三个文件
PKGBUILD、dwm.install、config.h。你于是可以用 makepkg 和 pacman -U
来按照自己喜欢的方式安装 dwm。

OK，你实际已经清楚了解了 ABS 和 pacman 的关系，那么 AUR 又和 ABS 还有
pacman 有什么联系呢？说的直白一点，你上传到 AUR 的 PKGBUILD
要足够“有品”才能直接通过 pacman 使用。对于“有品”，我是这样定义的。你的
PKGBUILD 要有很多人用（很多人投票），没有恶意代码，没有太多的
Bug……而判定你的 PKGBUILD 够不够“有品”的人是一些叫作 TU（Trusted
User）的人。这些人的工作是检查 AUR，关注那些特别受欢迎的
PKGBUILD。之后，他会仔细检查，确定这些 PKGBUILD
是不是安全。然后，他们会给这些 PKGBUILD 打上安全的标签，并且把这些
PKGBUILD 从 unsupported（我们上传的 PKGBUILD 一开始都是在 unsupported
中）移到 community 的 Repo 中。

在 community repo 里面的 PKGBUILD 会提前编译好，如果你在
/etc/pacman.conf 中开了 community
repo，你就可以直接使用这些软件的二进制包了。也许有一天，你当初上传的
PKGBUILD 变得特别重要，这个软件可能被移到 testing，extra 或者 core 的
repo 中。补充一点，testing repo 里面一般是需要测试，又准备放到 core 或者
extra 中的软件。

Archlinux 就是这样，非常灵活。既有 pacman 这样好的二进制包管理工具，又有
ABS 和 AUR 这样方便的源代码服务。通过
ABS，你可以完全控制你自己的系统到底是如何建立的。如果在 pacman -Ss
的时候找不到一个软件，你可以到 AUR
去找，如果还是找不到，为什么不自己试着从源代码开始，写一个 PKGBUILD
然后放到 AUR 中和别人分享呢？

说到这里，我希望我已经把 Archlinux
最核心的东西讲明白了。有些人说我的文章写得比 wiki
里的文章清楚。其实，我写的东西只是在順序上不一样。我是从 PKGBUILD
开始讲到 AUR 和 ABS，再到 pacman。这个順序和 Archlinux
实际的开发过程是一致的，所以逻辑上容易理解很多。如果你从 pacman
入手反过来读，你可能就完全错过了理解 Archlinux 核心概念的机会。

TOY 会很快再写一篇关于 yaourt 的文章，yaourt 是一个把 pacman 和 AUR
结合起来的很好用的工具。有了 yaourt，你不需要去 AUR 网站也能在 shell
下直接取得 AUR 的 package，还方便了投票的过程。

如果大家对某些问题感兴趣，可以留言告诉我，我会尽量把我了解的用这样比较容易理解的文章与大家交流。
