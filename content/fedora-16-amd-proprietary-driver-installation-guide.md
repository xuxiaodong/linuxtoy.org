Title: Fedora 16 AMD 闭源驱动安装指南
Date: 2012-01-15 11:22
Author: lovenemesis
Category: Tutorials
Tags: Catalyst, Fedora
Slug: fedora-16-amd-proprietary-driver-installation-guide

鉴于近来有刚入门朋友在邮件列表问及这个问题，且目前也没有专门针对的教程，于是补上此文。

目的是在 Fedora 16 系统上从 RPMFUSION 仓库安装 AMD Catalyst
闭源驱动，通用于于 32 位、32 位 PAE 和 64 位系统。

**准备步骤**

如果之前使用 AMD 提供的 run 文件安装过驱动的话，请卸载并修复 Mesa 库：

`su -c 'yum reinstall mesa-libGL'`

然后若还没启用过 RPMFUSION 仓库，那么请安装并启用：

`su -c 'rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm'`

**安装**

`pkcon install akmod-catalyst xorg-x11-drv-catalyst xorg-x11-drv-catalyst-libs.i686`

**配置**

首先需要禁用 KMS，编辑 GRUB2 配置文件 `/etc/default/grub`
，为已有变量增加 `nomodeset` 参数，例如：

    GRUB_CMDLINE_LINUX="quiet rhgb nomodeset"

之后运行 `grub2-mkconfig -o /boot/grub2/grub.cfg` 重新生成配置文件。

第二步需要给驱动里一个库文件加上 SELinux 标签，至少在 11.11
中需要这一步，看来是 AMD 遗漏了……

    su -c 'chcon -t textrel_shlib_t /usr/lib/dri/fglrx_dri.so'

最后一步是生成 /`etc/X11/xorg.conf` 文件，可选，因为
`/etc/X11/xorg.conf.d/` 中的配置已经可以使其正常工作了，但是 `aticonfig`
工具需要它。

`su -c 'aticonfig --initial'`

最后，**重启系统生效**！

**使用**

*测试*

重启后可以测试下 Catalyst 驱动是否已经启用了，运行一下：

`fglrxinfo`

也可以看看 3D 加速：

    fgl_glxgears

*PowerXpress 内置和独立显卡切换(root 用户执行)*

使用内置显卡(节能模式)，运行后注销/重启 X11 生效：

`aticonfig --px-igpu`

使用独立显卡(高性能模式)，运行后注销/重启 X11 生效：

`aticonfig --px-dgpu`

查看当前正在使用的显卡：

`aticonfig --pxl`

*OverDrive 超频选项*

显示当前 GPU 核心及显存频率、理论范围和 **GPU 占有率**：

`aticonfig --odgc`

获取当前 GPU 温度：

`aticonfig --odgt`

设置新的 GPU 频率和显存频率：

    aticonfig --odsc=GPU_CLOCK,GDDR_CLOCK

如果新频率不稳定的话，那么可以恢复原始，运行后注销/重启 X11 生效：

`aticonfig --odrd`

如果新频率稳定可用，那么可以设置为启动时自动超频，运行后注销/重启 X11
生效：

`aticonfig --odcc`

*UVD2 硬件解码*

目前 `mplayer` 和 `VLC` 等只能使用 VAAPI 做为中介调用 XVBA 实现 UVD2
硬件解码，但是经过本人实际测试效果不理想：

-   在近两年多核 CPU 的过期配置下远不如 ffmpeg-mt 效率高。
-   不能处理 H264 5.1 Profile 的视频。
-   mplayer 不能加载字幕。

故此就不介绍其中的折腾过程了，实在不值得。不过现在 XBMC 有直接访问 XVBA
无需 VAAPI 中转的分支，据说性能有提升(依然不能处理 H264 5.1 Profile
的视频)。

**卸载**

如果对于闭源驱动不满意，那么可以卸载来切换回开源驱动：

`su -c 'yum remove akmod-catalyst kmod-catalyst-* xorg-x11-drv-catalyst xorg-x11-drv-catalyst-libs.i686'`

然后删除 X.org 配置文件：

`su -c 'rm /etc/X11/xorg.conf'`

然后仿照之前步骤移除 GRUB2 配置文件 `/etc/default/grub`，删除
`nomodeset` 参数。

以免万一，还可以恢复 Mesa 配置：

`su -c 'yum reinstall mesa-libGL'`

重启即可。
