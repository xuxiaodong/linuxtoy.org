Title: 如何启用 Ubuntu 中的 root 帐号
Date: 2006-09-28 21:07
Author: toy
Category: Tutorials
Slug: howto_enable_ubuntu_root_account

其实我个人认为这没有多大必要，因为当你需要 root 的权限时，使用 sudo
便可以了。如果你实在需要在 Ubuntu 中启用 root
帐号的话，那么不妨执行下面的操作：

    sudo passwd root

此命令将会重新设置 root
的密码，按照提示输入新的密码，并加以确认。之后，重启系统时，就可以用
root 登录了。

如果你想要禁用 root 帐号，则执行下列命令：

    sudo passwd -l root

（Via [Debian
Admin](http://www.debianadmin.com/enable-and-disable-ubuntu-root-password.html),
thanks!）
