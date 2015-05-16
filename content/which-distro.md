Title: 哪个发行版能解决?
Date: 2008-12-28 18:40
Author: toy
Category: AskLinuxtoy
Slug: which-distro

[fcicq](http://www.fcicq.net/wp/) 写道：

“最近有那么一点点想换发行版的愿望, 虽然现在 Gentoo 很好...

需要考虑的问题如下:  
1 启动速度  
Fedora 10 这方面好像不错, Ubuntu 听说也可以, 但现在的 OpenRC
就不那么令人满意.

2 运行  
偶的 64bit kernel 不需要 32bit 的支持, gentoo 有 no-multilib profile,  
只要重新编译几个包(gcc, glibc, binutils ...), 系统就是干净的, 没有
32bit 的可执行程序(grub  
就先不算了).

3 软件的安装  
工作需要安装大量第三方开源软件, gentoo 写 ebuild 不错,
虽然还是有那么一点点麻烦.  
用惯了 gentoo, 讨厌类似 libxxxxx-devel 这样的包, 讨厌 ./configure &&
make && sudo  
make install. (而且不干净)  
gentoo 之外哪个发行版能更好的解决这个问题?

4 系统的安装  
(1) gentoo 装好之后需要细调的有点太多. -- 如果其它发行版需要调的一样多,
那这条就不算是问题了.  
(2) gentoo 安装严格讲根本不需要 livecd, 好像 debian/ubuntu 有
debootstrap, 这个好用吗?  
(3) 以 gentoo 作为包干净的标准的话, 其它发行版做的又怎么样呢?  
(4) 除 gentoo 外, kernel source 的分发方式好像都是自有(当然是 deb/rpm
之类)的打包方式,  
小升级的时候偶如果需要重新编译核心的话又会是怎样的?
(如果需要重新下一遍源码的话就太不好了...)  
(gentoo 是 linux-2.6.xx.tar.bz2(满世界都是镜像的文件...) +
genpatches.tar.bz2,  
重新抓的部分仅限于后者, 非常小)

---

简单总结就是, gentoo 在细节上表现(好像?)不如更流行的发行版,
方便程度上有一部分是符合偶的需求的, 另一部分不太符合...  
最后一句, 哪个发行版能解决? :D”
