Title: 修正 mldonkey 2.8 中文文件名 bug
Date: 2006-10-22 15:32
Author: toy
Category: Tutorials
Slug: fix_mldonkey_chinese_filename_bug

mldonkey 2.8.0 处理包含中文的文件名时会把中文用下划线代替。这个 bug 到
2.8.1 中仍然存在。问题在于不能正确识别 utf-8 locale。

mldonkey 2.7.7 虽然也不能正确识别 utf-8 locale。但会强制 utf-8
文件名转换。

以下步骤可以为 2.8.1 打上解决这个问题的补丁。适用于 linux 平台。

1.  `$sudo apt-get install zlibc zlib1g-dev ＃安装编译所需要的库文件`
2.  下载 [mldonkey
    源码](http://prdownloads.sourceforge.net/mldonkey/mldonkey-2.8.1.tar.bz2?download)。  
    ` $tar jvxf mldonkey-2.8.1.tar.bz2 ＃解压源码`
3.  下载 [utf-8locale
    补丁](http://savannah.nongnu.org/patch/download.php?file_id=10445)
    (法国帅哥
    [spiralovoice](https://savannah.nongnu.org/users/spiralvoice) 提供
    ）。
    把下载到的 unicode.patch 复制到 mldonkey-2.8.1/patches/ 目录。  

    ` $cd mldonkey-2.8.1 $./configure #检查编译条件，自动下载 ocaml 编译器 $./make`

ok. 一切顺利的话。可以在 mldonkey-2.8.1 目录下 ./mlnet
运行支持中文文件名的 mldonkey 了。

tips：可以通过 ./mlnet >/dev/null 2>&1 & 来把 mldonkey 放到后台运行。

（注：此文作者为 lvs，由其本人投递到
linuxtoy，[原始链接](http://lvscar.blogspot.com/2006/10/mldonkey28-bug.html)，非常感谢）
