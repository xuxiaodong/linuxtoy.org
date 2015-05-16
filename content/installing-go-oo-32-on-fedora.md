Title: 在 Fedora 安装 Go-Oo 3.2
Date: 2010-03-21 18:05
Author: toy
Category: Tips
Tags: Fedora, Go-oo
Slug: installing-go-oo-32-on-fedora

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

OpenOffice.org 是 Linux 平台上广泛使用的办公套件，各大 Linux  
发行版的软件库都有 OpenOffice.org，而且不少发行版已经把 OpenOffice.org  
列为标准组件。虽说都是同一套源代码，但是各个发行版对 OpenOffice.org  
都略有区别。例如 Debian、Ubuntu、openSUSE 等发行版都集成了  
[Go-Oo](http://linuxtoy.org/archives/go-oo.html) 的补丁，而  
Fedora 则是完全利用 OpenOffice.org 的初始源代码重编译，仅仅加入一些修复
bug  
的补丁，基本不会对性能进行优化和改进功能。

[![Go-Oo](http://i.linuxtoy.org/images/2010/03/gooo-3.2-thumb.jpeg)](http://i.linuxtoy.org/images/2010/03/gooo-3.2.jpeg)

以下操作都是在终端里的 root 用户完成。

安装 Go-Oo 首先要卸载原来的 OpenOffice.org

yum remove openoffice*

添加 Go-Oo 的 yum
源，到[这里](http://go-oo.mirrorbrain.org/stable/linux-i586/GoOo-release-0.0.3-0.noarch.rpm)下载一个
rpm 包，然后安装。如果是 x86\\\_64 的用户，还需要修改一下 repo 文件，把
/etc/yum.repos.d/GoOo.repo 里 baseurl 的链接修改为
http://go-oo.mirrorbrain.org/stable/linux-x86\\\_64/  
。

紧接着安装 openoffice.org-ure 1.6.0

yum install openoffice.org-ure-1.6.0

随后需要添加一个 exclude 到 yum.conf，因为 Fedora 自带的
openoffice.org-ure 的版本号跟随 OpenOffice.org 的版本号 3.2.0，比 1.6.0
高很多，但是安装前前者无法让 Go-Oo 运行，所以需要排除这个软件包。

echo “exclude=openoffice.org-ure” >> /etc/yum.conf

然后就是正式安装 Go-Oo：

yum install openoffice.org3-zh-CN.x86\_64 openoffice.org3.2-redhat-menus
ooobasis3.2-{writer,calc,impress,math,draw,base}

{} 里面的都是 OpenOffice.org
的组件，用户可以根据需要来安装。稍等片刻，安装就会完成了。

使用 Go-Oo
替换，速度上明显会感觉到提升。特别是使用了微软模板的演示文档，速度和兼容性有了质的飞跃。所以我还是渴望
Fedora 能够整合 Go-Oo 的补丁。Fedora 原版和 Go-Oo 似乎都没有解决到与
GNOME 的字体渲染一致的问题，虽然我已经安装了 OpenOffice.org 的 GNOME
界面整合包，还是请牛人帮忙解决。

{ Thanks liangsuilong. }
