Title: 使用 script 录制终端会话
Date: 2007-05-08 23:45
Author: toy
Category: Tutorials
Slug: record-terminal-session-with-script

script 真是一个神奇的小家伙，别看它小不起眼，可是却足够的好玩。script
能够将终端的会话过程录制下来，然后使用 scriptreplay
就可以将其录制的结果播放给他人观看。script
的好处就在于，你在终端中的所有操作过程，它都可以原原本本地进行录制。试想一下，我们可以将这种录制应用在很多方面，诸如教学、演示等等。

[![script](http://i.linuxtoy.org/i/2007/05/script_s.png)](http://i.linuxtoy.org/i/2007/05/script.png)

一般来说，script 和 scriptreplay 在 Linux
发行版中都有默认安装。如果你打算使用 script
开始录制终端会话，可以敲入下列指令：  
`script -t 2>demo.timing -a demo.session`

该指令中的 -t 选项指明输出录制的时间数据，而 -a
选项则输出录制的文件。你可以将指令中的 demo
换成自己设置的名称。当终端中返回“Script started, file is
demo.session”的信息时，你就可以进行需要录制的操作了。

如果需要结束录制过程，则输入 `exit` 即可。

要播放已录制完成的终端会话，可以使用指令：`scriptreplay demo.timing demo.session`

关于 script 及 scriptreplay 的更多信息，可以使用 man script 或 man
scriptreplay 查询。

[[via](http://www.linuxinsight.com/replaying-terminal-sessions-with-scriptreplay.html)]
