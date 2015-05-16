Title: LinuxDNA: 高性能 Linux 内核项目
Date: 2009-02-27 18:18
Author: toy
Category: News
Tags: Kernel, LinuxDNA
Slug: linuxdna

开源项目 LinuxDNA 旨在针对 Intel 的 C/C++
编译器（简称“ICC”）提供一个兼容的 Linux 内核源。据 Linux Journal
的报道称，LinuxDNA 项目在本月初使用 ICC 成功的编译了 Linux Kernel
2.6.22。编译不仅没有出错，而且完全可以引导进入 Linux 系统。

可能有人会问：为什么要使用 gcc
之外的编译器来编译内核？答案是，性能。早期使用 ICC 编译 Linux
内核的研究表明，使用 ICC 编译内核，性能可提升达 40%
之多。一名德国的开发者 Ingo A. Kubblin 也指出：“核心的某些部分性能提升了
40%，平均性能可提升 8-9%。”

目前，LinuxDNA 项目网站提供了一份安装 ICC
及编译内核的说明，不过该说明是基于 Gentoo Linux 发行版。使用其他 Linux
发行版的朋友在参照时需略作调整。

相关源代码及脚本可从 LinuxDNA 项目官方网站下载。

[LinuxDNA](http://www.linuxdna.com/)

[via [Linux
Journal](http://www.linuxjournal.com/content/linuxdna-supercharges-linux-intel-cc-compiler)
& [Solidot](http://linux.solidot.org/linux/09/02/27/0313201.shtml)]
