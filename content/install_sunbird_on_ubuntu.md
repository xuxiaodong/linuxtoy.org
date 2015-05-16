Title: Howto：在 Ubuntu 中安装 Sunbird 最新版
Date: 2006-10-11 21:14
Author: toy
Category: Tutorials
Slug: install_sunbird_on_ubuntu

Mozilla [Sunbird](http://www.mozilla.org/projects/calendar/sunbird/)
在今天发布了 0.3
正式版，将新的存贮体系、更多的直观界面、重新设计的首选项对话框、插件支持、更佳的打印效果、24
时查看、可靠的警报提醒、改进的本地化支持（可惜尚无中文版）
、许多的可靠性及性能改进等众多特性带给了用户。更加详细的新特性介绍可查看[发布注记](http://www.mozilla.org/projects/calendar/releases/sunbird0.3.html)。如果你想要在
Ubuntu 中使用 Sunbird，那么下面的安装指南应该对你有所帮助。

![Sunbird](http://i.linuxtoy.org/i/sunbirdlogo.png)

1.  `wget -c  http://releases.mozilla.org/ pub/mozilla.org/calendar/sunbird/ releases/0.3/linux-i686/en-US/sunbird-0.3.en-US.linux-i686.tar.bz2`
2.  `sudo tar xvjf sunbird-0.3.en-US.linux-i686.tar.bz2 -C /opt/`
3.  `sudo chown -R root:root /opt/sunbird/`
4.  `sudo chmod -R 755 /opt/sunbird/`
5.  `sudo ln -s /opt/sunbird/sunbird /usr/bin/sunbird`

现在，在终端中执行 sunbird 就可以运行 Sunbird 了。
