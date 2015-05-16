Title: 在 Nexus 4 上安装 Fedora 19
Date: 2013-06-06 10:20
Author: lovenemesis
Category: Distros
Tags: Fedora, Freedreno
Slug: fedora-19-on-nexus4

尽管桌面版本还未正式发布，但是您已经可以在 Nexus 4 上体验 Fedora 19 了。

别激动，这不代表 Fedora/Red Hat 要追随 [Ubuntu
的步伐进军智能手机](http://linuxtoy.org/archives/ubuntu-for-phones.html)市场。这个其实是
**Freedreno 项目为了方便展示当下适用于 Qualcomm A320 的逆向工程
Gallium3D 开源驱动成果**。相比 Ubuntu Phone 所依赖的 Android
底层，Freedreno 所实现的 Gallium3D 驱动和桌面版 Linux 更为相似。

**警告：**尽管以上过程是通过 `chroot`
实现的，且没有永久性的更新内核，不过依然需要谨慎进行。

**系统需求**：

-   已经打开开发者选项（[快速敲击编译版本号七次](http://geekcaves.blogspot.com/2013/05/how-to-unlock-developer-options-on.html)）的
    Nexus 4 一枚。
-   /data 分区至少保有 3G 的空闲空间。
-   一台装有 Fedora 系统的主机。

**步骤**：

1.  从 Github
    下载所需脚本：[fedora-nexus4](https://github.com/freedreno/nexus4-fedora)，然后进入所在目录。
2.  在 Fedora
    主机上安装必要工具：`sudo yum install android-tools abootimg`
3.  在 Nexus 4
    上最好关闭数据流量且在开发者选项中打开“保持唤醒状态”，然后按住音量减小键开机，进入
    `fastboot` 模式
4.  用 USB 链接至 Fedora
    主机上，然后运行以下命令：`sudo fastboot boot boot/mako-boot.img`
5.  运行 `./install-rootfs.sh` 安装根分区，稍稍耐心下。
6.  之后使用 `adb shell` 切换至 Nexus 4 上的终端环境，然后运行
    `/data/fedora/start-chroot.sh` 开始运行。需要安装 `X11` 和
    `gnome-desktop` 等组件，所以请保证 WiFi 稳定并耐心等待。

若是您懒得折腾的话，也可以在[这里查看在 Nexus 4 上运行 Fedora 19 及
GNOME Shell
的视频](http://www.youtube.com/watch?v=xXSOp-4Pyvg&feature=player_embedded)。如视频中所示，激活预览视图（桌面版中的
`SUPER` 键），需要在左侧向上滑动。

[Github
代码仓库及英文安装步骤](https://github.com/freedreno/nexus4-fedora)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTM4NDY)
