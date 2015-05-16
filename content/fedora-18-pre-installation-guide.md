Title: Fedora 18 安装前指南
Date: 2013-01-07 14:50
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-18-pre-installation-guide

代号为 Spherical Cow 的 Fedora 18
带来了大量变化，其中有不少内容值得在安装使用前知晓。

**Secure Boot 与 Win 8**

随着 Win8 的发布，先前关于 [Secure Boot 和 UEFI
的诸多猜测](http://linuxtoy.org/archives/fedora-18-might-supports-uefi-secure-boot.html)也得到了证实，Fedora
18 也将如同当初计划的那样使用 `shim + grub2`
的链式引导方式应对。对于最终用户来说，或许以下的 FAQ
可以便于解答您关心的问题：

-   **Q:** 我买了预装 Win8 的电脑，可以跑 Fedora 18 么，需要在 UEFI
    中做什么更改么？ **A:** 您无需进入 UEFI 做任何更改即可运行 Fedora
    18。
-   **Q:** 我发现在使用 Fedora 18 时无法挂载 NTFS 分区了！**A:**
    这种情况发生在您使用 Win8
    的“快速重启”功能了，该功能的设计缺陷可能会在 Win8
    下次启动时清空在其他系统下往 NTFS
    分区写入的文件。为了阻止这种情况发生，Fedora 18 中搭载的 `ntfs-3g`
    在检测到“快速重启”启用时将拒绝挂载 NTFS 分区。若要想正常挂载 NTFS
    分区，请禁用“快速重启”。
-   **Q:** 我的机子预装 Win8 且打开了 Secure Boot，之前 Fedora 18
    运行的好好的，为什么在安装闭源显卡驱动/Virtual Box /VMWare
    之后就无法引导了呢？ **A:** 闭源显卡驱动/Virtual Box /VMWare
    需要加载额外的内核模块，这将变化原先签名的内核镜像。若是不想创建自定义证书（后续教程待定），可以暂先使用开源显卡驱动/KVM
    或者关闭 Secure Boot。
-   **Q:** 我买的新主板是 UEFI 且有 Win8 兼容徽标的，需要担心 Secure
    Boot 么？ **A:** 通过 DIY 渠道购买的 UEFI 主板目前默认关闭 Secure
    Boot，您可以安装任何基于 GRUB2 引导的发行版比如 Fedora
    18，甚至不支持 Secure Boot 的 Fedora 17 都可以。
-   **Q:** 我的 Win8 是从老版本升级/自行单独购买的，所以硬盘还是 MBR
    分区表的，可以安装 Fedora 18 么？**A:** 建议参照[此教程转换为 GPT
    分区表](http://www.rodsbooks.com/gdisk/mbr2gpt.html)，不过现在您可以在
    Live 介质引导时增添 `nogpt` 选项强制在安装目标主机使用 MBR 分区表。

**配置文件移位**

在**系统配置**方面，位于 `/etc/sysconfig`
目录下的配置文件已经不再使用，转而使用 /etc
下应用程序独立目录的方式体现。具体变化如下：

-   改用 `/etc/localtime` 配置时间及时区。
-   使用 `/etc/locale.conf` 管理区域相关的环境变量。
-   现由 `/etc/vconsole.conf` 负责虚拟终端的配置。
-   主机名由 `/etc/hostname` 配置。
-   更改显示管理器只需要 `systemctl enable --force DMNAME`
    即可，不再需要编辑 `/etc/sysconfig/desktop` 文件。

更多内容可以参考对应的 `man` 手册，比如 `man localtime`
可以获知关于新的时区分配的配置。

此外一般用户的关机重启等权限也改由
`/usr/share/polkit-1/actions/org.freedesktop.login1.policy`
配置，不再使用 `/etc/pam.d` 中的设置了。

在用户**个人配置**方面，根据最新的 Free Desktop
标准变更了部分配置文件位置，如：

-   `$HOME/.xinputrc` 已​被​移​至​ `$HOME/.config/imsettings/xinputrc`。
-   `$HOME/.imsettings.log` 已​被​移​至​ `$HOME/.cache/imsettings/log`
-   `$HOME/.fonts.conf` 已被移至 `$HOME/.config/fontconfig/fonts.conf`。
-   `$HOME/.fonts.conf.d` 已被移至
    `$HOME/.config/fontconfig/fonts.conf.d`。

**GNOME 3.6 与输入法**

Fedora 18 搭载的 GNOME 3.6 默认使用 IBus
输入法框架，但是没有默认绑定输入法切换快捷键，要设定快捷键请：

1.  在​“系​统​设​”置​中​的“​输​入​源”​选​项​下​点​击​“快​捷​键​设​置”​链​接​，或​者​点​击​顶​端​的​键​盘​图​标​然​后​选​择“快​捷​键​选​项”​，再​点​击​左​侧​面​板​的​输​入​部​分​。​
2.  点​击​切​换​至​下​一​输​入​源​，然​后​按​ `CTRL + SPACE`​。

该[问题已经汇报](https://bugzilla.redhat.com/show_bug.cgi?id=889533)，可能会在后续更新中修复。

​尽管 GNOME 3.6 中集成了 IBus 输入法框架，但是您依然可以使用诸如 FCITX
等其他输入法框架。以 fcitx 为例步骤如下：

1.  当然是安装第三方输入法框架了：`pkcon install fcitx-libpinyin fcitx-configtool fcitx-gtk2 fcitx-gtk3 fcitx-qt4`。
2.  然后在终端运行关闭 GNOME 对于 XKB
    的接管：`gsettings set org.gnome.settings-daemon.plugins.keyboard active false`
    。
3.  使用应用程序中的“输入法选择器”或者在终端执行 im-chooser 选择 fcitx。

完成以上步骤后就可以立即使用
fcitx，**无需注销/重启，变更限定为当前用户，无需删除任何软件包**。

更多内容可以参考 [GNOME 3.6
发行摘要中相关章节](https://live.gnome.org/ThreePointFive/Features/IBus#How_to_use_other_IM_frameworks)。

近期 Fedora 18 正式版由于新安装器在处理 btrfs 文件系统的一些问题被推迟至
**1 月 15 日发布**。若是您不打算使用 btrfs 文件系统，可以**现在就下载
Fedora 18 RC4 版本开始使用**：

[Fedora 18 RC1
发布公告](https://lists.fedoraproject.org/pipermail/test-announce/2013-January/000600.html)

[RC4 DVD
安装镜像](https://dl.fedoraproject.org/pub/alt/stage/18-RC4/Fedora/)

[RC4 Live 镜像](https://dl.fedoraproject.org/pub/alt/stage/18-RC4/Live/)

[完整中文发布摘要](https://docs.fedoraproject.org/zh-CN/Fedora/18/html/Release_Notes/index.html)
