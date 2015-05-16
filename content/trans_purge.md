Title: trans-purge：Linux 桌面瘦身加速工具组
Date: 2006-10-16 09:03
Author: toy
Category: Apps
Slug: trans_purge

trans-purge 是对岸朋友[洪任论](http://pcman.sayya.org)（也是 PCMan File
Manager 的作者）写的一组可使 Linux
桌面瘦身并让程序加速启动的小工具。这组工具包括 desktop-purge、mime-purge
和 gconf-purge 三种。其中，desktop-purge 可从 *.desktop
文件中删除无用的翻译内容；mime-purge 能删除 mime-database
中无用的翻译内容；gconf-purge 则针对 gconf schema
中无用的翻译内容进行删除处理。总体来说，trans-purge
这组小工具是通过删除系统上无用的多国语言翻译来达到让 Linux
瘦身、使程序启动更快的目的。经过 trans-purge 的处理，Linux
系统中将只剩下英文和目前正在使用的 locale。

trans-purge 这组小工具使用过程如下：

1.  下载源代码：  

    ` wget http://pcman.sayya.org/desktop-purge.c wget http://pcman.sayya.org/mime-purge.c wget http://pcman.sayya.org/gconf-purge.c`
2.  安装编译依赖：  
    `sudo apt-get install libglib2.0-dev`
3.  编译程序：  

    ``  gcc `pkg-config glib-2.0 --cflags --libs` -o desktop-purge desktop-purge.c gcc `pkg-config glib-2.0 --cflags --libs` -o mime-purge mime-purge.c gcc `pkg-config glib-2.0 --cflags --libs` -o gconf-purge gconf-purge.c ``
4.  安装程序：  

    ` sudo cp desktop-purge /usr/bin/ sudo cp mime-purge /usr/bin/ sudo cp gconf-purge /usr/bin/`
5.  执行清理：
    1.  手动清理：  
        ` sudo desktop-purge sudo mime-purge sudo gconf-purge`
    2.  自动清理：
        让每次 apt-get 安装软件后自动进行清理。创建
        /etc/apt/apt.conf.d/99-transpurge 文件，并添加下列内容：  

        ` DPkg { Post-Invoke {"if [ $(ps w -p "$PPID" | grep -c remove) != 1 ]; then /usr/bin/desktop-purge > /dev/null; /usr/bin/mime-purge >/dev/null ; /usr/bin/gconf-purge > /dev/null; else exit 0; fi";}; };`

警告：无用翻译在清除后无法还原，若使用后造成系统损坏，作者并不负责。

PS.我用过后很并无其他问题。

（Via
[自由软体技术交流网](http://freesf.tw/modules/news/article.php?storyid=2881),
thanks!）
