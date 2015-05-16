Title: fedmsg-notify
Date: 2013-03-17 11:11
Author: lovenemesis
Category: Desktop Stuff
Tags: Fedora
Slug: fedmsg-notify

fedmsg-notify 这款桌面提示工具可以帮助您掌握 Fedora
项目中的各项动态，适用于多个不同的桌面环境。

[![](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-config-0-203x250.png "fedmsg-notify-config-0")](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-config-0.png)

如上图所示，fedmsg-notify 将启动一个后台系统服务，按照您的需求去查询
Fedora
项目基础构建系统的信息并实时提醒，支持包括软件包更新、IRC会议提醒、 Wiki
编辑、构建通知在内的各项内容。

[![](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-config-1-203x250.png "fedmsg-notify-config-1")](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-config-1.png)

更为强大的是 fedmsg 可以和 [ABRT
自动错误汇报工具](http://abrt.fedorahosted.org/)和
[PackageDB](https://admin.fedoraproject.org/pkgdb)
相关联，提供包括软件包构建及 Bug 状态提醒等高级功能。

fedmsg 使用通用的
[notification-spec](https://developer.gnome.org/notification-spec/)
方式实现桌面通知，**适用于各种常见的桌面环境。**

Fedora 18 下安装方法： `pkcon install fedmsg-notify`

安装后在终端运行 `fedmsg-notify-config` 打开配置界面。

若是使用 GNOME 3
的话，安装对应的扩展小程序**（可选）**，实现如下图的效果：

[![](http://lt-file.b0.upaiyun.com/files/2013/03/gnome-shell-extension-fedmsg.png "gnome-shell-extension-fedmsg")](http://lt-file.b0.upaiyun.com/files/2013/03/gnome-shell-extension-fedmsg.png)

[![](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-0-crop-300x107.png "fedmsg-notify-0-crop")](http://lt-file.b0.upaiyun.com/files/2013/03/fedmsg-notify-0-crop.png)

Fedora 18 下安装方法：`pkcon install gnome-shell-extension-fedmsg`

之后可以通过 [GNOME Shell
Extension](https://extensions.gnome.org/local/) 或者 `gnome-tweak-tool`
启用。

更多技术细节请前往[图片出处及博客原文](http://lewk.org/blog/fedmsg-notify)
