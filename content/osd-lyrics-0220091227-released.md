Title: OSD-Lyrics 0.2.20091227 发布
Date: 2010-01-02 18:09
Author: toy
Category: Apps
Tags: OSD-Lyrics
Slug: osd-lyrics-0220091227-released

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

虽然发布了已经有几天了，但还是要告知一下大家吧。

这个版本着重修复了前一版本的 bug，并且增加了 MPD  
的支持。对 MPD 的粉丝来说，是一个不错的选择。

另外，[OSD-Lyrics](http://code.google.com/p/osd-lyrics/) 默认关闭了对
Amarok 1.4  
的支持，但是可以在编译的时候添加参数  
--enable-amarok1，以获得相应的支持。

使用 Fedora 12 的朋友，可以在这里获取 rpm 包 (默认已经开启  
Amarok 1.4 的支持，理论上此包还可以用在旧版本 Fedora )：
href="http://dl.dropbox.com/u/1352061/yum/12/x86\_64/osd-lyrics-0.2.20091227-1.fc12.x86\_64.rpm">64
位，
href="http://dl.dropbox.com/u/1352061/yum/12/i386/osd-lyrics-0.2.20091227-1.fc12.i686.rpm">32
位

或者使用下列命令获取 OSD-Lyrics 的 Fedora rpm 包：

su -c 'wget http://dl.dropbox.com/u/1352061/liangsuilong.repo -P
/etc/yum.repos.d/'

然后刷写缓存后即可透过用 yum 安装 OSD-Lyrics

yum makecache && yum install osd-lyrics

[OSD-Lyrics  

源代码下载地址](http://osd-lyrics.googlecode.com/files/osdlyrics-0.2.20091227.tar.gz)

{ Thanks liangsuilong. }
