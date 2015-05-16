Title: pyRenamer－批量重命名工具
Date: 2007-07-24 10:51
Author: toy
Category: Apps, Tools
Slug: pyrenamer

[pyRenamer](http://www.infinicode.org/code/pyrenamer/)
是一个小巧实用的批量重命名工具。使用它你可以同时对多个文件进行重命名操作，让人感觉非常快捷。pyRenamer
使用 PyGTK 所写，可用于 GNOME、Xfce、KDE 等多个桌面环境。

[![pyRenamer](http://i.linuxtoy.org/i/2007/07/pyrenamer_s.jpg)](http://i.linuxtoy.org/i/2007/07/pyrenamer.jpg)  
*使用 pyRenamer 进行批量文件重命名操作*

**pyRenamer 功能简介**

pyRenamer 当前提供了以下几种方式用于文件的批量重命名操作：

1.  匹配模式
2.  通过置换
3.  插入或者删除
4.  根据音乐文件的 ID3 标签
5.  根据图像文件的 EXIF 数据
6.  手动更名

**安装 pyRenamer**

通用 Linux 用户可以执行下列指令安装 pyRenamer：

` $ wget http://www.infinicode.org/code/pyrenamer/pyrenamer-0.2.tar.gz $ tar xzvf pyrenamer-0.2.tar.gz $ cd pyrenamer-0.2 $ ./configure --prefix /usr $ sudo make install`

对于 Debian/Ubuntu 使用者，可以通过下载 deb 包进行安装：

` $ wget http://www.infinicode.org/code/pyrenamer/pyrenamer_0.2-1_all.deb $ sudo dpkg -i pyrenamer_0.2-1_all.deb`

**启动并使用 pyRenamer**

在终端中输入 pyrenamer，或者点击“应用程序 → 附件 →
pyRenamer”菜单命令，可以启动
pyRenamer。在使用时，先选择需要重命名的文件，然后选择适合的方式执行操作即可。
