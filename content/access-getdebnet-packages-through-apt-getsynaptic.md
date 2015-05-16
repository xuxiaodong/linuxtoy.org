Title: 通过 Apt-get/Synaptic 安装 GetDeb 网站的软件
Date: 2007-09-02 08:00
Author: toy
Category: Tips
Slug: access-getdebnet-packages-through-apt-getsynaptic

想必使用 Ubuntu 的朋友都知道有个名叫 [GetDeb](http://www.getdeb.net/)
的网站（[这里是我们曾经的介绍](http://linuxtoy.org/archives/ubuntu_click_and_run.html)），它将最新的软件、游戏打包成
deb 格式供 Ubuntu 用户直接下载安装使用，可谓对 Ubuntu
的使用者帮助不小。为了更好的使用 GetDeb 网站，我们介绍一个从 Apt-get 或
Synaptic 来安装其上的软件、游戏的方法。

[![GetDeb](http://i.linuxtoy.org/i/2007/09/getdeb_s.png)](http://i.linuxtoy.org/i/2007/09/getdeb.png)  
*从 Synaptic 安装 GetDeb 网站的软件、游戏*

要通过 Apt-get 或 Synaptic 安装 GetDeb
网站上的软件或游戏，其操作步骤如下：

1.  打开终端并输入下列指令以编辑 /etc/apt/sources.list 文件：
    `sudo gedit /etc/apt/sources.list`
2.  然后添加下列内容：

    `deb http://ubuntu.org.ua/ getdeb/`

    在保存文件后退出编辑程序。

3.  更新源：
    `sudo apt-get update`
4.  如果你需要对当前的软件更新，可以执行：

    `sudo apt-get upgrade`

    如果你希望安装自己喜欢的软件或游戏，使用如下命令即可：

    `sudo apt-get install software/game`

[[via](http://xubuntu.wordpress.com/2007/08/05/howto-access-getdebnet-packages-through-apt-getsynaptic/)]
