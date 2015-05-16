Title: DEMAE：可以解决 MP3 标签乱码的播放器
Date: 2008-12-18 18:40
Author: toy
Category: Apps
Tags: Demae
Slug: demae

[撰文/[yang](http://www.shouguang.org/yang/)]

Linux 下 MP3 标签乱码很烦人。众多的 MP3 播放器，不管是重量级的 Rhythmbox
还是轻量级的 Quod Libet 都存在乱码问题。具体详细的解释，可以看 nicky
的[这篇文章](http://www.osxcn.com/ubuntu/mp3-tag-encoding.html)。

虽然可以使用 [id3iconv](http://www.cs.berkeley.edu/~zf/id3iconv/) 或者
[Mutagen](http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen)
来重新转换 MP3 的标签编码，但是有点罗嗦：我每次下载单个
MP3，就要重新用命令来转换编码，太麻烦了。

昨天我在寻找基于 mpg123（mpg321）的前端播放器，找到了
[DEMAE](http://sourceforge.net/projects/demae) 这个小玩意，可以解决掉
MP3 标签乱码。但是界面太简单，功能太弱了，所以很勉强能够在平常中使用。

我尝试使用 Sonata、Audacious、Quod Libet 来和它比较，确实能够正确的处理
MP3 标签编码（支持 ID3v1/v2、APEv2），不过要在配置选项里面加入 GBK
编码。

截图如下（googleMusic 下载的两首中文歌）：

[![mp3id1](http://i.linuxtoy.org/images/2008/12/mp3id1-thumb.png)](http://i.linuxtoy.org/images/2008/12/mp3id1.png)

配置选项中需要添加 GBK 编码：

[![mp3id2](http://i.linuxtoy.org/images/2008/12/mp3id2-thumb.png)](http://i.linuxtoy.org/images/2008/12/mp3id2.png)

关于安装： 把源码包中的 ext/i686-linux/gtk\_treemodel\_xtra.so
拷贝到源码包根目录，然后执行 demae，出现依赖错误，可参考 README。

[[原文链接](http://www.shouguang.org/yang/?p=376)]
