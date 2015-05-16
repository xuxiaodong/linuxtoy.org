Title: 小技巧: 实用的一行 Linux 命令
Date: 2007-11-16 17:11
Author: toy
Category: Tips
Slug: useful-linux-commands-2

下面这些 Linux
命令都只有一行，虽然简短，但却非常实用。如若善于使用它们，定会给你的
Linux
使用过程带来便利。其中包括创建存档文件、递归查找文件内的字符串、搜索并替换文件里的内容、查看磁盘及目录占用情况等。

1.  创建存档文件

    `tar -czpf folder_name.tar.gz folder_name`

    该命令将 folder\_name 创建为 folder\_name.tar.gz 存档文件。

2.  递归查找文件内的字符串

    `find ./ -name ‘*.html’ -exec grep “breadcrumbs.inc.php” ‘{}’ \; -print`

    这条命令将查找所有包含 breadcrumbs.inc.php 的 HTML 文件。

3.  搜索并替换文件里的内容

    `sed -i ’s/b/strong/g’ index.html`

    此命令搜索 index.html 文件中的 b 并将其替换为 strong。

4.  查看目录的磁盘占用情况
    `du -h --max-depth=1 | sort -n -r`

[via [Micah
Carrick](http://www.micahcarrick.com/10-30-2007/handy-linux-commands.html)]
