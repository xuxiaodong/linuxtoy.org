Title: FluxBox 与 GDM
Date: 2006-10-13 15:51
Author: toy
Category: Tutorials
Slug: fluxbox_and_gdm

实在无法经受 Edgy 中
[GDM](http://linuxtoy.org/archives/ubuntu_6_1_0_knot_3.html)
的诱惑，于是毫不犹豫地替换了系统中现有的 XDM。

1.  先删掉 XDM：
    `sudo apt-get remove xdm`
2.  再安装 GDM 及 Edgy GDM 主题：

    `sudo apt-get install gdm edgy-gdm-themes`

    当然还有其他的主题可供选择：blubuntu-gdm-theme（蓝色外观的 GDM
    主题）、human-gtk-theme（默认的 GDM 主题）。

3.  接着，还需要考虑让 FluxBox 与 GDM 整合，也就是说，当从 GDM
    中登录时，可以直接进入 FluxBox。这儿有两种解决办法：
    -   法一：创建 ~/.xsession 文件，添加下列内容：
        `exec startfluxbox`
    -   法二：创建 ~/.xinitrc 文件，填入如下内容：
        `exec startfluxbox`

通过 sudo gdmsetup 可对 GDM 进行配置，如选择主题、设置用户自动登录等等。
