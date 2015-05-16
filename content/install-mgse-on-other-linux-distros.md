Title: 在其他 Linux 发行版上安装 MGSE
Date: 2011-11-28 13:26
Author: lovenemesis
Category: Desktop Environment
Tags: gnomeshell, mgse
Slug: install-mgse-on-other-linux-distros

前段时间报道的 [Linux Mint GNOME Shell
Extensions](http://linuxtoy.org/archives/mint-gnome-shell-extensions.html)
随着近日代号 Lisa 的 Linux Mint 12
的正式发布十分变得抢眼。若是您不想重头安装 Linux Mint 12
的话，亦可使用已有的 PPA 仓库或源代码在现有发行版下安装。

**Ubuntu 11.10:**

`sudo add-apt-repository ppa:webupd8team/gnome3`

`sudo apt-get update`

`sudo apt-get install mgse-bottompanel mgse-menu mgse-windowlist`

如果还想模仿 Linux Mint 的绿色系主题的话，那么再：

`sudo add-apt-repository ppa:webupd8team/themes`

`sudo apt-get update`

`sudo apt-get install zukitwo-theme-all`

**Arch:**

[AUR 信息](http://aur.archlinux.org/packages.php?ID=53742)

得益于 GIR 技术，其他发行版通过 JavaScript **源代码安装 GNOME Shell
扩展亦十分简单：**

1.  从 [MGSE Github](https://github.com/linuxmint/MGSE) 获取源代码。
2.  执行其中的 `test` 安装脚本。

因为部分 MGSE 扩展是从原先的 GNOME Shell 扩展 fork
出来的，所以若是一次性全部安装的话可能会存在兼容性问题，**建议选择切实需要的扩展去安装**。

[Mint 风格主题源代码 Github
下载](https://github.com/linuxmint/mint-z-theme)

*消息来源：*[WebUpd8](http://www.webupd8.org/2011/11/try-new-mint-gnome-shell-extensions.html)
