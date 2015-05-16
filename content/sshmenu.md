Title: SSHMenu — 快速访问 SSH 连接
Date: 2007-08-18 10:26
Author: toy
Category: Apps
Slug: sshmenu

如果你需要经常使用 SSH 连接登录服务器，那么
[SSHMenu](http://www.mclean.net.nz/ruby/sshmenu/)
是一个不可错过的好工具。SSHMenu 这个 GNOME 面板程序允许你直接从 GNOME
面板打开或者保存 SSH
连接，并且它能够使用你选择的终端配置文件，以便符合用户的个人使用习惯。

[![SSHMenu](http://i.linuxtoy.org/i/2007/08/sshmenu_s.png)](http://i.linuxtoy.org/i/2007/08/sshmenu.png)  
*SSHMenu 屏幕截图*

SSHMenu 当前版本为
3.13，其[源码包](http://www.mclean.net.nz/ruby/sshmenu/download/)可从这里获取。如果你使用
Debian 或 Ubuntu 系统，则可以从作者的个人源直接加以安装：

`deb http://www.mclean.net.nz/debian stable contrib`

你需要将上面的内容添加到 /etc/apt/sources.list 文件，并获取作者的 [PGP
密钥](http://pgp.mit.edu:11371/pks/lookup?search=0x4CC00851&op=get)。

然后在终端执行下列指令：  
` sudo apt-get update sudo apt-get install sshmenu-gnome`

[[via](http://ubuntu.wordpress.com/2007/08/17/ssh-menu-save-and-open-ssh-connections-from-the-panel/)]
