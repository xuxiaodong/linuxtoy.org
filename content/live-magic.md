Title: 用 Live Magic 制作 Debian Live 光盘
Date: 2010-03-12 18:16
Author: toy
Category: Tips
Tags: Debian, Live Magic, Ubuntu
Slug: live-magic

{ 撰文/七米深蓝 }

最近无事翻 Ubuntu 的软件中心，发现一个有趣的软件，叫做 Live  
Magic，这东西可以非常傻瓜的制作 Debian 的 Live 盘。

首先在 Ubuntu 软件中心下载 Live Magic
这个软件，装完之后会在应用程序-附件中出现 Live Magic 的快捷方式。

打开 Live Magic 它会先让你选择是要制作 Standard Debian 安装盘还是带有  
GNOME/KDE/Xfce 其中一种的 Live 盘或者 rescue 盘。然后需要选择是要使用
Stable，Testing 还是 Unstable 的 Debain 作为 Live
盘的基础，下一步选择是要生成 ISO，或是用于 USB/HDD 的 image 镜像或者是
Network boot 启动盘。下一步会要求输入 Debian 的源，例如我要使用 163
的源就在此输入

http://mirrors.163.com/ubuntu/

下一步会要求选择生成的 Live
盘是否要带有硬盘安装程序，接下来选择语言和键盘布局，最后选择生成镜像的目录，最后按下应用，接下来只需要漫长的等待即可，程序会自动从源下载需要的包构建
Live 盘。简单轻松的几步即可制作自定义的一张 Debian Live 盘。

{ Thanks 七米深蓝. }
