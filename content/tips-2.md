Title: 小贴士
Date: 2006-09-05 18:41
Author: toy
Category: Tips
Slug: tips-2

不知大家有没有遇到这样的现象：就是以 root
权限执行程序时，其界面外观往往十分简陋，比如通过 sudo synaptic
这样执行程序。使用下面两步将让它变得更加好看。

1.  `sudo ln -s /home/toy/.themes/Rezlooks-graphite/ /root/.themes/Rezlooks-graphite`
    注意，请将 toy 更改为你目前的用户名，并更换 Rezlooks-graphite
    为你所使用的 GNOME 主题。
2.  `sudo ln -s /home/toy/.icons/Tango/ /root/.icons/Tango`
    与上类似，需要更换 toy 为你的用户名及 Tango 为你现在所用的图标主题。

