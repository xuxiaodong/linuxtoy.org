Title: 怎样安装 KDE 4.0 [含 Ubuntu, Arch Linux, openSUSE, MagicLinux, Gentoo]
Date: 2008-01-14 08:30
Author: toy
Category: Featured
Slug: how-to-install-kde-40

在 [KDE 4.0
发布](http://linuxtoy.org/archives/kde-400-released.html)之后，可能有的朋友在使用包含它的
Live CD 进行体验。如果你打算让 KDE 4.0 在自己的 Linux
系统中安家，那么摆在你面前的首要问题就是怎样安装 KDE
4.0。我们搜集了一些安装 KDE 4.0 的资料，希望对你有所帮助。

[![KDE 4.0
桌面](http://i.linuxtoy.org/i/2008/01/my-kde4-desktop-thumb.png)](http://i.linuxtoy.org/i/2008/01/my-kde4-desktop.png)

**在 U(K)buntu 7.10 Gutsy 中安装 KDE 4.0**

如果你是 Ubuntu 或 Kubuntu Gutsy 用户，那么可以按如下步骤来安装 KDE
4.0：

1、编辑 /etc/apt/sources.list 文件：

`sudo vim /etc/apt/sources.list`

然后，添加下列内容：

`deb http://ppa.launchpad.net/kubuntu-members-kde4/ubuntu gutsy main`

2、安装 KDE 4.0 包：  
` sudo aptitude update sudo aptitude install kde4-core`

注意：如果你有安装过 KDE 4.0
之前的版本，需要先使用以下命令删除相关包，以免冲突：

`sudo aptitude remove kdelibs5 kde4base-data kde4libs-data`

3、从登录管理器中选择 KDE 4 可以进入 KDE 4 桌面环境。

**在 Arch Linux 中安装 KDE 4.0**

对 Arch Linux 用户而言，可以安装 KDEmod 4。目前，KDEmod 4 位于
kdemod-testing 仓库。要安装 KDEmod 4，可执行下列步骤：

1、启用 Arch Linux 的 testing 仓库，并添加 kdemod-testing
仓库地址。你需要编辑 /etc/pacman.conf 文件：

`vim /etc/pacman.conf`

然后，删掉以下两行前面的注释符：  
` [testing] Include = /etc/pacman.d/testing`

并添加 kdemod-testing 仓库地址：  
` [kdemod-testing] Server = http://kdemod.ath.cx/repo/testing/i686`

由于在我这里上面的地址被阻尼了，所以我换用：  

` [kdemod-testing] Server = http://kdemod.podzone.net/repo/testing/i686/`

接着，同步一下：

`pacman -Sy`

2、(可选) 如果你已安装 KDEmod 3.x，则执行：  

` pacman -Rd qt-enhanced pacman -Rd kdemod-gtk-qt-engine pacman -S kdemod-testing/qt-enhanced pacman -S kdemod-testing/kdemod-gtk-qt-engine`

3、执行下列命令更新系统：

`pacman -Su`

4、删除 qt：

`pacman -Rd qt`

5、安装 KDE 4.0：

基本的 KDE 4 桌面：

`pacman -S kdemod4`

完整的 KDE 4 桌面：

`pacman -S kdemod4-complete`

安装简体中文语言：

`pacman -S kdemod4-kde-l10n-zh_cn`

注意：事实上，在我执行第四步后，再执行第五步时，出现了下列依赖问题：  

` resolving dependencies... looking for inter-conflicts... error: failed to prepare transaction (could not satisfy dependencies) :: strigi: requires qt>=4.3.2 :: soprano: requires qt>=4.3.2 :: telepathy-qt: requires qt>=4.3.2 :: tapioca-qt: requires qt>=4.3.2 :: qimageblitz: requires qt>=4.3.2 :: qca: requires qt>=4.3.2`

根据 KDEmod 论坛的提示，执行以下命令后解决：  

` pacman -S qt pacman -S strigi soprano telepathy-qt tapioca-qt qimageblitz qca pacman -Rd qt pacman -S qtmod`

感谢 fireflyoo 补充：更新 Pacman 后，请将 /etc/pacman.conf 里 [testing]
段的内容改为：  
` [testing] Include = /etc/pacman.d/mirrorlist`

**在 openSUSE 10.3 中安装 KDE 4.0**

openSUSE 10.3 的用户可以使用下面的一键安装按钮获得 KDE 4.0 桌面环境：

[![安装 KDE
4.0](http://i.linuxtoy.org/i/2008/01/Kde4-ymp.png)](http://download.opensuse.org/repositories/KDE:/KDE4/openSUSE_10.3/KDE4-DEFAULT.ymp)

或者，你也可以安装一个更[基本的 KDE 4
桌面](http://download.opensuse.org/repositories/KDE:/KDE4/openSUSE_10.3/KDE4-BASIS.ymp)。开发者还可以安装
[KDE 4
编译依赖](http://download.opensuse.org/repositories/KDE:/KDE4/openSUSE_10.3/KDE4-DEVEL.ymp)，以便从源代码编译
KDE 4.0。

**在 MagicLinux 中安装 KDE 4.0** [感谢 [nihui
朋友提供](http://www.linuxfans.org/bbs/thread-182132-1-1.html)]

1、添加 apt 源。root 权限：

`/etc/apt/sources.list.d/magic.list`

添加一行：

`rpm http://wiki.magiclinux.org/ftp/nihui/kde4 4.0.0 kde400`

2、请一定要删除以前 rc2/beta3 的源，否则可能造成冲突。然后在 root
状态下执行 (su)：  
` apt-get dist-upgrade apt-get install kde4-session qt4-*`

同样，也可以使用 smart 进行安装。

安装完成之后，无需修改任何配置文件，只需注销一下便能进入。

3、简体中文语言包安装：

`apt-get install kde4-l10-zh_CN`

4、其他安装：

kdegraphics (包含 okular/gwenview 等)：

`apt-get install kdegraphics4`

kdeedu (包含 kalzium/marble/ 等)：

`apt-get install kdeedu4`

nihui 注：kalgebra 程序在我这边启动时会造成重启
X，与显卡的性能有关。如果显卡不支持硬件 opengl 渲染的话 (比如我的 sis
显卡)，那么只要有 opengl/pixel buffer 的部分都会导致 X 崩溃，而单纯的
opengl 图像渲染是不会引起崩溃的。

kdegames (包含 ksudoku 等)：

`apt-get install kdegames4`

extragear-plasma  
kdemultimedia  
kdenetwork  
kdesdk

已经过测试，暂时没有加进 apt 中 (编译依赖不完整，比如 krdc 缺少 vnc
支持等等)：<http://wiki.magiclinux.org/ftp/nihui/kde4/4.0.0/tmp/>

**在 Gentoo 中安装 KDE 4.0** [感谢
[fcicq](http://linuxtoy.org/archives/how-to-install-kde-40.html#comment-71608)]

请参考：<http://www.gentoo.org/proj/en/desktop/kde/kde4.xml>

欢迎朋友们提供自己的 KDE 4.0 安装方法，以充实本文。

[via [Kubuntu](http://kubuntu.org/announcements/kde-4.0.php),
[KDEmod](http://www.kdemod.ath.cx/bbs/viewtopic.php?id=406),
[openSUSE](http://news.opensuse.org/2008/01/11/kde-40-released-with-opensuse-packages-and-live-cd/)]
