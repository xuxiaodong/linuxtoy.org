Title: ttyrec：录制你的 tty 控制台
Date: 2007-05-14 09:21
Author: toy
Category: Apps
Slug: ttyrec

这是一个与
[script](http://linuxtoy.org/archives/record-terminal-session-with-script.html)
有着异曲同工之妙的小工具。[ttyrec](http://0xcc.net/ttyrec/) 是一个 tty
控制台录制程序，其所录制的数据文件可以使用与之配套的 ttyplay
播放。不管是你在 tty 中的各种操作，还是在 tty
中耳熟能详的软件，都可进行录制。

![ttyrec](http://i.linuxtoy.org/i/2007/05/ttyrec.png)  
*使用 ttyrec 进行录制的情形*

ttyrec 当前版本为 1.0.8，于去年 6 月发布。你可在所用的 Linux
发行版中搜索安装。若是没有，也可下载其源代码，自行编译。

你若要编译 ttyrec，可以执行 `make`
指令，这个过程很快就会完成。在编译成功后，其目录包括
ttyrec、ttyplay、ttytime 三个可执行文件：

-   ttyrec－用于录制 tty 控制台
-   ttyplay－用来播放 ttyrec 所录制的数据文件
-   ttytime－了解 ttyrec 所录制数据文件的时间

ttyrec 的使用亦很简单，为了方便其执行，你可以将上述三个文件复制到
/usr/bin 或 /usr/local/bin 目录。

1.  在执行 `ttyrec` 指令后，即开始录制过程。注意，ttyrec
    没有输出任何提示信息。
2.  若是录制完成，则可以使用 `exit` 结束。
3.  ttyrec 所录制的数据文件一般为 ttyrecord，可使用 `ttyplay ttyrecord`
    播放。

一点注意事项：最好能够使录制和播放的终端尺寸保持一致。
