Title: 在 Fedora 下安装 Android SDK 开发环境
Date: 2009-06-27 17:55
Author: lovenemesis
Category: Development
Tags: Android, Fedora
Slug: howto-set-sup-android-sdk-under-fedora

Android 是 Google 推出的基于 Linux 的开源智能手机平台，本文讲述如何在
Fedora 系统下架设 Android 开发环境。

全部流程以 Fedora 11 X86 版本为例。

*1. 下载 Android SDK*

首先，前往从以下网站获取 Android Linux 平台的 SDK 套件，目前只有 i386
架构的。

<http://developer.android.com/sdk/>

撰写本文时最新版本为 1.5 Release 2，下载完成会得到一个 zip
格式的压缩档案。

*2. 解压缩并配置相关环境变量*

将获得的 zip 解压到所喜好的位置即可，无须安装。

接下来需要将 SDK 目录中的 tools 添加到 PATH 路径中，方便调用。编辑
$HOME/.bash\_profile 文件，在 PATH 一行末尾添加 SDK 中 tools
文件路径即可，用冒号分割。

**推荐为其 Android SDK 目录创建一个不包括版本号的符号链接，这样日后 SDK
升级时就无须调整 PATH 路径了。**

*3. 安装 Eclipse 集成开发环境*

Android 推荐的 IDE 为 Eclipse，使用下面的命令安装它：

`.su -c 'yum install eclipse-jdt java-1.6.0-openjdk-devel'`

即可获得 Fedora Eclipse 3.4.2 版本。

*4.配置 Android Development Tools*

首先要添加 Eclipse 的官方升级仓库，满足 Android Development Tools
所需要的 eclipse-wdt 。

在 Eclipse -> Help -> Software Updates -> Available Software ->
Manage Sites 中勾选 Ganymede Update Site，点击 Close 返回 Available
Software。

在 Available Software 点击 Add sites，输入

`https://dl-ssl.google.com/android/eclipse/`

然后勾选新出现的 Android DDMS 和 Android Development Tools 即可。

此刻 Android SDK 配置完成，可以开始 Android 平台应用软件的开发啦！

**PS:** 网上目前的在 Fedora Eclipse 使用 Android
的配置皆有不足，故有此文。
