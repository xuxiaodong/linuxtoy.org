Title: 在 KDE 3 中使用 Oxygen 图标主题
Date: 2006-12-11 21:38
Author: toy
Category: Tutorials
Slug: using-oxygen_icons_in_kde3

[Oxygen](http://www.oxygen-icons.org) 原本是为 KDE 4
所准备的一套新的图标主题，其外观相当漂亮。不过 KDE 4
仍在开发当中，作为普通用户的你想要在 KDE 3 中体验 Oxygen
图标带来的魅力吗？以下的提示将给你一些帮助。

![Oxygen](http://i.linuxtoy.org/i/2006/12/oxygen.png)  
*Image from Oxygen-icons.org*

1.  安装 inkscape，如果你已经装好了，那么可以跳过此步。  
    `sudo apt-get -f install inkscape`
2.  从 svn 下载图标。  

    `svn co svn://anonsvn.kde.org/home/kde/trunk/playground/artwork/Oxygen/`  
    `cd Oxygen/utils`
3.  执行脚本生成 KDE 3 使用的图标主题，虽有些错误信息，但可以忽略。  
    `./generate_oxy_theme.sh`
4.  安装图标包，注意位置在 Oxygen/theme/oxygen*.tar.gz。

[
[via](http://ubuntuos.com/2006/12/take-kde4-oxygen-icons-out-for-a-test-drive),
thanks! ]
