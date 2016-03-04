Title: File Roller/Unzip 解压中文 Zip 文件名乱码
Author: lovenemesis
Date: 2016-03-04
Category: AskLinuxToy
Tags: fileroller, gnome, zip, unzip, i18n
Slug: wrong-handling-of-chinese-coded-filename-in-fileroller-unzip
Summary: 如果使用 Linux 的您某日收到一个在 Win 平台压缩成的 Zip 文件，恭喜您，进入了一个长达 11 年仍未解决的大坑。

其实这个问题自从给家父换用 Fedora 后便遇到了，似乎总是有那么一两个人喜欢使用 zip 格式压缩下无论是多么小的文件。两三个 GNOME 版本更新却仍然如此，实在奇怪。于是这次坐下来查了查，才发觉这是一个大坑。

接下来的内容可以说是在下根据网上查找一些资料的验证/解决方案。没什么技术含量，随便哪个思维正常的 SA 都会做。记录下来，只是因为**搜索引擎给出中文结果都已经不生效了**！

**** 问题重现

很简单，在一台 Win 系统的设备上创建一个以**中文命名**的空白文件，然后用 7-zip 或者其他任意压缩工具压缩城 zip 格式。

将生成的文件复制到 Linux 系统下，尝试打开。

至少在 Fedora 23 上，无论使用 GNOME 桌面的 `File-Roller` 或者终端的 `unzip` 结果都是乱码的。

**** 错误尝试

放狐搜索出来的结果前几个：

1. 为 `unzip` 使用 `-O` 选项指定编码

这个当年的隐藏参数在 6.0 版本中已经完全没有了

2. 解压后使用 `convmv` 转换编码

不少文章提出使用这个方式 `convmv -f gbk -t utf8 -r MY_DIR`

实际上 convmv 会汇报文件名已经是 UTF-8 的了，不会做任何操作。

这样的结果不奇怪，毕竟 Win 也早经过了 XP 时代，中文 Linux 也默认 UTF-8 很久了。

3. 使用 `p7zip` 解压 zip 文件

无论是使用 `7za` 还是 `7z`，乱码依旧

放鸭搜索出来的结果倒是很有趣：

1. GNOME Bugzilla

根据记录，[这个 Bug](https://bugzilla.gnome.org/show_bug.cgi?id=306403) 最早汇报于 2005 年的 file-roller 2.14 版本。 40 个长长的评论中提到了在终端使用 `unar` 临时解决方案和为何 `unar` 现在没被当作处理 zip 文件的首选方案。

嗯，当然 `unar` 可以处理这个问题，好歹是 FSF 当年认定的 rar v3 解压的完美开源解决方案。

其间还提到了 unzip 6.10 版本和 libnatspec 库已经解决了这个问题。很遗憾，经过在下快速的尝试，单纯使用 unzip 官方提供的 6.10 Beta 源代码配合 libnatspec 并不能解决该问题。况且更重要的是 unzip 6.10 的正式发布遥遥无期。

2. Mate Desktop Issue Tracker

很显然这个问题延伸到了 Mate，在[其 Issue Tracker](https://github.com/mate-desktop/engrampa/issues/5) 上有开发者指出了这个其实是 zip 创建软件的问题，若是在 UTF-8 的 Linux 系统上用 p7zip 创建 zip 则不会有类似问题。在一番激烈的讨论之后，什么方案也没有，没有，没有……

**** 结论：坑仍在

目前，对于所有不幸收到包含非 ASC-II 编码文件名的 zip 文档的 Linux 用户来讲，在终端使用 `unar` 恐怕是最快最便捷的临时解决方案了。其他的中文搜索结果给出的方案，都不可行。

