Title: 分布式源代码管理系统 BitKeeper 开源
Date: 2016-05-11 16:08:46
Authors: toy
Category: News
Tags: scm
Slug: bitkeeper
Via: BitKeeper|https://www.bitkeeper.org/index.html
Thank: LWN.net|http://lwn.net/Articles/686896/

十年前，BitKeeper 因作为 Linux Kernel 的源代码管理系统而闻名。不过由于其为商业软件，后来 Linus Torvalds 受其启发开发了 Git 来管理内核源代码。最近，BitKeeper 宣布以 Apache 2.0 许可发布其源代码，可谓姗姗来迟。

<!-- PELICAN_END_SUMMARY -->

[![bitkeeper]({filename}/images/bitkeeper.thumb.png)]({filename}/images/bitkeeper.png)

相较起来，BitKeeper 对于很大型的项目在性能及可伸缩性上具有优势。同时，BitKeeper 的 Binary Asset Manager (BAM) 能够方便的存储并快速访问二进制资源文件。此外，在安全方面，BitKeeper 允许将源代码树的子集分享给内部或外部团队，无需管理负担；并会收集用于深入分析和审计的数据。

BitKeeper 为 Linux 提供有二进制包，只需下载后按提示即可安装，以 64 位为例：

    chmod a+x bk-7.2ce-x86_64-glibc219-linux.bin
    ./bk-7.2ce-x86_64-glibc219-linux.bin
