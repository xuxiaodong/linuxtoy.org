Title: Howto：在 Ubuntu 中安装 Flock
Date: 2006-08-30 14:33
Author: toy
Category: Tutorials
Slug: flock_on_ubuntu

[![Flock](http://i.linuxtoy.org/i/flock_s.png)](http://i.linuxtoy.org/i/flock.png)

本 Howto 将向你一步一步地介绍在 Ubuntu 中安装 Flock 的过程。

1.  到 <http://www.flock.com/download/> 下载 Flock，目前为 0.7.4 for
    Linux。
2.  `sudo tar xvzf flock*.tar.gz -C /opt/`
3.  `sudo chown -R root:root /opt/flock/`
4.  `sudo chmod -R 755 /opt/flock/`
5.  `sudo vim /opt/flock/flock`，在文件开头加入
    `GTK_IM_MODULE=xim`，为的是解决 SCIM 与 Flock 的冲突问题。（可选）
6.  sudo ln -s /opt/flock/flock /usr/bin/flock

现在，打开终端，输入 flock，你应该能够看到它的美丽面容了。

如果，你不知道 Flock 究竟为何物，请访问 <http://www.flock.com>。
