Title: 打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (5)
Date: 2008-02-24 19:54
Author: toy
Category: Featured
Slug: the-perfect-linux-desktop-arch-linux-2007-08-2-5

抱歉，让期待《打造完美的 Linux 桌面 — Arch Linux 2007.08-2
([1](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-1.html)、[2](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-2.html)、[3](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-3.html)、[4](http://linuxtoy.org/archives/the-perfect-linux-desktop-arch-linux-2007-08-2-4.html))》系列文章的朋友等了这么久。通过前面四个部分的介绍，相信大家对于建立一个完整的
Arch Linux 桌面应该是没有问题了。接下来，我们就来说说 Arch Linux
本身的一些特色。

### Pacman ── Arch Linux 的包管理工具

**Pacman 简介**

[Pacman](http://www.archlinux.org/pacman/) 是 Arch Linux
默认的包管理工具，该工具由 Arch Linux 的创始人 Judd Vinet
所开发。截止写本文时为止，Pacman 的最新版本为 3.1.2，于 2008 年 2 月 20
日发布。使用 Pacman，你不仅可以更新 Arch Linux
的整个系统，而且能够对包进行管理，包括安装、删除、升级等。同时，Pacman
也允许你搜索包和查看有关包的信息。此外，与 Apt 类似，Pacman
能够自动处理包的依赖。

**配置 Pacman**

Pacman 的配置文件为 pacman.conf，该文件位于 /etc
目录，使用文本编辑器就可对其进行编辑。以下为该文件的部分内容：

    # /etc/pacman.conf
    [options]
    LogFile     = /var/log/pacman.log
    HoldPkg     = pacman glibc
    [core]
    Include = /etc/pacman.d/mirrorlist
    [extra]
    Include = /etc/pacman.d/mirrorlist
    [community]
    Include = /etc/pacman.d/mirrorlist
    [testing]
    Include = /etc/pacman.d/mirrorlist
    ......
    [archlinuxfr]
    Server = http://repo.archlinux.fr/i686

其中，行首具有 # 字符的为注释行。在 options 部分可以对 Pacman
进行设置。core、extra、community、testing 这些属于 Arch Linux
的官方仓库，在其下的 mirrorlist
文件中可以定义服务器的镜像地址。如果你需要使用第三方的仓库，那么可以按如下的方式加入到
pacman.conf 文件中：

    [仓库名称]：如上面的 [archlinuxfr]
    服务器地址：如 Server = http://repo.archlinux.fr/i686

**使用 Pacman**

Pacman
是一个命令行工具，这意味着当你执行下面的命令时，必须在终端或控制台中进行。

1、更新系统

在 Arch Linux 中，使用一条命令即可对整个系统进行更新：

`pacman -Syu`

如果你已经使用 `pacman -Sy`
将本地的包数据库与远程的仓库进行了同步，也可以只执行：

`pacman -Su`

2、安装包

-   `pacman -S 包名` 例如，执行 `pacman -S firefox` 将安装
    Firefox。你也可以同时安装多个包，只需以空格分隔包名即可。
-   `pacman -Sy 包名`
    与上面命令不同的是，该命令将在同步包数据库后再执行安装。
-   `pacman -Sv 包名` 在显示一些操作信息后执行安装。
-   `pacman -U` 安装本地包，其扩展名为 pkg.tar.gz。

3、删除包

-   `pacman -R 包名` 该命令将只删除包，不包含该包的依赖。
-   `pacman -Rs 包名` 在删除包的同时，也将删除其依赖。
-   `pacman -Rd 包名` 在删除包时不检查依赖。

4、搜索包

-   `pacman -Ss 关键字` 这将搜索含关键字的包。
-   `pacman -Qi 包名` 查看有关包的信息。
-   `pacman -Ql 包名` 列出该包的文件。

5、其他用法

-   `pacman -Sw 包名` 只下载包，不安装。
-   `pacman -Sc` Pacman 下载的包文件位于 /var/cache/pacman/pkg/
    目录。该命令将清理未安装的包文件。
-   `pacman -Scc` 清理所有的缓存文件。

关于 Pacman 更加详细的用法，可以[阅读 Pacman
的手册页](http://www.archlinux.org/pacman/pacman.8.html)。

**Pacman 的 GUI 前端**

如果你对 Pacman 的图形化前端感兴趣，可以参考 [Arch Linux 的 Wiki
页面](http://wiki.archlinux.org/index.php/Pacman_GUI_Frontends)。其中介绍了包括
Jacman、gtkPacman、Guzuta 等在内的 Pacman GUI 前端。
