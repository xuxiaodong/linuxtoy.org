Title: KDE 3.5.5 for Kubuntu 现在已经可用
Date: 2006-10-11 22:57
Author: toy
Category: Apps
Slug: kde_3_5_5_for_kubuntu

诚如之前的[消息](http://linuxtoy.org/archives/kde_3_5_5_coming_soon.html)所言，KDE
3.5.5 已经发布，假如你是 Kubuntu 用户的话，那么现在就可以立即更新了。

Kubuntu 6.06 LTS（Dapper）升级步骤如下：

-   获取并添加数字签名：

        wget http://people.ubuntu.com/~jriddell/kubuntu-packages-jriddell-key.gpg
        sudo apt-key add kubuntu-packages-jriddell-key.gpg

-   将

        deb http://kubuntu.org/packages/kde-355 dapper main

    添加到 /etc/apt/sources.list
    文件。你也可以使用[其他镜像](http://kubuntu.org/announcements/kde-355.php)。

-   然后执行：

        sudo apt-get update && sudo apt-get upgrade

    更新即可。

另外，对于 Kubuntu Edgy 来说，KDE 3.5.5
也已经上传完毕，同样可以更新并使用。
