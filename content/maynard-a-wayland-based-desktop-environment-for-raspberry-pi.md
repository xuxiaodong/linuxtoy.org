Title: Maynard：面向树莓派的 Wayland 桌面环境
Date: 2014-06-18 13:00
Author: lovenemesis
Category: Desktop Environment
Tags: Maynerd, wayland
Slug: maynard-a-wayland-based-desktop-environment-for-raspberry-pi

Raspberry Pi 基金会和 Collaborra 携手为树莓派用户打造基于 Wayland
的新一代桌面环境。

Maynard 使用 Wayland 的参考混成器 Weston 及 GTK+ 打造，衍生自
weston-gtk-shell。它充分利用 BCM2835 的硬件视频缩放(HVS)
功能实现流畅的视觉效果。

[![Maynard\_desktop](http://lt-file.b0.upaiyun.com/files/2014/06/Maynard_desktop.jpg)](http://lt-file.b0.upaiyun.com/files/2014/06/Maynard_desktop.jpg)

安装运行比较简单：

`wget http://raspberrypi.collabora.co.uk/setup-maynard.sh`

`bash ./setup-maynard.sh`

`maynard`

当然 Maynerd
也可以安装到非树莓派电脑上，不过就需要[自己重新编译](https://github.com/raspberrypi/maynard/wiki/Develop-on-a-computer)。

[演示视频](https://www.youtube.com/watch?v=VPu_IMj9ZBI)

[Github 项目首页](https://github.com/raspberrypi/maynard)

*消息来源：*[CNX
Software](http://www.cnx-software.com/2014/06/17/maynard-wayland-desktop-environment-raspberry-pi/)
