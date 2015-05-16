Title: Gentoo 实用脚本：e-file
Date: 2008-12-02 19:30
Author: toy
Category: Apps
Tags: Gentoo, Scripts
Slug: e-file

有时候，在 Gentoo
系统中我们需要查询某个文件属于哪个包。有鉴于此，[bones7456](http://li2z.cn/)
兄从
[apt-file](http://ubuntucookbook.com/recipes/apt-file-usage.html)（for
Debian）获得灵感编写了 e-file 这个实用的脚本。

![e-file](http://i.linuxtoy.org/images/2008/12/efile.png)

e-file 需要 curl，直接从 [portagefilelist.de](http://portagefilelist.de)
获取数据。比如：我要查询 pdfinfo 属于哪个包，执行 `e-file pdfinfo`
后，返回如上图所示的结果。

e-file 可通过 Gentoo China Overlay
获取，或从[这里下载](http://linuxfire.com.cn/~lily/e-file)。

[via [bones7456](http://li2z.cn/2008/12/01/e-file-20081201/)]
