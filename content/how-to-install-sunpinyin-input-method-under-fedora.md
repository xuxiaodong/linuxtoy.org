Title: Fedora 下安装 SunPinYin 输入法
Date: 2009-11-10 03:58
Author: lovenemesis
Category: Desktop Stuff
Tags: ibus, sunpinyin
Slug: how-to-install-sunpinyin-input-method-under-fedora

SunPinYin 是 Sun 亚洲研究中心为 OpenSolaris
开发的一套基于统计学语言模型的拼音输入法，目前已经移植到 iBus
输入法框架下，可以在 Fedora 系统下使用。

**1. 安装必要编译工具**

在终端下使用如下命令安装：

`su -c 'yum install make gcc-c++ ibus-devel python-devel sqlite-devel'`

**2. 下载源代码包**

前往[项目主页](http://code.google.com/p/ibus-sunpinyin/downloads/list)下载最新的源代码包，建议选择包含
LM 数据文件的，通常是体积较大的那个。本文撰写时最新的为 2.0 RC2。

**3.编译并安装**

在保存有刚才下载文件的目录依次执行以下命令：

`tar xvf ibus-sunpinyin*.tar.gz`

`cd sunpinyin-2.0`

`./configure --enable-ibus --disable-documents --prefix=/usr --libexecdir=/usr/lib/ibus-sunpinyin`

`make`

如果编译无误的话，那么执行安装：

`su -c 'make install'`

**4.启用 SunPinYin**

右键点击 iBus 的图标，选择“重新启动”。

之后在右键菜单“首选项”-“输入法”的汉语部分就可以看到 SunPinYin
了。此时可以选择向上移动调整成默认汉语输入法。

**5. 配置**

首次运行时，点击输入法最右侧的齿轮型图标可进入配置界面，在这里可以个人习惯调整一些配置。

比较重要的是在“快捷键”标签页下的“翻页键”设置。

[ibus-sunpinyin 项目主页](http://code.google.com/p/ibus-sunpinyin/)

[Sun Input Method
项目主页](http://hub.opensolaris.org/bin/view/Project+input-method/#)

[Sun PinYin
开发者论坛](http://groups.google.com/group/sunpinyin-developers)

[Fedora 12 i686 RPM 包 感谢liangsuilong
兄](http://dl.dropbox.com/u/1352061/ibus-sunpinyin-2.0-0.3.rc2.fc12.i686.rpm)

[Fedora 12 x86\_64 RPM 包 感谢liangsuilong
兄](http://dl.dropbox.com/u/1352061/ibus-sunpinyin-2.0-0.3.rc2.fc12.x86_64.rpm)
