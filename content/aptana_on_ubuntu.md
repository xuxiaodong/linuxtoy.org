Title: Howto：在 Ubuntu Dapper 中安装 Aptana
Date: 2006-09-07 21:35
Author: toy
Category: Tutorials
Slug: aptana_on_ubuntu

[Aptana](http://www.aptana.com) 号称是 Web 2.0 IDE，主要聚焦于
JavaScript、HTML、CSS
的开发。个人使用最强烈的感受是，它的代码助手功能超级好用，能够大大的提高编码效率。本
Howto 将提供其在 Ubuntu 中的安装指导。

[![Aptana](http://i.linuxtoy.org/i/aptana_s.png)](http://i.linuxtoy.org/i/aptana.png)

1.  下载 [Aptana for
    Linux](http://www.web20.com/downloads/current/Linux/VM/Aptana_IDE_Setup_Current.bin)，当前版本为
    0.2.4。使用我们之前介绍的
    [Axel](http://linuxtoy.org/archives/axel.html)
    将为你节省不少下载时间。
2.  准备使用依赖，运行 Aptana 需要安装 Mozilla 和 libswt3.1。
    `sudo apt-get install mozilla`  
    `sudo apt-get install libswt3.1-gtk-java`
3.  让先前下载的 Aptana\_IDE\_Setup\_Current.bin 文件具有可执行权限。
    `chmod +x Aptana_IDE_Setup_Current.bin`
4.  执行 sudo ./Aptana\_IDE\_Setup\_Current.bin，按照安装向导完成安装。
5.  `touch aptana`  
    `sudo vim aptana`

    然后，输入下列内容：

    `#/usr/bin export MOZILLA_FIVE_HOME=/usr/lib/mozilla /opt/aptana/aptana`

    注意，最后一行需要根据你的 aptana 实际安装路径作出相应修改。

6.  `chmod 755 aptana`
7.  最后将 aptana 复制到 /usr/bin：`sudo cp aptana /usr/bin/`

（Via
[BrianPedigo.info](http://brianpedigo.info/how_to_install_aptana_on_ubuntu_dapper_drake_70),
thanks!）
