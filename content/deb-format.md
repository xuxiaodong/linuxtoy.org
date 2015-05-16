Title: deb 源代码包新格式
Date: 2009-03-08 16:54
Author: toy
Category: Tips
Tags: Debian
Slug: deb-format

本文为读者 tumashu 在 man dpkg-source 过程中所作的阅读笔记，其中包含 deb
源代码新格式的一些介绍，也许有的朋友会感兴趣。

**一.新格式的优点**

1.  支持 bzip2、lzma (~~估计就是 7z 格式~~)、gzip 压缩格式
2.  支持多个上游 tarballs
3.  支持包含二进制文件，旧格式使用 diff
    文件（diff.gz）来存储打包过程中对源代码的改变，而 diff
    文件是处理文本文件的，所以如果想添加一个二进制文件（比如 png
    图标），就需要使用 uuencode 把二进制文件转换为文本文件，比较麻烦
4.  不需要因为 strip debian 目录而重新打包上游 tarball（debian 目录在
    deb
    源代码包解压缩的时候自动被.debian.tar.{gz,bz2,lzma}里面的内容取代）
5.  Debian-specific 的改变现在不是保存在单一的 .diff.gz
    文件里面而是保存在 debian/patches/ 下的多个 patch
    文件里。这种处理方式和 quilt 的处理方式兼容但不需要使用 quilt，因为
    dpkg-source 可以处理所有的事情，它在解压缩过程中使用 patch
    文件，在构建二进制包的过程中更新 patch series
6.  NMU workflow is now really: unpack, hack, rebuild (for all 3.0
    (quilt) packages).

**二.新格式的种类**

1.  Format：1.0
2.  Format：2.0
3.  Format：3.0 (native)
4.  Format：3.0 (quilt)
5.  Format：3.0 (git)
6.  Format：3.0 (bzr)

**三.Format：1.0 格式介绍**

这个是原来的格式：一个 .dsc 文件，一个 .orig.tar.gz 文件，一个 .diff.gz
文件

**四.Format：2.0 格式介绍**

这个格式不建议广泛使用，是个过渡格式

**五.Format：3.0 (native) 格式介绍**

这个格式是 Format：1.0 的扩展，可以支持多种压缩方式{gz,bz2,lzma}

**六.Format：3.0 (quilt) 格式介绍**

这个格式可能被 debian 的下一个版本采用，它是 Format：2.0
的扩展，因为它补丁的处理方式和 quilt 兼容，所以如此命名

源代码包的组成:

1.  一个 .orig.tar.{gz,bz2,lzma}压缩包，这个包是上游源代码更名后得到的
2.  一个 .debian.tar.{gz,bz2,lzma}压缩包，这个包包含了 debian
    化的所有更改
3.  零个或者多个
    .orig-<component>.tar.{gz,bz2,lzma}，比如：.orig-hello.tar.{gz,bz2,lzma}
    或 .orig-world.tar.{gz,bz2,lzma}。这是为了支持多个上游 tarball
4.  一个 .dsc 文件

源代码包的解压缩：

1.  orig 包首先解压缩，产生一个目录，比如：helloworld\_0.1.1.orig.tar.gz
    就会生成 helloworld-0.1.1 这个包含上游源代码的目录
2.  所有 orig-<component>
    解压缩，产生一个目录，比如：helloworld\_0.1.1.orig-toy.tar.gz
    就会生成 helloworld-0.1.1/toy/ 目录，这个目录包含
    helloworld\_0.1.1.orig-toy.tar.gz 里面所有的内容，原来存在的
    helloworld-0.1.1/toy/ 将被取代 (man dpkg-source
    这一段没有看懂，可能理解有误。)
3.  debian 包解压缩，生成 debian
    目录，比如：helloworld\_0.1.1.debian.tar.gz 就会生成
    helloworld-0.1.1/debian/
    目录，原来存在的这个目录在这个过程中将被删除....注意：debian.tar.{gz,bz2,lzma}里面必须包含一个
    debian 目录，它也可以包含二进制文件。
4.  应用补丁：文件 debian/patches/debian.series 或者
    debian/patches/series 里面罗列的补丁。补丁必须是 patch -p1
    的。补丁也可以删除文件。如果在解压缩过程中应用了某些补丁，那么
    debian/patch/.dpkg-source-applied 文件会记录它们。
5.  和 quilt 的默认相似，这里使用补丁也可以删除文件

源代码包的构建：

1.  更新 debian-changes-<version> 补丁：当前目录中所有的源代码包 (orig
    包，component 包) 都会解压缩到一个临时目录中，然后 debian
    目录也拷贝到这个临时目录最后打上除 debian-changes-<version>
    补丁外的所有补丁，比较临时目录和源代码所得补丁(如果不同），会保存为
    debian/patches/<debian-changes-version>
    补丁文件，任何二进制文件的变化都不会出现在 diff
    中，否则会导致构建失败，除非维护人员决定在 debian 包中包含二进制文件
    (相对于源代码目录，在 debian/source/include-binaries
    中列出添加或更改的二进制文件的文件名) 如果发现 debian
    子目录中有二进制文件，构建也会失败，除非文件名已经在
    debian/source/include-binaries 中列出。
2.  更新 debian.tar.{gz,bz2,lzma}：通过更新的 debian
    目录和更改过的二进制文件 (列出的) 会重新生成 debian 包

注意：自动生成的 diff 不包含 VCS 描述文件和许多临时文件 (参照 -i 选项)
的变化，例如：quilt 使用的 .pc 目录在生成自动补丁时就会被忽略。

**七.Format：3.0 (git)**

这个源代码格式是实验性质的，也许会在 debian
的下下或者下下下个版本采用，也许永远不会采用......这是源代码包和版本控制系统
(git) 的结合，具体细节请：man dpkg-source。

**八.Format：3.0 (bzr)**

这个源代码格式是实验性质的，也许会在 debian
的下下或者下下下个版本采用，也许永远不会采用.........这是源代码包和版本控制系统
(bzr) 的结合，具体细节请：man dpkg-source。

[感谢 tumashu 朋友分享]
