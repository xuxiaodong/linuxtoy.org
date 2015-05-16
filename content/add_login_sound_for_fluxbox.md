Title: 为 Fluxbox 加上启动声音
Date: 2006-10-08 21:49
Author: toy
Category: Tutorials
Slug: add_login_sound_for_fluxbox

在系统升级到 Edgy Eft
之后，我根据[这篇帖子](http://ubuntuguide.org/wiki/Ubuntu_Edgy#Make_it_make_the_pretty_sound_on_login)给
Fluxbox 添加了启动声音，无它，只是让它更好玩一点。

1.  安装 [SoX](http://sox.sourceforge.net)

        sudo apt-get install sox

    SoX
    是一个可播放、录制、转换声音文件的命令行小工具。安装后，可在配置文件中调用它。

2.  编辑 ~/.fluxbox/startup

        vim ~/.fluxbox/startup

    找到这一行：

        exec /usr/bin/fluxbox

    此处 fluxbox 的位置也有可能是 /usr/local/bin/fluxbox，最好使用 which
    fluxbox 查一下。

    在它的上面添加：

        play /usr/share/sounds/login.wav > /dev/null 2>&1 &

现在，重启吧。

PS. Edgy Eft 的启动音乐似乎比 Dapper 的要好听些。 :)
