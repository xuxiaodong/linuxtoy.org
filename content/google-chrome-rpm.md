Title: Google 提供 Chrome 的 RPM 源
Date: 2009-11-10 09:39
Author: toy
Category: Tips
Tags: Fedora, Google Chrome, RPM
Slug: google-chrome-rpm

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

看到黑日白月兄的消息，说 Google 把 Chrome 的 RPM 包推送到自家的 RPM  
源，只要开启了 Google 的 Linux  
软件源，就可以透过发行版的软件包管理工具直接更新了。

方法如下：

首先在 /etc/yum.repos.d 里建立一个名为 google.repo
文件，然后复制以下内容到该文件，保存即可。


    [google]
    name=Google - i386
    baseurl=http://dl.google.com/linux/rpm/stable/i386
    enabled=1
    gpgcheck=1
    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

若是使用 64 位系统，则复制以下内容并保存。


    [google64]
    name=Google - x86_64
    baseurl=http://dl.google.com/linux/rpm/stable/x86_64
    enabled=1
    gpgcheck=1
    gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

然后在软件包管理器安装 google-chrome-unstable 即可。Fedora
下可以在终端里输入命令：

yum install google-chrome-unstable

有点奇怪的是在 Fedora 安装 x86\\\_64 的 google-chrome-unstable
的时候，Yum 会安装大量的 i586/i686
的软件包，但实际上安装的软件包，安装后产生的软链接是连接到 /usr/lib64 和
/lib64 目录里面的文件里，看来有点莫名其妙。另外安装完成以后会在
/etc/yum.repos.d 生成 google-chrome.repo 文件，内容上跟 google.repo
的一样，不过也无伤大雅。

[![](http://dl.dropbox.com/u/1352061/photo/google-chrome-rpm.jpeg)](http://dl.dropbox.com/u/1352061/photo/google-chrome-rpm.jpeg)

使用效果跟 Chromium 差异不大，不过这个 RPM 包感觉是 DEB
包的解压后重打包，使用上不会有什么问题。如果有需要，可以安装使用。

{ [Source](http://www.liangsuilong.info/?p=484). Thanks liangsuilong. }
