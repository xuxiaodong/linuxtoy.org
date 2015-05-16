Title: Audacious 1.1 DR1
Date: 2006-06-08 15:08
Author: toy
Category: Apps
Slug: audacious

相信大家都在 XMMS & XMMS 2 和 BMP & BMPx 之间徘徊。今天在装了 XMMS、XMMS
2、BMPx 后（都令我失望），Google 带我找到了一个基于 XMMS & BMP 的播放器
[Audacious](http://audacious-media-player.org)。

[![audacious](http://i.linuxtoy.org/i/audacious_s_jazzi.png)](http://i.linuxtoy.org/i/audacious_jazzi.png)

Audacious 是基于 Beep-media-player 和 XMMS 的播放器，因为
Beep-media-player 已经停止开发了，至少 Beep-media-player 在 Gentoo
里就因为 upstream 的原因被 mask 了。Audacious 和 Beep- media-player
很象，并且兼容它们的皮肤。而且它依赖的东西很少，就一个包。它的设置选项跟
Beep-media-player 基本一样，但是比 XMMS 的简单多了，只要设定了标题编码
UTF-8 码转换，也没有所谓的中文问题。

我在 Dapper 下编译制作了个 Audacious 1.1 的 32 位的 deb
包，安装步骤如下：

1.满足依赖关系

`sudo apt-get install libvorbis-dev libasound2-dev libjack0.100.0-dev libsamplerate0 libtagc0-dev`

2.下载安装我提供的 deb 包

`sudo dpkg -i audacious_dr1-1_i386.deb`

3.执行下列操作（注意要半角输入）

`sudo -s -H`

`echo '/usr/local/lib' >> /etc/ld.so.conf`

4.可以了，在终端中输入 audacious 试试

[下载 Audacious](/deb/audacious_dr1-1_i386.deb)

[撰文/[jazzi](mailto:jazzihong22@gmail.com)]
