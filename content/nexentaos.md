Title: Nexenta OS——太阳系中的UBUNTU
Date: 2008-08-12 16:39
Author: Kardinal
Category: Distros
Slug: nexentaos

子曾经曰过： FreeBSD典雅 Solaris豪华 Linux混乱

简单的说，在UNIX系统中，Linux相当于TOYOTA，FreeBSD相当于Benz，Solaris相当于
Ferrari

NexentaOS是一个在OpenSolaris内核之上运行的UBUNTU系统

为什么需要这样一个系统呢？经常看到许多朋友对ZFS艳羡不已，这下我们可以在ZFS上跑UBUNTU了

下面是下载地址

<http://www.nexenta.org/releases/nexenta-core-platform_2.0-b85-alpha1_x86.iso.zip>

这个是稳定版，应该比较实用，只是有点老旧(好处是有很多预编译软件包可以用）

<http://www.nexenta.org/releases/nexenta-core-platform_1.0.1-b85_x86.iso.zip>

或者到这个页面中寻找速度较快的镜像

<http://www.nexenta.org/os/DownloadMirrors>

下面是最新的Ubuntu Hardy版本的介绍

安装界面

![安装界面](http://i.linuxtoy.org/i/2008/08/1.jpg)

选择键盘布局

![选择键盘布局](http://i.linuxtoy.org/i/2008/08/2.jpg)

选择时区

![选择时区](http://i.linuxtoy.org/i/2008/08/3.jpg)

选择分区

![选择分区](http://i.linuxtoy.org/i/2008/08/part.jpg)

管理员密码

![管理员密码](http://i.linuxtoy.org/i/2008/08/pass.jpg)

![管理员密码](http://i.linuxtoy.org/i/2008/08/pass2.jpg)

配置网卡

![配置网卡](http://i.linuxtoy.org/i/2008/08/net.jpg)

开始安装

![开始安装](http://i.linuxtoy.org/i/2008/08/install.jpg)

启动界面

![启动界面](http://i.linuxtoy.org/i/2008/08/start.jpg)

登录

![登录](http://i.linuxtoy.org/i/2008/08/login.jpg)

Solaris中的 /etc/vfstab 相当于Linux中的/etc/fstab

![fstab](http://i.linuxtoy.org/i/2008/08/fstab.jpg)

根目录使用的是ZFS文件系统

在/etc/apt/sources.lst文件中加入源代码的源

![源](http://i.linuxtoy.org/i/2008/08/src.jpg)

同步源

![同楦??](http://i.linuxtoy.org/i/2008/08/sync.jpg)

apt-get update 过程中，可能会遇到pgp error的错误，像这样

W: GPG error: <span style="#0000ff;"><http://xxxxxx></span>
unstable Release: 由于没有公钥，下列签名无法进行验证： NO\_PUBKEY 40976EAF<span
style="#0080ff;">437D05B5</span>

在wwwkeys.eu.pgp.net 上获取编号为<span
style="#0080ff;">437D05B5 </span> 的KEY（NO\_PUBKEY后面那串数字的后8位）

#gpg --keyserver  wwwkeys.eu.pgp.net --recv-keys <span
style="#0080ff;">437D05B5</span>

把KEY添加到APT系统里

#gpg --armor --export <span
style="#0080ff;">437D05B5</span> | apt-key add -

Nexenta的软件安装基本靠编译，所以要安装一个开发包

# apt-get install devscripts （已安装）

假设package-name是你要编译的软件包名、  
# apt-get build-dep package-name  
# apt-get source package-name  
# cd package-name-(version)

# dch -i #修改一下关于此软件的说明  
# dpkg-buildpackage -sa

# dpkg-deb -c ../*.deb #确保包里面没有遗漏的东西  
# dpkg -i ../*.deb #安装此包  
# apt-get -f install
