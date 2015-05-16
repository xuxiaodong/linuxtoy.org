Title: GTK+3 Ambiance 和 Radiance 主题
Date: 2011-06-23 11:29
Author: lovenemesis
Category: Themes
Tags: gtk3, Ubuntu
Slug: gtk3-ambiance-and-radiance-themes

Ubuntu 的 Ambiance 和 Radiance 主题风格移植到 GTK3+ 上了。

该主题预期将登陆 Ubuntu Oneiric Ocelot。

效果比较图：

[![](http://linuxtoy.org/img/2011/06/light-themes-oneiric.png "light-themes-oneiric")](http://linuxtoy.org/img/2011/06/light-themes-oneiric.png)

值得注意根据报道目前只能通过 `dconf-editor`
手动调整主题（疑问：gnome-tweak-tool 没打包？？）

通过 `sudo apt-get install dconf-tools` 安装后再依次浏览到
**org-->gnome-->desktop-->interface**，将其中的 `gtk-theme` 调整为
`Radiance` 或 `Ambiance` 即可。

*消息来源：*[iloveubuntu](http://iloveubuntu.net/gtk3-ambiance-and-radiance-have-landed-oneiric-ocelot)
