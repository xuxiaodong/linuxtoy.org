Title: Musicbox：网易云音乐命令行版本
Date: 2015-01-13
Author: lovenemesis
Category: Multimedia
Tags: neteasemusic, python, terminal
Slug: musicbox-neteasemusic-in-terminal
Summary: 如果您是系统管理员的话，不仅你会喜欢这个在终端中运行的网易云音乐客户端，你的树莓派会更喜欢。

这款命令行的客户端使用 Python 构建，以 mpg123 作为播放后端：

* Vim 式的流畅操作，支持快捷键绑定
* 支持电台、收藏等各种特色功能
* 支持 OS X 及各类 Linux 发行版

Fedora 平台下安装（需要启用 rpmfusion 仓库）：

`sudo pip2 install NetEase-MusicBox`

`sudo dnf install mpg123`

之后在终端输入 `musicbox` 即可。

[更多详情参考位于 Github 上的项目](https://github.com/darknessomi/musicbox)

[消息来源](https://twitter.com/eastwoodnet/status/686836059573850112)
