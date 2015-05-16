Title: Pidgin GNOME Shell Extension
Date: 2011-05-31 09:23
Author: lovenemesis
Category: Tips
Tags: gnomeshell, Pidgin
Slug: pidgin-gnome-shell-extension

GNOME Shell
的引入的一个新特性就是内建即时通讯（在消息通知窗口中直接回复而无需离开焦点），不过默认仅支持
Empathy。那么 Pidgin 用户怎么办呢？看这里吧～

1.  从这个[github
    仓库](https://github.com/kagesenshi/gnome-shell-extensions-pidgin)下载扩展文件。
2.  将下载的扩展文件(`extension.js` 和 `metadata.json`)解压至
    `$HOME/.local/share/gnome-shell/extensions/pidgin@gnome-shell-extensions.gnome.org`
    目录下，如果不存在的话请创建。
3.  由于目前 GNOME Shell 已经升级至 3.0.2
    版本，所以需要修改下扩展中的版本检测。打开 `metadata.json`
    文件，将其中的 `3.0.1` 修改为 `3.0.2`，保存并退出。
4.  重新启动 Pidgin 和 GNOME Shell (Alt+F2 然后输入 r 回车)即可。

现在，Pidgin 用户在 GNOME Shell 里也可以享受高效率的内建即时通讯功能了。
