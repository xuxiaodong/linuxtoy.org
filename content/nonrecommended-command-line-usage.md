Title: 不推荐的命令行用法
Date: 2009-02-15 08:48
Author: toy
Category: AskLinuxtoy
Slug: nonrecommended-command-line-usage

[fcicq](http://www.fcicq.net/wp/) 同学写道：

“第一行总是不好的, 或许第二行只是好了那么一点.

这个比较重要. 如果文件坏了, 前者可查不出来.  
`sudo nano /etc/sudoers sudo visudo`

同理, 这样的也是问题.  
`sudo nano /etc/hosts sudoedit /etc/hosts`

这个毛病偶没有.  
`` kill `pgrep something` pkill something ``  
(还有些人用 killall, 你觉得好还是不好?)

这个 ps 的不好说, 谁知道偶为什么就喜欢用前者了?  
只是因为查看 zombie 进程的 ppid 比较方便?  
`ps -el ps aux`

知道两者的区别吗? 非常不幸偶是用前者的那种人.  
`su su -`

两条都不好的一组. 如果必要的话大概还是要用吧.  
`sudo su sudo screen`

有想限制上面某些操作的同学可以考虑类似:  
`%wheel ALL=(ALL) ALL, !/bin/su, !/bin/bash`

ps:  
如果你也有什么不良习惯, 赶快晒出来吧... :D”
