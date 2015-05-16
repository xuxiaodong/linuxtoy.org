Title: 打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (3)
Date: 2007-12-19 22:36
Author: toy
Category: Featured
Slug: the-perfect-linux-desktop-arch-linux-2007-08-2-3

通过本文[第一部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-1.html)和[第二部分](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-2.html)，我们所建立的
[Arch Linux](http://archlinux.org/)
桌面已初具雏形，不过还缺少那些熟悉的应用程序。在本部分中，我们将解决这方面的问题，让
Arch Linux 逐渐丰富起来。

### 安装 ALSA

完美的 Linux 桌面怎么少得了美妙动听的音乐呢。现在，让我们为 Arch Linux
安装 ALSA 吧。实际上，ALSA 已被包含到 2.6 版的内核中。因此，我们只需安装
ALSA 的相关工具即可。你可以在终端中输入下列指令：

`pacman -S alsa-utils`

接着，我们将当前用户添加到 audio 用户组，以便使用声卡设备 (注意把
xiaodong 换成你的用户名)：

`gpasswd -a xiaodong audio`

同时，将 alsa 添加到 /etc/rc.conf 配置文件的 DAEMONS 中：

`DAEMONS=(syslog-ng network netfs crond gdm alsa)`

值得注意的是，ALSA 默认是静音状态，你需要先打开音量。另外，也可点击”系统
→ 首选项 → 音效“进行测试。

### 安装常用软件

**网络浏览**

我一直使用 Firefox 网络浏览器，所以执行以下指令来安装它：

`pacman -S firefox firefox-i18n`

该命令中的前者为 Firefox
主程序，后者为语言包。在安装完成后，可通过”应用程序 → Internet →
Firefox“启动。

你也可以选择其他的网络浏览器，比如 Opera：

`pacman -S opera`

**图像编辑**

图像编辑软件首选 GIMP，要安装它可以执行命令：

`pacman -S gimp`

你可以通过”应用程序 → 图像 → GIMP“来运行 GIMP。

另外，矢量图形编辑软件可以使用 Inkscape：

`pacman -S inkscape`

命令行的可以装上 ImageMagick：

`pacman -S imagemagick`

用来捕获图像的 Scrot：

`pacman -S scrot`

**办公处理**

我们安装 OpenOffice.org 这套办公处理软件：

`pacman -S openoffice-base openoffice-zh_cn`

为了让 OpenOffice.org 运行于 GTK 2 模式，我们向 ~/.bashrc
添加如下内容：

`export OOO_FORCE_DESKTOP=gnome`

OpenOffice.org 安装完成后，可在 ”应用程序 →
办公“中找到相应的启动菜单条目。

**即时通讯**

要与朋友即时聊天，我们可以选用 Pidgin，它支持 Gtalk、MSN、QQ
等多种协议：

`pacman -S pidgin`

同时，Skype 也不可错过：

`pacman -S skype`

**音影播放**

音乐播放软件我选择 Quod Libet，你可以凭自己的喜好来安装：

`pacman -S quodlibet`

其他的音乐播放器包括 MPD、Audacious、Exaile、Amarok 等。

如果是看电影的话，MPlayer 不错，同时也加上浏览器插件和常用解码器：

`pacman -S mplayer mplayer-plugin codecs gstreamer0.10-bad gstreamer0.10-ugly gstreamer0.10-ffmpeg gstreamer0.10-mad gstreamer0.10-mpeg2dec`

如果需要 MPlayer 的前端，那么可以安装 SMPlayer：

`pacman -S smplayer`

当然，另一个选择 VLC 也挺好：

`pacman -S vlc`

**下载工具**

命令行下载工具，我们有 wget。此外，aria2
也不错，它支持断点续传和多线程下载：

`pacman -S aria2`

BitTorrent 下载工具，我们选用 Deluge：

`pacman -S deluge`

其他的包括 Azureus、rTorrent 等。

另外，我们把 aMule 也安装上：

`pacman -S amule`

为了能够让 aMule 直接从 Firefox 浏览器中处理 ed2k 链接，我们在 Firefox
的 about:config 中新建字符串
network.protocol-handler.app.ed2k，并将其设为 /usr/bin/ed2k。

**新闻阅读**

RSS 离线阅读软件，我们安装 Liferea：

`pacman -S liferea`

**邮件收发**

电子邮件客户端，可以选择 Thunderbird：

`pacman -S thunderbird thunderbird-i18n`

**图像查看**

我们安装一个轻快的图像查看软件 GQview：

`pacman -S gqview`

或者 GNOME 默认的 Eog：

`pacman -S eog`

**文本编辑**

如果要求简单的话，可以选用 Gedit：

`pacman -S gedit`

我们选择安装 Vim，要图形界面的话，可以加上 Gvim：

`pacman -S vim`

Emacs 迷们可以执行：

`pacman -S emacs`

Emacs CVS 版本可在 community 中找到。

**FTP 软件**

我选择命令行的 Lftp：

`pacman -S lftp`

图形化的有 gFTP、FileZilla 等。

**光盘刻录**

我们选择 K3b，你可以通过以下指令安装：

`pacman -S k3b`

为了让当前用户能够使用光盘刻录设备，需要将其添加到 optical 用户组中
(请将 xiaodong 替换成你的用户名)：

`gpasswd -a xiaodong optical`

**文档查看**

查看 PDF 文档，可以安装 Evince：

`pacman -S evince`

CHM 文档，可以选用：

`kchmviewer`

**其他工具**

计算器：

`pacman -S gcalctool`

压缩/解压 rar、zip 等格式：

`pacman -S unrar unzip`

另外，图形化的可以用 File-roller：

`pacman -S file-roller`

词典翻译，我们安装 StarDict：

`pacman -S stardict`

同时，词典文件需从 [StarDict
官方网站](http://stardict.sourceforge.net/Dictionaries_zh_CN.php)下载，并释放到
/usr/share/stardict/dic/ 目录。

Java 支持：

`pacman -S jre`

Flash 插件：

`pacman -S flashplugin`

**安装主题**

GDM 可以安装 [Arch Boomerang
Underlight](http://i.linuxtoy.org/files/archlinux/arch-boomerang-underlight-gdm.tar.gz)
这套清爽的主题。下载后，执行：  

` tar zxvf arch-boomerang-underlight-gdm.tar.gz mv arch-underlight-* /usr/share/gdm/themes/`

然后在”系统 → 系统管理 →
登录窗口“中将样式更改为主题模式，并选择已安装的主题即可。

[![Arch Linux
登录画面](http://i.linuxtoy.org/i/archlinux/archlinux94-thumb.png)](http://i.linuxtoy.org/i/archlinux/archlinux94.png)

鼠标指针主题可以装上
[DMZ](http://linuxtoy.org/archives/dmz-cursor-themes.html)：

`pacman -S xcursor-vanilla-dmz xcursor-vanilla-dmz-aa`

安装完成后，可到“系统 → 首选项 → 外观 → 主题 → 自定义 → 指针”中选取。

一些不错的 GTK 主题引擎 Murrine、Rezlooks 等：

`pacman -S gtk-engine-murrine gtk-rezlooks-engine`

[![Arch Linux
桌面](http://i.linuxtoy.org/i/archlinux/archlinux95-thumb.png)](http://i.linuxtoy.org/i/archlinux/archlinux95.png)

(待续)

[声明：本系列文章尚需完善，谢绝转载]
