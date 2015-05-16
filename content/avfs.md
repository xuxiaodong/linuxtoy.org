Title: 使用 AVFS 解决 Linux 下压缩包直读问题
Date: 2008-05-01 11:05
Author: toy
Category: Tutorials
Tags: AVFS, How-tos
Slug: avfs

Linux 下面的压缩包直读相比 Windows 一直是个不大不小的问题。比如 Windows
下面 Foobar 和 KMplayer 都能直读压缩包内的音频视频，ACDSee 和 Hamana
Comic Viewer
都能直读压缩包内的图片。在电骡里面下载的资源多是打包的压缩文件，既想下载后共享资源，又不想解压缩出来一份占空间，这时候压缩包直读就很有用。但是试过
Linux 下面的 Qcomic 等等能直读的看图软件，不是对 rar
支持极不稳定，就是预读太慢，还没有 Wine+Hamana
快......支持视频音频直读的播放器恐怕只有
MPlayer。可是还看不到内部。所有歌曲连成一个播.....所以一直在用Wine+Foobar。本人一直在想，Windows
下面的 WinMount 的宣传是像 Linux mount 一样方便的 mount 压缩包，Linux
下面怎能没有相应的功能呢？可是也是自己笨，直到今天才 Google
到这个东东──[AVFS](http://avf.sourceforge.net/)。

AVFS 现在支持 floppies、tar 及 gzip 文件、zip、bzip2、ar 及 rar
文件、ftp sessions、http、webdav、rsh/rcp、ssh/scp。通过
[ExtFS](http://www.boomerangsworld.de/cms/avfs/extfs?lang=en)
还可以扩展支持 arc、7zip、cab 等压缩格式。

使用方案有好几个，不过 Gentoo portage 中似乎推荐 FUSE 方案。安装需要
FUSE，安装完 AVFS 之后，在自己的主目录下面建立文件夹
.avfs。注意有个"."。然后运行 mountavfs，这个不需要 root 权限。然后再打开
.avfs
文件夹，会看到整个根目录的一个镜像目录结构。在这里面的压缩包都可以像文件夹一样打开，但是不是直接以名字访问，而是要加上
#，例如 /home/yourname/a.rar 访问时候应该如此，要进入 a.rar "目录"：

`cd /home/yourname/.avfs/home/yourname/a.rar#/`

文件管理器访问时候或者是文件选择对话框中也需要自己在路径上加
#，而不是直接双击压缩包就可以....其他程序访问时候也是如此。除去打开压缩包目录时候的延迟外，与访问普通目录没有区别。而且速度很快。用
MPlayer+AVFS 完全感受不到与 Foobar 打开压缩包直读延时的差别。

**注意事项**：最好把带有预览功能的东东关了。PCMan File Manager
默认预览小于 1MB
的图片，所以打开一个漫画包，硬盘灯狂闪。如果关闭，则没有多余的读取动作。另外就是好像编码支持仍然是个问题。（以下属于猜测）一些非
utf-8
文件名编码的文件压缩成的压缩包打开后文件名是乱码。文件管理器中打开没有问题，可是
bash 下面怎么访问呢？

相似的项目还有
podfuk：<http://atrey.karlin.mff.cuni.cz/~machek/podfuk/podfuk.html>

[撰文/comicfans44]
