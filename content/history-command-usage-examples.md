Title: History（历史）命令用法 15 例
Date: 2008-09-07 08:00
Author: toy
Category: Cli
Tags: Commands, History
Slug: history-command-usage-examples

如果你经常使用 Linux 命令行，那么使用
history（历史）命令可以有效地提升你的效率。本文将通过实例的方式向你介绍
history 命令的 15 个用法。

**使用 HISTTIMEFORMAT 显示时间戳**

当你从命令行执行 history
命令后，通常只会显示已执行命令的序号和命令本身。如果你想要查看命令历史的时间戳，那么可以执行：


    # export HISTTIMEFORMAT='%F %T '
    # history | more
    1  2008-08-05 19:02:39 service network restart
    2  2008-08-05 19:02:39 exit
    3  2008-08-05 19:02:39 id
    4  2008-08-05 19:02:39 cat /etc/redhat-release

**注意**：这个功能只能用在当 HISTTIMEFORMAT
这个环境变量被设置之后，之后的那些新执行的 bash
命令才会被打上正确的时间戳。在此之前的所有命令，都将会显示成设置
HISTTIMEFORMAT 变量的时间。[感谢 NightOwl 读者补充]

**使用 Ctrl+R 搜索历史**

Ctrl+R
是我经常使用的一个快捷键。此快捷键让你对命令历史进行搜索，对于想要重复执行某个命令的时候非常有用。当找到命令后，通常再按回车键就可以执行该命令。如果想对找到的命令进行调整后再执行，则可以按一下左或右方向键。


    # [Press Ctrl+R from the command prompt, which will display the reverse-i-search prompt]
    (reverse-i-search)`red‘: cat /etc/redhat-release
    [Note: Press enter when you see your command, which will execute the command from the history]
    # cat /etc/redhat-release
    Fedora release 9 (Sulphur)

**快速重复执行上一条命令**

有 4 种方法可以重复执行上一条命令：

1.  使用上方向键，并回车执行。
2.  按 !! 并回车执行。
3.  输入 !-1 并回车执行。
4.  按 Ctrl+P 并回车执行。

**从命令历史中执行一个指定的命令**

在下面的例子中，如果你想重复执行第 4 条命令，那么可以执行 !4：


    # history | more
    1  service network restart
    2  exit
    3  id
    4  cat /etc/redhat-release
    # !4
    cat /etc/redhat-release
    Fedora release 9 (Sulphur)

**通过指定关键字来执行以前的命令**

在下面的例子，输入 !ps 并回车，将执行以 ps 打头的命令：


    # !ps
    ps aux | grep yp
    root     16947  0.0  0.1  36516  1264 ?        Sl   13:10   0:00 ypbind
    root     17503  0.0  0.0   4124   740 pts/0    S+   19:19   0:00 grep yp

**使用 HISTSIZE 控制历史命令记录的总行数**

将下面两行内容追加到 .bash\_profile 文件并重新登录 bash
shell，命令历史的记录数将变成 450 条：


    # vi ~/.bash_profile
    HISTSIZE=450
    HISTFILESIZE=450

**使用 HISTFILE 更改历史文件名称**

默认情况下，命令历史存储在 ~/.bash\_history 文件中。添加下列内容到
.bash\_profile 文件并重新登录 bash shell，将使用 .commandline\_warrior
来存储命令历史：


    # vi ~/.bash_profile
    HISTFILE=/root/.commandline_warrior

**使用 HISTCONTROL 从命令历史中剔除连续重复的条目**

在下面的例子中，pwd 命令被连续执行了三次。执行 history
后你会看到三条重复的条目。要剔除这些重复的条目，你可以将 HISTCONTROL
设置为 ignoredups：


    # pwd
    # pwd
    # pwd
    # history | tail -4
    44  pwd
    45  pwd
    46  pwd [Note that there are three pwd commands in history, after executing pwd 3 times as shown above]
    47  history | tail -4
    # export HISTCONTROL=ignoredups
    # pwd
    # pwd
    # pwd
    # history | tail -3
    56  export HISTCONTROL=ignoredups
    57  pwd [Note that there is only one pwd command in the history, even after executing pwd 3 times as shown above]
    58  history | tail -4

**使用 HISTCONTROL 清除整个命令历史中的重复条目**

上例中的 ignoredups
只能剔除连续的重复条目。要清除整个命令历史中的重复条目，可以将
HISTCONTROL 设置成 erasedups：


    # export HISTCONTROL=erasedups
    # pwd
    # service httpd stop
    # history | tail -3
    38  pwd
    39  service httpd stop
    40  history | tail -3
    # ls -ltr
    # service httpd stop
    # history | tail -6
    35  export HISTCONTROL=erasedups
    36  pwd
    37  history | tail -3
    38  ls -ltr
    39  service httpd stop
    [Note that the previous service httpd stop after pwd got erased]
    40  history | tail -6

**使用 HISTCONTROL 强制 history 不记住特定的命令**

将 HISTCONTROL 设置为
ignorespace，并在不想被记住的命令前面输入一个空格：


    # export HISTCONTROL=ignorespace
    # ls -ltr
    # pwd
    #  service httpd stop [Note that there is a space at the beginning of service, to ignore this command from history]
    # history | tail -3
    67  ls -ltr
    68  pwd
    69  history | tail -3

**使用 -c 选项清除所有的命令历史**

如果你想清除所有的命令历史，可以执行：

    # history -c

**命令替换**

在下面的例子里，!!:$ 将为当前的命令获得上一条命令的参数：


    # ls anaconda-ks.cfg
    anaconda-ks.cfg
    # vi !!:$
    vi anaconda-ks.cfg

**补充**：使用 !$ 可以达到同样的效果，而且更简单。[感谢 wanzigunzi
读者补充]

下例中，!^ 从上一条命令获得第一项参数：


    # cp anaconda-ks.cfg anaconda-ks.cfg.bak
    anaconda-ks.cfg
    # vi -5 !^
    vi anaconda-ks.cfg

**为特定的命令替换指定的参数**

在下面的例子，!cp:2 从命令历史中搜索以 cp
开头的命令，并获取它的第二项参数：


    # cp ~/longname.txt /really/a/very/long/path/long-filename.txt
    # ls -l !cp:2
    ls -l /really/a/very/long/path/long-filename.txt

下例里，!cp:$ 获取 cp 命令的最后一项参数：


    # ls -l !cp:$
    ls -l /really/a/very/long/path/long-filename.txt

**使用 HISTSIZE 禁用 history**

如果你想禁用 history，可以将 HISTSIZE 设置为 0：


    # export HISTSIZE=0
    # history
    # [Note that history did not display anything]

**使用 HISTIGNORE 忽略历史中的特定命令**

下面的例子，将忽略 pwd、ls、ls -ltr 等命令：


    # export HISTIGNORE=”pwd:ls:ls -ltr:”
    # pwd
    # ls
    # ls -ltr
    # service httpd stop
    # history | tail -3
    79  export HISTIGNORE=”pwd:ls:ls -ltr:”
    80  service httpd stop
    81  history
    [Note that history did not record pwd, ls and ls -ltr]

[via [The Geek
Stuff](http://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history/)]
