Title: GrNotify: 即时获取 Google Reader 更新
Date: 2008-02-13 15:38
Author: toy
Category: Apps, Feed Reader
Slug: grnotify

RSS 恐怕是如今最为流行的获取资讯方式。如果你在使用 Google Reader
订阅、管理、阅读 Feed，那么不妨通过
[GrNotify](http://grnotify.sourceforge.net/)
这款小程序来即时获得更新。GrNotify 能够驻留在系统托盘，并自动刷新 Google
Reader 所订阅的 Feed，为你呈上未读的 Feed 项目和数量。

![GrNotify](http://i.linuxtoy.org/i/2008/02/grnotify.png)

GrNotify
目前的功能还比较简单，如果能够提供更多有用信息和交互链接，就不错了。GrNotify
包括 [deb
包和源码包](http://sourceforge.net/project/showfiles.php?group_id=217132)，前者可用如下指令安装：

`sudo dpkg -i *.deb`

后者在解包后可用下面的命令安装：

`sudo python ./install.py`

当启动 GrNotify 后，需要设置你的 Google Reader
用户名及密码方能正常工作。
