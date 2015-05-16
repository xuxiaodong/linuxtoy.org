Title: 没有 Nautilus？照样使用 Dropbox
Date: 2008-10-26 19:19
Author: toy
Category: Tips
Tags: Dropbox
Slug: using-dropbox-without-nautilus

我们介绍的 [Dropbox](http://linuxtoy.org/archives/dropbox.html)
目前只提供了 Nautilus 的插件，对于像我这样的非 GNOME
用户可是有点不够友好。如果没有 Nautilus，可以照样使用 Dropbox
吗？回答是肯定的。下面就跟我一起来实战吧。

1.  [下载 dropbox-lnx
    文件](http://www.getdropbox.com/download?plat=lnx.x86)，并保存到
    $HOME 目录下。我下载的文件名称为
    dropbox-lnx.x86-0.6.382.tar.gz，适合 32 位 Linux 系统。如果你需要 64
    位的
    dropbox-lnx，那么可从[这里下载](http://www.getdropbox.com/download?plat=lnx.x86_64)。
2.  转到主目录下，执行解包命令：`tar zxvf dropbox-lnx.x86-0.6.382.tar.gz`，这将在用户目录下创建
    .dropbox-dist 文件夹，其中包括使用 Dropbox 的若干二进制文件。
3.  执行 `./.dropbox-dist/dropboxd` 初始化 Dropbox 帐户，需要填入 E-mail
    及密码。完成后，用户主目录下将创建 Dropbox 文件夹。

    ![Dropbox Setup](http://i.linuxtoy.org/i/2008/10/dropbox-setup.png)

    如果需要开机即执行 dropboxd，可以将其放入自动启动脚本，如 .xinitrc。

4.  OK. 大功告成。将需要上传的文件链接到用户主目录下的 Dropbox
    文件夹即可，可使用 ln 命令。也可建立各种目录分类管理。

